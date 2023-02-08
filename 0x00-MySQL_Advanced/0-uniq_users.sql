-- Creates a new table called users
CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, email CHAR(255) UNIQUE, name CHAR(255));
