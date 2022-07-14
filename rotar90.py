# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:13:07 2022

@author: Jorge Ortega
"""

#imagen
import numpy as np
#tamaño 4
A= [[1,1,1,0],
    [1,1,0,0],
    [1,0,1,0],
    [1,0,0,1]]

#tamaño 2
B= [[1,0],
    [1,0]]

#tamaño 8
C= [[1,1,1,1,1,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,0,1,0,0,0],
    [1,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1]]

def rotar90(img, tam):
    mitad=int(tam/2) #la mitad del arreglo
    auxImg=np.copy(img)
    if(tam==2):# caso base
        auxImg[0][0]=img[1][0]
        auxImg[0][1]=img[0][0]
        auxImg[1][0]=img[1][1]
        auxImg[1][1]=img[0][1]
        return auxImg
    else:
        newImg=np.identity(mitad, int) #crea una matriz vacia del tamaño del parametro
        #separar la matriz en cuadrantes
        #primer cuadrante
        for i in range(0, mitad): #0-1    
            for j in range(0, mitad): #0-1
                newImg[i][j]=auxImg[i][j]
        C1=rotar90(newImg, mitad) #se itera hasta que se tenga una matriz de 2x2
        #segundo cuadrante
        for i in range(0, mitad):#0-1    
            for j in range(mitad, tam): #2-3
                newImg[i][j-mitad]=auxImg[i][j]
        C2=rotar90(newImg, mitad)
        #tercer cuadrante
        for i in range(mitad, tam):#2-3    
            for j in range(0, mitad): #0-1
                newImg[i-mitad][j]=auxImg[i][j]
        C3=rotar90(newImg, mitad)
        #cuarto cuadrante
        for i in range(mitad, tam):#2-3    
            for j in range(mitad, tam): #2-3
                newImg[i-mitad][j-mitad]=auxImg[i][j]
        C4=rotar90(newImg, mitad)
        
    #unir cuadrantes rotados, girando al sentido del reloj
    rotImg=np.identity(tam, int) #crea una matriz vacia del tamaño del parametro
    #primer cuadrante - tercer cuadrante
    for i in range(0, mitad): #0-1    
        for j in range(0, mitad): #0-1
            rotImg[i][j]=C3[i][j]
            #print(newImg[i][j])
            
    #print(rotImg)
    #segundo cuadrante - primer cuadrante
    for i in range(0, mitad):#0-1    
        for j in range(mitad, tam): #2-3
            rotImg[i][j]=C1[i][j-mitad]
    #print(rotImg)
    #tercer cuadrante - cuarto cuadrante
    for i in range(mitad, tam):#2-3    
        for j in range(0, mitad): #0-1
            rotImg[i][j]=C4[i-mitad][j]
    #print(rotImg)
    #cuarto cuadrante - segundo cuadrante
    for i in range(mitad, tam):#2-3    
        for j in range(mitad, tam): #2-3
            rotImg[i][j]=C2[i-mitad][j-mitad]
    
    
    return rotImg    
    
            

auxA=rotar90(C, 8)   # matriz a rotar 90 grados al sentido del reloj, tamaño de la matriz     
formatoA=np.copy(auxA)
print("\n------resultado de la rotación-----\n")
print(formatoA) 
print("\nNota: no se puede ver la rotacion de la matriz paso a paso, ya que")
print("al ser resuelta por divide y venceras, saldran soluciones de matrices 4x4")     
print("(en el caso de una matriz 8x8), que vistas a simple vista no tienen sentido, ")
print("hasta que se realiza el corrimiento y union de cada una de ellas formando la solucion \n")
   