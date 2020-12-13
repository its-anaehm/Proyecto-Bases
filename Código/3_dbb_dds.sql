DROP DATABASE IF EXISTS DBB;

CREATE DATABASE DBB CHARACTER SET latin1;

USE DBB;

CREATE TABLE Draws(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL COMMENT "Id del usuario que creo el dibujo.", 
    var_name VARCHAR(50) NOT NULL COMMENT "Nombre del dibujo.",
    blo_drawInfo BLOB NOT NULL COMMENT "Contiene archivos .json encriptados con la información del dibujo."

) COMMENT "Dibujos realizados por los usuarios.";

DELIMITER $$

DROP TRIGGER IF EXISTS tg_addCodedDrawB $$

CREATE TRIGGER tg_addCodedDrawB BEFORE INSERT ON Draws
    FOR EACH ROW
    BEGIN

        SET NEW.var_name = AES_ENCRYPT(NEW.var_name, "admin");
        -- SET NEW.blo_drawInfo = AES_ENCRYPT(NEW.blo_drawInfo, "admin");

    END $$

DELIMITER ;


