# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 21:48:35 2022

@author: Jorge Ortega
"""
import time
inicio = time.time()
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


print("Fibonacci sequence:")
for i in range(35):
    print(recur_fibo(i))

fin = time.time()
print(fin-inicio)