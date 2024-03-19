-- Creates a test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a test user
CREATE USER IF NOT EXISTS
'hbnb_test'@'localhost' IDENTIFIED BY
'hbnb_test_pwd';

-- Grants all priveleges to the test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select priveleges to the test user on the performance schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
