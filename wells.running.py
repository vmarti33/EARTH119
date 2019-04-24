# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:01:46 2019

@author: lopez
"""

"""
    (1)- create synthethic well pressure
    (2)- compute mean in each well 
    (3)- compute std in each well 
"""
#Parameteres
iWell = 10
iMeas = 12

#create synthetic data
import numpy as np 
a_mu_syn = np.random.random_integers(20, 40, iWell)
a_std_syn= np.random.random_integers(1, 10, iWell)*.1

m_Data = np.array([])
for i in range(iWell):
    if i ==0:
        m_Data = a_mu_syn[i]+a_std_syn[i]*np.random.randn(iMeas)
    else:
        m_Data = np.vstack( (m_Data, a_mu_syn[1]+ a_std_syn[i]*np.random.randn(iMeas)))
        

a_mean= np.dot(m_Data, np.ones(iMeas, dtype = float).reshape(iMeas,1))/iMeas

#test code performance 
print( 'syn results', np.round(a_mu_syn, 2) )
print('comp means', np.round(a_mean.flatten(),2))
#flatten means to convert a matrix into a one row matrix 
#
