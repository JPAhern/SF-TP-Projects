# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 20:12:39 2022

@author: ahernjo
Comp Lab 3 Part (b)
"""

import numpy as np
import matplotlib.pylab as plt


B = 1.6*10**-4 # N s m^-2
C = 0.25 # N s^2 m^-4

b = 1.6*10**-8
g = 9.81
m = 1.05*10**-9
dt = 0.001

Ranges = []
CAngles = []

def MRange(V, theta, b, m):
    V_xi = V*np.cos(np.deg2rad(theta))
    V_yi = V*np.sin(np.deg2rad(theta))
    
    global T, Vl_y, Vl_x, Yl, Xl
    t, X, Y = 0, 0, 0
    T = []
    Vl_y = []
    Vl_x = []
    Yl = []
    Xl = []
    for i in range(0, 100000, 1):
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
            Ranges.append(X)
            CAngles.append(theta)
            break

def OptAngle(V, b, m):
    for i in range(0, 91, 1):
        MRange(V, i, b, m)


def MassAngle(V, b):
    global M, Ranges, CAngles, MRanges
    M = []
    MRanges = []
    for p in range(1, 751, 1):
        m = p/100000000000
        Ranges = []
        CAngles = []
        M.append(m)
        OptAngle(V, b, m)
        MRanges.append(Ranges.index(max(Ranges)))



# OptAngle(5, 1.6*10**-10, 1.05*10**-9)
# print(Ranges.index(max(Ranges)), max(Ranges), CAngles)


# Ranges=[]

# MRange(5, 45, 1.6*10**-10, 1.05*10**-9)
# MRange(5, 46, 1.6*10**-10, 1.05*10**-9)
# print(Ranges)

fig1 = plt.figure(dpi=1200)
plt.title("Plot of Range against Launch Angle", fontsize=14)
plt.xlabel("Launch Angle (degrees)", fontsize=12)
plt.ylabel("Range (m)", fontsize=12)
plt.grid(True)

OptAngle(5, 1.6*10**-8, 1.05*10**-9)
plt.plot(CAngles, Ranges, label = "b ~ $10^{-8}$")
print(Ranges.index(max(Ranges)))
Ranges, CAngles = [], []

OptAngle(5, 1.6*10**-9, 1.05*10**-9)
plt.plot(CAngles, Ranges, label = "b ~ $10^{-9}$")
print(Ranges.index(max(Ranges)))
Ranges, CAngles = [], []

OptAngle(5, 1.6*10**-10, 1.05*10**-9)
plt.plot(CAngles, Ranges, label = "b ~ $10^{-10}$")
print(Ranges.index(max(Ranges)))
Ranges, CAngles = [], []

x = np.arange(0, 90, 0.005)
plt.plot(x, 0.0*x, 'k')
plt.legend()


fig2 = plt.figure(dpi=1200)
plt.title("Plot of Optimal Launch Angle against Mass", fontsize=14)
plt.ylabel("Launch Angle (degrees)", fontsize=12)
plt.xlabel("Mass (kg)", fontsize=12)
plt.grid(True)
# x = np.arange(0, 90, 0.005)
# plt.plot(x, 0.0*x, 'k')

MassAngle(29, 1.6*10**-9)
plt.plot(M, MRanges, 'r')

plt.show()
