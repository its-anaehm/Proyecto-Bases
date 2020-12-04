
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
            self.user = userName
            self.password = password
            return (True, "Logged")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Datos erróneos")
                return (False, "Wrong data")
            else:
                print("Error de conexión")
                print(err.errno)
                return (False, "Error")
    
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

    

    def addUser(self, userName, userPassword, admin):
        try:

            self.mysql_create = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s'" % (
                userName, userPassword)
            self.link.execute(self.mysql_create)

            if admin:
                print("Usuario admin")
                self.mysql_grant = "GRANT ALL PRIVILEGES ON *.* TO '%s'@'localhost' WITH GRANT OPTION" % (userName)                
                self.mysql_insert = "INSERT INTO Users(var_user, var_pass, var_category) VALUES (%s, %s, 'Administrador')"
                self.data = (userName, userPassword)
                self.link.execute(self.mysql_grant)                
                self.link.execute(self.mysql_insert, self.data)
                

            else:
                print("No admin") 
                self.mysql_grantDraws = "GRANT INSERT, SELECT ON %s.Draws TO '%s'@'localhost'" % (self.database, userName)
                self.mysql_grantBinnacle = "GRANT INSERT ON %s.Binnacle TO '%s'@'localhost'" % (self.database, userName)
                self.mysql_grantUsers = "GRANT SELECT ON %s.Users TO '%s'@'localhost'" % (self.database, userName)
                self.mysql_insert = "INSERT INTO Users(var_user, var_pass, var_category) VALUES (%s, %s, 'Operador')"
                self.data = (userName, userPassword)

                self.link.execute(self.mysql_insert, self.data)
                self.link.execute(self.mysql_grantDraws)
                self.link.execute(self.mysql_grantBinnacle)
                self.link.execute(self.mysql_grantUsers)


            self.con.commit()
            print("User added")
            return True

        except mysql.connector.Error as error:            
            print("Inserción fallida {}".format(error))

    def dropUser(self, userName) -> bool:
        try:            

            self.mysql_sgbd = "DROP USER '%s'@'localhost'" % (userName)
            self.mysql_delete = "DELETE FROM Users WHERE var_user = %s"
            self.data = userName

            self.link.execute(self.mysql_delete, (self.data,))
            self.link.execute(self.mysql_sgbd)
            self.con.commit()

            print("User dropped")
            return True

        except mysql.connector.Error as error:
            print("Eliminación fallida {}".format(error))
            return False

    def retrieveUsers(self):
        self.mysql_consult = self.select("SELECT var_user FROM Users")
        self.userArray= []

        for name in self.mysql_result:
            self.userArray.append(name)

        return self.userArray
    

    def alterUser(self, userName, newUserName):
        try:


            self.mysql_sgbdUser = "ALTER USER "
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