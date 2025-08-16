CREATE USER 'tradeuser'@'%' IDENTIFIED BY 'trade123';

-- Grant all privileges on all tables in the 'tradeportal' database
-- to the newly created user
GRANT ALL PRIVILEGES ON `tradeportal`.* TO 'tradeuser'@'%';

-- Flush privileges to ensure the changes take effect immediately
FLUSH PRIVILEGES;