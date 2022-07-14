# -*- coding: utf-8 -*-
"""
Ortega Silva Jorge Eduardo
Solver sudoku 3x3 (suma f/c=15)

"""

A= [[8,0,0],
    [0,5,0],
    [4,9,0]]

solucion=[]

def resolverSudoku(sudo):

    resuelto=0
    while resuelto==0:#repetir hasta que no encuentre ceros
        resuelto=1
        for i in range(0,3):#contar los numeros que hay en las filas
            for j in range(0,3):
                if(sudo[i][j]==0):
                    resuelto=0
        if resuelto==0:#si hay algun 0 rsolver por filas
            resueltoFilas=resolverSudokuFilas(sudo)

        for i in range(0,3):#contar los numeros que hay en las filas
            for j in range(0,3):
                if(sudo[i][j]==0):
                    resuelto=0
        if resuelto==0:#si hay algun 0 resolver por columnas
            sudo=resolverSudokuColumnas(resueltoFilas)
    return sudo
    
def resolverSudokuColumnas(sudoCol):
    colElegida=2
    while colElegida!=-1:
        i=0
        j=0
        colElegida=0
        numerosCol=[0,0,0]
        n=[0,0,0]
        for i in range(0,3):#contar los numeros que hay en las columnas
            for j in range(0,3):
                if(sudoCol[j][i]!=0):
                    numerosCol[i]=numerosCol[i]+1
        i=0
        while (i!=3):#buscar la columna con 2 elementos
            if(numerosCol[i]==2):
                for j in range(0,3):
                    n[j]=sudoCol[j][i]
                colElegida=i
                i=2
            else:
                colElegida=-1
            i+=1
                
                
        if(colElegida!=-1):
            for i in range(0,3):#al elemento 0 cambiarlo por el correspondiente
                if n[i]==0:
                    j=1
                    while (n[0]+n[1]+n[2]!=15):#hasta que la suma sea 15
                        n[i]=j;
                        j+=1;
                        
            for i in range(0,3):#actualizar el sudoku
                sudoCol[i][colElegida]=n[i]    
    return sudoCol

def resolverSudokuFilas(sudoFila):
    filaElegida=2
    while filaElegida!=-1:
        i=0
        j=0
        filaElegida=0
        numerosFilas=[0,0,0]
        n=[0,0,0]
        for i in range(0,3):#contar los numeros que hay en las filas
            for j in range(0,3):
                if(sudoFila[i][j]!=0):
                    numerosFilas[i]=numerosFilas[i]+1
        
        i=0
        while (i!=3):#buscar la columna con 2 elementos
            if(numerosFilas[i]==2):
                for j in range(0,3):
                    n[j]=sudoFila[i][j]
                filaElegida=i
                i=2
            else:
                filaElegida=-1
            i+=1
        
                
        if(filaElegida!=-1):
            for i in range(0,3):#al elemento 0 cambiarlo por el correspondiente
                if n[i]==0:
                    j=1
                    while (n[0]+n[1]+n[2]!=15):#hasta que la suma sea 15
                        n[i]=j;
                        j+=1;
                        
            for i in range(0,3):#actualizar el sudoku
                sudoFila[filaElegida][i]=n[i]
    
    return sudoFila
                
             
print("----Sudoku----")
for i in range(0,3):#Imprimir resultado
    print("|",A[i][0], A[i][1],  A[i][2], "|")                
                
solucion=resolverSudoku(A)   
     
print("\n")         
print("----Solucion del sudoku----")
for i in range(0,3):#Imprimir resultado
    print("|",solucion[i][0], solucion[i][1],  solucion[i][2], "|")