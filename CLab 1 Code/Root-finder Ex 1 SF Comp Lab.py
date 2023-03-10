# -*- coding: utf-8 -*-
# 21363697 - ahernjo@tcd.ie

import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as ptc

a = 3
b = 7
c = -9

x_1 = -3.1 #s.t f(x_1) < 0
x_3 = 7.6 #s.t f(x_3) > 0
x_2 = 0.5 * (x_1 + x_3)
tol = 0.000000001  #The acceptable tollerance for the root-finder
x_1_True_Pos = (-b+(b**2-4*a*c)**(1/2))/(2*a)
x_1_True_Neg = (-b-(b**2-4*a*c)**(1/2))/(2*a)

def f(x):
    return a * x ** 2 + b * x + c

def find_root(X1,X2,X3,t,col,plots,pri): #X1,X2,X3, tollerance, dot colour, plot(1,0), print(1,0)
    global steps, root
    steps = 0
    while abs(f(X2)) > t:
        #print("x_1 = %s, x_2 = %s, x_3 = %s" % (X1, X2, X3))        
        if f(X2) > 0:
            X3 = X2
        elif f(X2) < 0:
            X1 = X2            
        X2 = 0.5 * (X1 + X3)
        steps += 1
        root = X2
    if plots == 1:
        plt.plot(X2, f(X2), col, markersize=8)  
    if pri == 1:
        print("x_2 = %s, f(x_2) = %s, |f(x_2)| = %s" % (X2, f(X2), abs(f(X2))))


fig1 = plt.figure(dpi=1200) 
plt.title("Plot of f(x) against x", fontsize=14)
x = np.arange(-5.0, 3.0, 0.2)
plt.plot(x, f(x), 'b')
plt.plot(x, 0.0*x, 'k')
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.grid(True)

Root1_Fit = ptc.Patch(color='red', label='Root 1 Fit')
Root2_Fit = ptc.Patch(color='green', label='Root 2 Fit')
Parabola = ptc.Patch(color='blue', label='Parabola')
plt.legend(handles=[Parabola, Root1_Fit, Root2_Fit])
   

if f(x_1)>0 or f(x_3)<0: #Checks that variables are correctly defined
    print("Warning Initial Variables Incorrectly Defined")
else:
    print("Finding Root 1")
    find_root(x_1, x_2, x_3, tol, 'ro', 1, 1)
    nsteps_R1 = steps
    Root_1 = root    
    print("\nFinding Root 2")
    find_root(-x_1, -x_2, -x_3, tol, 'go', 1, 1)
    nsteps_R2 = steps
    Root_2 = root
    print("""\nRoot 1 = %s  Found in %s iterations.
Root 2 = %s  Found in %s iterations.""" % (Root_1, nsteps_R1, Root_2, nsteps_R2))
    print("\nError in Root 1 = %s \nError in Root 2 = %s" % (x_1_True_Pos-Root_1, x_1_True_Neg-Root_2))
    
    fig2 = plt.figure(dpi=1200)
    plt.xscale('log')
    plt.title("Plot of nsteps against the log of Tolerance", fontsize=14)
    plt.ylabel("nsteps", fontsize=12)
    plt.xlabel("Tolerance", fontsize=12)
    plt.grid(True)
    
    nsteps = []
    tol_n = []
    for i in range(1000, 10000000, 210):
        tol = 1/i
        find_root(x_1, x_2, x_3, tol, 'ro', 0, 0)
        nsteps.append(steps)
        tol_n.append(i)
    plt.plot(tol_n, nsteps, markersize=5)
    

print("\nx_1_True_Pos =", x_1_True_Pos)
print("x_1_True_Neg =", x_1_True_Neg)


plt.show()
