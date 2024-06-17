-- 20-best_genre.sql
-- This script lists all genres in the hbtn_0d_tvshows_rate database by their rating sum.
-- Each record displays: tv_genres.name - rating sum.
-- Results are sorted in descending order by their rating sum.
-- The script accepts the database name as an argument.

SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON s.`genre_id` = g.`id`

       INNER JOIN `tv_show_ratings` AS r
       ON r.`show_id` = s.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
