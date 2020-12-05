
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
            self.userData(userName)
            
            return {"status":True, "message":"Logged"}
            
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Datos erróneos" , err)
                return {"status":False, "message":"Wrong data", "ErrorData":err.errno}
            else:
                print("Error de conexión")
                print(err)
                return {"status":False, "message":"Error", "ErrorData":err.errno}
    
    def select(self, query):
        """
        Encargada de ejecutar querys en la base de datos.
        :param q
        """
        self.link.execute(query)
        return self.link.fetchall()

    def closeDataBase(self):
        """
        Cierra la conexión con la base de datos
        """
        self.link.close()
        self.con.close()

        print("Connection ended.")

    def userLoginRegister(self, userName):
        """
        Se encarga de registrar en la bitácora el inicio de sesión de un usuario.
        :param userName: Nombre de usuario que inició sesión.
        :type userName: String.
        """
        try :
            self.mysql_register = "INSERT INTO Binnacle(userId, tex_event) VALUES((SELECT Us.id FROM Users Us WHERE '%s' = Us.var_user), 'Inicio de Sesión')" % (userName)

            self.link.execute(self.mysql_register)
            self.con.commit()
            print("Registro añadido a Bitácora")
        
        except mysql.connector.Error as error:
            print("Operación fallida. {}".format(error))

    

    def addUser(self, userName, userPassword, admin) -> bool:
        """
        Método para agregar un usuario a la base de datos de usuarios y como
        usuario del sistema de gestión de base de datos, tambien se encarga de establecer
        los permisos adecuados para usuarios administradores y operadores.
        :param userName: Nombre del usuario que se agregará a la tabla.
        :type userName: String.
        :param userPassword: Contraseña del usuario que se agregará a la tabla.
        :type userPassword: String.
        :param admin: True si el usuario se crea como admin. False si el usuario se crea como operador.
        :type admin: bool.
        """
        try:

            self.mysql_create = "CREATE USER '%s'@'%s' IDENTIFIED BY '%s'" % (
                userName, self.server, userPassword)
            self.link.execute(self.mysql_create)

            if admin:
                #Asignación de permisos a usuarios administradores
                self.mysql_grant = "GRANT ALL PRIVILEGES ON *.* TO '%s'@'%s' WITH GRANT OPTION" % (userName, self.server)                
                self.mysql_insert = "INSERT INTO Users(var_user, var_pass, var_category) VALUES (%s, %s, 'Administrador')"
                self.data = (userName, userPassword)
                self.link.execute(self.mysql_grant)                
                self.link.execute(self.mysql_insert, self.data)
                

            else:
                #Asignación de permisos para usuarios operadores
                self.mysql_grantDraws = "GRANT INSERT, SELECT ON %s.Draws TO '%s'@'%s'" % (self.database, userName, self.server)
                self.mysql_grantBinnacle = "GRANT INSERT ON %s.Binnacle TO '%s'@'%s'" % (self.database, userName, self.server)
                self.mysql_grantUsers = "GRANT SELECT ON %s.Users TO '%s'@'%s'" % (self.database, userName, self.server)
                self.mysql_insert = "INSERT INTO Users(var_user, var_pass, var_category) VALUES (%s, %s, 'Operador')"
                self.data = (userName, userPassword)

                self.link.execute(self.mysql_insert, self.data)
                self.link.execute(self.mysql_grantDraws)
                self.link.execute(self.mysql_grantBinnacle)
                self.link.execute(self.mysql_grantUsers)


            self.con.commit()
            return True

        except mysql.connector.Error as error:            
            print("Inserción fallida {}".format(error.errno))

    def dropUser(self, userName) -> bool:
        """
        Procedimiento ejecutado para eliminar un usuario.
        :param userName: Nombre de usuario a eliminar.
        :type userName: String
        """
        try:            

            self.mysql_sgbd = "DROP USER '%s'@'%s'" % (userName, self.server)
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

    def retrieveUsers(self) -> list:
        """
        Devuelve una lista con el nombre de los usuarios
        """
        self.mysql_consult = self.select("SELECT var_user FROM Users")
        self.userArray= []

        for name in self.mysql_consult:
            self.userArray.append(name)

        return self.userArray
        
    def alterUser(self, userName, newUserName=None, password=None):
        """
        Modifica los atributos de un usuario de la base de datos.
        :param userName: Nombre del usuario a editar.
        :type userName: String.
        :param newUserName: Nuevo nombre del usuario.
        :type newUserName: String.
        :param password: Nueva contraseña del usuario.
        :type password: String.
        """
        print("entro en función alter user = %s, newUser = %s, password=%s" % (userName, newUserName, password))
        try:
            
            if newUserName:
                #Procedimiento para cambiar nombre
                self.mysql_alterName = "RENAME USER '%s'@'%s' TO '%s'@'%s'" % (userName, self.server, newUserName, self.server)
                self.mysql_modifyName = "UPDATE Users SET var_user = '%s' WHERE var_user = '%s'" % (newUserName, userName)
                #self.data = (newUserName, userName)
                self.link.execute(self.mysql_alterName)
                self.link.execute(self.mysql_modifyName)
            
            if password:
                #Procedimiento para cambiar contraseña
                self.mysql_alterPass = "ALTER USER '%s'@'%s' IDENTIFIED BY '%s'" % (userName, self.server, password)
                self.mysql_modifyPass = "UPDATE Users SET var_pass = '%s' WHERE var_user = '%s'" % (password, userName)
                self.link.execute(self.mysql_alterPass)
                self.link.execute(self.mysql_modifyPass)
            
            self.con.commit()

            print("Usuario Actualizado.")
            return True

        except mysql.connector.Error as error:
            print("Actualización de Usuario fallida. {}".format(error))
            return False

    def insertDraw(self, drawName, drawConfig):     
        self.mysql_nameExists = self.select(("SELECT id FROM Draws WHERE var_name = '%s' and userId = %d") % (drawName, self.mysql_userId))
        
        if self.mysql_nameExists:
            return {"status":False, "message":"Draw already exist.", "drawId":self.mysql_nameExists[0][0]}

        else:
            self.mysql_insert = "INSERT INTO Draws(userId, var_name, jso_drawInfo) VALUES (%s, '%s', '%s')" % (self.mysql_userId, drawName, drawConfig)
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

            self.link.execute(self.mysql_delete)
            self.con.commit()

            print("Dibujo Eliminado.")

        except mysql.connector.Error as error:
            print("Borrado de dibujo fallido. {}".format(error))

    def modifyDraw(self, drawId, drawJson):
        try:
            self.mysql_drawUpdate = "UPDATE Draws SET jso_drawInfo = '%s' WHERE id = %d" % (drawJson, drawId)

            self.link.execute(self.mysql_drawUpdate)
            self.con.commit()
        except mysql.connector.Error as error:
            print("Dibujo no se pudo modificar. {}".format(error))


    def retrieveDraws(self):
        """
        Devuelve los registros correspondientes con dibujos
        :param userName: Nombre de usuario dueño de los dibujos.
        """
        try:            
            self.mysql_drawQuery = "SELECT id, var_name, DATE(tim_time), TIME(tim_time) FROM Draws WHERE userId = %d" % (self.mysql_userId)
            self.result = self.select(self.mysql_drawQuery)

            return self.result
                
            # Aquí se deben devolver las configuraciones de los dibujos guardados y se deben desplegar en la interfaz.

        except mysql.connector.Error as error:
            print("No se han podido recuperar los dibujos {}".format(error))
    
    def userData(self, userName):
        self.mysql_userId = self.select("SELECT id FROM Users WHERE var_user = '%s'" % (userName))[0][0]

        self.mysql_userCategory = self.select("SELECT var_category FROM Users WHERE var_user = '%s'" % (userName))[0][0]

        return {"id":self.mysql_userId, "category":self.mysql_userCategory}

    def retrieveDrawJSON(self, drawID):
        self.mysql_drawConfig = "SELECT jso_drawInfo FROM Draws WHERE id = %d" % (drawID)

        self.result = self.select(self.mysql_drawConfig)
        return self.result[0][0]

        
        

