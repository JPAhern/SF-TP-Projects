# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:46:58 2022

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
t_m = 10
V = 0
t=0

print("Mass =", m)

T = []
V_y = []

# fig1 = plt.figure(dpi=1200)
# plt.title("Plot of V$_y$(t) against t", fontsize=14)
# x = np.arange(0, 0.5, 0.005)
# plt.plot(x, 0.0*x, 'k')
# plt.xlabel("t (s)", fontsize=12)
# plt.ylabel("V$_y$(t) (m/s)", fontsize=12)
# plt.grid(True)


# for i in range(0, 500, 1):
#     T.append(t)
#     V_y.append(V)
#     dV = -g*dt - (b/m)*V*dt
#     V = V + dV
#     t = t + dt
    
# print(T)
# print(V_y)
# plt.plot(T, V_y, label = "Numerical V$_y$(t)")

# plt.legend()

def an_V(m,t):
    return ((m*g)/b)*(np.exp(-((b*t)/m))-1)

#print(an_V(1.05*10**-8, 4))

V = 0
t=0
error = 0
T = []
V_y = []
aV_y = []

fig2 = plt.figure(dpi=1200)
plt.title("Plot of Error against t", fontsize=14)
x = np.arange(0, 0.6, 0.005)
plt.plot(x, 0.0*x, 'k')
plt.xlabel("t (s)", fontsize=12)
plt.ylabel("Error (m/s)", fontsize=12)
plt.grid(True)


for i in range(0, 600, 1):
    error = an_V(m,t) - V
    T.append(t)
    V_y.append(V)
    aV_y.append(error)
    dV = -g*dt - (b/m)*V*dt
    V = V + dV
    t = t + dt

plt.plot(T, aV_y, 'r', label = "Analytical $-$ Numerical")

plt.legend()

#(e)

# fig3 = plt.figure(dpi=1200)
# plt.title("Plot of height against time", fontsize=14)
# x = np.arange(0, 5, 0.005)
# plt.plot(x, 0.0*x, 'k')
# plt.xlabel("t (s)", fontsize=12)
# plt.ylabel("Height (m)", fontsize=12)
# plt.grid(True)

# m = 1.05*10**-9
# V = 0
# Y = 5
# t = 0

# T = []
# Y_h = []

# for i in range(0, 1000000, 1):
#     if Y > 0:
#         T.append(t)
#         Y_h.append(Y)
#         V = V + dt*an_V(m,t)
#         Y = Y + dt*V
#         t = t + dt
#     else:
#         print("Time of Flight =", t)
#         break
    
# plt.plot(T, Y_h, 'g', label = "Y$_{pos}$(t)")

# plt.legend()

# fig4 = plt.figure(dpi=1200)
# plt.title("Plot of Time of Flight against Mass", fontsize=14)
# plt.xlabel("Mass (kg)", fontsize=12)
# plt.ylabel("Time (s)", fontsize=12)
# plt.grid(True)


# M = []
# T_t = []

# for p in range(1, 250, 1):
#     V = 0
#     Y = 5
#     t = 0
#     m = p/100000000000
#     M.append(m)
#     for i in range(0, 10000000, 1):
#         if Y > 0:
#             V = V + dt*an_V(m,t)
#             Y = Y + dt*V
#             t = t + dt
#         else:
#             T_t.append(t)
#             break

# plt.plot(M, T_t, 'y', label = "Time/Mass")

# plt.legend()

plt.show()


