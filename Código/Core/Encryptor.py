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
        for i in range(len(data)):
            passChar = password[i%len(password)]
            encode.append(chr(ord(data[i]) - ord(passChar)))
        return "".join(encode)

em = Encryptor()

f = open("adminEncrypted.txt","w")
f.write(em.encrypt("admin"))
f.close()

