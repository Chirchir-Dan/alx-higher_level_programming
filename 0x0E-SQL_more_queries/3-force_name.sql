-- This script creates the table force_name in the specified database.
-- The table has two columns: id (INT) and name (VARCHAR(256) NOT NULL).
-- If the table force_name already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
