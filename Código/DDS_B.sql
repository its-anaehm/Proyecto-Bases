DROP DATABASE IF EXISTS DBB;

CREATE DATABASE DBB CHARACTER SET utf8;

USE DBB;

CREATE TABLE Draws(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL COMMENT "Id del usuario que creo el dibujo.", 
    var_name VARCHAR(50) NOT NULL COMMENT "Nombre del dibujo.",
    blo_drawInfo BLOB NOT NULL COMMENT "Contiene archivos .json encriptados con la información del dibujo."

) COMMENT "Dibujos realizados por los usuarios.";


