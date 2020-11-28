# -*- coding: utf-8 -*-
"""
    @author Moisesgomez00
    @version 1.0
    @date 26/11/2020
"""

class Encryptor:
    """
    The abstraction of an encryptor object
    Methods
    -------
    encrypt(data, password) -> str
    Encrypt the data with the password and return it.
    """

    def __init__(self):
        pass

    def encrypt(self,data, password):
        encode = []
        for i in range(len(data)):
            passChar = password[i%len(password)]
            encode.append(chr(ord(data[i] )+ ord(passChar)))
        return "".join(encode)

    def decrypt(self,data, password):
        encode = []
        for i in range(len(data)):
            passChar = password[i%len(password)]
            encode.append(chr(ord(data[i]) - ord(passChar)))
        return "".join(encode)