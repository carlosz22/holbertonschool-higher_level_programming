-- Lists all shows with their rating
SELECT T_S.title, SUM(T_S_R.rate) AS rating
FROM tv_show_ratings AS T_S_R
INNER JOIN tv_shows AS T_S
ON T_S_R.show_id = T_S.id
GROUP BY T_S_R.show_id
ORDER BY rating DESC;

