-- create_states_table.sql
-- This script creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on the MySQL server.
-- The table states has two columns: id (INT, unique, auto generated, primary key) and name (VARCHAR(256), not null).
-- If the database hbtn_0d_usa or the table states already exist, the script will not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
