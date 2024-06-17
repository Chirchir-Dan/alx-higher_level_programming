-- 17-not_my_genre.sql
-- This script lists all genres not linked to the show Dexter from the hbtn_0d_tvshows database.
-- The tv_shows table contains only one record where title = Dexter.
-- Each record displays: tv_genres.name.
-- Results are sorted in ascending order by the genre name.
-- The script accepts the database name as an argument.

SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
      SELECT tv_genres.id FROM tv_genres
      JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
      JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
      WHERE tv_shows.title = "DEXTER" )
ORDER BY tv_genres.name;
