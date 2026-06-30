-- 1. Create a workspace database
CREATE DATABASE network_security_db;

-- 2. Switch to the database
USE network_security_db;

-- 3. Create a table to log open ports and vulnerabilities
CREATE TABLE scan_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    target_ip VARCHAR(50) NOT NULL,
    port_number INT NOT NULL,
    port_status VARCHAR(20) DEFAULT 'OPEN',
    scan_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE USER 'scanner_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'scanner_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
