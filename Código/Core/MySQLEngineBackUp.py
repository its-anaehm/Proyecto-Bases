#-*- coding:utf8 -*-
import os
import subprocess

from tkinter import *
from tkinter import filedialog, messagebox

import mysql
import mysql.connector as DBCon
import configparser

"""
Objeto utilizado como interfaz entre la
base de datos B y algún programa.
@author leonardo.mass@unah.hn
@version 5.1
"""
class MySQLEngineBackup:

    """
    Constructor de la clase.
    """
    def __init__(self):
        self.connection = None
        self.cursor = None


    """
    abrir una conexión con la base de datos

    @param filename  Nombre de archivo de configuración. Opcional
    @param contectionData  datos necesarios para iniciar una conexión.
    """
    def connect(self, **conectionData) -> bool:
        try:
            data = {}
            if "filename" in conectionData:
                data = self.readConfigFile(conectionData["filename"])
            data = self.purgeData(data1=data, data2=conectionData)

            if not data:
                raise AttributeError

            #Realizar la conexión con la base de datos
            self.connection = DBCon.connect(**data)

            #Establecer un cursor
            self.cursor = self.connection.cursor()

            return True

        except DBCon.Error as err:
            if err.errno == DBCon.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Datos de usuario erroneos")
            else:
                print(err.errno)
            return False


    """
    Datos dos diccionarios de datos solo toma los necesarios
    para la conexión y revisa que esten todos.

    @param data1 diccionario de que contiene datos de conexión.
    @param data2 Diccionario de datos de conexión.
    """
    def purgeData(self, data1, data2 = {}) -> dict:
        neededData = ["host","port","user","password","database"]
        verifiedData = {}

        for i in neededData:
            if i in data1:
                verifiedData[i] = data1[i]

            if i in data2:
                verifiedData[i] = data2[i]

            if not i in data1 and not i in data2:
                return {}

        return verifiedData


    """       
    Lee la configuración de un archivo dado
    @param filename: Archivo de datos de configuración
    @type: String
    @param section: Sección del archivo de configuración donde estan ubicados elementos de conexión.
    @type: String
    """
    def readConfigFile(self, filename:str, section:str='DEFAULT') -> dict:
        config = configparser.ConfigParser()
        config.read(filename)
        return dict(config[section])

    """
    Ejecuta una query
    @param query : Cadena que representa sentencias de correctas de mysql.
    """
    def execute(self, query):
        return self.cursor.execute(query)

    """
    Obtiene el resultado de la última query ejecutada
    """
    def getResult(self) -> list:
        return self.cursor.fetchall()

    """
    Inserta un dibujo en la base de datos de respaldo.
    @param userId: Id del usuario que creó el dibujo.
    @trype String
    @param drawName: Nombre del dibujo.
    @type String
    @param drawJSON: String en formato JSON que representa el dibujo.
    @type String
    """
    def insertDraw(self, userId, drawName, drawJSON):
        self.cursor.execute(
            "SELECT * FROM Draws WHERE var_name = %s and userId = %s",
            (drawName, userId)
        )
        result = self.cursor.fetchall()
        self.connection.commit()
        print(result)

        if result:
            print("No insertado ya existe")
            return {"status":False, "message":"Already exists"}

        else:
            self.connection
            
            fileAbsPath = os.path.join(os.path.abspath("."), "%s.json" % drawName)
            f = open(fileAbsPath, "w")  # Se guardará como un archivo .json
            f.write(drawJSON)
            f.close()

            # Comprime la el archivo en formato .gz mediante la terminal
            subprocess.call(['gzip', '-9', fileAbsPath])  
            compressedFilePath = "%s.gz" % fileAbsPath
            #compressedFilePath = "%s" % fileAbsPath
            

            f = open(compressedFilePath, "rb")
            data = f.read()  # Lee los bits del archivo comprimido
            f.close()
            # Guarda los bits en la base de datos
            self.cursor.execute(
                "INSERT INTO Draws(userId, var_name, blo_drawInfo) VALUES (%s, %s, %s)",
                (userId, drawName, data)
            )

            self.connection.commit()

            # subprocess.call(['rm', compressedFilePath])

            print("Dibujo insertado")
            return {"status": True, "message": "Draw inserted"}

    """
    Elimina un dibujo de la base de datos.
    @param userId : Identificador de usuario en la base de datos.
    @param drawName : Nombre del dibujo a eliminar.
    """
    def deleteDraw(self, userId, drawName):
        try:
            self.cursor.execute(
                "DELETE FROM Draws WHERE userId = %s and var_name = %s",
                (userId, drawName)
            )
            self.connection.commit()
            print("Dibujo eliminado de B")
            return {"status":True, "message":"Draw deleted"}

        except mysql.connector.Error as error:
            print("Borrando de dibujo. {}".format(error))
            return {"status":False, "message":"Fail F"}
    
    """
    Borra todos los dibujos de un usuario.
    @param userId: El id que identifica el usuario del cual se eliminarán los dibujos.
    @type String
    """
    def deleteAllUserDraws(self, userId):
        try:
            self.cursor.execute(
                "DELETE FROM Draws WHERE userId = %s",
                (userId,)
            )
            self.connection.commit()
            print("Dibujos eliminados de B")
            return {"status":True, "message":"Draws deleted"}

        except mysql.connector.Error as error:
            print("Borrando de dibujo. {}".format(error))
            return {"status":False, "message":"Fail F"}
        
    """
    Modifica un dibujo de la base de datos de respaldo.
    @param userId: El id del usuario dueño del dibujo a modificar.
    @type String
    @param drawName: El nombre del dibujo a eliminar.
    @type String
    @param drawJSON: JSON del dibujo a modificar.
    @type JSON
    """
    def modifyDraw(self, userId, drawName, drawJSON):
        try:
            self.cursor.execute(
                "UPDATE Draws SET blo_drawInfo = %s WHERE userId = %s and var_name = %s",
                (drawJSON, userId, drawName)
            )
            self.connection.commit()

            print("Dibujo actualizado")
            return {"status":True, "message":"Draw updated"}

        except mysql.connector.Error as error:
            return {"status":False, "message":"Fail updated", "error":error}

    """
    Descarga los dibujos del usuario.
    @param drawId: Id del dibujo a descarar.
    @type int
    @param path: Ruta del dibujo.
    """
    def download(self, drawId:int, path:str):
        
        self.cursor.execute(
            "SELECT blo_drawInfo FROM Draws WHERE id = %s",
            (drawId, )
        )
        
        fn = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File")
        fn = "%s.json.gz" % fn
        r = self.cursor.fetchall()

        f = open(fn, "wb")

        f.write(r[0][0])

        f.close()
        """
        for i in r:
    	    data = i[0] # this is the binary from database
        with open(fn,"wb") as f:
	        f.write(data)
        f.close()
        """        
        subprocess.call(['gzip', '-d', fn])  #descomprime el archivo



"""bk = MySQLEngineBackup()
bk.connect(filename="Core/connectionConfigBackup.ini")
bk.download(24,"Core/pruebaj.json")"""