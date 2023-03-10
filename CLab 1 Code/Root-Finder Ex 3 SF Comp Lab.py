# -*- coding: utf-8 -*-
# 21363697 - ahernjo@tcd.ie

import numpy as np
import matplotlib.pylab as plt

ke = 1.44 #eV nm
A = 1090 #eV
p = 0.033 #nm

tol = 0.000000001

def V(x):
    return ((A*(np.exp(-x/p))) - (ke*(1/x)))

def d_V(x):
    return (((-A/p)*(np.exp(-x/p))) + (ke*(1/x**2)))

def d2_V(x):
    return (((A/(p**2))*(np.exp(-x/p))) - (ke*(2/x**3)))

fig1 = plt.figure(dpi=1200)
x = np.arange(0.2, 1, 0.00001)
plt.plot(x, V(x), 'b', label="V(x)")
plt.plot(x, -d_V(x), 'y', label="V'(x)")
plt.title("Plot of Ionic Potential over Distance")
plt.plot(x, 0.0*x, 'k')
plt.ylabel("Potential Energy (eV)")
plt.xlabel("x (nm)")
plt.grid(True)

x_1 = 0.1

while abs(d_V(x_1)) > tol:
    x_1 -= d_V(x_1)/d2_V(x_1)

print(x_1)
print(V(x_1))
plt.plot(x_1, V(x_1), 'ro', label="Minimum", markersize='5')

plt.legend()  
plt.show()
