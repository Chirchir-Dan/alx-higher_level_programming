-- 6-create_states_table.sql
-- This script creates the database hbtn_0d_usa and the table states within it.
-- The table states has two columns: id (INT, unique, auto-generated, primary key, cannot be null) and name (VARCHAR(256), cannot be null).
-- If the database hbtn_0d_usa or the table states already exist, the script will not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
