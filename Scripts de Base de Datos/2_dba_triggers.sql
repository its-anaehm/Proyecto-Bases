/*
    @author: emilio.sosa@unah.hn
    @date : 08/12/2020
    @versión 1.0
*/

USE DBA;

DELIMITER $$

    /*
        Trigger que registra una inserción de evento en la bicácora luego de que un usuario ha sido insertado en su respectiva tabla.
    */
    DROP TRIGGER IF EXISTS tg_binAddUser $$
    CREATE TRIGGER tg_binAddUser AFTER INSERT ON Users
        FOR EACH ROW
        BEGIN            
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id                    
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(SESSION_USER(), "@",1))), "admin") = Us.var_user),
                "Inserción de Usuario"
              );
        END $$

    /*
        Trigger registra en la bitácora la eliminación de un usuario.
    */
    DROP TRIGGER IF EXISTS tg_binDeleteUser $$ 
    CREATE TRIGGER tg_binDeleteUser AFTER DELETE ON Users
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(SESSION_USER(), "@",1))), "admin") = Us.var_user),
                "Eliminación de Usuario"
            );
        END $$
    
    /*
        Trigger que registra una inserción de evento en la bicácora luego de que un usuario ha sido actualizado en su respectiva tabla.
    */
    DROP TRIGGER IF EXISTS tg_binUpdateUser $$
    CREATE TRIGGER tg_binUpdateUser AFTER UPDATE ON Users
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(SESSION_USER(), "@",1))), "admin") = Us.var_user),
                "Modificación de Usuario"
                );
        END $$    
    
    /*
        Trigger que registra una inserción de evento en la bicácora luego de que un dibujo ha sido insertado en su respectiva tabla.
    */
    DROP TRIGGER IF EXISTS tg_binAddDraw $$
    CREATE TRIGGER tg_binAddDraw AFTER INSERT ON Draws
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(SESSION_USER(), "@",1))), "admin") = Us.var_user),
                "Inserción de Dibujo"
                );
        END $$
    
    /*
    Trigger que registra en la bitácora la eliminación de un dibujo.
    */
    DROP TRIGGER IF EXISTS tg_binDeleteDraw $$    
    CREATE TRIGGER tg_binDeleteDraw AFTER DELETE ON Draws
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(SESSION_USER(), "@",1))), "admin") = Us.var_user),
                "Eliminación de Dibujo"
                );
        END $$
    
    /*
        Trigger que registra una inserción de evento en la bicácora luego de que un dibujo ha sido modificado en su respectiva tabla.
    */
    DROP TRIGGER IF EXISTS tg_binModifyDraw $$ 
    CREATE TRIGGER tg_binModifyDraw AFTER UPDATE ON Draws
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(SESSION_USER(), "@",1))), "admin") = Us.var_user),
                "Modificación de Dibujo"
            );

        END $$

    -- DROP TRIGGER IF EXISTS tg_binSelectDraws $$ 
    -- CREATE TRIGGER tg_binSelectDraws AFTER SELECT ON Draws
    --     FOR EACH ROW
    --     BEGIN

    --         INSERT INTO Binnacle(userId, tex_event) VALUES(
    --             (SELECT Us.id
    --                 FROM Users Us
    --                 WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
    --             "Selección y Visualización de Dibujos"
    --         );

    --     END $$

    /*
        Trigger que registra una inserción de evento en la bicácora luego de que la configuración de color de un dibujo ha sido modificado en su respectiva tabla.
    */
    DROP TRIGGER IF EXISTS tg_binModifyDrawConfig $$
    CREATE TRIGGER tg_binModifyDrawConfig AFTER UPDATE ON drawsConfig
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(SESSION_USER(), "@",1))), "admin") = Us.var_user),
                "Modificación de Configuración de Colores de Dibujo"
            );

        END $$    

    /*
        Trigger que encripta los nuevos datos agregados a la tabla de usuarios cuando detecta una insersión.
    */
    DROP TRIGGER IF EXISTS tg_addCodedUser $$
    CREATE TRIGGER tg_addCodedUser BEFORE INSERT ON Users
        FOR EACH ROW
        BEGIN

            SET NEW.var_pass = AES_ENCRYPT(NEW.var_pass, 'admin');
            SET NEW.var_user = AES_ENCRYPT(NEW.var_user, 'admin');
            SET NEW.var_category = AES_ENCRYPT(NEW.var_category, 'admin');
            
        END $$

    /*
        Trigger que encripta los nuevos datos agregados a la tabla de usuarios cuando detecta una modificación.
    */
    DROP TRIGGER IF EXISTS tg_updateCodedUser $$
    CREATE TRIGGER tg_updateCodedUser BEFORE UPDATE ON Users
        FOR EACH ROW
        BEGIN
            IF OLD.var_user <> NEW.var_user THEN
                SET NEW.var_user = AES_ENCRYPT(NEW.var_user, 'admin');
            END IF;

            IF OLD.var_pass <> NEW.var_pass THEN
                SET NEW.var_pass = AES_ENCRYPT(NEW.var_pass, 'admin');
            END IF;
        END $$

    /*
        Trigger que encripta los nuevos datos agregados a la tabla de dibujos cuando detecta una insersión.
    */
    DROP TRIGGER IF EXISTS tg_addCodedDraw $$
    CREATE TRIGGER tg_addCodedDraw BEFORE INSERT ON Draws
        FOR EACH ROW
        BEGIN
            SET NEW.var_name = AES_ENCRYPT(NEW.var_name, 'admin');
            -- SET NEW.jso_drawInfo = AES_ENCRYPT(NEW.jso_drawInfo, "admin");
        END $$

    /*
        Trigger que encripta los nuevos datos agregados a la tabla de dibujos cuando detecta una modificación.
    */
    DROP TRIGGER IF EXISTS tg_updateCodedDraw $$
    CREATE TRIGGER tg_updateCodedDraw BEFORE UPDATE ON Draws
        FOR EACH ROW
        BEGIN
            IF OLD.var_name <> NEW.var_name THEN
                SET NEW.var_name = AES_ENCRYPT(NEW.var_name, "admin");
            END IF;

        END $$

    /*
        Trigger que encripta los nuevos datos agregados a la tabla de configuración de colores de dibujo cuando detecta una modificación.
    */
    DROP TRIGGER IF EXISTS tg_updateCodedColorConfiguration $$
    CREATE TRIGGER tg_updateCodedColorConfiguration BEFORE UPDATE ON drawsConfig
        FOR EACH ROW

        BEGIN
            IF OLD.var_penColor <> NEW.var_penColor THEN
                SET NEW.var_penColor = AES_ENCRYPT(NEW.var_penColor, "admin");
            END IF;

            IF OLD.var_fillColor <> NEW.var_fillColor THEN
                SET NEW.var_fillColor = AES_ENCRYPT(NEW.var_fillColor, "admin");
            END IF;
        END $$

    DROP TRIGGER IF EXISTS tg_AddCodedColorConfiguration $$
    CREATE TRIGGER tg_AddCodedColorConfiguration BEFORE INSERT ON drawsConfig
        FOR EACH ROW
        BEGIN
            SET NEW.var_penColor = AES_ENCRYPT(NEW.var_penColor, "admin");        
            SET NEW.var_fillColor = AES_ENCRYPT(NEW.var_fillColor, "admin");        
        END $$

DELIMITER ;

CALL sp_addMainUser("Administrador");
INSERT INTO drawsConfig(var_penColor, var_fillColor) VALUES ("#000000", "#000000");