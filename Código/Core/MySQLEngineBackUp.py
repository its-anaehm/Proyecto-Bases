from Core.MySQLEngine import *
import subprocess
import os


class MySQLEngineBackUp(MySQLEngine):
    def __init__(self):
        super().__init__("./Core/connectionConfigBackup.ini")
        self.authentication("admin","admin")

    def insertDraw(self, drawName, drawConfig):     
        self.mysql_nameExists = self.select(("SELECT id FROM Draws WHERE var_name = '%s' and userId = %d") % (drawName, 1))
        
        if self.mysql_nameExists:
            return {"status":False, "message":"Draw already exist.", "drawId":self.mysql_nameExists[0][0]}

        else:
            fileAbsPath = os.path.join(os.path.abspath("."),"%s.json" % drawName)
            f = open(fileAbsPath,"w") #Se guardará como un archivo .json
            f.write(drawConfig)

            subprocess.call(['gzip','-9',fileAbsPath]) #Comprime la el archivo en formato .gz
            compressedFilePath = "%s.gz" % fileAbsPath

            f = open(compressedFilePath,"rb")
            data = f.read() #Lee los bits del archivo comprimido

            #Guarda los bits en la base de datos
            self.mysql_insert = "INSERT INTO Draws(userId, var_name, blo_drawInfo) VALUES (%d, '%s', %s)" % (1, drawName, data)
            
            subprocess.call(['rm', compressedFilePath])

            self.link.execute(self.mysql_insert)
            self.con.commit()
            print("Dibujo insertado")
            return {"status":True, "message":"Draw inserted"}

    def dropDraw(self, drawId):
        """
        Elimina un dibujo de la base de datos
        :param userID: Ud del usuario dueño del dibujo
        :param drawName: Nombre del dibujo
        """
        try:
            self.mysql_delete = "DELETE FROM Draws WHERE id = %d" % (drawId)

            """
            self.mysql_delete_B = "DELETE FROM Draws WHERE id = %d" % (drawId)
            """

            self.link.execute(self.mysql_delete)
            self.con.commit()

            print("Dibujo Eliminado.")

        except mysql.connector.Error as error:
            print("Borrado de dibujo fallido. {}".format(error))
    
    def modifyDraw(self, drawId, drawJson):
        try:
            self.mysql_drawUpdate = "UPDATE Draws SET jso_drawInfo = '%s' WHERE id = %d" % (drawJson, drawId)

            """
            filePath = "../temp/temp.json" #Dirección de la carpeta donde se guardará el dibujo
            f = open(filePath,"w") #Se guardará como un archivo .json
            f.write(drawJson)

            subprocess.call(['gzip','-9',filePath]) #Comprime la el archivo en formato .gz
            compressedFilePath = "%s.gz" % filePath

            f = open("compressedFilePath","rb")
            data = f.read() #Lee los bits del archivo comprimido

            #Guarda los bits en la base de datos
            self.mysql_drawUpdate_B = "UPDATE Draws SET blo_drawInfo = '%s' WHERE id = %d" % (data, drawId)"
            
            subprocess.call(['rm', compressedFilePath])
            """

            self.link.execute(self.mysql_drawUpdate)
            self.con.commit()
        except mysql.connector.Error as error:
            print("Dibujo no se pudo modificar. {}".format(error))