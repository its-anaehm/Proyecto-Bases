import mysql.connector
from mysql.connector import Error

"""
    @author: emilio.sosa@unah.hn
    @date: 2020/26/11
    @version: 1.0
"""

class MySQLEngine:

    def __init__(self, config):
        self.server = config.server
        self.port = config.port
        self.user = config.user
        self.password = config.password
        self.database = config.database

        self.authentication(self.user, self.password)
        
        
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
        if(self.con.is_connected()):
            return True
        else:
            return False

    def authentication(self, userName, password):
        try:
            self.con = mysql.connector.connect(
                host = self.server,
                port = self.port,
                userName = self.user,
                password = self.password,
                database = self.database

            )

            self.link = self.con.cursor()

        except mysql.connector.Error as error:
            print("Usuario no válido. {}".format(error))

    def select(self, query):
        self.link.execute(query)
        return self.link.fetchall()    

    def closeDataBase(self):
        #Cierre
        self.link.close()
        self.con.close()

        print("Connection ended.")


    def addUser(self, userName, userPassword):
        try:

            self.mysql_insert = "INSERT INTO Users(var_user, var_pass) VALUES (%s, %s)"
            self.data = (userName, userPassword)
           
            self.mysql_create = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s'" % (userName, userPassword)

            self.link.execute(self.mysql_insert, self.data)
            self.link.execute(self.mysql_create)

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

    #def insertDraw(self, userName, drawConfig):

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
            self.mysql_drawQuery = "SELECT * FROM Draws WHERE var_name = %s" % (userName)

            self.result = self.select(self.mysql_drawQuery)
            for name,draw in self.result:
                return ("")
            ## Aquí se deben devolver las configuraciones de los dibujos guardados y se deben desplegar en la interfaz.

        except mysql.connector.Error as error:
            print("No se han podido recuperar los dibujos {}".format(error))




    
    
    
        

    

        
