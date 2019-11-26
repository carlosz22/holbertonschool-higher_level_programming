-- Lists all Comedy shows
SELECT T_S.title
FROM tv_show_genres AS T_S_G
INNER JOIN tv_shows AS T_S
ON T_S_G.show_id = T_S.id
INNER JOIN tv_genres AS T_G
ON T_S_G.genre_id = T_G.id
WHERE T_G.name = "Comedy"
ORDER BY T_S.title ASC;
