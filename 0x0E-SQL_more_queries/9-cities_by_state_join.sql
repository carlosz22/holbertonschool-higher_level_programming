-- Displays all cities with their state
SELECT C.id, C.name, S.name
FROM cities AS C
LEFT JOIN states AS S
ON C.id = S.id
ORDER BY C.id ASC;

