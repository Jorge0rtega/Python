# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:49:23 2022

@author: Jorge Ortega
"""
import numpy as np

tabla = np.empty((1, 5), float)
def amortizacion(capital, taza, plazo, renta, tabla):  #(capital, taza, periodo de inicio, renta, matriz a llenar )
    interes=capital*taza
    amort=renta-interes
    saldo=capital-amort
    plazo=plazo+1
    if(saldo<1 ):#caso base
        #llenado de la ultima fila de la tabla
        tabla = np.append(tabla, np.array([[format(plazo, '.1f'), format(renta, '.2f'), format(interes, '.2f'), format(amort, '.2f'), format(saldo, '.2f')]]), axis=0)
        return tabla
    else:
        #llenado de la segunda fila de la tabla a la penultima
        tabla = np.append(tabla, np.array([[format(plazo, '.1f'), format(renta, '.2f'), format(interes, '.2f'), format(amort, '.2f'), format(saldo, '.2f')]]), axis=0)       
        tabla=amortizacion(saldo, taza, plazo, renta, tabla)
        #para rellenar la primera fila de la tabla
        for i in range(0, 4):
            tabla[0][i]=0
        tabla[0][4]=capital
        return tabla
        
#calculo de la renta    
def renta(capital, taza, plazo):
    return capital*taza/(1-(1+taza)**-plazo)


renta=renta(500000, 0.08, 5)
print(amortizacion(500000, 0.08, 0, renta, tabla))#parametros(capital, taza, periodo de inicio, renta, matriz a llenar )
        