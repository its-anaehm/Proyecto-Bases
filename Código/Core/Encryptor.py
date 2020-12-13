# -*- coding: utf-8 -*-
import json
"""
@author Moisesgomez00
@version 1.0
@date 26/11/2020

Abstracción que representa un objeto encriptador.
"""
class Encryptor:

    def __init__(self):
        pass
    """
    Retorna un texto encriptado.
    @param data: Texto se será encriptado.
    @param password: Texto usado como contraseña para encriptar.
    """
    def encrypt(self,data, password="admin"):
        encode = []
        if type(data) == str:
            for i in range(len(data)):
                if type(data[i]) == type("string"):
                    passChar = password[i%len(password)]
                    encode.append(chr(ord(data[i] )+ ord(passChar)))
                elif type(data[i]) == int or type(data[i]) == float:
                    passChar = password[i%len(password)]
                    encode.append(data[i] + ord(passChar))
            return "".join(encode)
        else:
            passwordSum = 0
            for i in password:
                passwordSum = passwordSum + ord(i)
            return data + passwordSum

    """
    Retorna un texto desencriptado.
    @param data: texto que será desencriptado.
    @param password: texto usado como contraseña.
    """
    def decrypt(self,data, password="admin"):
        encode = []
        if type(data) == str:
            for i in range(len(data)):
                if type(data[i]) == type("string"):
                    passChar = password[i%len(password)]
                    encode.append(chr(ord(data[i] ) - ord(passChar)))
                elif type(data[i]) == int or type(data[i]) == float:
                    passChar = password[i%len(password)]
                    encode.append(data[i] - ord(passChar))
            return "".join(encode)
        else:
            passwordSum = 0
            for i in password:
                passwordSum = passwordSum + ord(i)
            return data - passwordSum

    def encryptJSON(self,data,password="admin"):
        if type(data) == type("text"):
            data = json.loads(data)
        result = {"Draw":[]}
        for command in data["Draw"]:
            cmd = {}
            for key,value in command.items():
                cmd[self.encrypt(key)] = self.encrypt(value)
            result["Draw"].append(cmd)
        return result

    def decryptJSON(self,data,password="admin"):
        if type(data) == str:
            data = json.loads(data)
        result = {"Draw":[]}
        for command in data["Draw"]:
            cmd = {}
            for key,value in command.items():
                cmd[self.decrypt(key)] = self.decrypt(value)
            result["Draw"].append(cmd)
        return result

em = Encryptor()

"""
jsons = '{"Draw":[{"command": "GoTo", "x": -121.0, "y": 8.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": -104.0, "y": -156.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": 62.0, "y": -81.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": -4.0, "y": 3.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": 62.0, "y": 159.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": 137.0, "y": -31.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": 44.0, "y": -83.0, "width": 1.0,"color": "#d9d9d9" },{"command":"end"}]}'

print(json.dumps(em.encryptJSON(jsons)))"""