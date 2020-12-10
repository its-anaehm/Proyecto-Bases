USE DBA;

DELIMITER $$
    DROP PROCEDURE IF EXISTS sp_addMainUser $$
    CREATE PROCEDURE sp_addMainUser(IN category VARCHAR(50))
        BEGIN

            INSERT INTO Users(var_user, var_pass, var_category) VALUES("admin", 'admin', category);
            
            CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
            GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
        
        END $$

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

    DROP PROCEDURE IF EXISTS sp_encryption $$
    CREATE PROCEDURE sp_encryption(IN textToEncrypt TEXT, OUT encryptedData TEXT)
        BEGIN

            SET encryptedData = AES_ENCRYPT(textToEncrypt, "admin");

        END $$

    DROP PROCEDURE IF EXISTS sp_decryption $$
    CREATE PROCEDURE sp_decryption(IN textToDecrypt TEXT, OUT decryptedData TEXT)
        BEGIN
            SET decryptedData = AES_DECRYPT(textToDecrypt, "admin");
        END $$
DELIMITER ;



