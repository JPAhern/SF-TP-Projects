# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 22:57:06 2022

@author: ahernjo
Comp Lab 3 Part (b)
"""

import numpy as np
import matplotlib.pylab as plt


B = 1.6*10**-4 # N s m^-2
C = 0.25 # N s^2 m^-4
D = 0.0001

c = 2.5*10**-9
b = 1.6*10**-8
g = 9.81
m = 1.05*10**-9
dt = 0.001

Ranges = []
CAngles = []

def Vel_lin(V, theta, b, m):
    V_xi = V*np.cos(np.deg2rad(theta))
    V_yi = V*np.sin(np.deg2rad(theta))
    
    global T, Vl_y, Vl_x, Yl, Xl
    t, X, Y = 0, 0, 0
    T = []
    Vl_y = []
    Vl_x = []
    Yl = []
    Xl = []
    for i in range(0, 1000000, 1):
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


def Vel_quad(V, theta, c, m):
    V_xi = V*np.cos(np.deg2rad(theta))
    V_yi = V*np.sin(np.deg2rad(theta))
    
    t, X, Y = 0, 0, 0
    T = []
    Vl_y = []
    Vl_x = []
    Yl = []
    Xl = []
    for i in range(0, 1000000, 1):
        if Y >= 0:
            T.append(t)
            Vl_y.append(V_yi)
            Yl.append(Y)
            Vl_x.append(V_xi)
            Xl.append(X)
            
            dYVl = -g*dt - (c/m)*V*V_yi*dt
            V_yi = V_yi + dYVl
            
            dXVl = - (c/m)*V*V_xi*dt
            V_xi = V_xi + dXVl
            
            V = (V_xi**2 + V_yi**2)**(1/2)
            
            Y = Y + dt*V_yi
            X = X + dt*V_xi
            t = t + dt
        else:
            break



# def OptAngle(V, b, m):
#     for i in range(0, 91, 1):
#         MRange(V, i, b, m)


# def MassAngle(V, b):
#     global M, Ranges, CAngles, MRanges
#     M = []
#     MRanges = []
#     for p in range(1, 751, 1):
#         m = p/100000000000
#         Ranges = []
#         CAngles = []
#         M.append(m)
#         OptAngle(V, b, m)
#         MRanges.append(Ranges.index(max(Ranges)))





fig1 = plt.figure(dpi=1200)
plt.title("Plot of Trajectory", fontsize=14)
plt.xlabel("X (m)", fontsize=12)
plt.ylabel("Y (m)", fontsize=12)
plt.grid(True)


Vel_lin(7, 35, 0, 1.05*10**-9)
plt.plot(Xl, Yl, 'r', label = "Vacuum")

Vel_lin(7, 35, 2.5*10**-9, 1.05*10**-9)
plt.plot(Xl, Yl, label = "Quadratic")

Vel_lin(7, 35, 1.6*10**-9, 1.05*10**-9)
plt.plot(Xl, Yl, label = "Linear")

x = np.arange(0, 5, 0.005)
plt.plot(x, 0.0*x, 'k')
plt.legend()


fig2 = plt.figure(dpi=1200)
plt.title("Plot of Trajectory", fontsize=14)
plt.xlabel("X (m)", fontsize=12)
plt.ylabel("Y (m)", fontsize=12)
plt.grid(True)


Vel_lin(9, 40, 0, 1.05*10**-8)
plt.plot(Xl, Yl, 'r', label = "Vacuum")

Vel_lin(9, 40, 2.5*10**-9, 1.05*10**-8)
plt.plot(Xl, Yl, label = "Quadratic")

Vel_lin(9, 40, 1.6*10**-9, 1.05*10**-8)
plt.plot(Xl, Yl, label = "Linear")

x = np.arange(0, 9, 0.005)
plt.plot(x, 0.0*x, 'k')
plt.legend()

fig3 = plt.figure(dpi=1200)
plt.title("Plot of Trajectory", fontsize=14)
plt.xlabel("X (m)", fontsize=12)
plt.ylabel("Y (m)", fontsize=12)
plt.grid(True)


Vel_lin(15, 43, 0, 1.05*10**-9)
plt.plot(Xl, Yl, 'r', label = "Vacuum")

Vel_lin(15, 43, 2.5*10**-9, 1.05*10**-9)
plt.plot(Xl, Yl, label = "Quadratic")

Vel_lin(15, 43, 1.6*10**-9, 1.05*10**-9)
plt.plot(Xl, Yl, label = "Linear")

x = np.arange(0, 23, 0.0005)
plt.plot(x, 0.0*x, 'k')
plt.legend()

plt.show()
