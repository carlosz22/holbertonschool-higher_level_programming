-- Lists all genres of the show Dexter
SELECT T_G.name
FROM tv_show_genres AS T_S_G
INNER JOIN tv_shows AS T_S
ON T_S_G.show_id = T_S.id
INNER JOIN tv_genres AS T_G
ON T_S_G.genre_id = T_G.id
WHERE T_S.title = "Dexter"
ORDER BY T_G.name ASC;
