-- 19-rotten_tomatoes.sql
-- This script lists all shows from the hbtn_0d_tvshows_rate database by their rating sum.
-- Each record displays: tv_shows.title - rating sum.
-- Results are sorted in descending order by the rating sum.
-- The script accepts the database name as an argument.

SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
