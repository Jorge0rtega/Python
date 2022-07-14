# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 21:16:44 2022

@author: Jorge Ortega
"""
import time
inicio = time.time()

def Hanoi (discos,TorreOrigen=1,TorreAuxiliar=2,TorreDestino=3):
    if discos==1:
        print (TorreOrigen,"a",TorreDestino)
        
    else:
        Hanoi(discos-1,TorreOrigen,TorreDestino,TorreAuxiliar)
        print(TorreOrigen,"a",TorreDestino)
        Hanoi (discos-1,TorreAuxiliar,TorreOrigen,TorreDestino)
    return

##Lo probamos con 3 discos
Hanoi(5)

fin = time.time()
print(fin-inicio)