# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:02:54 2019

@author: lopez
"""
import numpy as np
pi = np.pi
total = 0
n = 50 
for i in range(n+1):
    term = 8 /((4*i + 1)*(4*i + 3))
    total = total + term 
    print( 'term' + str(term))
print(total)
