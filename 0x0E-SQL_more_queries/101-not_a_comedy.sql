-- Lists all the shows without genre Comedy
SELECT title
FROM tv_shows
WHERE id NOT IN
(SELECT T_S_G.show_id
FROM tv_show_genres AS T_S_G
INNER JOIN tv_genres AS T_G
ON T_S_G.genre_id = T_G.id
WHERE T_G.name = "Comedy")
ORDER BY title ASC;
