-- Display number of shows in a genre
SELECT T_G.name AS genre,
COUNT(T_S_G.show_id) AS number_of_shows
FROM tv_show_genres AS T_S_G
LEFT JOIN tv_genres AS T_G
ON T_S_G.genre_id = T_G.id
GROUP BY T_G.name
ORDER BY number_of_shows DESC;
