-- cities_of_california.sql
-- This script lists all the cities of California from the database hbtn_0d_usa.
-- The states table contains only one record where name = California.
-- Results are sorted in ascending order by cities.id.
-- JOIN keyword is not used.

USE $1;

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
