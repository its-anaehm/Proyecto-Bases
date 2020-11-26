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

    def encrypt(self, data, password):
        encoded_chars = []
        for i in range(len(data)):
            key_c = password[i % len(password)]
            encoded_c = chr(ord(data[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = "".join(encoded_chars)
        return encoded_string

    def decrypt(self, data, password):
        encoded_chars = []
        for i in range(len(data)):
            key_c = password[i % len(password)]
            encoded_c = chr(ord(data[i]) - ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = "".join(encoded_chars)
        return encoded_string
