# <span style="color:#083CC1">**Base de Datos B - Análisis**</span>

Al realizar un pequeño y minucioso estudio de los elementos que se deben representar en esta base de datos, se logró distinguir una serie de atributos necesarios para lograr un mejor desempeño en el programa.

A continuación se presenta una explicación detallada de todos los elementos que se encuentran en la Base de Datos B del archivo *DDS_B.sql*.

-----

## <span style="color:#146FBA">Modelado ER y Diagrama ER</span>

-----

La base de datos B es requerida para guardar archivos JSON de resaldo con compresión. Estos archivos JSON deben ser los mismos que se almacenan en la base de datos A con tipo de dato JSON y que funcionan como componentes de almacenamiento de datos del sistema de dibujo.

![M&DER](https://drive.google.com/uc?export=view&id=1KU8MS-PngERSjkfhbSpVskMQUXF67q3u "M&DER.png")

Este diagrama y modelado fueron creados bajo la percepción general de la entidad *Draws* con sus atributos:

- id
- userId
- name
- drawInfo

Ya que esta base de datos solo debe de funcionar como un respaldo de la información de los dibujos en el programa no se establece relación con ninguna otra entidad.

**NOTA:** *Esta es la versión 1.0 del análisis de la base de datos*

-----

## <span style="color:#146FBA">Análisis de la Tabla y sus Atributos</span>

-----

### <span style="color:#3498DB">**Tabla *Draws***</span>

Esta tabla representa los dibujos creados por los usuarios que pasan a la base de datos B como archivos encriptados.

![DBA-002](https://drive.google.com/uc?export=view&id=1DxnNanewDetG0WYMo1VBJOwjPTlu_SwK "DBA-002.png")

Se definen cuatro atributos para la tabla Draws los cuales son:

- ***id:*** Un atributo de tipo de dato entero con valor autoincremental, definido como la llave primaria de la tabla; este dato es único para cada dibujo generado por los usuarios, que se ingresa en la base de datos y nos permite identificarlo en cualquier otra instancia necesaria.
- ***userId:*** Atributo de tipo de dato entero no nulo, definido en la tabla users y llave foránea de la tabla draws; este dato permite vincular a un usuario con sus dibujos en la tabla draws ya que el usuario puede realizar uno o varios dibujos.
- ***var_name:*** Atributo de tipo de dato varchar no nulo, que corresponde al nombre del dibujo creado por el usuario, este dato es asignado por el usuario, ya sea un usuario normal o el administrador.
- ***blo_drawInfo:*** Atributo de tipo de dato BLOB no nulo. Este dato contiene el archivo .json encriptado con la información de respaldo de los dibujos en la base de datos A.

Estos atributos son las propiedades de cada dibujo necesarias como respaldo dentro del programa y la base de datos B, los cuales solo pueden ser modificados en caso de que lo haga el  administrador del programa.
