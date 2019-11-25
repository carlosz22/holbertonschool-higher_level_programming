-- DIsplays the top 3 cities avg temp during July and August
SELECT city, AVG(value) AS avg_tmp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;
