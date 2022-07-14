# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:13:17 2022

@author: Jorge Ortega
"""
#padding
"""

from cryptography.hazmat.primitives import padding
padder = padding.PKCS7(128).padder()
padded_data = padder.update(b"11111111111111112222222222")
print(padded_data);
"""
#randomGeneration
"""
import os
iv = os.urandom(16)
serial = int.from_bytes(os.urandom(20), byteorder="big")
"""

#AES
"""
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(16)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ct = encryptor.update(b"JorgeOrtegaSilva") + encryptor.finalize()#CBC 16 letras
print(ct)
decryptor = cipher.decryptor()
print(decryptor.update(ct) + decryptor.finalize())
"""



#AES con padding
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)
secret_data = b"jorgeOrtega"
#padding
padder = padding.PKCS7(128).padder()
padded_data = padder.update(secret_data) + padder.finalize()


#cifrado
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(padded_data) + encryptor.finalize()
print("cifrado")
print(ct)


#descifrado
decryptor = cipher.decryptor()
resultado=decryptor.update(ct) + decryptor.finalize()
#decifrado con el padding
print(resultado)
#quita el padding
unpadder = padding.PKCS7(128).unpadder()
unpadder_data = unpadder.update(resultado) + unpadder.finalize()
print(unpadder_data)
# de bytes a string
cadena=unpadder_data.decode("utf-8")
print(cadena)
#de string a bytes
CBytes=cadena.encode("utf-8")
print(CBytes)


