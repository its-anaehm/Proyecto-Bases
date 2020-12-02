import mysql.connector
from mysql.connector import Error
import configparser

"""
    @author: emilio.sosa@unah.hn
    @date: 2020/26/11
    @version: 1.0
"""


class MySQLEngine:

    def __init__(self):

        # Reading data from config file
        self.config = configparser.ConfigParser()
        self.config.read("./Core/conectionConfig.ini")
        self.config.sections()
        self.port = self.config['DEFAULT']['port']
        self.database = self.config['DEFAULT']['database']
        self.server = self.config['DEFAULT']['host']

        self.con = None

    """
    def start(self):
        self.con = mysql.connector.connect(
            host = self.server,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database

        )

        # Versión texto de Con
        print("Versión de texto del objeto de conexión a MySQL: %s" % (self.con))

        #Enlace
        self.link = self.con.cursor()
    """

    def connectionCheck(self):
        return self.con
    
    def authentication(self, userName, password):
        try:
            self.con = mysql.connector.connect(
                host=self.server,
                port=self.port,
                username=userName,
                password=password,
                database=self.database

            )

            self.link = self.con.cursor()

        except mysql.connector.Error as error:
            self.con = None
            print("Usuario no válido. {}".format(error))
    
    def select(self, query):
        self.link.execute(query)
        return self.link.fetchall()

    def closeDataBase(self):
        # Cierre
        self.link.close()
        self.con.close()

        print("Connection ended.")

    def userLoginRegister(self, userName):
        try :
            self.mysql_register = "INSERT INTO Binnacle(userId, tex_event) VALUES((SELECT Us.id FROM Users Us WHERE '%s' = Us.var_user), 'Inicio de Sesión')" % (userName)

            self.link.execute(self.mysql_register)
            self.con.commit()
            print("Registro añadido a Bitácora")
        
        except mysql.connector.Error as error:
            print("Operación fallida. {}".format(error))

    def addUser(self, userName, userPassword):
        try:

            self.mysql_insert = "INSERT INTO Users(var_user, var_pass) VALUES (%s, %s)"
            self.data = (userName, userPassword)

            self.mysql_create = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s'" % (
                userName, userPassword)

            self.mysql_grant = "GRANT INSERT ON %s.Draws TO '%s'@'localhost'" % (self.database, userName)

            self.link.execute(self.mysql_insert, self.data)
            self.link.execute(self.mysql_create)
            self.link.execute(self.mysql_grant)

            self.con.commit()
            print("User added")

        except mysql.connector.Error as error:            
            print("Inserción fallida {}".format(error))

    def dropUser(self, userName):
        try:

            self.mysql_delete = "DELETE FROM Users WHERE var_user = %s"
            self.data = userName

            self.link.execute(self.mysql_delete, (self.data,))
            self.con.commit()

            print("User dropped")

        except mysql.connector.Error as error:
            print("Eliminación fallida {}".format(error))

    def alterUser(self, userName, newUserName):
        try:

            self.mysql_modify = "UPDATE Users SET var_user = %s WHERE var_user = %s"
            self.data = (newUserName, userName)

            self.link.execute(self.mysql_modify, self.data)
            self.con.commit()

            print("Usuario Actualizado.")

        except mysql.connector.Error as error:
            print("Actualización de Usuario fallida. {}".format(error))

    # def insertDraw(self, userName, drawConfig):

    def dropDraw(self, userID, drawName):
        try:
            self.mysql_delete = "DELETE FROM Draws WHERE userId = %d AND var_name = %s"
            self.data = (userID, drawName)

            self.link.execute(self.mysql_delete, self.data)
            self.con.commit()

            print("Dibujo Eliminado.")

        except mysql.connector.Error as error:
            print("Borrado de dibujo fallido. {}".format(error))

    def retrieveDraws(self, userName):
        try:
            self.mysql_drawQuery = "SELECT * FROM Draws WHERE var_name = %s" % (
                userName)

            self.result = self.select(self.mysql_drawQuery)
            for name, draw in self.result:
                return ("")
            # Aquí se deben devolver las configuraciones de los dibujos guardados y se deben desplegar en la interfaz.

        except mysql.connector.Error as error:
            print("No se han podido recuperar los dibujos {}".format(error))



MySQLEngine()