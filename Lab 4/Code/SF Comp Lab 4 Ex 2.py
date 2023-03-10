# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:12:08 2022

@author: ahernjo

SF Comp Lab 4 - Fourier Analysis
Ex 2 (Part 1)
"""

import numpy as np
import matplotlib.pylab as plt
from scipy.signal import square

plt.rcParams['figure.dpi'] = 1200

a = 0
b = 2*np.pi
n = 500

w = 1

def Func(x):
    return square(x)

def Simpson(f):
    h = float(b-a)/n
    eve = np.array([a + 2*h*j for j in np.arange(1,n//2)])
    odd = np.array([a + h*(2*j-1) for j in np.arange(1,n//2+1)])
    return (h/3)*(f(a)+2*np.sum(f(eve))+4*np.sum(f(odd))+f(b))



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

Range = 4*np.pi

fig1 = plt.figure()
plt.title("Plot of Analytical Function")
plt.grid(True)
x = np.arange(0, Range, 0.005)
plt.plot(x, 0.0*x, 'k')
plt.plot(x, Func(x), 'b')


# fig2 = plt.figure()
# plt.title("Plot of Fourier Approximation")
# plt.grid(True)
# x = np.arange(0, Range, 0.005)
# plt.plot(x, 0.0*x, 'k')

# X = []
# Y = []
# for i in np.arange(0, Range, 0.01):
#     X.append(i)
#     Y.append(FourierS(Func, 30, i))

# plt.plot(X, Y, 'r')


# print(a_0(Func))
# print(a_k(Func, 1))
# print(a_k(Func,5))
# print(b_k(Func, 1))
# print(b_k(Func, 3))
# print(b_k(Func,2))

n = 100

fig3 = plt.figure()
plt.title("Plot of Analytical Function")
x = np.arange(0, Range, 0.005)
plt.plot(x, 0.0*x, 'k')

plt.subplot(2, 3, 1)
X = []
Y = []
for i in np.arange(0, Range, 0.01):
    X.append(i)
    Y.append(FourierS(Func, 2, i))
plt.plot(X, Y, 'r')

plt.subplot(2, 3, 2)
X = []
Y = []
for i in np.arange(0, Range, 0.01):
    X.append(i)
    Y.append(FourierS(Func, 3, i))
plt.plot(X, Y, 'r')

plt.subplot(2, 3, 3)
X = []
Y = []
for i in np.arange(0, Range, 0.01):
    X.append(i)
    Y.append(FourierS(Func, 5, i))
plt.plot(X, Y, 'r')

plt.subplot(2, 3, 4)
X = []
Y = []
for i in np.arange(0, Range, 0.01):
    X.append(i)
    Y.append(FourierS(Func, 10, i))
plt.plot(X, Y, 'r')

plt.subplot(2, 3, 5)
X = []
Y = []
for i in np.arange(0, Range, 0.01):
    X.append(i)
    Y.append(FourierS(Func, 20, i))
plt.plot(X, Y, 'r')

plt.subplot(2, 3, 6)
X = []
Y = []
for i in np.arange(0, Range, 0.01):
    X.append(i)
    Y.append(FourierS(Func, 30, i))
plt.plot(X, Y, 'r')



plt.show()

