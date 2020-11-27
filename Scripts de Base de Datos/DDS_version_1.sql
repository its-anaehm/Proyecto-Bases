
DROP DATABASE DBA;

CREATE DATABASE DBA;

USE DBA;

CREATE TABLE Users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_user VARCHAR(50) NOT NULL,
    var_pass VARCHAR(50) NOT NULL
);

CREATE TABLE Draws(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    var_name VARCHAR(50) NOT NULL,
    jso_drawInfo JSON NOT NULL,

    FOREIGN KEY (userId)
        REFERENCES Users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Binnacle(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    tex_event TEXT NOT NULL,
    tim_time TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (userId)
        REFERENCES Users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- DELIMITER $$

--     DROP PROCEDURE IF EXISTS sp_addUser $$

--     CREATE PROCEDURE sp_addUser(IN userName VARCHAR(50), IN pass VARCHAR(50))

--     BEGIN

--         DECLARE `_HOST` CHAR(14) DEFAULT '@\'localhost\'';
--         SET `userName` := CONCAT('\'', REPLACE(TRIM(`userName`), CHAR(39), CONCAT(CHAR(92), CHAR(39))), '\''),
--         `pass` := CONCAT('\'', REPLACE(`pass`, CHAR(39), CONCAT(CHAR(92), CHAR(39))), '\'');
--         SET @`sql` := CONCAT('CREATE USER ', `userName`, `_HOST`, ' IDENTIFIED BY ', `pass`);
--         PREPARE `stmt` FROM @`sql`;
--         EXECUTE `stmt`;
--         SET @`sql` := CONCAT('GRANT ALL PRIVILEGES ON *.* TO ', `userName`, `_HOST`);
--         PREPARE `stmt` FROM @`sql`;
--         EXECUTE `stmt`;
--         DEALLOCATE PREPARE `stmt`;
--         FLUSH PRIVILEGES;

--         INSERT INTO Users(var_user, var_pass) VALUES (userName, pass);

--     END $$

--     DROP PROCEDURE IF EXISTS sp_lookDraws $$

--     CREATE PROCEDURE sp_lookDraws(IN userName VARCHAR(50))

--     BEGIN
--         SET @name = userName;
--         IF (SELECT userName IN (SELECT var_user FROM Users)) THEN

--             DROP VIEW IF EXISTS showUserDraws;

--             CREATE VIEW showUserDraws AS
--                 SELECT *
--                     FROM Draws
--                     WHERE var_user = @name;
        
--         END IF;
            
--     END $$

--     DROP PROCEDURE IF EXISTS sp_deleteUser $$

--     CREATE PROCEDURE sp_deleteUser(IN userName VARCHAR(50))

--     BEGIN
        
--         IF(SELECT userName IN (SELECT var_user FROM Users)) THEN

--             DROP USER userName@'localhost';

--             DELETE FROM Users WHERE var_user = userName;

--         END IF;

--     END $$

-- DELIMITER ;

-- CALL sp_addUser("sebastian", "holi");
-- CALL sp_addUser("odin", "soidiosito");

SELECT * FROM Users;

SELECT user FROM mysql.user;

