"""
Created on Wed Oct 19 10:26:21 2022

@author: ahernjo
"""

# -*- coding: utf-8 -*-
# 21363697 - ahernjo@tcd.ie
#Ex 5

import numpy as np
import matplotlib.pylab as plt

k = 0.5
phi = 0.66667
A = 0.9

iteration_number = 0 
transient = 5000

theta = 1
omega = 0.0
t = 0.0
dt = 0.01
nsteps = []
theta_l = []
omega_l = []

def f(Theta, Omega, T):
    return (-Theta - k*Omega + A*np.cos(phi*T))

def f_nl(Theta, Omega, T, A):
    return (-np.sin(Theta) - k*Omega + A*np.cos(phi*T))

def plot_t(a_t, a_o, a, s):
    iteration_number = 0 
    transient = 25000
    a_t2 = a_t
    a_o2 = a_o    
    l = 0
    T = []
    theta_l = []
    omega_l = []
    
    fig1 = plt.figure(dpi=1200)    
    plt.xlabel("Omega (radians)", fontsize=12)    
    plt.ylabel("Theta (radians)", fontsize=12)
    plt.title("Plot Theta (%s) against Omega (%s) with Amplitude (%s)" % (a_t, a_o, a), fontsize=14)
    for i in range(0, 45000, 1):
        if iteration_number >= transient:
            theta_l.append(a_t2)
            omega_l.append(a_o2)
        T.append(l)
        k1a = dt * a_o2
        k1b = dt * f_nl(a_t2, a_o2, l, a)
        k2a = dt * (a_o2 + k1b/2)
        k2b = dt * f_nl(a_t2 + k1a/2, a_o2 + k1b/2, l + dt/2, a)
        k3a = dt * (a_o2 + k2b/2)
        k3b = dt * f_nl(a_t2 + k2a/2, a_o2 + k2b/2, l + dt/2, a)
        k4a = dt * (a_o2 + k3b)
        k4b = dt * f_nl(a_t2 + k3a, a_o2 + k3b, l + dt, a)
        a_t2 = a_t2 + (k1a + 2*k2a + 2*k3a + k4a) / 6
        a_o2 = a_o2 + (k1b + 2*k2b + 2*k3b + k4b) / 6
        iteration_number += 1
        l = l + dt       
        if (np.abs(a_t2) > np.pi):
            a_t2 -= 2 * np.pi * np.abs(a_t2) / a_t2
        if (a_t2 > np.pi + s):
            a_t2 -= 2*np.pi
        if (a_t2 < -np.pi + s):
            a_t2 += 2*np.pi
    plt.plot(omega_l, theta_l, 'ro', markersize=0.5)
    plt.grid(True)


plot_t(3, 0, 0.0, 0.4)
plot_t(3, 0, 0.9, 0.4)
plot_t(3, 0, 1.07, 0.4)
plot_t(3, 0, 1.35, 0.4)
plot_t(3, 0, 1.47, 0.08)
plot_t(3, 0, 1.5, -0.2)
#plot_t(3, 0, 1.8, 0.4)

plt.show()