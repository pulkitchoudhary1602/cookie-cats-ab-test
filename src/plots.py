import os
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportion_confint


def retention_chart(df, outdir="reports/figures"):
    """Bar chart of Day-1 and Day-7 retention by group with 95% Wilson CIs.

    df needs columns: version, n, ret1_count, ret7_count (one row per group).
    """
    os.makedirs(outdir, exist_ok=True)
    g30 = df[df.version == "gate_30"].iloc[0]
    g40 = df[df.version == "gate_40"].iloc[0]
    metrics = [("Day-1", "ret1_count"), ("Day-7", "ret7_count")]

    x = np.arange(len(metrics))
    width = 0.35
    fig, ax = plt.subplots(figsize=(6, 4))

    for i, (label, grp) in enumerate([("Gate 30", g30), ("Gate 40", g40)]):
        rates, err_lo, err_hi = [], [], []
        for _, col in metrics:
            n, k = int(grp["n"]), int(grp[col])
            p = k / n
            lo, hi = proportion_confint(k, n, method="wilson")
            rates.append(p * 100)
            err_lo.append((p - lo) * 100)
            err_hi.append((hi - p) * 100)
        bars = ax.bar(x + (i - 0.5) * width, rates, width,
                      yerr=[err_lo, err_hi], capsize=4, label=label)
        for b, r in zip(bars, rates):
            ax.text(b.get_x() + b.get_width() / 2, 1, f"{r:.2f}%",
                    ha="center", va="bottom", color="white", fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels([m[0] for m in metrics])
    ax.set_ylabel("Retention (%)")
    ax.set_title("Retention by gate position (95% CI)")
    ax.legend()
    fig.tight_layout()
    path = os.path.join(outdir, "retention_by_group.png")
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def diff_chart(results, outdir="reports/figures"):
    """Difference (Gate 40 - Gate 30) in percentage points with bootstrap CI.

    results: {"Day-1": (diff, ci_low, ci_high), "Day-7": (...)} in percentage points.
    """
    os.makedirs(outdir, exist_ok=True)
    labels = list(results.keys())
    diffs = np.array([results[k][0] for k in labels])
    lows = np.array([results[k][1] for k in labels])
    highs = np.array([results[k][2] for k in labels])
    y = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.errorbar(diffs, y, xerr=[diffs - lows, highs - diffs],
                fmt="o", capsize=5)
    ax.axvline(0, linestyle="--", color="gray")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Difference in retention, Gate 40 - Gate 30 (percentage points)")
    ax.set_title("Effect of moving the gate to level 40 (95% bootstrap CI)")
    fig.tight_layout()
    path = os.path.join(outdir, "retention_difference.png")
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path