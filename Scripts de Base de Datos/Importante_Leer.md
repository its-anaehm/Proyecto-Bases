# Bases de Datos I - III PAC 2020 #

## Ingeniero José Inestroza ##

### Comentario antes de ejecutar los scripts .sql ###

Los scripts de la base de datos deben ser ejecutados con un usuario llamado "admin" y contraseña "admin" este debe tener todos los permisos en el SGBD.

Comandos para crear el usuario con los permisos requeridos.

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

GRANT ALL PRIVILEGES ON \*.\* TO 'admin'@'localhost' WITH GRANT OPTION;
