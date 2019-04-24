# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 08:59:46 2019

@author: lopez
"""
'''
while loop, find ma height
'''
v0 = 5 # meters per sec 
g = 9.81
n = 2000
X= 1000 # for github use 
# time steps 
# time
import numpy as np 
a_t = np.linspace(0,1,n) # we created an array 
# computations 
y = v0*a_t - 0.5*g*a_t**2

print( a_t)
print(y)

# find max height in while loop
i = 1 
while y[i] > y[i-1]:
    largest_height = y[i]
    i += 1 
    
print( 'max. hieght: %10.2f'%(largest_height) )
import matplotlib.pyplot as plt
plt.plot( a_t, y )
plt.show()
# the difference between a while loop and a for loop is that it will stop and it is more usful for comparing 
# for a for loop you would need a break statement 
# 