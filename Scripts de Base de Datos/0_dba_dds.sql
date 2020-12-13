
/*
    @author: emilio.sosa@unah.hn
    @date : 26/11/2020
    @versión 2.0
*/

DROP DATABASE IF EXISTS DBA;

CREATE DATABASE DBA CHARACTER SET latin1;

USE DBA;

CREATE TABLE Users(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Llave identificadora de los usuarios",
    var_user VARCHAR(100) NOT NULL COMMENT "Nombre del usuario registrado",
    var_pass VARCHAR(100) NOT NULL COMMENT "Contraseña del Usuario registrado",
    var_category VARCHAR(20) NOT NULL COMMENT "Categoría que define los permisos de Usuarios"
)  COMMENT "Tabla que almancena los datos de usuarios de la aplicación de dibujo.";

CREATE TABLE Draws(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Llave identificadora del dibujo",
    userId INT NOT NULL COMMENT "Identificador del usuario al que pertenece el dibujo",
    var_name VARCHAR(50) NOT NULL COMMENT "Nombre del dibujo almacenado",
    tim_time TIMESTAMP DEFAULT NOW() COMMENT "Registro del momento en que se almacenó el dibujo",
    jso_drawInfo JSON NOT NULL COMMENT "Configuración interna del dibujo guardado por el usuario.",

    FOREIGN KEY (userId)
        REFERENCES Users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)   COMMENT "Tabla que almacena los dibujos creados en la aplicación de dibujo.";

CREATE TABLE drawsConfig(    
    var_penColor VARCHAR(50) NOT NULL COMMENT "Configuración del atributo PenColor en la aplicación Draw.",
    var_fillColor VARCHAR(50) NOT NULL COMMENT "Configuración del atributo FillColor en la aplicación Draw."
) COMMENT "Tabla que guarda los datos que se configuran para las opciones de FillColor y PenColor.";

CREATE TABLE Binnacle(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Llave identificadora del evento.",
    userId INT NOT NULL COMMENT "Identificador del usuario que disparó el evento.",
    tex_event TEXT NOT NULL COMMENT "Texto que describe el evento.",
    tim_time TIMESTAMP DEFAULT NOW() COMMENT "Momento en que se almacenó el registro del evento.",

    FOREIGN KEY (userId)
        REFERENCES Users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) COMMENT "Tabla que almacena registros de los eventos de la aplicación.";


