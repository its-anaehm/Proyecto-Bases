#-*- coding:utf8 -*-
import os
import subprocess

from tkinter import *
from tkinter import filedialog, messagebox

import mysql
import mysql.connector as DBCon
import configparser

class MySQLEngineBackup:
    """
    Objeto utilizado como interfaz entre la
    base de datos y algún programa.
    """
    def __init__(self):
        self.connection = None
        self.cursor = None


    def connect(self, **conectionData) -> bool:
        """
        abrir una conexión con la base de datos

        args:
            filename  Nombre de archivo de configuración. Opcional
            contectionData  datos necesarios para iniciar una conexión.
        """
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


    def purgeData(self, data1, data2 = {}) -> dict:
        """
        Datos dos diccionarios de datos solo toma los necesarios
        para la conexión y revisa que esten todos.
        """
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


    def readConfigFile(self, filename:str, section:str='DEFAULT') -> dict:
        """
            Lee la configuración de un archivo dado
        """
        config = configparser.ConfigParser()
        config.read(filename)
        return dict(config[section])

    def execute(self, query):
        """
        Ejecuta una query
        :param query: Cadena que representa sentencias de correctas de mysql.
        """
        return self.cursor.execute(query)

    def getResult(self):
        """
        Obtiene el resultado de la última query ejecutada
        """
        return self.cursor.fetchall()

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
            return {"status":False, "message":"Fail updated"}

    def download(self, drawId:int, path:str):
        """
        Descarga los dibujos del usuario.
        """
        
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




    def insertInto(self, tableName:str, fields:list, values:list):
        """

        """
        fields = ",".join("%s" % x for x in fields)
        values = ",".join("%s" % str(x) for x in values)

        print("INSERT INTO %s(%s) VALUES %s;" % (tableName, fields, values))
        self.cursor.execute("INSERT INTO %s(%s) VALUES %s;" % (tableName, fields, values))

    def delete(self,tableName, condition):
        print("DELETE FROM %s WHERE %s" % (tableName, condition))
        self.cursor.execute("DELETE FROM %s WHERE %s" % (tableName, condition))


bk = MySQLEngineBackup()
bk.connect(filename="Core/connectionConfigBackup.ini")
bk.download(24,"Core/pruebaj.json")