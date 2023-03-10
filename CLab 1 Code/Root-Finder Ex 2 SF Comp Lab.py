# -*- coding: utf-8 -*-
# 21363697 - ahernjo@tcd.ie

import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as ptc

a = 3
b = 7
c = -9

x_1 = 2.3
tol = 0.000000001

def f(x):
    return a * x ** 2 + b * x + c

def d_f(x):
    return 2*a*x+b

x_1_True_Pos = (-b+(b**2-4*a*c)**(1/2))/(2*a)
x_1_True_Neg = (-b-(b**2-4*a*c)**(1/2))/(2*a)


fig1 = plt.figure(dpi=1200)
plt.title("Plot of f(x) against x", fontsize=14)
x = np.arange(-5.0, 3.0, 0.2)
plt.plot(x, f(x), 'b')
plt.plot(x, d_f(x), 'y')
plt.plot(x, 0.0*x, 'k')
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.grid(True)


Root1_Fit = ptc.Patch(color='red', label='Root 1 Fit')
Root2_Fit = ptc.Patch(color='green', label='Root 2 Fit')
Parabola = ptc.Patch(color='blue', label='Parabola')
Derivative = ptc.Patch(color='y', label='Derivative')
plt.legend(handles=[Parabola, Derivative, Root1_Fit, Root2_Fit])


steps_R1 = steps_R2 = 0
x_1_R1 = x_1
x_1_R2 = -x_1
print("Finding Root 1")
while abs(f(x_1_R1)) > tol:
    x_1_R1 -= f(x_1_R1)/d_f(x_1_R1)
    steps_R1 += 1
plt.plot(x_1_R1, f(x_1_R1), 'ro')
print("x_2 = %s, f(x_2) = %s, |f(x_2)| = %s" % (x_1_R1, f(x_1_R1), abs(f(x_1_R1))))

print("\nFinding Root 2")
while abs(f(x_1_R2)) > tol:
    x_1_R2 -= f(x_1_R2)/d_f(x_1_R2)
    steps_R2 += 1
plt.plot(x_1_R2, f(x_1_R2), 'go')
print("x_2 = %s, f(x_2) = %s, |f(x_2)| = %s" % (x_1_R2, f(x_1_R2), abs(f(x_1_R2))))
   
print("""\nRoot 1 = %s  Found in %s iterations.
Root 2 = %s  Found in %s iterations.""" % (x_1_R1, steps_R1, x_1_R2, steps_R2))
print("\nError in Root 1 = %s \nError in Root 2 = %s" % (x_1_True_Pos-x_1_R1, x_1_True_Neg-x_1_R2))


fig2 = plt.figure(dpi=1200)
plt.xscale('log')
plt.title("Plot of nsteps against the log of Tolerance", fontsize=14)
plt.ylabel("nsteps", fontsize=12)
plt.xlabel("Tolerance", fontsize=12)
plt.grid(True)

steps_n = 0    
nsteps = []
tol_n = []
for i in range(1, 10000000, 1):
    tol = 1/i
    while abs(f(x_1)) > tol:
        x_1 -= f(x_1)/d_f(x_1)
        steps_n += 1
    nsteps.append(steps_n)
    tol_n.append(i)
plt.plot(tol_n, nsteps, markersize=5)



plt.show()
