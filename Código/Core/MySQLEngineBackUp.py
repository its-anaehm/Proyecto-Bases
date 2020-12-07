#-*- coding:utf8 -*-
import os
import subprocess

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
            print("Bases de datos B")
            fileAbsPath = os.path.join(os.path.abspath("."), "%s.json" % drawName)
            f = open(fileAbsPath, "w")  # Se guardará como un archivo .json
            f.write(drawJSON)

            subprocess.call(['gzip', '-9', fileAbsPath])  # Comprime la el archivo en formato .gz
            compressedFilePath = "%s.gz" % fileAbsPath

            f = open(compressedFilePath, "rb")
            data = f.read()  # Lee los bits del archivo comprimido

            # Guarda los bits en la base de datos
            # self.mysql_insert = "INSERT INTO Draws(userId, var_name, blo_drawInfo) VALUES (%s, %s, %s)"
            # self.link.execute(self.mysql_insert, (1,drawName,data, ))
            self.cursor.execute(
                "INSERT INTO Draws(userId, var_name, blo_drawInfo) VALUES (%s, %s, %s)",
                (userId, drawName, data)
            )

            self.connection.commit()


            subprocess.call(['rm', compressedFilePath])

            print("Dibujo insertado")
            return {"status": True, "message": "Draw inserted"}

    def deleteDraw(self, userId, drawName):
        try:
            self.cursor.execute(
                "DELETE FROM Draws WHERE userId = %s and var_name = %s",
                (userId, drawName)
            )
            self.connection.commit()
            print("Dibujo eliminado")
            return {"status":True, "message":"Draw deleted"}

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

