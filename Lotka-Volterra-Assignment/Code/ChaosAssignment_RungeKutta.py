# -*- coding: utf-8 -*-
"""
@author: Jordan Ahern 21363697
Chaos Assignment, March 2023
The Lotka-Volterra Equations - Runge Kutta
"""

import matplotlib.pylab as plt

k_1 = 0.09
k_2 = 0.0018
k_3 = 0.0023
k_4 = 0.12

dt = 0.01
T_total = 10000

def X_dot(X,Y):
    DX = X*(k_1-k_2*Y)
    return DX

def Y_dot(X,Y):
    DY = Y*(k_3*X-k_4)
    return DY

def X1(X,Y):
    R1 = X_dot(X,Y)
    return R1

def Y1(X,Y):
    R1 = Y_dot(X,Y)
    return R1

def X2(X,Y):
    R2 = X_dot((X+((dt/2)*X1(X,Y))),(Y+((dt/2)*Y1(X,Y))))
    return R2

def Y2(X,Y):
    R2 = Y_dot((X+((dt/2)*X1(X,Y))),(Y+((dt/2)*Y1(X,Y))))
    return R2

def X3(X,Y):
    R3 = X_dot((X+((dt/2)*X2(X,Y))),(Y+((dt/2)*Y2(X,Y))))
    return R3

def Y3(X,Y):
    R3 = Y_dot((X+((dt/2)*X2(X,Y))),(Y+((dt/2)*Y2(X,Y))))
    return R3

def X4(X,Y):
    R4 = X_dot((X+((dt)*X3(X,Y))),(Y+((dt)*Y3(X,Y))))
    return R4

def Y4(X,Y):
    R4 = Y_dot((X+((dt)*X3(X,Y))),(Y+((dt)*Y3(X,Y))))
    return R4

def X_i(X,Y):
    XN = X + (dt/6)*(X1(X,Y)+2*X2(X,Y)+2*X3(X,Y)+X4(X,Y))
    return XN

def Y_i(X,Y):
    YN = Y + (dt/6)*(Y1(X,Y)+2*Y2(X,Y)+2*Y3(X,Y)+Y4(X,Y))
    return YN

def itterate(X,Y):
    steps=[]
    X_list=[]
    Y_list=[]
    for i in range(0, T_total, 1):
        steps.append(i*dt)
        Xt = X_i(X,Y)
        Yt = Y_i(X,Y)
        X = Xt
        Y = Yt
        X_list.append(X)
        Y_list.append(Y)
    return steps, X_list, Y_list

def plot_XY(X,Y):
    steps, X_list, Y_list = itterate(X,Y)
    return plt.plot(steps, X_list, 'ro', markersize=1, label=("X")), plt.plot(steps, Y_list, 'bo', markersize=1, label=("Y"))

def plot_phase(X,Y):
    steps, X_list, Y_list = itterate(X,Y)
    return plt.plot(X_list, Y_list, 'o', markersize=1)

fig1 = plt.figure(dpi=1200)
plt.grid(True)
plt.title("Plot X(t), Y(t) against time", fontsize=14)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("X(t), Y(t)", fontsize=12)
plot_XY(58,40)
plt.legend()
# plt.savefig('Fig1.pdf', format='pdf', dpi=1200, bbox_inches='tight')

fig2 = plt.figure(dpi=1200)
plt.grid(True)
plt.title("Phase Space Graph (Runge Kutta)", fontsize=14)
plt.xlabel("X(t)", fontsize=12)
plt.ylabel("Y(t)", fontsize=12)
plt.plot(0,0, 'bo', label=("Fixed Point 1"))
plt.plot((k_4)/(k_3), (k_1)/(k_2), 'ro', label=("Fixed Point 2"))
#plot_phase(50,50)
#plot_phase(0.1,0.1)
plot_phase(5,5)
plot_phase(15,10)
plot_phase(20,24)
plot_phase(30,35)
plot_phase(55,45)
plt.legend()
#plt.savefig('Fig9.pdf', format='pdf', dpi=1200, bbox_inches='tight')

plt.show()
