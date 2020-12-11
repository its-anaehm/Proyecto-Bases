
import mysql.connector
from mysql.connector import Error
import configparser

"""
    @author: emilio.sosa@unah.hn
    @date: 2020/26/11
    @version: 5.0
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
        self.adminPass = self.config['DEFAULT']['adminPass']

        self.con = None

    def connectionCheck(self):
        return self.con

    
    def authentication(self, userName:str, password:str) -> dict:
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
            self.userLoginRegister(userName)
            
            return {"status":True, "message":"Logged"}
            
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Datos erróneos" , err)
                return {"status":False, "message":"Wrong data", "ErrorData":err.errno}
            else:
               print("Error de conexión")
               print(err)
               return {"status":False, "message":"Error", "ErrorData":err.errno}
    
    """
    Encargada de ejecutar querys en la base de datos.
    @param query : Es la consulta que se manda a la base de datos para recuperar datos.
    """
    def select(self, query:str) -> list:
        self.link.execute(query)
        return self.link.fetchall()

    """
    @function closeDataBase : Cierra la conexión con la base de datos.    
    """
    def closeDataBase(self):
        self.link.close()
        self.con.close()

        print("Connection ended.")

    """
    Se encarga de registrar en la bitácora el inicio de sesión de un usuario.
    @param userName : Nombre de usuario que inició sesión.
    @type userName: String.
    """
    def userLoginRegister(self, userName:str):
        try :
            self.mysql_register = "INSERT INTO Binnacle(userId, tex_event) VALUES((SELECT Us.id FROM Users Us WHERE AES_ENCRYPT('%s','%s') = Us.var_user), 'Inicio de Sesión')" % (userName,self.adminPass)

            self.link.execute(self.mysql_register)
            self.con.commit()
            print("Registro añadido a Bitácora")
        
        except mysql.connector.Error as error:
            print("Operación fallida. {}".format(error))

    

    """
    Método para agregar un usuario a la base de datos de usuarios y como
    usuario del sistema de gestión de base de datos, tambien se encarga de establecer
    los permisos adecuados para usuarios administradores y operadores.
    @param userName: Nombre del usuario que se agregará a la tabla.
    @type userName: String.
    @param userPassword: Contraseña del usuario que se agregará a la tabla.
    @type userPassword: String.
    @param admin: True si el usuario se crea como admin. False si el usuario se crea como operador.
    @type admin: bool.
    """
    def addUser(self, userName:str, userPassword:str, admin:bool) -> bool: 
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
                self.mysql_grantConfigurations = "GRANT SELECT ON %s.drawsConfig TO '%s'@'%s'" % (self.database, userName, self.server)
                self.mysql_insert = "INSERT INTO Users(var_user, var_pass, var_category) VALUES (%s, %s, 'Operador')"
                self.data = (userName, userPassword)

                self.link.execute(self.mysql_insert, self.data)
                self.link.execute(self.mysql_grantDraws)
                self.link.execute(self.mysql_grantBinnacle)
                self.link.execute(self.mysql_grantUsers)
                self.link.execute(self.mysql_grantConfigurations)


            self.con.commit()
            return True

        except mysql.connector.Error as error:
            print("Inserción fallida {}".format(error.errno))
            return False            

    """
    Procedimiento ejecutado para eliminar un usuario.
    @param userName: Nombre de usuario a eliminar.
    @type userName: String
    """
    def dropUser(self, userName) -> bool:
        try:            

            self.mysql_sgbd = "DROP USER '%s'@'localhost'" % (userName)
            self.mysql_delete = "DELETE FROM Users WHERE var_user = AES_ENCRYPT('%s','%s')" % (userName,self.adminPass)            

            self.link.execute(self.mysql_delete)
            self.link.execute(self.mysql_sgbd)
            self.con.commit()

            print("User dropped")
            return True

        except mysql.connector.Error as error:
            print("Eliminación fallida {}".format(error))
            return False

    """
    Devuelve una lista con el nombre de los usuarios
    """
    def retrieveUsers(self) -> list:
        self.mysql_consult = self.select("SELECT AES_DECRYPT(var_user, '%s') FROM Users" % (self.adminPass)) 
        self.userArray= []

        for name in self.mysql_consult:
            self.userArray.append(name)

        return self.userArray
        
    """
    Modifica los atributos de un usuario de la base de datos.
    @param userName: Nombre del usuario a editar.
    @type userName: String.
    @param newUserName: Nuevo nombre del usuario.
    @type newUserName: String.
    @param password: Nueva contraseña del usuario.
    @type password: String.
    """
    def alterUser(self, userName:str, newUserName:str=None, password:str=None) -> bool:
        print("entro en función alter user = %s, newUser = %s, password=%s" % (userName, newUserName, password))
        try:
            
            if newUserName:
                #Procedimiento para cambiar nombre
                self.mysql_alterName = "RENAME USER '%s'@'%s' TO '%s'@'%s'" % (userName, self.server, newUserName, self.server)
                self.mysql_modifyName = "UPDATE Users SET var_user = '%s' WHERE var_user = AES_ENCRYPT('%s', '%s')" % (newUserName, userName, self.adminPass)
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

    """
    Almacena un dibujo nuevo en la base de datos.
    @param drawName: Nombre del dibujo.
    @param drawConfig: string que representa un json que es generado por el módulo de dibujo.
    """
    def insertDraw(self, drawName:str, drawConfig:str) -> dict:
        self.mysql_nameExists = self.select(("SELECT id FROM Draws WHERE var_name = AES_ENCRYPT('%s','%s') and userId = %d") % (drawName, self.adminPass,self.mysql_userId))
        
        if self.mysql_nameExists:
            return {"status":False, "message":"Draw already exist.", "drawId":self.mysql_nameExists[0][0]}

        else:
            self.mysql_insert = "INSERT INTO Draws(userId, var_name, jso_drawInfo) VALUES (%s, %s, %s)"
            self.link.execute(self.mysql_insert,(self.mysql_userId, drawName, drawConfig))
            self.con.commit()
            print("Dibujo insertado")
            return {"status":True, "message":"Draw inserted"}

    """
    Elimina un dibujo de la base de datos
    @param drawId: Id del dibujo a eliminar
    """
    def dropDraw(self, drawId) -> bool:
        try:
            self.mysql_delete = "DELETE FROM Draws WHERE id = %d" % (drawId)
            self.link.execute(self.mysql_delete)
            self.con.commit()
            print("Dibujo Eliminado.")
            return True

        except mysql.connector.Error as error:
            print("Borrado de dibujo fallido. {}".format(error))
            return False

    """
    Modifica los datos que representan un dibujo en la base de datos.
    @param drawId: Id de la base de datos
    """
    def modifyDraw(self, drawId:int, drawJson):
        try:
            self.mysql_drawUpdate = "UPDATE Draws SET jso_drawInfo = '%s' WHERE id = %d" % (drawJson, drawId)

            self.link.execute(self.mysql_drawUpdate)
            self.con.commit()
        except mysql.connector.Error as error:
            print("Dibujo no se pudo modificar. {}".format(error))


    """
    Devuelve los registros correspondientes con dibujos
    @param userName: Nombre de usuario dueño de los dibujos.
     """
    def retrieveDraws(self):
        try:            
            self.mysql_drawQuery = "SELECT id, AES_DECRYPT(var_name, %s), DATE(tim_time), TIME(tim_time) FROM Draws WHERE userId = %d" % (self.adminPass, self.mysql_userId)
            self.result = self.select(self.mysql_drawQuery)

            return self.result
                
            # Aquí se deben devolver las configuraciones de los dibujos guardados y se deben desplegar en la interfaz.

        except mysql.connector.Error as error:
            print("No se han podido recuperar los dibujos {}".format(error))
    
    """
    Realiza querys a la base de datos para obtener información del usuario.
    Establece en el atributo mysql_userId el id del usuario.
    Establece en el atributo mysql_userCategory la categoria del usuario
    @param userName: Nombre de usuario del cual se recuperaran los datos.
        Este debe ser un usuario existente en la tabla de usuarios.
    """
    def userData(self, userName) -> dict:
        self.mysql_userId = self.select("SELECT id FROM Users WHERE var_user = AES_ENCRYPT('%s','%s')" % (userName, self.adminPass))[0][0]
        self.mysql_userCategory = self.select("SELECT AES_DECRYPT(var_category,'%s') FROM Users WHERE var_user = AES_ENCRYPT('%s','%s')" % (self.adminPass,userName, self.adminPass))[0][0]
        return {"id":self.mysql_userId, "category":self.mysql_userCategory}
        
    
    """
    Retorna si el usuario actual es administrador o no.
    """
    def isAdmin(self) -> bool:
        return self.mysql_userCategory == "Administrador"

    """
    Recupera desde la base de datos el JSON que representará un dibujo.
    @param drawID: id que identifica el dibujo en la base de datos.
    """
    def retrieveDrawJSON(self, drawID):
        self.mysql_drawConfig = "SELECT AES_DECRYPT(jso_drawInfo, %s) FROM Draws WHERE id = %d" % (self.adminPass, drawID)

        self.result = self.select(self.mysql_drawConfig)
        return self.result[0][0]

    """
    Recupera desde la base de datos la información de la bitácora
    """
    def retrieveBinnacleInfo(self) -> list:
        try:
            # ! Devolver el usuario en la primera posición
            self.mysql_binnacle = self.select("SELECT AES_DECRYPT(Users.var_user, '%s'), tex_event, DATE(tim_time), TIME(tim_time) FROM Binnacle JOIN Users ON Binnacle.userId = Users.id" % self.adminPass) 
            return self.mysql_binnacle
        except mysql.connector.Error as error:
            print("No se puedieron recuperar los registros de bitácora. {}".format(error))

    """
    Guarda la configuracioón de dibujo en la base de datos.
    @param pennColor: string que representa un número hexadecimal para el penColor.
    @param fillColor: string que representa un número hexadecimal que será usado para el fillColor.
    """
    def updateDrawConfiguration(self, pennColor=None, fillColor=None):
        if pennColor:
            self.mysql_config = "UPDATE drawsConfig SET var_penColor = %s" % (pennColor)

            self.link.execute(self.mysql_config)
            self.con.commit()

        if fillColor:
            self.mysql_config = "UPDATE drawsConfig SET var_fillColor = %s" % (fillColor)

            self.link.execute(self.mysql_config)
            self.con.commit()
            
    """
    Recupera la configuración de dibujo (pen color y fill color) almacenada en
    la base de datos.
    """
    def retrieveColorConfig(self) -> tuple:
        self.mysql_colorConfiguration = self.select("SELECT * FROM drawsConfig")
        return self.mysql_colorConfiguration[0]
        
        

