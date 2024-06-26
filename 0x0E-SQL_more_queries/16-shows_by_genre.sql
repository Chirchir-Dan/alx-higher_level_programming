-- 16-list_shows_and_genres.sql
-- This script lists all shows and their linked genres from the hbtn_0d_tvshows database.
-- If a show doesn’t have a genre, NULL is displayed in the genre column.
-- Each record displays: tv_shows.title - tv_genres.name.
-- Results are sorted in ascending order by the show title and genre name.
-- The script accepts the database name as an argument.

SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name;
