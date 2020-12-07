
DROP DATABASE IF EXISTS DBA;

CREATE DATABASE DBA;

USE DBA;

CREATE TABLE Users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_user VARCHAR(50) NOT NULL,
    var_pass VARCHAR(50) NOT NULL,
    var_category VARCHAR(50) NOT NULL
);

CREATE TABLE Draws(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    var_name VARCHAR(50) NOT NULL,
    tim_time TIMESTAMP DEFAULT NOW(),
    jso_drawInfo JSON NOT NULL,

    FOREIGN KEY (userId)
        REFERENCES Users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE drawsConfig(    
    var_penColor VARCHAR(50) NOT NULL DEFAULT "#000000",
    var_fillColor VARCHAR(50) NOT NULL DEFAULT "#000000"
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

-- DELETE FROM Users WHERE var_user = "admin" and var_pass = "admin" and var_category = "Administrador";

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

DELIMITER $$

    DROP TRIGGER IF EXISTS bin_addUser $$
    CREATE TRIGGER bin_addUser AFTER INSERT ON Users
        FOR EACH ROW
        BEGIN            
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id                    
                    FROM Users Us
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
                "Inserción de Usuario"
              );
        END $$

    DROP TRIGGER IF EXISTS bin_deleteUser $$ 
    CREATE TRIGGER bin_deleteUser AFTER DELETE ON Users
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
                "Eliminación de Usuario"
            );
        END $$
    
    DROP TRIGGER IF EXISTS bin_updateUser $$
    CREATE TRIGGER bin_updateUser AFTER UPDATE ON Users
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
                "Modificación de Usuario"
                );
        END $$

    DROP TRIGGER IF EXISTS bin_addDraw $$
    CREATE TRIGGER bin_addDraw AFTER INSERT ON Draws
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
                "Inserción de Dibujo"
                );
        END $$
    
    DROP TRIGGER IF EXISTS bin_deleteDraw $$    
    CREATE TRIGGER bin_deleteDraw AFTER DELETE ON Draws
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
                "Eliminación de Dibujo"
                );
        END $$
    
    DROP TRIGGER IF EXISTS bin_modifyDraw $$
 
    CREATE TRIGGER bin_modifyDraw AFTER UPDATE ON Draws
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
                "Modificación de Dibujo"
            );

        END $$

    CREATE TRIGGER bin_modifyDrawConfig AFTER UPDATE ON drawsConfig
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
                "Modificación de Configuración de Colores de Dibujo"
            );

        END $$

    DROP PROCEDURE IF EXISTS sp_addMainUser $$
    CREATE PROCEDURE sp_addMainUser(IN category VARCHAR(50))
        BEGIN

            INSERT INTO Users(var_user, var_pass, var_category) VALUES(((SUBSTRING_INDEX(CURRENT_USER(), "@",1))), 'admin', category);
            
            CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
            GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
        
        END $$

DELIMITER ;

SELECT * FROM Users;

CALL sp_addMainUser("Administrador");

INSERT INTO drawsConfig() VALUES ();

SELECT user FROM mysql.user;

