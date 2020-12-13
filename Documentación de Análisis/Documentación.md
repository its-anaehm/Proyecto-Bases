    Universidad Nacional Autónoma de Honduras (UNAH)
    III PAC 2020   
    Clase: Bases de Datos I
    Sección: 0900
    Catedrático: José Manuel Inestroza Murillo
    Alumnos: Emilio Sebastián Sosa Amador - 20171003818 - emilio.sosa@unah.hn
            Moisés David Gómez Amador - 20181001683 - mdgomeza@unah.hn
            Leonardo Mass Sosa - 20171031716 - leonardo.mass@unah.hn
            Ana Evelin Hernández Martínez - 20171001620 - aehernandezm@unah.hn

# **Proyecto Final - Documentación (Análisis e Investigación)**

## **Índice**

- [**Proyecto Final - Documentación (Análisis e Investigación)**](#proyecto-final---documentación-análisis-e-investigación)
  - [**Índice**](#índice)
  - [**Lluvia de Ideas**](#lluvia-de-ideas)
    - [**Modelados ER y Diagramas ER**](#modelados-er-y-diagramas-er)
  - [**Diseño de Ventanas y sus Funciones**](#diseño-de-ventanas-y-sus-funciones)
    - [*Ventana de Bienvenida*](#ventana-de-bienvenida)
    - [*Ventana de Inicio*](#ventana-de-inicio)
    - [*Ventana de Dibujo*](#ventana-de-dibujo)
    - [*Ventana de salvado de Dibujo*](#ventana-de-salvado-de-dibujo)
    - [*Ventana para seleccionar un dibujo existente*](#ventana-para-seleccionar-un-dibujo-existente)
    - [*Ventana de configuración*](#ventana-de-configuración)
    - [*Ventána para cambios de color*](#ventána-para-cambios-de-color)
    - [*Ventana de agregar usuario*](#ventana-de-agregar-usuario)
    - [*Ventana para selección de usuario*](#ventana-para-selección-de-usuario)
    - [*Ventana para la modificación de datos del usuario*](#ventana-para-la-modificación-de-datos-del-usuario)
    - [*Ventana para eliminar usuario*](#ventana-para-eliminar-usuario)
    - [*Ventana de descarga*](#ventana-de-descarga)
    - [*Ventana de la Bitácora*](#ventana-de-la-bitácora)
  - [**Elementos Conceptuales**](#elementos-conceptuales)
    - [**Tkinter**](#tkinter)
    - [**configparser**](#configparser)
    - [**JSON**](#json)
    - [**MySQL Connector**](#mysql-connector)
  - [**Bitácora de Actividades**](#bitácora-de-actividades)
    - [**- Lunes 23/11/2020**](#--lunes-23112020)
    - [**- Martes 24/11/2020**](#--martes-24112020)
    - [**- Miércoles 25/11/2020**](#--miércoles-25112020)
    - [**- Jueves 26/11/2020**](#--jueves-26112020)
    - [**- Viernes 27/11/2020**](#--viernes-27112020)
    - [**- Sábado 28/11/2020**](#--sábado-28112020)
    - [**- Domingo 29/11/2020**](#--domingo-29112020)
    - [**- Lunes 30/11/2020**](#--lunes-30112020)
    - [**- Martes 01/12/2020**](#--martes-01122020)
    - [**- Miércoles 02/12/2020**](#--miércoles-02122020)
    - [**- Jueves 03/12/2020**](#--jueves-03122020)
    - [**- Viernes 04/12/2020**](#--viernes-04122020)
    - [**- Sábado 05/12/2020**](#--sábado-05122020)
    - [**- Domingo 06/12/2020**](#--domingo-06122020)
    - [**- Lunes 07/12/2020**](#--lunes-07122020)
    - [**- Martes 08/12/2020**](#--martes-08122020)
    - [**- Miercoles 09/12/2020**](#--miercoles-09122020)
    - [**- Jueves 10/12/2020**](#--jueves-10122020)
    - [**- Viernes 11/12/2020**](#--viernes-11122020)
    - [**- Sábado 12/12/2020**](#--sábado-12122020)
    - [**- Domingo 13/12/20200**](#--domingo-131220200)
  - [**NOTAS Y BIBLIOGRÍAS**](#notas-y-bibliogrías)

## **Lluvia de Ideas**

-----

### **Modelados ER y Diagramas ER**

A continuación se presentan los diagramas y modelados finales para ambas bases de datos con sus versiones correspondientes

Versión 3.0 del diagrama y modelado para la base de datos A.

![M&D-ER-A](https://drive.google.com/uc?export=view&id=13ynWUuLOS4r-CrPaJpXnfuOVNNLgk8R7 "M&D-ER-A.png")

Versión 1.0 del diagrama y modelado para la base de datos B.

![M&D-ER-B](https://drive.google.com/uc?export=view&id=1V1G3cDie8m9x_CHkYszBgZ4S9EvJCxpR "M&D-ER-B.png")

-----

## **Diseño de Ventanas y sus Funciones**

-----

> En esta sección se muestran las ventanas del proyecto y las actividades que se pueden realizar en las mismas.

### *Ventana de Bienvenida*

En esta venta se muestra el logo creado por los miembros del equipo para el proyecto como bienvenida al mismo y un botón que le permitirá acceder a la siguiente ventana.

![01](https://drive.google.com/uc?export=view&id=1b0aPBEtBsdkrnYVausCXf8Mj7R0_tPU2 "01.png")

### *Ventana de Inicio*

Para esta ventana se le pide al usuario del programa que ingrese sus datos de validación los cuales son su nombre y contraseña de usuario, junto a un botón que le brinda el acceso a la siguiente ventana.

![02](https://drive.google.com/uc?export=view&id=1iFOckdtBTh1KqK9gHkwJl7F7NL5h1t3r "02.png")

### *Ventana de Dibujo*

Esta ventana hace uso del código fuente hecho en Tkinter del sistema de dibujo del capítulo 1.4 del libro “Data Structures and Algorithms with Python” aquí los usuarios pueden crear sus dibujos y posteriormente guardarlos.

![03](https://drive.google.com/uc?export=view&id=1-p6dgrKgnsXpad5bUpZRS3aebE5V7BOK "03.png")

### *Ventana de salvado de Dibujo*

Una vez que el usuario ha terminado de crear su dibujo y procede a guardarlo en la opción que se encuentra en el menú file se despliega una ventana adicional en la cual se le pide que ingrese un nombre para que este sea guardado.

![04](https://drive.google.com/uc?export=view&id=1IfH9iOib56R39cCk8ucQ_LR0pNN8CQfb "04.png")

### *Ventana para seleccionar un dibujo existente*

Si un usuario que ingresa a la ventana de dibujo pero quiere abrir un dibujo ya existente se va al menú file donde encontrará una opción para abrir dibujos existentes y se desplegará una ventana que le muestre únicamente los dibujos que ese usuario ha creado para que seleccione uno.

![05](https://drive.google.com/uc?export=view&id=1b2A6NXNv_WX3FXcwHDIH_ceq4Iw1qmnv "05.png")

### *Ventana de configuración*

La ventana de configuración estará disponible en el menú file únicamente para el usuario administrador. En esta ventana se le permite al usuario administrador hacer cambios tanto en la configuración de usuario como en la configuración de los dibujos.

![06](https://drive.google.com/uc?export=view&id=1YtZPfH21OyayTDfdYPGNqGdWQ7SflJ4x "06.png")

### *Ventána para cambios de color*

Si el administrador desea hacer cambios en la configuración de los colores del dibujo aparecerá una ventana en la cuál se desplegarán las opciones de color.

![07](https://drive.google.com/uc?export=view&id=1jzwLcdqSUQN1zUxmsmGcWREc-RSfTkJF "07.png")

### *Ventana de agregar usuario*

Cuando el administrador desee agregar un nuevo usuario al programa aparecerá una ventana donde le pide los datos para la validación del usuario a ingresar que son el nombre y la contraseña.

![08](https://drive.google.com/uc?export=view&id=1qu03X4p-hlwWbtITLC_nF18OXtHipLGs "08.png")

### *Ventana para selección de usuario*

Si el administrador desea cambiar los datos de un usuario debe seleccionar esta opción en el menú de la ventana de configuración posteriormente le aparecerá una ventana con todos los nombres de los usuarios registrados en la base de datos para que seleccione al usuario a modificar.

![09](https://drive.google.com/uc?export=view&id=1FKvFmuVXQQWBh5bdErTGlK_A6QUWXKnH "09.png")

### *Ventana para la modificación de datos del usuario*

Una vez que el administrador ya seleccionó un usuario le aparecerá una ventana donde debe de dar click al botón que corresponde a la acción que desea realizar ya sea la de cambiar nombre o cambiar contraseña del usuario a modificar. Luego de esto se desplegará otra ventana que le permitirá cambiar el nombre o contraseña dependiendo de su selección.

![10](https://drive.google.com/uc?export=view&id=1TJZplJ3FB3wqC6gRPHnxnkZgIH5549iN "10.png")

### *Ventana para eliminar usuario*

Cuando el administrador seleccione la opción de eliminar a un usuario se desplegará una ventana que le muestre a todos los usuarios en la base de datos del programa para seleccionar a quien eliminar.

![11](https://drive.google.com/uc?export=view&id=15VAOXIV3T3o3NMaB2kBCWKTK6wlWi_Iz "11.png")

### *Ventana de descarga*

Si un usuario desea descargar uno de sus dibujos selecciona esta opción en el menú file y se desplegará una ventana que le muestre los dibujos realizados por él, donde deberá seleccionar el dibujo a descargar.

![12](https://drive.google.com/uc?export=view&id=1JhEJYeKfa2nonlp85F2dwmOTosRlyJHg "12.png")

### *Ventana de la Bitácora*

Si el administrador desea revisar la bitácora de eventos está opción le aparecerá en el menú file y se desplegará una ventana que detalla todas las acciones realizadas en el programa.

![13](https://drive.google.com/uc?export=view&id=18I4_A1gsAg4PfAx69Qiq4OEw0mV7OdX_ "13.png")

-----

## **Elementos Conceptuales**

En el proyecto se hacen uso de algunas librerías y clases de Python que se definirán a continuación:

### **Tkinter**

-----

Es una librería que proporciona a las aplicaciones de Python una interfaz de usuario fácil de programar. Además es un conjunto de herramientas GUI de Tcl/Tk (Tcl: Tool Command Language), proporcionando una amplia gama de usos, incluyendo aplicaciones web, de escritorio, redes, administración, pruebas y muchos más.

Tkinter no es solo la única librería para python especializada en la creación de interfaces gráficas, entre las más empleadas están wxPython, PyQt y PyGtk, todas con ventajas y desventajas. Entre los puntos fuertes que caracterizan a Tkinter en la creación de GUI, es que viene instalado con python en casi todas las plataformas, su sintaxis es clara, fácil de aprender y documentación completa.

**Ejemplo:** *holaMundo_tk* - Ventana con mensaje "¡Hola Mundo!"

    import tkinter as tk

    class MainWindow:
       def __init__(self, root):
           root.geometry("100x50")
           button = tk.Button(root, text="Hola", command=self.hola)
           button.pack()

       def hola(self):
           print("¡Hola mundo!")

    app = tk.Tk()
    window = MainWindow(app)
    app.mainloop()

### **configparser**

-----

Es una clase que proporciona una función llamada *interpolation* que se puede usar para combinar valores juntos. Los valores que contienen cadenas de formato Python estándar activan la función de interpolación cuando se recuperan. Las opciones nombradas dentro del valor que se está recuperando se reemplazan por sus valores, hasta que no sea necesaria más sustitución.

La interpolación se realiza por defecto cada vez que se llama a *get()*. Pasa un valor verdadero en el argumento raw para recuperar el valor original, sin interpolación.

**Ejemplo:** *configparser_interpolation.py*

    from configparser import ConfigParser

    parser = ConfigParser()
    parser.read('interpolation.ini')

    print('Original value       :', parser.get('bug_tracker', 'url'))

    parser.set('bug_tracker', 'port', '9090')
    print('Altered port value   :', parser.get('bug_tracker', 'url'))

    print('Without interpolation:', parser.get('bug_tracker', 'url', raw=True))

### **JSON**

Es un formato de intercambio de datos ligero inspirado en la sintaxis literal de objetos JavaScript[6].

**Ejemplo:** *impresión de datos*

    >>> import json
    >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
    {
       "4": 5,
       "6": 7
    }

### **MySQL Connector**

MySQL Connector/Python[7] permite que los programas Python accedan a las bases de datos MySQL, utilizando una API que cumple con la especificación de la API de la base de datos de Python v2.0 (PEP 249).

MySQL Connector/Python incluye soporte para:

- Casi todas las funciones proporcionadas por MySQL Server hasta MySQL Server version 8.0 inclusive.
- Connector/Python 8.0 también es compatible con X DevAPI. Para obtener documentación de los conceptos y el uso de MySQL Connector/Python con X DevAPI, consulte la Guía del usuario de X DevAPI.
- Conversión de valores de parámetros entre tipos de datos de Python y MySQL, por ejemplo, Python datetime y MySQL DATETIME. Puede activar la conversión automática por conveniencia o desactivarla para un rendimiento óptimo.
- Todas las extensiones de MySQL a la sintaxis SQL estándar.
- Compresión de protocolo, que permite comprimir el flujo de datos entre el cliente y el servidor.
- Conexiones usando sockets TCP/IP y en Unix usando sockets Unix.
- Conexiones TCP/IP seguras mediante SSL.
- Conductor autónomo. Connector/Python no requiere la biblioteca cliente MySQL ni ningún módulo de Python fuera de la biblioteca estándar.

Connector/Python no es compatible con los antiguos métodos de autenticación de MySQL Server, lo que significa que las versiones de MySQL anteriores a 4.1 no funcionarán.

-----

## **Bitácora de Actividades**

-----

> A continuación se especifican todas las actividades que se realizaron de forma detallada para el desarrollo del proyecto, desde su inicio hasta el día de entrega.

### **- Lunes 23/11/2020**

Por la tarde del día 23 de Noviembre se presentó la definición del proyecto por parte del catedrático responsable de la clase, de la cual se hizo lectura ese mismo día.

Se planificó una reunión[1] para el siguiente día con motivo de la discusión del proyecto[2].

### **- Martes 24/11/2020**

Se desarrolló la reunión planificada en la cual se hizo una lectura grupal de la definición del proyecto junto con todos sus componentes y una pequeña distribución de asignaciones.

Se creó el repositorio en Github donde se estará actualizando el código del proyecto de acuerdo a los avances logrados y se realizó un rapido análisis del código fuente hecho en Tkinter[3] propuesto en el libro *"Data Structures and Algorithms with Python”* Capítulo 1.4[4], y con el cual se deben construir las pantallas del proyecto.

![Repositorio-Gitbub](https://drive.google.com/uc?export=view&id=1n6Oy_77WTuLCBiJ7cMeUYv40s7b9CW9i "Repositorio-Gitbub.png")

Se llegó a un acuerdo de seguír con el trabajo el siguiente día para poder hacer lectura de toda la documentación necesaria para poder comenzar con el proceso de codificación del proyecto.

### **- Miércoles 25/11/2020**

Al iniciar la reunión se creó un documento en la plataforma de [Lucidchart](http://www.lucid.app/) para poder realizar los esquemas y diagramas ER correspondientes para la creación de la base de datos.

![Lucidchart](https://drive.google.com/uc?export=view&id=1YfOQMqnwooRdjliYuUqM6akbNY1nXOeq "Lucidchart.png")

Durante este proceso se analizaron todos los elementos que se debían considerar en la base de datos.

### **- Jueves 26/11/2020**

Se comenzó a trabajar en la estructura de la base de datos con tres tablas (una para usuarios, una para dibujos, y otra para la bitácora)

![BD1](https://drive.google.com/uc?export=view&id=1w4RpJ1BqMrcHn3hwbbApx3cTEBv1PGr- "BD1.png")

También se obtuvo un progreso con la generación de datos y archivos en JSON, al igual que con el objeto encargado de cifrar datos.

### **- Viernes 27/11/2020**

Se desarrolló una reunión para analizar cuáles serían las ventanas necesarias para la interacción del usuario con el programa además de hacer una lluvia de ideas sobre cómo se debían de ver estas.

Se ordenó el JSON para obtener de forma precisa los datos de los archivos.

### **- Sábado 28/11/2020**

Se comenzaron a programar las ventanas del proyecto utilizando la librería tkinter, para que posteriormente las acciones que se puedan llevar a cabo en estas se conecten con la base de datos y el resto del programa.

También se creó el archivo que funciona como motor de conexión entre la base de datos y el programa.

Junto a un análisis poco enriquecido se intentó hacer bajo procedimientos en sql la eliminación de usuarios y visualización de dibujos. Elementos cuya revisión queda pendiente.

### **- Domingo 29/11/2020**

Al avanzar con el análisis del proyecto se creó una cuarta tabla que permitía almacenar los datos de configuración de dibujo y que a su vez ayudaba con la necesidad de normalizar la base de datos del programa.

También se logró completar una segunda versión para el cifrado de datos.

### **- Lunes 30/11/2020**

Al ya contar con un avance en cuanto a la programación de las ventanas del proyecto se decidieron hacer las primeras pruebas de estas y su conexión entre sí.

### **- Martes 01/12/2020**

Este día se hizo la última publicación de lecturas por parte del catedrático de la clase por lo que se dio un paro a las actividades del proyecto con el objetivo de que todos los miembros del equipo completaran las lecturas de la segunda unidad de la clase.

### **- Miércoles 02/12/2020**

A partir de este día se retomó el trabajo en grupo durante sesiones por la plataforma de discord.

Aplicando lo que se comprendió de las lecturas se decidió implementar trigger para la inserción, eliminación y modificación de usuarios y dibujos en la base de datos.

Se hicieron unos pequeños arreglos en algunas de las ventanas del proyecto que no cumplían con los requerimientos necesarios. Se realizó una función registro para insertar en la bitácora el inicio de sesión de un usuario y también se agregó línea de "grant" para darle permisos de inserción de dibujos a usuarios operadores del programa.

### **- Jueves 03/12/2020**

Se agregaron opciones "grant" para dar permisos a los usuarios administradores, así como también se lograron concretar las funciones para la creación y eliminación de usuarios.

Y junto a un poco de frustración se siguieron modificando elementos de las ventanas que eran poco satisfactorios en el proyecto agregando una ventana para la eliminación de los usuarios.

### **- Viernes 04/12/2020**

Se logró un avance con la verificación de datos en algunas entradas del programa como ser el caso de dibujos y usuarios, junto con esto se logró ejecutar el proceso de guardado de dibujos y la obtención de estos en una lista para mostrarselos a los usuarios.

### **- Sábado 05/12/2020**

A lo largo de la jornada de trabajo de este día se obtuvieron varios logros entre ellos se encuentra la lectura de dibujos en la base de datos y la modificación y eliminación de estos.

Se creó una ventana de configuración en la cual se podrán modificar elementos de color en los dibujos. También se creó el logo para mostrar en la pantalla de bienvenida del programa.

El programa logró ser capaz de guardar los cambios en la configuración de colores que realiza el usuario administrador del programa.

### **- Domingo 06/12/2020**

No fue un día muy fructífero puesto que se comenzó con el proceso de encriptación de datos el cual se planea poder desarrollar con funciones de encriptación y desencriptar en sql pero hasta el momento no funciona como se espera que deba hacerlo.

![BD1](https://drive.google.com/uc?export=view&id=15sQJSlyt6rW2iKfESCDnyg7XEvC_tHZk "BD1.png")

### **- Lunes 07/12/2020**

Durante la reunión de este día se realizó el análisis de la base de datos B así como su programación para que ya fuese funcional según los requerimientos detallados en la definición del proyecto.

La encriptación se pospuso por un rato hasta que se logró encontrar una forma factible para poder realizar ese proceso.

### **- Martes 08/12/2020**

Se identificó que un factor por los que se dificulta el proceso de desencriptar era porque buscaba hacerlo con elementos no encriptados y se le dió solución a este inconveniente.

### **- Miercoles 09/12/2020**

Con la confirmación de extensión de tiempo para la entrega del proyecto los miembros del grupo se tomaron el día para poder cumplir con las asignaciones académicas de otras clases.

### **- Jueves 10/12/2020**

Se implementó la encriptación con AES que brindó una luz verde para esta acción. Pero se encontraron problemas con el guardado del JSON por errores con los tipos de datos.

También se realizó el proceso de documentar con docstring todos los archivos del proyecto.

### **- Viernes 11/12/2020**

Este día se dio por finalizado el proyecto luego de arreglar unos errores que surgían al modificar un dibujo.

### **- Sábado 12/12/2020**

Se realizó la grabación del video requerido como parte de las asignaciones del proyecto y se terminó de documentar todo.

### **- Domingo 13/12/20200**

Día de presentación del proyecto.

-----

## **NOTAS Y BIBLIOGRÍAS**

-----

- [1]: Todas las reuniones síncronas del equipo de trabajo se llevaron a cabo en Discord la cual es una aplicación freeware de diálogo y texto. Estas reuniones se realizaban a partir de las 4pm cuando los miembros del equipo ya habian terminados sus jornada academica para así contar con a disposición de tiempo necesaria para poder cumplir con los deberes del proyecto.

![Server-Discord](https://drive.google.com/uc?export=view&id=1m3_0Gf8dQZMjbiqkJnC5yNubM12qT0gn "Server-Discord.png")

- [2]: Para las discución y la planeación del proyecto de forma asíncrona se creó un grupo de whatsapp y se le dio uso al canal de texto en el servidor de Discord.
- [3] "tkinter - Interfaz de Python a Tcl / Tk - Documentación de Python 3.9.1", Docs.python.org , 2020. [En línea]. Disponible: https://docs.python.org/3/library/tkinter.html. [Consultado: 24 de Noviembre de 2020].
- [4] "configparser - Analizador de archivos de configuración - Documentación de Python 3.9.1", Docs.python.org , 2020. [En línea]. Disponible: https://docs.python.org/3/library/configparser.html. [Consultado: 24 de noviembre de 2020].
- [5] K. Lee y S. Hubbard, Estructuras de datos y algoritmos con Python. , 2ª ed. Springer, 2015.
- [6] "json - Codificador y decodificador JSON - Documentación de Python 3.9.1", Docs.python.org , 2020. [En línea]. Disponible: https://docs.python.org/3/library/json.html. [Consultado: 06-Dic-2020].
- [7] "MySQL :: MySQL Connector / Python Developer Guide :: 1 Introducción a MySQL Connector / Python", Dev.mysql.com , 2020. [En línea]. Disponible: https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html. [Consultado: 07-Dic-2020].
- [8]: Para las reuniones donde se debia programar en conjunto se llevaróna a cabo sesiones a través de la extensión de visual studio code - live shere.
