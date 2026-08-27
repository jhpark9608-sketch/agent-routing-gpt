#!/usr/bin/env python3
"""Compare paired Codex benchmark runs.

Usage:
    python benchmarks/compare_results.py benchmarks/results.csv \
        --output benchmarks/BENCHMARK_RESULTS.md

Only rows with recorded metrics participate in each metric's aggregate.
Task-success values accepted: 1/0, true/false, yes/no, pass/fail.
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean


BASELINE = "baseline_sol_medium"
ROUTING = "agent_routing_gpt"


def to_float(value):
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def to_bool(value):
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in {"1", "true", "yes", "y", "pass", "passed"}:
        return True
    if text in {"0", "false", "no", "n", "fail", "failed"}:
        return False
    return None


def pct_reduction(base, routed):
    if base is None or routed is None or base == 0:
        return None
    return (base - routed) / base * 100.0


def fmt_num(x, digits=1):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "—"
    return f"{x:,.{digits}f}"


def fmt_pct(x):
    if x is None:
        return "—"
    sign = "+" if x < 0 else ""
    return f"{sign}{x:.1f}%"


def avg_metric(rows, key):
    vals = [to_float(r.get(key)) for r in rows]
    vals = [v for v in vals if v is not None]
    return mean(vals) if vals else None


def success_rate(rows):
    vals = [to_bool(r.get("task_success")) for r in rows]
    vals = [v for v in vals if v is not None]
    return (sum(vals) / len(vals) * 100.0) if vals else None


def test_pass_rate(rows):
    passed = 0.0
    total = 0.0
    for r in rows:
        p = to_float(r.get("tests_passed"))
        t = to_float(r.get("tests_total"))
        if p is not None and t is not None and t > 0:
            passed += p
            total += t
    return (passed / total * 100.0) if total else None


def total_token_average(rows):
    values = []
    for r in rows:
        u = to_float(r.get("uncached_input_tokens"))
        c = to_float(r.get("cached_input_tokens"))
        o = to_float(r.get("output_tokens"))
        if u is None and c is None and o is None:
            continue
        values.append((u or 0) + (c or 0) + (o or 0))
    return mean(values) if values else None


def completed_pairs(rows):
    grouped = defaultdict(dict)
    for r in rows:
        key = (r.get("task_id"), r.get("replicate"))
        grouped[key][r.get("condition")] = r
    return sum(
        1 for pair in grouped.values()
        if BASELINE in pair and ROUTING in pair
        and to_float(pair[BASELINE].get("credits")) is not None
        and to_float(pair[ROUTING].get("credits")) is not None
    )


def build_report(rows):
    groups = defaultdict(list)
    for r in rows:
        groups[r.get("condition", "")].append(r)

    base = groups[BASELINE]
    routed = groups[ROUTING]

    metrics = [
        ("Uncached input tokens / run", "uncached_input_tokens"),
        ("Cached input tokens / run", "cached_input_tokens"),
        ("Output tokens / run", "output_tokens"),
        ("Credits / run", "credits"),
        ("Wall time (s) / run", "wall_time_s"),
        ("Sol calls / run", "sol_calls"),
    ]

    lines = [
        "# Benchmark Results",
        "",
        "> Generated from benchmarks/results.csv. Do not treat incomplete rows as final evidence.",
        "",
        f"Completed credit-matched A/B pairs: **{completed_pairs(rows)}**",
        "",
        "## Aggregate comparison",
        "",
        "| Metric | Sol Medium baseline | agent-routing-gpt | Reduction |",
        "|---|---:|---:|---:|",
    ]

    total_base = total_token_average(base)
    total_routed = total_token_average(routed)
    lines.append(
        f"| Total tokens / run | {fmt_num(total_base)} | {fmt_num(total_routed)} | "
        f"{fmt_pct(pct_reduction(total_base, total_routed))} |"
    )

    for label, key in metrics:
        b = avg_metric(base, key)
        r = avg_metric(routed, key)
        lines.append(
            f"| {label} | {fmt_num(b)} | {fmt_num(r)} | {fmt_pct(pct_reduction(b, r))} |"
        )

    b_success = success_rate(base)
    r_success = success_rate(routed)
    b_tests = test_pass_rate(base)
    r_tests = test_pass_rate(routed)

    lines += [
        "",
        "## Quality",
        "",
        "| Metric | Sol Medium baseline | agent-routing-gpt | Difference |",
        "|---|---:|---:|---:|",
        f"| Task success rate | {fmt_num(b_success)}% | {fmt_num(r_success)}% | "
        f"{fmt_num(None if b_success is None or r_success is None else r_success-b_success)} pp |",
        f"| Test pass rate | {fmt_num(b_tests)}% | {fmt_num(r_tests)}% | "
        f"{fmt_num(None if b_tests is None or r_tests is None else r_tests-b_tests)} pp |",
        "",
        "## Interpretation",
        "",
    ]

    credit_base = avg_metric(base, "credits")
    credit_routed = avg_metric(routed, "credits")
    credit_red = pct_reduction(credit_base, credit_routed)

    if credit_red is None:
        lines.append("- Credit data are incomplete; no cost-efficiency claim can be made yet.")
    else:
        lines.append(f"- Average credit reduction: **{credit_red:.1f}%**.")

    if b_success is None or r_success is None:
        lines.append("- Task-success data are incomplete.")
    elif r_success < b_success:
        lines.append("- Routing currently has a lower task-success rate; investigate quality before making an efficiency claim.")
    else:
        lines.append("- Routing matches or exceeds the recorded baseline task-success rate.")

    if b_tests is None or r_tests is None:
        lines.append("- Test-pass data are incomplete.")
    elif r_tests < b_tests:
        lines.append("- Routing currently has a lower test-pass rate; investigate regressions before making an efficiency claim.")
    else:
        lines.append("- Routing matches or exceeds the recorded baseline test-pass rate.")

    lines += [
        "",
        "## Reporting checklist",
        "",
        "- Same start commit for paired runs",
        "- Same prompt for paired runs",
        "- Fresh session for each run",
        "- A/B order counterbalanced",
        "- Cached and uncached input recorded separately",
        "- At least 3 replicates where practical",
        "- No fabricated or manually imputed usage values",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    with args.csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    report = build_report(rows)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
