# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 22:35:57 2022

@author: Jorge Ortega
"""

#laberinto
import numpy as np
A= [[0,1,1,1,1,0,0],
    [0,0,0,0,1,0,0],
    [1,0,1,0,0,0,0],
    [0,0,1,0,0,1,0],
    [1,0,0,0,0,0,1],
    [1,0,0,1,1,0,1],
    [0,1,0,0,1,0,0]]



def resolverLab(lab, tamCol, tamFil):
    tamCol=tamCol-1
    tamFil=tamFil-1
    auxLab=np.copy(lab)
    fila=0
    col=0
    auxF=0
    auxC=0
    stop=0 #contador para ver cuando no hay movimiento
    pasos=1
    while(fila!=tamFil or col!=tamCol):
        auxF=fila
        auxC=col
        stop=0
        if(col+1>=0 and col+1<=tamCol and stop==0):
            if(lab[fila][col+1]==0):#mover a la derecha
                pasos=pasos+1
                lab[fila][col]=pasos
                col=col+1
                #print("derecha")
                stop=1
        if(col-1>=0 and col-1<=tamCol and stop==0):
            if(lab[fila][col-1]==0):#mover a la izquierda
                pasos=pasos+1
                lab[fila][col]=pasos
                col=col-1
                #print("izquierda")
                stop=1
        if(fila+1>=0 and fila+1<=tamFil and stop==0):
            if(lab[fila+1][col]==0):#mover a la abajo
                pasos=pasos+1
                lab[fila][col]=pasos
                fila=fila+1
                #print("abajo")
                stop=1
        if(fila-1>=0 and fila-1<=tamFil and stop==0):
            if(lab[fila-1][col]==0):#mover a la arriba
                pasos=pasos+1
                lab[fila][col]=pasos
                fila=fila-1
                #print("arriba")
                stop=1
                
        if(auxF==fila and auxC==col):#sin salida (regreso)
            if(col+1>=0 and col+1<=tamCol and stop==0):
                if(lab[fila][col+1]==pasos):#mover a la derecha
                    lab[fila][col]=1
                    pasos=pasos-1
                    col=col+1
                    #print("derecha")
                    stop=1
            if(col-1>=0 and col-1<=tamCol and stop==0):
                if(lab[fila][col-1]==pasos):#mover a la izquierda
                    lab[fila][col]=1
                    pasos=pasos-1
                    col=col-1
                    #print("izquierda")
                    stop=1
            if(fila+1>=0 and fila+1<=tamFil and stop==0):
                if(lab[fila+1][col]==pasos):#mover a la abajo
                    lab[fila][col]=1
                    pasos=pasos-1
                    fila=fila+1
                    #print("abajo")
                    stop=1
            if(fila-1>=0 and fila-1<=tamFil and stop==0):
                if(lab[fila-1][col]==pasos):#mover a la arriba
                    lab[fila][col]=1
                    pasos=pasos-1
                    fila=fila-1
                    #print("arriba")
                    stop=1
            
        #formatoA=np.copy(lab)
        #print(formatoA)
    lab[fila][col]=pasos+1
    for i in range(0, tamFil+1):#pasar la solucion al laberinto original
        for j in range(0, tamCol+1):
            if(auxLab[i][j]==0 and lab[i][j]!=1 and lab[i][j]!=0):
                auxLab[i][j]=lab[i][j]-1
        
    return auxLab
        
print("\n")         
print("----Laberinto----")
formatoS=np.copy(A)
print(formatoS)
   
s=resolverLab(A,7,7)#Parametros: Laberinto, tamaño de columnas, tamaño de filas

print("\n")         
print("----Solucion del laberinto----")
formatoS=np.copy(s)
print(formatoS)
