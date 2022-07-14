# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 22:35:57 2022

@author: Jorge Ortega
"""

#laberinto
import numpy as np
A= [[0,1,1,1,1,0,0],
    [0,0,0,0,1,0,0],
    [1,0,1,1,1,0,0],
    [0,0,1,0,0,1,0],
    [1,0,1,1,1,0,1],
    [0,0,0,0,0,0,0],
    [0,1,0,0,1,0,0]]



def resolverLab(lab, tamCol, tamFil):
    tamCol=tamCol-1
    tamFil=tamFil-1
    auxLab=np.copy(lab)
    fila=0
    col=0
    auxF=0
    auxC=0
    backF=0
    backC=0
    stop=0 #contador para ver cuando no hay movimiento
    while(fila!=tamFil or col!=tamCol):
        auxF=fila
        auxC=col
        stop=0
        if(col+1>=0 and col+1<=tamCol and stop==0):
            if(lab[fila][col+1]==0):#mover a la derecha
                lab[fila][col]=3
                backC=col
                backF=fila
                col=col+1
                #print("derecha")
                stop=1
        if(col-1>=0 and col-1<=tamCol and stop==0):
            if(lab[fila][col-1]==0):#mover a la izquierda
                lab[fila][col]=3
                backC=col
                backF=fila
                col=col-1
                #print("izquierda")
                stop=1
        if(fila+1>=0 and fila+1<=tamFil and stop==0):
            if(lab[fila+1][col]==0):#mover a la abajo
                lab[fila][col]=3
                backC=col
                backF=fila
                fila=fila+1
                #print("abajo")
                stop=1
        if(fila-1>=0 and fila-1<=tamFil and stop==0):
            if(lab[fila-1][col]==0):#mover a la arriba
                lab[fila][col]=3
                backC=col
                backF=fila
                fila=fila-1
                #print("arriba")
                stop=1
                
        if(auxF==fila and auxC==col):#sin salida (regreso)
            if(fila==backF and col==backC):# si no hay memoria de la casilla anterior, sigue tus pasos
                if(col+1>=0 and col+1<=tamCol and stop==0):
                    if(lab[fila][col+1]==3):#mover a la derecha
                        lab[fila][col]=1
                        col=col+1
                        #print("derecha")
                        stop=1
                if(col-1>=0 and col-1<=tamCol and stop==0):
                    if(lab[fila][col-1]==3):#mover a la izquierda
                        lab[fila][col]=1
                        col=col-1
                        #print("izquierda")
                        stop=1
                if(fila+1>=0 and fila+1<=tamFil and stop==0):
                    if(lab[fila+1][col]==3):#mover a la abajo
                        lab[fila][col]=1
                        fila=fila+1
                        #print("abajo")
                        stop=1
                if(fila-1>=0 and fila-1<=tamFil and stop==0):
                    if(lab[fila-1][col]==3):#mover a la arriba
                        lab[fila][col]=1
                        fila=fila-1
                        #print("arriba")
                        stop=1
            else:
                lab[fila][col]=1
                fila=backF# casilla anterior
                col=backC
            
        #for i in range(0,tamFil+1):#Imprimir resultado
           # print("|",lab[i][0], lab[i][1],  lab[i][2], lab[i][3],  lab[i][4], lab[i][5],  lab[i][6],"|")
    lab[fila][col]=3
    print(lab,"\n")
    print(auxLab,"\n")
    for i in range(0, tamFil+1):
        for j in range(0, tamCol+1):
            if(auxLab[i][j]==0 and lab[i][j]==3):
                auxLab[i][j]=3
        
    return auxLab
        
    
s=resolverLab(A,7,7)#Parametros: Laberinto, tamaño de columnas, tamaño de filas

print("\n")         
print("----Solucion del laberinto----")
for i in range(0,7):#Imprimir resultado
    print("|",s[i][0], s[i][1],  s[i][2], s[i][3],  s[i][4], s[i][5],  s[i][6],"|")