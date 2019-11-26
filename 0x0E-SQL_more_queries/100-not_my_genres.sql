-- Shows all genres not tied to the show Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN
(SELECT T_S_G.genre_id
FROM tv_show_genres AS T_S_G
INNER JOIN tv_shows AS T_S
ON T_S_G.show_id = T_S.id
WHERE T_S.title = "Dexter")
ORDER BY name ASC;
