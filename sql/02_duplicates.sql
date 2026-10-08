-- Duplicate user IDs?
SELECT COUNT(*) - COUNT(DISTINCT userid) AS duplicates FROM players;

