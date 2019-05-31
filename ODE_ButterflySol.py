# -*- coding: utf-8 -*-
"""
We will solve for the set of idealized ODEs, The Lorenz Equations, using the Runge Kutta 4th order  
    - We will also analyze its non-periodic system and sensitivty to initial conditions 
    - 
from __future__ import division

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
"""
#--------------fct definitions--------------------------
def runge_kutta_vec( tn, Yn, fct_RHS, params):
    """
    fourth order runge kutta stepper, for single or system of  ODEs
    :input       tn           - current time step
                 Yn           - function value at time tn
                 fct_RHS      - vectorised function that defines slope (derivative) at point (t, y)
                                = all RHS of the system of ODEs

                 params   - py dictionary that includes step size 'h'
                            and all parameters needed in function:
                            fct_RHS

    :return: a_fn1 - values of derivatives at current tn for all ODEs
    """
    h = params['h']
    Kn1 = fct_RHS( tn , Yn,   params)
    Kn2 = fct_RHS( tn + h*.5, Yn + h*.5*Kn1,  params)
    Kn3 = fct_RHS( tn + h*.5, Yn + h*.5*Kn2,  params)
    Kn4 = fct_RHS( tn + h*.5 ,Yn + h*.5*Kn3,  params)
    return (Kn1 + 2*Kn2 + 2*Kn3 + Kn4)/6
def f_ctx(sigma, x, y):
    return 
def runge_kutta_vec(x, y, z, f_ctx, f_cty, f_ctz, params):
    x1 = fa(a, b, c)*
    y1 = fb(a, b, c)*hs
    z1 = f_ctz(a, b, c)*hs
    ak = a + a1*0.5
    bk = b + b1*0.5
    ck = c + c1*0.5
    a2 = fa(ak, bk, ck)*hs
    b2 = fb(ak, bk, ck)*hs
    c2 = fc(ak, bk, ck)*hs
    ak = a + a2*0.5
    bk = b + b2*0.5
    ck = c + c2*0.5
    a3 = fa(ak, bk, ck)*hs
    b3 = fb(ak, bk, ck)*hs
    c3 = fc(ak, bk, ck)*hs
    ak = a + a3
    bk = b + b3
    ck = c + c3
    a4 = fa(ak, bk, ck)*hs
    b4 = fb(ak, bk, ck)*hs
    c4 = fc(ak, bk, ck)*hs
    a = a + (a1 + 2*(a2 + a3) + a4)/6
    b = b + (b1 + 2*(b2 + b3) + b4)/6
    c = c + (c1 + 2*(c2 + c3) + c4)/6
    return a, b, c

def oscillator( t, Yn, par):
    """
        ODE:  x' + sigma*x = sigma*y 
              y' +  y = x*(rho - z)
              z' +  beta*z = x*y 
             u   =  y; v = y'
             u'  =  v
             v'  = 
    :input - t - time vector
             u  - displacement
             v  - velocity
             w  - 
             F  - amplitude of forcing fct
             w0 -  parameter: natural fequency: w0**2 = k/m

    :return:  [displ, vel, ]
    """
    u, v, w= Yn[0], Yn[1], Yn[2]
    fn1 = v
    fn2 = -par['w0']**2*u - par['gamma']*v 
    fn3 = 
    # num. params
    return np.array([fn1, fn2, fn3)

def num_sol( at, y0, par):
    """
    - solve second order ODE for forced, undamped oscillation by solving two first order ODEs
       ODE:  y''(t) + ky(t) = f(t)
                              f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :       - time vector
    :param par :       - dictionary with fct parameters
    :return: ay_hat    - forward Euler
             ay_hat_rk = 4th order runge kutta
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    # set initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        # slope at previous time step, i
        fn1, fn2     = runge_kutta_vec( at[i], np.array([au_hat[i], av_hat[i]]), oscillator, dPar)
        # forward Euler: y[n+1] = y[n] + fn*h
        #fn1 = av_hat[i]
        #fn2 = -par['w0']**2*au_hat[i]

        # Integration step: Runge Kutta or Euler formula
        au_hat[i+1] = au_hat[i] + fn1*dPar['h']
        av_hat[i+1] = av_hat[i] + fn2*dPar['h']
    return au_hat, av_hat

#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = { #frequencies
        'sigma':  10, #= sqrt(k/m) --> natural frequency
        'rho'  :   28,
        'beta' : 8/3 # damping constant, set to 0 to compare to exact solution
        # initial conditions for displ. and velocity
        'x0' : 1.0, 'y0' : 1.0, 'z0' : 1.0, 
        # time stepping
        'h'      : 1e-2,
        'tStart' : 0,
        'tStop'  : 100,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
ay_ana    = dPar['y01']*np.cos(dPar['w0']*a_t)

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)
#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
ax = plt.subplot( 111) #plt.axes( [.12, .12, .83, .83])
ax.plot( a_t,   aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.plot( a_t,  ay_ana, 'r--', lw = 1, label = 'ana')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()