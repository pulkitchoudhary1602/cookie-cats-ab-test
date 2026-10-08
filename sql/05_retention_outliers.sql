WITH cutoff AS (
    SELECT sum_gamerounds
    FROM players
    ORDER BY sum_gamerounds
    LIMIT 1 OFFSET CAST(0.99 * (SELECT COUNT(*) FROM players) AS INTEGER)
),
filtered AS (
    SELECT *
    FROM players
    WHERE sum_gamerounds <= (SELECT sum_gamerounds FROM cutoff)
)
SELECT
    version,
    COUNT(*) AS n,
    SUM(retention_1) AS ret1_count,
    SUM(retention_7) AS ret7_count,
    AVG(retention_1) AS ret1_rate,
    AVG(retention_7) AS ret7_rate
FROM filtered
GROUP BY version;