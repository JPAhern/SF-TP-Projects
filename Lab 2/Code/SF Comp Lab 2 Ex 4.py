"""
Created on Wed Oct 19 10:26:21 2022

@author: ahernjo
"""

# -*- coding: utf-8 -*-
# 21363697 - ahernjo@tcd.ie
#Ex 4

import numpy as np
import matplotlib.pylab as plt

k = 0.5
phi = 0.66667
A = 0.0

theta = 1
omega = 0.0
t = 0.0
dt = 0.01
nsteps = []
theta_l = []
omega_l = []

def f(Theta, Omega, T):
    return (-Theta - k*Omega + A*np.cos(phi*T))

def f_nl(Theta, Omega, T):
    return (-np.sin(Theta) - k*Omega + A*np.cos(phi*T))

def plot_t(a_t, a_o):
    a_t2 = a_t
    a_o2 = a_o    
    l = 0
    T = []
    theta_l = []
    omega_l = []
    for i in range(0, 2500, 1):
        theta_l.append(a_t2)
        omega_l.append(a_o2)
        T.append(l)
        k1a = dt * a_o2
        k1b = dt * f_nl(a_t2, a_o2, l)
        k2a = dt * (a_o2 + k1b/2)
        k2b = dt * f_nl(a_t2 + k1a/2, a_o2 + k1b/2, l + dt/2)
        k3a = dt * (a_o2 + k2b/2)
        k3b = dt * f_nl(a_t2 + k2a/2, a_o2 + k2b/2, l + dt/2)
        k4a = dt * (a_o2 + k3b)
        k4b = dt * f_nl(a_t2 + k3a, a_o2 + k3b, l + dt)
        a_t2 = a_t2 + (k1a + 2*k2a + 2*k3a + k4a) / 6
        a_o2 = a_o2 + (k1b + 2*k2b + 2*k3b + k4b) / 6
        l = l + dt 
    fig2 = plt.figure(dpi=1200)
    plt.axis([0, 25, -np.pi, np.pi]) 
    plt.title("Plot Theta (%s) against Time" % (a_t), fontsize=14)
    plt.plot(T, theta_l, markersize=5, label=("Theta"))
    plt.xlabel("t (s)", fontsize=12)    
    plt.ylabel("Theta (radians)", fontsize=12)
    plt.grid(True)
    plt.legend()
    fig3 = plt.figure(dpi=1200)    
    plt.axis([0, 25, -np.pi, np.pi]) 
    plt.title("Plot Omega (%s) against Time" % (a_o), fontsize=14)
    plt.plot(T, omega_l, markersize=5, label=("Omega"))
    plt.xlabel("t (s)", fontsize=12)
    plt.ylabel("Omega (radians)", fontsize=12)
    plt.grid(True) 
    plt.legend()



plot_t(3, 0)
# plot_t(0, 3)


plt.show()