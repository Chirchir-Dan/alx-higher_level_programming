-- 5-unique_id.sql
-- This script creates a table called unique_id in the specified database.
-- The table has two columns: id (INT with the default value 1, must be unique) and name (VARCHAR(256)).
-- If the table unique_id already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
