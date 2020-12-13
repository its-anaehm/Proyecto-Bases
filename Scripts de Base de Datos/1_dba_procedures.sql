/*
    @author: emilio.sosa@unah.hn
    @date : 08/12/2020
    @versión 1.0
*/


USE DBA;

DELIMITER $$

    /*
        Procedimiento almacenado que agrega al usuario administrador por defecto.
    */
    DROP PROCEDURE IF EXISTS sp_addMainUser $$
    CREATE PROCEDURE sp_addMainUser(IN category VARCHAR(50))
        BEGIN

            INSERT INTO Users(var_user, var_pass, var_category) VALUES("admin", 'admin', category);
            
            CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
            GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
        
        END $$

   
DELIMITER ;



