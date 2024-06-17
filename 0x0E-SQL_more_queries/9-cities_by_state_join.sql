-- list_cities.sql
-- This script lists all cities contained in the database hbtn_0d_usa, along with their corresponding state names.
-- Each record displays: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id.
-- The script accepts the database name as an argument.

SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON states.id = cities.state_id
ORDER BY cities.id;
