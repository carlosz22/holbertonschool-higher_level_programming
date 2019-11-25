-- Lists all records by name not NULL
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
