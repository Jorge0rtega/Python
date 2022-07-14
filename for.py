# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 11:43:06 2022

@author: Jorge Ortega
"""

for i in [1,2,3,4]:
    print(i, end=" ")

email=False
correo=input("Introduce tu correo electronico: ")

for i in correo:
    print(i)
    if (i=="@"):
        email=True
        break
    
  
if email==True:
    print("el correo es valido")
else:
    print("el correo es invalido")
  
