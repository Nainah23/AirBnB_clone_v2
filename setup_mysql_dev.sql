-- Creates a new User
CREATE USER IF NOT EXISTS
'hbnb_dev'@'localhost' IDENTIFIED BY
'hbnb_dev_pwd';

-- Creates a new database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Grant all privileges to the created database
GRANT * ON hbnb_dev_db	TO 'hbnb_dev'@'localhost';

-- Grant select privileges to the user on the performance schema database
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
