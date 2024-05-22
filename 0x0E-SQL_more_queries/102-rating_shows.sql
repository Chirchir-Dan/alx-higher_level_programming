-- 19-rotten_tomatoes.sql
-- This script lists all shows from the hbtn_0d_tvshows_rate database by their rating sum.
-- Each record displays: tv_shows.title - rating sum.
-- Results are sorted in descending order by the rating sum.
-- The script accepts the database name as an argument.


SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating_sum DESC;
