# -*- coding: utf-8 -*-
# 21363697 - ahernjo@tcd.ie
#Ex 3

import numpy as np
import matplotlib.pylab as plt

k = 0.0
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
    fig2 = plt.figure(dpi=1200)
    plt.axis([0, 120, -np.pi, np.pi]) 
    plt.title("Plot Theta (%s) against Time" % (a_t), fontsize=14)
    plt.xlabel("t (s)", fontsize=12)    
    plt.ylabel("Theta (radians)", fontsize=12)
    l = 0
    T = []
    theta_l = []
    omega_l = []
    for i in range(0, 12000, 1):
        theta_l.append(a_t)
        omega_l.append(a_o)
        T.append(l)
        k1a = dt * a_o
        k1b = dt * f_nl(a_t, a_o, l)
        k2a = dt * (a_o + k1b/2)
        k2b = dt * f_nl(a_t + k1a/2, a_o + k1b/2, l + dt/2)
        k3a = dt * (a_o + k2b/2)
        k3b = dt * f_nl(a_t + k2a/2, a_o + k2b/2, l + dt/2)
        k4a = dt * (a_o + k3b)
        k4b = dt * f_nl(a_t + k3a, a_o + k3b, l + dt)
        a_t = a_t + (k1a + 2*k2a + 2*k3a + k4a) / 6
        a_o = a_o + (k1b + 2*k2b + 2*k3b + k4b) / 6
        l = l + dt
    plt.plot(T, theta_l, markersize=5, label=("Runge-Kutta"))
    l = 0
    T = []
    theta_2 = []
    omega_2 = []
    for i in range(0, 12000, 1):
        theta_2.append(a_t2)
        omega_2.append(a_o2)
        T.append(l)
        k1a = dt * a_o2
        k1b = dt * f_nl(a_t2, a_o2, l)
        k2a = dt * (a_o2 + k1b)
        k2b = dt * f_nl(a_t2 + k1a, a_o2 + k1b, l + dt)        
        a_t2 = a_t2 + (k1a + k2a)/2
        a_o2 = a_o2 + (k1b + k2b)/2
        l = l + dt
    plt.plot(T, theta_2, markersize=5, label=("Trapezoid"))    
    plt.grid(True)
    plt.legend()



plot_t(3, 0)
plt.legend()
plot_t(3.1415, 0)
plt.legend()


plt.show()