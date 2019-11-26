-- Lists all genres by their rating
SELECT T_G.name, SUM(T_S_R.rate) AS rating
FROM tv_show_ratings AS T_S_R
INNER JOIN tv_show_genres AS T_S_G
ON T_S_R.show_id = T_S_G.show_id
INNER JOIN tv_genres AS T_G
ON T_S_G.genre_id = T_G.id
GROUP BY T_G.name
ORDER BY rating DESC;
