-- 18-no_comedy_tonight.sql
-- This script lists all shows without the genre 'Comedy' from the hbtn_0d_tvshows database.
-- The tv_genres table contains only one record where name = 'Comedy'.
-- Each record displays: tv_shows.title.
-- Results are sorted in ascending order by the show title.
-- The script accepts the database name as an argument.


SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
      SELECT tv_shows.id FROM tv_shows
      JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
      JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
      WHERE tv_genres.name = "Comedy" )
ORDER BY tv_shows.title;
