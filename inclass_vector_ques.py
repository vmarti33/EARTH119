# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:52:01 2019

@author: lopez

"""
"""
    determine thr crossover point between two functions 
    f(t) and g(t)
    (1)- as a loop 
    (2)- vectorized problem using numpy 
"""
#Parameters 
#
# 

tmin, tmax = -10, 10 
iN         = 1000
f_dt       = float(tmax-tmin)/(iN-1) 


#fct params
t0= 2.5
c=  1.1
A=  5
eps= 0.1

#Function def
# 
#

def f_t(t,c,t0):
    return c*(t-t0)**2
def g_t(t, A):
    return A*t+t0

#find cross over point
#
#
f_curr_t = tmin
for i in range(iN):
    f_curr_t += f_dt
    f_curr_f_t = f_t( f_curr_t, c, t0)
    f_curr_g_t = g_t(f_curr_t, A)
    # fct value comaprison 
    if abs( f_curr_f_t - f_curr_g_t) < eps:
        print("croos over point at t=%.2f, f(t)=%.2f, g(t)=%.2f"%(f_curr_t, f_curr_f_t, f_curr_g_t))
        
##B## vectorized solution 
import numpy as np 
a_t= np.linspace(tmin, tmax, iN)
#evaluate fct
a_ft= f_t(a_t, c, t0)
a_gt= g_t(a_t, A)
#find cross over
sel= abs(a_ft - a_gt) < eps
print( 'cross over point' , a_t[sel], a_ft[sel], a_gt[sel])

#plot function 
import matplotlib.pyplot as plt
plt.plot(a_t, a_ft,'ro', ms=2)
plt.plot(a_t, a_gt,'go', ms=2 )
plt.show()

         
        
        
        
    