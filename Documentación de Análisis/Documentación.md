    Universidad Nacional Autónoma de Honduras (UNAH)
    III PAC 2020    
    Clase: Bases de Datos I
    Sección: 0900
    Catedrático: José Manuel Inestroza Murillo
    Alumnos: Emilio Sebastián Sosa Amador - 20171003818
             Moisés David Gómez Amador - 20181001683
             Leonardo Mass Sosa - 20171031716
             Ana Evelin Hernández Martínez - 20171001620

# **Proyecto Final - Documentación (Análisis e Investigación)**

## **Índice**

- [**Proyecto Final - Documentación (Análisis e Investigación)**](#proyecto-final---documentación-análisis-e-investigación)
  - [**Índice**](#índice)
  - [**Lluvia de Ideas**](#lluvia-de-ideas)
    - [Modelado ER y Diagrama ER](#modelado-er-y-diagrama-er)
  - [**Elementos Conceptuales**](#elementos-conceptuales)
    - [**Tkinter**](#tkinter)
    - [**configparser**](#configparser)
  - [**Bitácora de Actividades**](#bitácora-de-actividades)
    - [**- Lunes 23/11/2020**](#--lunes-23112020)
    - [**- Martes 24/11/2020**](#--martes-24112020)
    - [**- Miércoles 25/11/2020**](#--miércoles-25112020)
    - [**- Jueves 26/11/2020**](#--jueves-26112020)
    - [**- Viernes 27/11/2020**](#--viernes-27112020)
    - [**- Sábado 28/11/2020**](#--sábado-28112020)
    - [**- Domingo 29/11/2020**](#--domingo-29112020)
    - [**- Lunes 30/11/2020**](#--lunes-30112020)
    - [**- Martes 01/11/2020**](#--martes-01112020)
    - [**- Miércoles 02/11/2020**](#--miércoles-02112020)
    - [**- Jueves 03/11/2020**](#--jueves-03112020)
    - [**- Viernes 04/11/2020**](#--viernes-04112020)
    - [**- Sábado 05/11/2020**](#--sábado-05112020)
    - [**- Domingo 06/11/2020**](#--domingo-06112020)
    - [**- Lunes 07/11/2020**](#--lunes-07112020)
    - [**- Martes 08/11/2020**](#--martes-08112020)
    - [**- Miércoles 09/11/2020**](#--miércoles-09112020)
  - [**NOTAS**](#notas)

## **Lluvia de Ideas**

-----

### Modelado ER y Diagrama ER

Versión 1.0 del diagrama y modelado para la base de datos.

![MER-DER](https://drive.google.com/uc?export=view&id=19ON6s6Hk1CDcWWUe4Z46ZKGqVv8zEnkf "MER-DER.png")

-----

## **Elementos Conceptuales**

En el proyecto se hacen uso de algunas librerias y clases de Python que se definiran acontinuación:

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

-----

## **Bitácora de Actividades**

-----

> A continuación se especifican todas las actividades que se realizaron de forma detallada para el desarrollo del proyecto, desde su inicio hasta el día de entrega.

### **- Lunes 23/11/2020**

Por la tarde del día 23 de Noviembre se presentó la definición del proyecto por parte del catedrático responsable de la clase, de la cual se hizo lectura ese mismo día.

Se planificó una reunión[1] para el siguiente día con motivo de la discusión del proyecto[2].

### **- Martes 24/11/2020**

Se desarollo la reunión planificada en la cual se hizo una lectura grupal de la definición del proyecto junto con todos sus componentes y una pequeña distribución de asignaciones.

Se creó el repositorio en Github donde se estará actualizando el código del proyecto de acuerdo a los avances logrados y se realizó un rapido análisis del código fuente hecho en Tkinter[3] propuesto en el libro *"Data Structures and Algorithms with Python”* Capítulo 1.4[4], y con el cual se deben construir las pantallas del proyecto.

![Repositorio-Gitbub](https://drive.google.com/uc?export=view&id=1n6Oy_77WTuLCBiJ7cMeUYv40s7b9CW9i "Repositorio-Gitbub.png")

Se llegó a un acuerdo de seguír con el trabajo el siguiente día para poder hacer lectura de toda la documentación necesaria para poder comenzar con el proceso de codificación del proyecto.

### **- Miércoles 25/11/2020**

Al iniciar la reunión se creó un documento en la plataforma de [Lucidchart](http://www.lucid.app/) para poder realizar los esquemas y diagramas ER correspondientes para la creación de la base de datos.

![Lucidchart](https://drive.google.com/uc?export=view&id=1YfOQMqnwooRdjliYuUqM6akbNY1nXOeq "Lucidchart.png")

Durante este proceso se analizaron todos los elementos que se debían considerar en la base de datos.

### **- Jueves 26/11/2020**

Se comenzo a trabajar en la estructura de la base de datos con tres tablas (una para usuarios, una para dibujos, y otra para la bitácora)

![BD1](https://drive.google.com/uc?export=view&id=1w4RpJ1BqMrcHn3hwbbApx3cTEBv1PGr- "BD1.png")

### **- Viernes 27/11/2020**

### **- Sábado 28/11/2020**

### **- Domingo 29/11/2020**

### **- Lunes 30/11/2020**

### **- Martes 01/11/2020**

### **- Miércoles 02/11/2020**

### **- Jueves 03/11/2020**

### **- Viernes 04/11/2020**

### **- Sábado 05/11/2020**

### **- Domingo 06/11/2020**

### **- Lunes 07/11/2020**

### **- Martes 08/11/2020**

### **- Miércoles 09/11/2020**

-----

## **NOTAS**

-----

- [1]: Todas las reuniones síncronas del equipo de trabajo se llevaron a cabo en Discord la cual es una aplicación freeware de diálogo y texto.

![Server-Discord](https://drive.google.com/uc?export=view&id=1m3_0Gf8dQZMjbiqkJnC5yNubM12qT0gn "Server-Discord.png")

- [2]: Para las discución y la planeación del proyecto de forma asíncrona se creó un grupo de whatsapp y se le dio uso al canal de texto en el servidor de Discord.
- [3]: (Enlace a la información sobre Tkinter).
- [3]: (Bibliografía del libro).
