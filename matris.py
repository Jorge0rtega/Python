# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#matriz
A= [[1,2,3,4],
    [5,4,2,7],
    [9,5,3,9]]

print("A= ", A)
print("Segunda fila de A = ", A[1])
print("Segunda fila de A segundo elemento = ", A[1][2])
print("Ultimo elemento de la ultima fila= ", A[2][-1])

#copiar una columna

colum=[] #lista vacia
for row in A:
    colum.append(row[2])
    print(row[2])
    
print(colum)


