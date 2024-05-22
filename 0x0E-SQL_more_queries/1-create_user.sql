-- This script creates the MySQL server user user_0d_1 with all privileges.
-- The user_0d_1 password is set to user_0d_1_pwd.
-- If the user user_0d_1 already exists, the script should not fail.

-- Create the user user_0d_1 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;
