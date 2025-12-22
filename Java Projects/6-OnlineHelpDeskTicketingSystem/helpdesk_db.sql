
CREATE DATABASE IF NOT EXISTS helpdesk_db;
USE helpdesk_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    role ENUM('user', 'admin') DEFAULT 'user'
);

CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category VARCHAR(100),
    priority ENUM('Low', 'Medium', 'High') NOT NULL,
    description TEXT,
    status ENUM('Open', 'In Progress', 'Closed') DEFAULT 'Open',
    resolution_comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO users (username, password, email, role)
VALUES ('admin', 'admin123', 'admin@helpdesk.com', 'admin');

DESC users;

ALTER TABLE users ADD COLUMN role VARCHAR(20) DEFAULT 'user';

select * from users;
SELECT * FROM users WHERE email IS NULL;
UPDATE users SET email = 'placeholder@example.com' WHERE email IS NULL;
ALTER TABLE users MODIFY email VARCHAR(255) NOT NULL;


ALTER TABLE tickets 
    MODIFY status VARCHAR(50) NOT NULL DEFAULT 'Open',
    MODIFY created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;

select * from tickets;
SELECT * FROM users WHERE username = 'bhoomi';
