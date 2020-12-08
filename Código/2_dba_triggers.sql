USE DBA;

DELIMITER $$

    DROP TRIGGER IF EXISTS tg_binAddUser $$
    CREATE TRIGGER tg_binAddUser AFTER INSERT ON Users
        FOR EACH ROW
        BEGIN            
            INSERT INTO Binnacle(userId, tex_event) VALUES(
                (SELECT Us.id                    
                    FROM Users Us
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
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
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
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
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
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
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
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
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
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
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
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
                    WHERE ((SUBSTRING_INDEX(CURRENT_USER(), "@",1))) = Us.var_user),
                "Modificación de Configuración de Colores de Dibujo"
            );

        END $$

DELIMITER ;