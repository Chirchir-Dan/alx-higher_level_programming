-- 13-shows_by_genre.sql
-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre, and the second column is called number_of_shows.
-- Genres without any linked shows are not displayed.
-- Results are sorted in descending order by the number of shows linked.
-- The script accepts the database name as an argument.


SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
