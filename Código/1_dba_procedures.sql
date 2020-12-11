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

    /*
        Procedimiento que encripta los datos pasados en primer parámetro con la contraseña en el segundo parámetro, 
        y los almacena en el tercer parámetro.
    */
    DROP PROCEDURE IF EXISTS sp_encrypt $$
    CREATE PROCEDURE sp_encrypt (IN textToEncrypt TEXT, IN pass VARCHAR(100), OUT encryptedData VARCHAR(200))
        BEGIN

            DECLARE passChar VARCHAR(1);
            DECLARE codedChar VARCHAR(1);

            SET @encode = "";
            SET @counter = 1;

            WHILE @counter <= CHAR_LENGTH(textToEncrypt) DO
                
                SET @passChar = SUBSTRING(pass, (@counter % (SELECT CHAR_LENGTH(pass))), 1);
                SELECT CHAR(
                    (ORD((SUBSTRING(textToEncrypt,@counter,1))) + ORD(@passChar))
                ) INTO @codedChar;
                SET @encode = CONCAT(@encode, @codedChar);
                SET @counter = @counter + 1;
            END WHILE;

            SELECT @encode;

            SET encryptedData = @encode;

        END $$

    /*
        Procedimiento que encripta los datos pasados en primer parámetro con la contraseña en el segundo parámetro, 
        y los almacena en el tercer parámetro.
    */
    DROP PROCEDURE IF EXISTS sp_decrypt $$
    CREATE PROCEDURE sp_decrypt (IN textToEncrypt TEXT, IN pass VARCHAR(100), OUT encryptedData VARCHAR(200))
        BEGIN

            DECLARE passChar VARCHAR(1);
            DECLARE codedChar VARCHAR(1);

            SET @encode = "";
            SET @counter = 1;

            WHILE @counter <= CHAR_LENGTH(textToEncrypt) DO
                
                SET @passChar = SUBSTRING(pass, (@counter % (SELECT CHAR_LENGTH(pass))), 1);
                SELECT CHAR(
                    (ORD((SUBSTRING(textToEncrypt,@counter,1))) - ORD(@passChar))
                ) INTO @codedChar;
                SET @encode = CONCAT(@encode, @codedChar);
                SET @counter = @counter + 1;
            END WHILE;

            SELECT @encode;

            SET encryptedData = @encode;

        END $$
    /*
        Encripta datos utilizando funciones build-in de mariadb.
    */
    DROP PROCEDURE IF EXISTS sp_encryption $$
    CREATE PROCEDURE sp_encryption(IN textToEncrypt TEXT, OUT encryptedData TEXT)
        BEGIN

            SET encryptedData = AES_ENCRYPT(textToEncrypt, "admin");

        END $$

    /*
        Desencripta datos usando funciones build-in de mariadb.
    */
    DROP PROCEDURE IF EXISTS sp_decryption $$
    CREATE PROCEDURE sp_decryption(IN textToDecrypt TEXT, OUT decryptedData TEXT)
        BEGIN
            SET decryptedData = AES_DECRYPT(textToDecrypt, "admin");
        END $$
DELIMITER ;



