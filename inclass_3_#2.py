# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:10:06 2019

@author: lopez
"""
import numpy as np 
import os 
### Create sample data 
file_out = 'dataIO_ex.text'
N = 10 
aX = np.arange(N)
aY = aX**2










#### Methods to load data and save data 
print(os.getcwd())
np.savetxt( file_out, np.array([aX,aY]).T, #fmt='%4.0f%4.0f',
           header = 'X  X^2')

mData = np.loadtxt(file_out).T 
print(mData)
## read file line by line 
with open(file_out, 'r') as file_obj:
    file_obj.next()
    for line in file_obj:
        lStr = line.split('')
        print(lStr)
        for my_str in lStr:
            print(int(float(my_str)))
            
            
### Read and write binary data 
import scipy.io
scipy.io.savemat(file_out.replace('txt', 'mat'),{'X' : aX, 'Y' : aY}, do_compression = True)
dicData = scipy.io.loadmat(file_out.replace('txt', 'mat'))
print( dicData['X'])
print( dicData['Y'])


        