-- 4-id_not_null.sql
-- This script creates a table called id_not_null in the specified database.
-- The table has two columns: id (INT with the default value 1, and cannot be NULL) and name (VARCHAR(256)).
-- If the table id_not_null already exists, the script will not fail.

USE $1;

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
