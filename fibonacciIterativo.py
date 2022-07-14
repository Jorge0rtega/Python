# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 21:45:30 2022

@author: Jorge Ortega
"""

import time
inicio = time.time()
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
        print(a)
    return a

print(f(1100))

fin = time.time()
print(fin-inicio)