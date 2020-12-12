# -*- coding: utf-8 -*-
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
        for i in range(len(data)):
            passChar = password[i%len(password)]
            encode.append(chr(ord(data[i] )+ ord(passChar)))
        return "".join(encode)

    """
    Retorna un texto desencriptado.
    @param data: texto que será desencriptado.
    @param password: texto usado como contraseña.
    """
    def decrypt(self,data, password="admin"):
        encode = []
        try:
            data = data.decode("utf-8")
        except (UnicodeDecodeError, AttributeError):
            pass
        
        for i in range(len(data)):
            passChar = password[i%len(password)]
            data[i]
            encode.append(chr(ord(data[i]) - ord(passChar)))
        return "".join(encode)

em = Encryptor()

"""jsons = '{"Draw":[{"command": "GoTo", "x": -121.0, "y": 8.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": -104.0, "y": -156.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": 62.0, "y": -81.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": -4.0, "y": 3.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": 62.0, "y": 159.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": 137.0, "y": -31.0, "width": 1.0,"color": "#d9d9d9" },{"command": "GoTo", "x": 44.0, "y": -83.0, "width": 1.0,"color": "#d9d9d9" },{"command":"end"}]}'
print(em.decrypt(em.encrypt(jsons,"admin"),"admin"))"""