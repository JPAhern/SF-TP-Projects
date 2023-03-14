# -*- coding: utf-8 -*-
"""
@author: Jordan Ahern 21363697
Chaos Assignment, March 2023
The Lotka-Volterra Equations - Eulers Method 
"""

import matplotlib.pylab as plt

k_1 = 0.09
k_2 = 0.0018
k_3 = 0.0023
k_4 = 0.12

dt = 0.01
T_total = 100000


def X_i(X,Y):
    return X+X*(k_1-k_2*Y)*dt

def Y_i(X,Y):
    return Y+Y*(k_3*X-k_4)*dt

def itterate(X,Y):
    steps=[]
    X_list=[]
    Y_list=[]
    for i in range(0, T_total, 1):
        Xt = X_i(X,Y)
        Yt = Y_i(X,Y)
        steps.append(i*dt)
        X=Xt
        Y=Yt
        X_list.append(X)
        Y_list.append(Y)
    return steps, X_list, Y_list

def plot_XY(X,Y):
    steps, X_list, Y_list = itterate(X,Y)
    return plt.plot(steps, X_list, 'ro', markersize=1, label=("X")), plt.plot(steps, Y_list, 'bo', markersize=1, label=("Y"))

def plot_phase(X,Y):
    steps, X_list, Y_list = itterate(X,Y)
    return plt.plot(X_list, Y_list, 'yo', markersize=1)

fig1 = plt.figure(dpi=1200)
plt.grid(True)
plt.title("Plot X(t), Y(t) against time (Euler)", fontsize=14)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("X(t), Y(t)", fontsize=12)
plot_XY(47,50)
plt.legend()
#plt.savefig('Fig7.pdf', format='pdf', dpi=1200, bbox_inches='tight')


fig2 = plt.figure(dpi=1200)
plt.grid(True)
plt.title("Phase Space Graph (Euler)", fontsize=14)
plt.xlabel("X(t)", fontsize=12)
plt.ylabel("Y(t)", fontsize=12)
plt.plot(0,0, 'bo', label=("Fixed Point 1"))
plt.plot((k_4)/(k_3), (k_1)/(k_2), 'ro', label=("Fixed Point 2"))
plot_phase(5,5)
plot_phase(15,10)
plot_phase(20,24)
plot_phase(30,35)
plot_phase(55,45)
#plot_phase(1,2)
#plot_phase(0.9,0.1)
plt.legend()
#plt.savefig('Fig6.pdf', format='pdf', dpi=1200, bbox_inches='tight')

plt.show()
