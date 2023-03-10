# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:21:51 2022

@author: ahernjo
Comp Lab 3
"""

import numpy as np
import matplotlib.pylab as plt


B = 1.6*10**-4 # N s m^-2
C = 0.25 # N s^2 m^-4

b = 1.6*10**-8
g = 9.81
m = 1.05*10**-9
dt = 0.001

def Trag(V_yi, V_xi, Y, X, t, b):
    global T, Vl_y, Vl_x, Yl, Xl
    T = []
    Vl_y = []
    Vl_x = []
    Yl = []
    Xl = []
    for i in range(0, 10000, 1):
        if Y >= 0:
            T.append(t)
            Vl_y.append(V_yi)
            Yl.append(Y)
            Vl_x.append(V_xi)
            Xl.append(X)
            
            dYVl = -g*dt - (b/m)*V_yi*dt
            V_yi = V_yi + dYVl
            
            dXVl = - (b/m)*V_xi*dt
            V_xi = V_xi + dXVl
            
            Y = Y + dt*V_yi
            X = X + dt*V_xi
            t = t + dt
        else:
            print("Range is :", X)
            break



fig1 = plt.figure(dpi=1200)
plt.title("Plot of Y against X", fontsize=14)
plt.xlabel("X (m)", fontsize=12)
plt.ylabel("Y (m)", fontsize=12)
plt.grid(True)

Trag(5, 9, 0, 0, 0, 1.6*10**-9)
plt.plot(Xl, Yl, label = "b ~ $10^{-9}$")
Trag(5, 9, 0, 0, 0, 1.6*10**-10)
plt.plot(Xl, Yl, label = "b ~ $10^{-10}$")
Trag(5, 9, 0, 0, 0, 0)
plt.plot(Xl, Yl, label = "Vacuum")

x = np.arange(0, 10, 0.005)
plt.plot(x, 0.0*x, 'k')
plt.legend()



plt.show()
