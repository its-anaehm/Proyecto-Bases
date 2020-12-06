# <span style="color:#083CC1">**Base de Datos A - Análisis**</span>

Al realizar un pequeño y minucioso estudio de los elementos que se deben representar en esta base de datos, se logró distinguir una serie de atributos necesarios para lograr un mejor desempeño en el programa.

A continuación se presenta una explicación detallada de todos los elementos que se encuentran en la Base de Datos A del archivo *DDS_version_1.sql*.

-----

## <span style="color:#146FBA">Modelado ER y Diagrama ER</span>

-----

![M&DER](https://drive.google.com/uc?export=view&id=13ynWUuLOS4r-CrPaJpXnfuOVNNLgk8R7 "M&DER.png")
Creados bajo una percepción general de las entidades, atributos y relaciones que componen la Base de Datos A se definen los siguientes:

**Entidades y sus Atributos:**

|Entidad|Atributos|Entidad|Atributos|Entidad|Atributos|Entidad|Atributos|
|---|---|---|---|---|---|---|---|
|User|id|Draws|id|Binnacle|id|drawsConfig|pennColor|
||name||userId||userId||fillcolor|
||password||name||time||||
||category||time||event||||
||||drawInfo||||||

Podemos definir el conjunto de relaciones de la siguiente manera:

- **Relación: *Users-Draws*:** Todas las relaciones de la forma Users-Draws, permiten obtener la información de los usuarios y sus respectivos dibujos. Esta relación es de cero a muchos puesto que un usuario puede ser ingresado a la base de datos pero no necesariamente tener algún dibujo realizado.
- **Relación: *Users-Binnacle*:** Todas las relaciones de la forma Users-Binnacle, permiten obtener la información de los usuarios y las actividades que desarrollan dentro del programa y guardarlas en la bitácora que representa el historial de todos los eventos. Esta relación es de uno a muchos porque es necesario que exista un usuario que interactúe con el programa para que se pueda registrar todo lo que hace.
- **Relación: *Draws-drawsConfig*:** Todas las relaciones de la forma Draws-drawsConfig, permiten obtener la información de los dibujos en cuanto a sus valores de configuración. Esta relación es de uno a muchos puesto que debe existir un dibujo para poder realizar estos cambios en la configuración.

**NOTA:** *Esta es la versión 3.0 del análisis de la base de datos*.

-----

## <span style="color:#146FBA">Análisis de las Tablas y sus Atributos</span>

-----

### <span style="color:#3498DB">**Tabla *Users***</span>

![DBA-001](https://drive.google.com/uc?export=view&id=1_LvawqUe2D5J9MyeY26Xe33Wl531Tb3h "DBA-001.png")

Se definen cuatro atributos para la tabla usuario los cuales son:

- ***id:*** Un atributo de tipo de dato entero con valor autoincremental no nulo, definido como la llave primaria de la tabla; este dato es único para cada usuario que se ingresa en la base de datos y nos permite identificarlo en cualquier otra instancia necesaria.
- ***var_user:*** Atributo de tipo de dato varchar no nulo, el cual almacena los nombre de los usuarios; estos nombres son ingresados por el mismo usuario o por el usuario administrador.
- ***var_pass:*** Atributo de tipo de dato varchar no nulo, en el que se almacena la contraseña de cada usuario en la tabla; estas contraseñas son definidas por el mismo usuario o por el usuario administrador.
- ***var_category:*** Atributo de tipo de dato varchar no nulo, en el que se define si un usuario es o no administrador.

Estos atributos son las propiedades de cada usuario necesarias para su creación y validación dentro del programa y la base de datos, los cuales solo pueden ser modificados por el administrador del programa.

### <span style="color:#3498DB">**Tabla *Draws***</span>

![DBA-002](https://drive.google.com/uc?export=view&id=19GV5mq_cjQRX3RJPYtpBxOZt6Z1unJT2 "DBA-002.png")

Se definen cinco atributos para la tabla Draws los cuales son:

- ***id:*** Un atributo de tipo de dato entero con valor autoincremental no nulo, definido como la llave primaria de la tabla; este dato es único para cada dibujo generado por los usuarios, que se ingresa en la base de datos y nos permite identificarlo en cualquier otra instancia necesaria.
- ***userId:*** Atributo de tipo de dato entero no nulo, definido en la tabla users y llave foránea de la tabla draws; este dato permite vincular a un usuario con sus dibujos en la tabla draws ya que el usuario puede realizar uno o varios dibujos.
- ***var_name:*** Atributo de tipo de dato varchar no nulo, que corresponde al nombre del dibujo creado por el usuario, este dato es asignado por el usuario ya sea un usuario normal o el administrador.
- ***tim_time:*** Atributo de tipo de dato timestamp no nulo, que guarda el registro de la hora y fecha instantánea en la que fue creado el dibujo por defecto.
- ***jso_drawInfo:*** Atributo de tipo de dato JSON no nulo, que se encarga de manejar el almacenamiento de datos del programa a la hora de la creación de un dibujo.

Estos atributos son las propiedades de cada dibujo necesarias para su creación y validación dentro del programa y la base de datos, los cuales solo pueden ser modificados por el administrador del programa.

### <span style="color:#3498DB">**Tabla *drawsConfig***</span>

![DBA-003](https://drive.google.com/uc?export=view&id=1D-LRQcfnGtVjBHN-6dFDyDJ0vRAeeNuO "DBA-003.png")

Se definen tres atributos para la tabla drawsConfig los cuales son:

- ***id:*** Un atributo de tipo de dato entero con valor autoincremental no nulo, definido como la llave primaria de la tabla; este dato es único para cada configuración, nos permite identificar cada acción que se realiza en el dibujo.
- ***var_pennColor:*** Atributo de tipo varcharno nulo, que permite saber la configuración de color de lápiz que está utilizando un usuario en su dibujo.
- ***var_fillColor:*** Atributo de tipo varchar no nulo, que permite saber la configuración de color de fondo que está utilizando un usuario en su dibujo.

Estos atributos son las propiedades de la configuración del dibujo necesarias para su creación y validación dentro del programa y la base de datos, los cuales solo pueden ser modificados por el administrador del programa.

### <span style="color:#3498DB">**Tabla *Binnacle***</span>

![DBA-004](https://drive.google.com/uc?export=view&id=1AvLWkjNyKK8ihWDynhvXGyDdJiRi87NO "DBA-4.png")

Se definen cinco atributos para la tabla Binnacle los cuales son:

- ***id:*** Un atributo de tipo de dato entero con valor autoincremental no nulo, definido como la llave primaria de la tabla; este dato es único para cada bitácora, que se ingresa en la base de datos y nos permite identificar el usuario y sus respectivos dibujos en cualquier otra instancia necesaria.
- ***userId:*** Atributo de tipo de dato entero no nulo, definido en la tabla users y llave foranea de la tabla binnacle; este dato permite vincular a un usuario con sus distintas acciones y estas serán guardadas como parte de un historial de trabajo en la bitácora.
- ***tex_event:*** Atributo de tipo de dato text no nulo, que se encarga de determinar cuál es la acción realizada dentro del programa que puede variar entre la creación, modificación y eliminación de usuarios o dibujos.
- ***tim_time:*** Atributo de tipo de dato timestamp no nulo, que guarda el registro de la hora y fecha instantánea en la que fue realizado algún evento.

Estos atributos son las propiedades de la bitácora necesarias para su creación y validación dentro del programa y la base de datos, los cuales no son modificables por ningun usuario del programa.

-----

## <span style="color:#146FBA">Análisis de Creación y Permisos para el Administrador</span>

-----

![DBA-005](https://drive.google.com/uc?export=view&id=1s5fwyu6MY5YZKwow3lcb8QT-3rkFQ_jD "DBA-005.png")

Se limpia la base de datos para poder establecer el usuario *Administrador* que será el encargado de la administración del programa, este usuario puede realizar acciones como crear, modificar y eliminar elementos tanto del usuario como de los dibujos, otorgándole privilegios especiales.

Este usuario podrá visualizar elementos de toda la base de datos que un usuario regular no podría.

-----

## <span style="color:#146FBA">Análisis de Triggers</span>

-----

Para la creación de los trigger se utilizan algunas funciones como:

- ***CURRENT_USER():*** Se encarga de devolver el nombre del contexto suplantado, que para este proyecto se solicita con el id del usuario y lo que retorna es el nombre del mismo.
- ***SUBSTRING_INDEX():***
 
**NOTA:** Se utiliza el delimitador ***"$$"***(dos signos de dólar) para especificar que las sentencias terminarán con el mismo; lo que nos sirve para pasar un trigger como una sola sentencia. Y al final de los trigger se vuelve a declarar como delimitador ***";"***(punto y coma) para las próximas sentencias de ejecución.

### <span style="color:#3498DB">**Trigger *bin_addUser***</span>

![DBA-006](https://drive.google.com/uc?export=view&id=1fxFfqB165Wm7Tt-wMy-MDBScJtBI3RRe "DBA-006.png")

Se elimina el trigger *bin_addUser* si es que este existe y posteriormente lo crea; este trigger trabaja con la tabla *Users* y la acción que realiza es que después de insertar en la tabla *Users* a un usuario, agregar el evento al historial de actividades que se encuentra en la tabla *Binnacle*.

El evento que desempeña un usuario al agregarse al programa, en este caso en específico al ser agregado a la base de datos, se hace con los valores de nombre del usuario (var_user) obteniendolo de la tabla Users e identificandolo con su id y el evento que en este caso se define como *"Inserción de Usuario"*.

### <span style="color:#3498DB">**Trigger *bin_deleteUser***</span>

![DBA-006](https://drive.google.com/uc?export=view&id=1VhzhBNKmschjRbsUO4p_1WUiH15semaK "DBA-006.png")

Se elimina el trigger *bin_deleteUser* si es que este existe y posteriormente lo crea; este trigger trabaja con la tabla *Users* y la acción que realiza es que después de eliminar en la tabla *Users* al usuario indicado, agrega el evento al historial de actividades que se encuentra en la tabla *Binnacle*.

Para este caso en específico al ser eliminado de la base de datos se debe identificar con los valores de nombre del usuario (var_user) obteniendolo de la tabla Users e identificandolo con su id y el evento que en este caso se define como *"Eliminación de Usuario"*.

### <span style="color:#3498DB">**Trigger *bin_updateUser***</span>

![DBA-006](https://drive.google.com/uc?export=view&id=1DCBlGiWcyEIzUF2UimiIrBo__a5sEdXm "DBA-006.png")

Se elimina el trigger *bin_updateUser* si es que este existe y posteriormente lo crea; este trigger trabaja con la tabla *Users* y la acción que realiza es que después de actualizar en la tabla *Users* al usuario indicado, agrega el evento al historial de actividades que se encuentra en la tabla *Binnacle*.

Al ser actualizado en la base de datos se debe identificar con los valores de nombre del usuario (var_user) obteniendolo de la tabla Users e identificandolo con su id y el evento que en este caso se define como *"Modificación de Usuario"*.

### <span style="color:#3498DB">**Trigger *bin_addDraw***</span>

![DBA-006](https://drive.google.com/uc?export=view&id=1mC1bH-Gvb5_S1M5-k5yQl9iLdzu7W6A7 "DBA-006.png")

Se elimina el trigger *bin_addDraw* si es que este existe y posteriormente lo crea; este trigger trabaja con la tabla *Draws* y la acción que realiza es que después de insertar en la tabla *Draws* un dibujo, agrega el evento al historial de actividades que se encuentra en la tabla *Binnacle*.

El evento que desempeña un usuario al agregar un dibujo al programa, en este caso en específico al agregarlo a la base de datos, se hace con los valores de nombre del usuario (var_user) obteniendolo de la tabla Users e identificandolo con su id y el evento que en este caso se define como *"Inserción de Dibujo"*.

### <span style="color:#3498DB">**Trigger *bin_deleteDraw***</span>

![DBA-006](https://drive.google.com/uc?export=view&id=1meokebtW8CNaKgj88Bh1FYs-X_18_NrD "DBA-006.png")

Se elimina el trigger *bin_deleteDraw* si es que este existe y posteriormente lo crea; este trigger trabaja con la tabla *Draws* y la acción que realiza es que después de eliminar en la tabla *Draws* al dibujo indicado, agrega el evento al historial de actividades que se encuentra en la tabla *Binnacle*.

Para este caso en específico al ser eliminado de la base de datos un dibujo, se debe identificar con los valores de nombre del usuario (var_user) obteniendolo de la tabla Users e identificandolo con su id y el evento que en este caso se define como *"Eliminación de Dibujo"*.

### <span style="color:#3498DB">**Trigger *bin_modifyDraw***</span>

![DBA-006](https://drive.google.com/uc?export=view&id=1F44qmotH5MS_4TijEASKwz43TiDPvx5G "DBA-006.png")

Se elimina el trigger *bin_modifyDraw* si es que este existe y posteriormente lo crea; este trigger trabaja con la tabla *Draws* y la acción que realiza es que después de actualizar en la tabla *Draws* al dibujo indicado, agrega el evento al historial de actividades que se encuentra en la tabla *Binnacle*.

Al ser actualizado en la base de datos se debe identificar con los valores de nombre del usuario (var_user) obteniendolo de la tabla Users e identificandolo con su id y el evento que en este caso se define como *"Modificación de Dibujo"*.
