USE DBA;

DELIMITER $$

    /*
    
    */
    DROP TRIGGER IF EXISTS tg_binAddUser $$
    CREATE TRIGGER tg_binAddUser AFTER INSERT ON Users
        FOR EACH ROW
        BEGIN            
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id                    
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(CURRENT_USER(), "@",1))), "admin") = Us.var_user),
                "Inserción de Usuario"
              );
        END $$

    DROP TRIGGER IF EXISTS tg_binDeleteUser $$ 
    CREATE TRIGGER tg_binDeleteUser AFTER DELETE ON Users
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(CURRENT_USER(), "@",1))), "admin") = Us.var_user),
                "Eliminación de Usuario"
            );
        END $$
    
    DROP TRIGGER IF EXISTS tg_binUpdateUser $$
    CREATE TRIGGER tg_binUpdateUser AFTER UPDATE ON Users
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(CURRENT_USER(), "@",1))), "admin") = Us.var_user),
                "Modificación de Usuario"
                );
        END $$

    -- DROP TRIGGER IF EXISTS tg_binSelectUsers $$
    -- CREATE TRIGGER tg_binSelectUsers AFTER SELECT ON Users
    --     FOR EACH ROW
    --     BEGIN
    --         INSERT INTO Binnacle(userId, tex_event) VALUES(
    --             (SELECT Us.id
    --                 FROM Users Us
    --                 WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
    --             "Selección y Visualización de Usuarios"
    --             );
    --     END $$

    DROP TRIGGER IF EXISTS tg_binAddDraw $$
    CREATE TRIGGER tg_binAddDraw AFTER INSERT ON Draws
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(CURRENT_USER(), "@",1))), "admin") = Us.var_user),
                "Inserción de Dibujo"
                );
        END $$
    
    DROP TRIGGER IF EXISTS tg_binDeleteDraw $$    
    CREATE TRIGGER tg_binDeleteDraw AFTER DELETE ON Draws
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(CURRENT_USER(), "@",1))), "admin") = Us.var_user),
                "Eliminación de Dibujo"
                );
        END $$
    
    DROP TRIGGER IF EXISTS tg_binModifyDraw $$ 
    CREATE TRIGGER tg_binModifyDraw AFTER UPDATE ON Draws
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(CURRENT_USER(), "@",1))), "admin") = Us.var_user),
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

    DROP TRIGGER IF EXISTS tg_binModifyDrawConfig $$
    CREATE TRIGGER tg_binModifyDrawConfig AFTER UPDATE ON drawsConfig
        FOR EACH ROW
        BEGIN

            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id
                    FROM Users Us
                    WHERE AES_ENCRYPT(((SUBSTRING_INDEX(CURRENT_USER(), "@",1))), "admin") = Us.var_user),
                "Modificación de Configuración de Colores de Dibujo"
            );

        END $$    

    DROP TRIGGER IF EXISTS tg_addCodedUser $$
    CREATE TRIGGER tg_addCodedUser BEFORE INSERT ON Users
        FOR EACH ROW
        BEGIN

            SET NEW.var_pass = AES_ENCRYPT(NEW.var_pass, 'admin');
            SET NEW.var_user = AES_ENCRYPT(NEW.var_user, 'admin');
            SET NEW.var_category = AES_ENCRYPT(NEW.var_category, 'admin');
            
        END $$

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

    DROP TRIGGER IF EXISTS tg_addCodedDraw $$
    CREATE TRIGGER tg_addCodedDraw BEFORE INSERT ON Draws
        FOR EACH ROW
        BEGIN
            SET NEW.var_name = AES_ENCRYPT(NEW.var_name, "admin");
            SET NEW.jso_drawInfo = AES_ENCRYPT(NEW.jso_drawInfo, "admin");
        END $$

    DROP TRIGGER IF EXISTS tg_updateCodedDraw $$
    CREATE TRIGGER tg_updateCodedDraw BEFORE UPDATE ON Draws
        FOR EACH ROW
        BEGIN
            IF OLD.var_name <> NEW.var_name THEN
                SET NEW.var_name = AES_ENCRYPT(NEW.var_name, "admin");
            END IF;

            IF OLD.jso_drawInfo <> NEW.jso_drawInfo THEN
                SET NEW.jso_drawInfo = AES_ENCRYPT(NEW.jso_drawInfo, "admin");
            END IF;
        END $$

    DROP TRIGGER IF EXISTS tg_updateCodedColorConfiguration $$
    CREATE TRIGGER tg_updateCodedColorConfiguration BEFORE UPDATE ON Draws
        FOR EACH ROW
        -- ? que es esto? entiendo
        -- modificaciones encriptadas para las configuraciones de color 
        -- penn color y fill color
        BEGIN
            IF OLD.var_penColor <> NEW.var_penColor THEN
                SET NEW.var_penColor = AES_ENCRYPT(NEW.var_penColor, "admin");
            END IF;

            IF OLD.var_fillColor <> NEW.var_fillColor THEN
                SET NEW.var_fillColor = AES_ENCRYPT(NEW.var_fillColor, "admin");
            END IF;
        END $$

DELIMITER ;

CALL sp_addMainUser("Administrador");