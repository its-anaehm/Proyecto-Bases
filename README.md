# Bases de Datos I - III PAC 2020 #

## Paint con usuarios ##

## Definición ##

* El protecto debe realizarse por equipos, según lo descrito en la Planificación Académica de la clase.

* El código debe ser entregado mediante un archivo de compresión 7z https://www.7-zip.org/

* Crear un programa en Python3 que haga uso de MariaDB/MySQL (en compatibilidad) para el almacenamiento, modificación, eliminación y recuperación de datos. El propósito del proyecto es hacer uso del código fuente hecho en Tkinter del sistema de dibujo del capítulo 1.4 del libro “Data Structures and Algorithms with Python” (ver debajo) usado en múltiples clases de Algoritmos y Estructuras de Datos de la carrera de Ingeniería en Sistemas de la UNAH,  reemplazando y sustituyendo los componentes de almacenamiento de datos del programa los cuales usan XML, y en su lugar creando almacenamiento de datos mediante JSON en una base de datos A, y en archivo JSON de respaldo con compresión (mediante Python3 y Linux) en una base de datos B. Adicionalmente, los programadores de cada equipo de trabajo deberán agregarle al sistema un módulo de autenticación, un módulo de registros de bitácora, una pantalla para creación, modificación y eliminación de usuarios, adicionalmente al componente de dibujo incluido en el código fuente al cual tendrá acceso siguiendo las indicaciones del libro.

    * El manejo de JSON debe ser mediante el tipo de dato JSON.

    * Todos los datos del sistema (con excepción de la bitácora, ver más adelante) deben estar encriptados usando la contraseña del usuario administrador. Debe existir un usuario administrador inicial en el sistema ya registrado en la base de datos.

    * El manejo de archivos BLOB debe ser mediante archivos “.json”.

    * Los datos de “Pen Color” y “Fill Color” deben tener valores de configuración en la base de datos, modificables por el administrador.

    * El administrador debe poder ser capaz de crear usuarios operadores. Un usuario operador puede crear dibujos y visualizar únicamente los dibujos creados por él mismo. Un usuario administrador puede crear y visualizar dibujos, y gestionar (crear, modificar nombre y contraseña, y eliminar) usuarios.

    * La bitácora deberá guardar todas las acciones del usuario, incluyendo, autenticación, visualización, creación, modificación, eliminación de dibujos, configuraciones (colores) y usuarios.

    * El estudiante debe seguir las indicaciones del libro para implementar el código del programa ya existente de generación de dibujos.

    * Sobre el menú File:

        * El menú “File->New” debe crear una nueva imagen dentro del repositorio de dibujos del usuario autenticado.

        * El menú “File->Load” debe permitir al usuario elegir un dibujo desde la base de datos, limitándose a mostrar únicamente los dibujos de este usuario. El listado de dibujos debe aparecer mediante nueva ventana, y al seleccionar un dibujo y presionar aceptar, ese dibujo se debe cargar en la pantalla de dibujo. Si el sistema no tiene dibujos de este usuario, el programa debe estar preparado para no fallar con error.

        * El menú “File->Load Intro” debe eliminarse.

    * El menú “File->Save As”, debe poder sobreescribir el dibujo ya existente en la base de datos A, o guardar la imagen como un nuevo dibujo en la base de datos A. Al mismo tiempo se debe guardar un archivo equivalente BLOB (compreso) en la base de datos B de respaldo. El contenido de dibujo de la base de datos B debe ser equivalente al dibujo de la base de datos A.

    * Se debe crear un nuevo menú “File->Download” que debe descargar el archivo guardado como “.json” en la base de datos de respaldo.

    * Se debe crear un nuevo menú “File->Configure” que debe ser visible únicamente por el usuario administrador, el cual debe habilitar una ventana donde se puedan gestionar los usuarios y modificar los valores de color antes mencionados.
