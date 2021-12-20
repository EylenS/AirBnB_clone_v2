-- This script prepares a MySQL server
-- Creates DB
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates user if not exists, identified by password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants all privileges to user on DB
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- Grants SELECT privileges to user on performance_schema DB
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
