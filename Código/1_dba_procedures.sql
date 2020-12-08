USE DBA;

DELIMITER $$
    DROP PROCEDURE IF EXISTS sp_addMainUser $$
    CREATE PROCEDURE sp_addMainUser(IN category VARCHAR(50))
        BEGIN

            INSERT INTO Users(var_user, var_pass, var_category) VALUES("admin", 'admin', category);
            
            CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
            GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
        
        END $$

DELIMITER ;

CALL sp_addMainUser("Administrador");