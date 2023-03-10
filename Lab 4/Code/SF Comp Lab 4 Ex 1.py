# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:07:35 2022

@author: ahernjo

SF Comp Lab 4 - Fourier Analysis
Ex 1
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as ptc

plt.rcParams['figure.dpi'] = 1200

#(1)-(3)

a = 0
b = 2*np.pi
n = 200

w = 1

def Func(t):
    return np.sin(t) + 2*np.cos(3*t) + 3*np.sin(5*t)

def Simpson(f):
    h = float(b-a)/n
    eve = np.array([a + 2*h*j for j in np.arange(1,n//2)])
    odd = np.array([a + h*(2*j-1) for j in np.arange(1,n//2+1)])
    return (h/3)*(f(a)+2*np.sum(f(eve))+4*np.sum(f(odd))+f(b))

#print(Simpson(Func)) #Good

# (4)

def a_0(f):
    return (1/b)*(Simpson(f))

def a_k(f, k):
    p = lambda x : f(x)*np.cos(w * k * x)
    return (2/b)*(Simpson(p))

def b_k(f, k):
    q = lambda x : f(x)*np.sin(w * k * x)
    return (2/b)*(Simpson(q))


def FourierS(f, k, x):
    I = a_0(f)
    for i in range(1, k, 1):
        I += (a_k(f, i)*np.cos(w*i*x))
        I += (b_k(f, i)*np.sin(w*i*x))
    return I



print(a_k(Func,3))


print(b_k(Func,1))

print(b_k(Func,5))


Range = 3*np.pi

# fig1 = plt.figure(dpi=1200)
# plt.title("Plot of Analytical Function")
# plt.grid(True)
# x = np.arange(0, Range, 0.005)
# plt.plot(x, 0.0*x, 'k')
# plt.plot(x, Func(x), 'b')


# fig2 = plt.figure(dpi=1200)
# plt.title("Plot of sin($\omega$t)+2cos(3$\omega$t)+3sin(5$\omega$t) against t")
# plt.xlabel("t (s)", fontsize = 10)
# plt.ylabel("sin($\omega$t)+2cos(3$\omega$t)+3sin(5$\omega$t)", fontsize = 10)
# plt.grid(True)
# x = np.arange(0, Range, 0.005)
# plt.plot(x, 0.0*x, 'k')
# plt.plot(x, Func(x), 'b')

# X = []
# Y = []
# for i in np.arange(0, Range, 0.03):
#     X.append(i)
#     Y.append(FourierS(Func, 20, i))

# plt.plot(X, Y, 'ro', markersize = 2)


# Coefficients = ptc.Patch(color='red', label='Fourier')
# Func_curve = ptc.Patch(color='blue', label='Function')
# plt.legend(handles=[Func_curve, Coefficients])


plt.show()

