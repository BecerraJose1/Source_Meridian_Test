CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE IF NOT EXISTS book (
    id VARCHAR(32) PRIMARY KEY NOT NULL,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    read_flag BOOLEAN DEFAULT FALSE
);

INSERT INTO book (id, title, author, read_flag) VALUES
    ('ce13a4af4fb245f1b0cb14798fbc5f11', 'On the Road', 'Jack Kerouac', TRUE),
    ('72d6668394a8493f8c15b74cfb5527fd', 'Harry Potter and the Philosopher\'s Stone', 'J. K. Rowling', FALSE),
    ('10c948f5c4584210909927021e92fb06', 'Green Eggs and Ham', 'Dr. Seuss', TRUE);

ALTER USER 'root'@'%' IDENTIFIED WITH 'caching_sha2_password' BY 'rootpassword';
FLUSH PRIVILEGES;
