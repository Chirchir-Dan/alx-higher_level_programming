-- 7-create_cities_table.sql
-- This script creates the table cities within the database hbtn_0d_usa.
-- The table cities has three columns: id (INT, unique, auto-generated, primary key, cannot be null), state_id (INT, cannot be null, foreign key referencing id of the states table), and name (VARCHAR(256), cannot be null).
-- If the database hbtn_0d_usa or the table cities already exist, the script will not fail.

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
