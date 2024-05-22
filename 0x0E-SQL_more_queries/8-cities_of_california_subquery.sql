-- 8-list_california_cities.sql
-- This script lists all the cities of California found in the database hbtn_0d_usa.
-- It retrieves cities from the cities table by filtering with the state_id obtained from the states table where name = California.
-- Results are sorted in ascending order by cities.id.
-- The database name will be passed as an argument of the mysql command.

USE $1;

SELECT cities.*
FROM cities, states
WHERE states.name = 'California' AND cities.state_id = states.id
ORDER BY cities.id ASC;
