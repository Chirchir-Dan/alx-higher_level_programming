-- list_shows_no_genre.sql
-- This script lists all shows contained in the database hbtn_0d_tvshows without a genre linked.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
-- If a show doesn’t have a genre, NULL is displayed.
-- The script accepts the database name as an argument.

SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
