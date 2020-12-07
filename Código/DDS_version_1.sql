
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


DELIMITER $$

    DROP FUNCTION IF EXISTS ft_encrypt $$
    CREATE FUNCTION ft_encrypt(dataToEncrypt VARCHAR(50)) RETURNS TEXT DETERMINISTIC
        BEGIN
            DECLARE encryptedData TEXT;
            DECLARE pass VARCHAR(50);

            (SELECT var_pass from Users WHERE var_user = "admin") INTO pass;
            SELECT AES_ENCRYPT(dataToEncrypt, pass) INTO encryptedData;

            RETURN encryptedData;
        END $$

    DROP FUNCTION IF EXISTS ft_decrypt $$
    CREATE FUNCTION ft_decrypt(dataToDecrypt VARCHAR(50)) RETURNS TEXT DETERMINISTIC
        BEGIN
            DECLARE decryptedData TEXT;
            DECLARE pass VARCHAR(50);

            SELECT AES_DECRYPT(dataToEncrypt, pass) INTO decryptedData;
            (SELECT var_pass from Users WHERE var_user = "admin") INTO pass;

            RETURN encryptedData;
        END $$  

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

            INSERT INTO Users(var_user, var_pass, var_category) VALUES('admin', 'admin', category);
            
            CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
            GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
        
        END $$
    

DELIMITER ;

SELECT * FROM Users;

CALL sp_addMainUser("Administrador");

INSERT INTO drawsConfig() VALUES ();

SELECT user FROM mysql.user;

