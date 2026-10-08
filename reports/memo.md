# Memo: Should the first gate move from level 30 to level 40?

**Recommendation:** Keep the first gate at level 30.

## Question
Cookie Cats players were split into two groups: the first gate at level 30 (control) or at level 40 (variant). Does moving the gate change player retention?

## Key results

| Metric | Gate 30 | Gate 40 | Difference (40 - 30) | 95% bootstrap CI | p-value |
|---|---|---|---|---|---|
| Day-1 retention | 44.82% | 44.23% | -0.59 pp | [-1.25, +0.07] | 0.0744 |
| Day-7 retention | 19.02% | 18.20% | -0.82 pp (-4.31% relative) | [-1.34, -0.31] | 0.0016 |

- **Day-7 retention fell** when the gate moved to level 40. This is roughly 820 fewer returning players per 100,000 installs.
- **Day-1 retention** showed no statistically significant change. The data are consistent with anything from a small decline to essentially no effect.
- The Day-7 result stayed significant under a stricter threshold (alpha = 0.025 per test, to account for two metrics) and after excluding the top 1% of players by game rounds (difference -0.83 pp).
- The experiment was adequately powered to detect a 1 pp difference (about 24,657 players needed per group; each group had about 45,000).

### Charts

![Retention by group](figures/retention_by_group.png)

![Retention difference](figures/retention_difference.png)

> Note: Error bars in the retention-by-group chart are 95% Wilson confidence
> intervals for each group's retention rate. The difference plot uses the
> 95% bootstrap confidence intervals for Gate 40 - Gate 30.

## Method
- Data cleaned and aggregated in SQL (SQLite); statistics in Python.
- Two-proportion z-tests, bootstrap confidence intervals for the difference, effect sizes, a power calculation, an outlier robustness check, and a sample ratio check.

## Caveats
- **Sample ratio mismatch:** group sizes were 44,700 and 45,489 (49.56% / 50.44%), which differs from 50/50 (chi-square p = 0.0086). The imbalance is small and its cause is unknown, so the result should be described as an association rather than a perfectly clean causal estimate.
- **No revenue data.** A later gate could lower retention while raising engagement or spending among remaining players. This analysis cannot rule that out.
- Only Day-1 and Day-7 retention were measured, at fixed points in time, and the data cannot explain why players leave.

## Suggested next steps
1. Investigate the cause of the group-size imbalance with the data owners.
2. Pull revenue and purchase data for both groups before any rollout decision.
3. Examine retention at later points (Day 14, Day 30) if available.