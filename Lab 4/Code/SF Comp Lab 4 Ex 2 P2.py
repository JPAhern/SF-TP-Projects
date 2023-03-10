# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:53:17 2022

@author: ahernjo

SF Comp Lab 4 - Fourier Analysis
Ex 2 (Part 2)
"""

import numpy as np
import matplotlib.pylab as plt
from scipy.signal import square

plt.rcParams['figure.dpi'] = 600


a = 0
b = 2*(np.pi)
n = 200

w = 1

def Func(x):
    if x <= 0.5:
        return 1
    elif 2.5<= x <= 3.5:
        return 1
    elif 5.5<= x <= 6.5:
        return 1
    else:
        return -1
    
    
    # return square(x)

def Simpson(f):
    I1 = I2 = []
    h = float(b-a)/n
    eve = np.array([a + 2*h*j for j in np.arange(1,n//2)])
    odd = np.array([a + h*(2*j-1) for j in np.arange(1,n//2+1)])
    for i in eve:
        I1.append(f(i))
    for i in odd:
        I2.append(f(i))
    return (h/3)*(f(a)+2*np.sum(I1)+4*np.sum(I2)+f(b))



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
    return I*(1/2)

Range = 2*np.pi

# fig1 = plt.figure()
# F = []
# plt.title("Plot of Rectangular Function")
# plt.grid(True)
# x = np.arange(0, Range, 0.005)
# for i in x:
#     F.append(Func(i))
# plt.plot(x, 0.0*x, 'k')
# plt.plot(x, F, 'b')


fig2 = plt.figure()
plt.title("Plot of Fourier Series of Rectangular Wave")
plt.grid(True)
x = np.arange(0, Range, 0.01)
plt.plot(x, 0.0*x, 'k')
F = []
for i in x:
    F.append(Func(i))
plt.plot(x, F, 'b', label = "True Wave")

X = []
Y = []
for i in np.arange(0, Range, 0.005):
    X.append(i)
    Y.append(FourierS(Func, 100, i))

plt.plot(X, Y, 'r', label = "Fourier Wave")
plt.legend()

print(a_0(Func))
print(a_k(Func, 1))
print(a_k(Func,5))
print(b_k(Func, 1))
print(b_k(Func, 3))
print(b_k(Func,2))

# Range = 2*np.pi
# n = 100

# fig3 = plt.figure()
# plt.suptitle("Plots of Rectangular Wave Fourier Series for K")
# x = np.arange(0, Range, 0.005)
# plt.plot(x, 0.0*x, 'k')

# plt.subplot(2, 3, 1)
# #plt.plot(x, Func(x), 'b')
# X = []
# Y = []
# for i in np.arange(0, Range, 0.01):
#     X.append(i)
#     Y.append(FourierS(Func, 2, i))
# plt.title("k = 2")
# plt.plot(X, Y, 'r')
# plt.plot(x, 0.0*x, 'k')

# plt.subplot(2, 3, 2)
# #plt.plot(x, Func(x), 'b')
# X = []
# Y = []
# for i in np.arange(0, Range, 0.01):
#     X.append(i)
#     Y.append(FourierS(Func, 3, i))
# plt.title("k = 3")
# plt.plot(X, Y, 'r')
# plt.plot(x, 0.0*x, 'k')

# plt.subplot(2, 3, 3)
# #plt.plot(x, Func(x), 'b')
# X = []
# Y = []
# for i in np.arange(0, Range, 0.01):
#     X.append(i)
#     Y.append(FourierS(Func, 5, i))
# plt.title("k = 5")
# plt.plot(X, Y, 'r')
# plt.plot(x, 0.0*x, 'k')

# plt.subplots_adjust(hspace=.4)

# plt.subplot(2, 3, 4)
# #plt.plot(x, Func(x), 'b')
# X = []
# Y = []
# for i in np.arange(0, Range, 0.01):
#     X.append(i)
#     Y.append(FourierS(Func, 10, i))
# plt.title("k = 10")
# plt.plot(X, Y, 'r')
# plt.plot(x, 0.0*x, 'k')

# plt.subplot(2, 3, 5)
# #plt.plot(x, Func(x), 'b')
# X = []
# Y = []
# for i in np.arange(0, Range, 0.01):
#     X.append(i)
#     Y.append(FourierS(Func, 20, i))
# plt.title("k = 20")
# plt.plot(X, Y, 'r')
# plt.plot(x, 0.0*x, 'k')

# plt.subplot(2, 3, 6)
# #plt.plot(x, Func(x), 'b')
# X = []
# Y = []
# for i in np.arange(0, Range, 0.01):
#     X.append(i)
#     Y.append(FourierS(Func, 30, i))
# plt.title("k = 30")
# plt.plot(X, Y, 'r')
# plt.plot(x, 0.0*x, 'k')



plt.show()

