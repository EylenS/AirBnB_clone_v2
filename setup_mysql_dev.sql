-- This script tests
-- Creates DB
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user if not exists, identified by password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all privileges to user on DB
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- Grants SELECT privileges to user on performance_schema DB
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
