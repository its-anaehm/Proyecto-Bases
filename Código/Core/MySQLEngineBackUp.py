#-*- coding:utf8 -*-
import configparser
import os
import subprocess
from tkinter import filedialog

import mysql
import mysql.connector as DBCon

from Core.Encryptor import Encryptor

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
    def __init__(self, sgbd):
        self.connection = None
        self.cursor = None
        self.sgbd = sgbd


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
            "SELECT * FROM Draws WHERE var_name = AES_ENCRYPT(%s,%s) and userId = %s",
            (drawName, self.sgbd.adminPass, userId)
        )
        result = self.cursor.fetchall()
        self.connection.commit()
        print(result)

        if result:
            print("No insertado ya existe")
            return {"status":False, "message":"Already exists"}

        else:
            self.connection
            encryptor = Encryptor()
            
            fileAbsPath = os.path.join(os.path.abspath("."), "%s.json" % drawName)
            f = open(fileAbsPath, "w")  # Se guardará como un archivo .json
            f.write(encryptor.encrypt(drawJSON, self.sgbd.adminPass))
            f.close()

            # Comprime la el archivo en formato .gz mediante la terminal
            subprocess.call(['gzip', '-9', fileAbsPath])  
            compressedFilePath = "%s.gz" % fileAbsPath
            #compressedFilePath = "%s" % fileAbsPath
            

            f = open(compressedFilePath, "rb")
            data = f.read()  # Lee los bits del archivo comprimido
            f.close()
            # Guarda los bits en la base de datos
            encryptor = Encryptor()
            self.cursor.execute(
                "INSERT INTO Draws(userId, var_name, blo_drawInfo) VALUES (%s, %s, %s)",
                (userId, drawName, data)
                )
            

            self.connection.commit()

            subprocess.call(['rm', compressedFilePath])
            #subprocess.call(['rm', fileAbsPath])

            print("Dibujo insertado")
            return {"status": True, "message": "Draw inserted"}

    """
    Elimina un dibujo de la base de datos.
    @param id: identificador del dibujo.
    """
    def deleteDraw(self, id):
        try:
            self.cursor.execute(
                "DELETE FROM Draws WHERE id = %s",
                (id, )
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
    @param id: El id del dibujo.
    @type Int
    @param drawJSON: JSON del dibujo a modificar.
    @type JSON
    """
    def modifyDraw(self, id, drawJSON):
        try:
            encryptor = Encryptor()
            self.cursor.execute(
                "UPDATE Draws SET blo_drawInfo = %s WHERE id = %s",
                (encryptor.encrypt(drawJSON, self.sgbd.adminPass), id)
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
    """
    def download(self, drawId:int):
        
        self.cursor.execute(
            "SELECT blo_drawInfo FROM Draws WHERE id = %s",
            #"SELECT blo_drawInfo FROM Draws WHERE id = %s",
            (drawId, )
        )
        fn = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File")

        fn = "%s.json" % fn
        fnc = "%s.gz" % fn

        r = self.cursor.fetchall()


        f = open(fnc, "wb")

        f.write(r[0][0])

        f.close()
     
        subprocess.call(['gzip', '-d', fnc])  #descomprime el archivo

        encryptor = Encryptor()

        f = open(fn,"r")
        content = encryptor.decrypt(f.read(),self.sgbd.adminPass)
        f.close()

        f = open(fn,"w")
        f.write(content)
        f.close()


"""
bk = MySQLEngineBackup()
bk.connect(filename="Core/connectionConfigBackup.ini")
bk.insertDraw(1,"holaMundo",'{"draw":["hola"]')"""