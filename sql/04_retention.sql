SELECT version,
       COUNT(*) AS n,
       SUM(retention_1) AS ret1_count,
       SUM(retention_7) AS ret7_count,
       AVG(retention_1) AS ret1_rate,
       AVG(retention_7) AS ret7_rate
FROM players
GROUP BY version;