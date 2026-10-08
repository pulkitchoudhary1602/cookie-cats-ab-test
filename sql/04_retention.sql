-- First look at retention by group
SELECT version,
       AVG(retention_1) AS ret_1,
       AVG(retention_7) AS ret_7
FROM players GROUP BY version;