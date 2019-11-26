-- Lists of all shows and therr genre_id including NULLs
SELECT T_S.title, T_S_G.genre_id
FROM tv_show_genres AS T_S_G
RIGHT JOIN tv_shows AS T_S
ON T_S_G.show_id = T_S.id
ORDER BY T_S.title ASC,
T_S_G.genre_id;
