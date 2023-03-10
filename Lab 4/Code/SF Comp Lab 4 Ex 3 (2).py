# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:55:31 2022

@author: ahernjo

SF Comp Lab 4 - Fourier Analysis
Ex 3
"""

import numpy as np
import matplotlib.pylab as plt

plt.rcParams['figure.dpi'] = 900

N = 32
h = 0.04
m = np.arange(0, N, 1)
t_m = h*m

# w_1 = (2*np.pi)/(N*h)
# n_1 = np.arange(1,N+1,1)
# w_n = w_1 * n_1



def Func(x):
    return np.cos(6*np.pi*x)

def F_nr(f,n):
    return np.sum(f(t_m)*np.cos((2*np.pi*m*n)/N))

def F_ni(f,n):
    return np.sum(f(t_m)*-1*np.sin((2*np.pi*m*n)/N))

# def f_m(f, m):
#     N_x = np.zeros(N)
#     FNR = np.empty(N)
#     FNI = np.empty(N)
#     q = np.arange(0, N, 1)
#     for n in np.arange(1, (N+1), 1):
#         N_x.append(n)
#         FNR.append(F_nr(Func, n))
#         FNI.append(F_ni(Func, n))
#     return (1/N)*np.sum((FNR + 1j*FNI)*(np.cos((2*np.pi*q*m)/N) + 1j*np.sin((2*np.pi*q*m)/N)))
      

R = N  

# fig1 = plt.figure()
# plt.grid(True)
# plt.title("Plot of sampled points")
# x = np.arange(0, R, 0.01)
# plt.plot(x, 0.0*x, 'k')
# plt.plot(t_m, Func(t_m), 'b', markersize=1, label="Function")
# plt.plot(t_m, Func(t_m), 'ro', markersize=4, label="samples")
# plt.legend()

N = 32
h = 0.6
m = np.arange(0, N, 1)
t_m = h*m

fig2 = plt.figure(figsize=(6,6))

plt.suptitle("Plots of Fourier components against n")
plt.subplot(3, 2, 1)
x = np.arange(0, R, 0.01)
plt.plot(x, 0.0*x, 'k')

plt.title("h=0.6")
plt.grid(True)

N_x = []
FNR = []
FNI = []
for n in np.arange(0, R, 1):
    N_x.append(n)
    FNR.append(F_nr(Func, n))
    FNI.append(F_ni(Func, n))
  

F_B = np.zeros(R, dtype=(complex))
T = []
for m in np.arange(0, R, 1):
    T.append(m*h)
    for n in np.arange(0, R, 1):
        F_B[m] += (FNR[n]+ 1j*FNI[n])*(np.cos((2*np.pi*m*n)/N) + 1j*np.sin((2*np.pi*m*n)/N))


F_B = (1/N)*F_B

plt.plot(N_x, FNR, 'ro', markersize = 1, label = "Real")
plt.plot(N_x, FNI, 'bo', markersize = 1, label = "Imaginary")


N = 32
h = 0.2
m = np.arange(0, N, 1)
t_m = h*m

plt.subplot(3, 2, 2)
plt.title("h=0.2")
plt.grid(True)
x = np.arange(0, R, 0.01)
plt.plot(x, 0.0*x, 'k')



N_x = []
FNR = []
FNI = []
for n in np.arange(0, R, 1):
    N_x.append(n)
    FNR.append(F_nr(Func, n))
    FNI.append(F_ni(Func, n))
  

F_B = np.zeros(R, dtype=(complex))
T = []
for m in np.arange(0, R, 1):
    T.append(m*h)
    for n in np.arange(0, R, 1):
        F_B[m] += (FNR[n]+ 1j*FNI[n])*(np.cos((2*np.pi*m*n)/N) + 1j*np.sin((2*np.pi*m*n)/N))


F_B = (1/N)*F_B

plt.plot(N_x, FNR, 'ro', markersize = 1, label = "Real")
plt.plot(N_x, FNI, 'bo', markersize = 1, label = "Imaginary")


N = 32
h = 0.1
m = np.arange(0, N, 1)
t_m = h*m

plt.subplot(3, 2, 3)
plt.title("h=0.1")
plt.grid(True)
x = np.arange(0, R, 0.01)
plt.plot(x, 0.0*x, 'k')


N_x = []
FNR = []
FNI = []
for n in np.arange(0, R, 1):
    N_x.append(n)
    FNR.append(F_nr(Func, n))
    FNI.append(F_ni(Func, n))
  

F_B = np.zeros(R, dtype=(complex))
T = []
for m in np.arange(0, R, 1):
    T.append(m*h)
    for n in np.arange(0, R, 1):
        F_B[m] += (FNR[n]+ 1j*FNI[n])*(np.cos((2*np.pi*m*n)/N) + 1j*np.sin((2*np.pi*m*n)/N))


F_B = (1/N)*F_B

plt.plot(N_x, FNR, 'ro', markersize = 1, label = "Real")
plt.plot(N_x, FNI, 'bo', markersize = 1, label = "Imaginary")


N = 32
h = 0.04
m = np.arange(0, N, 1)
t_m = h*m

plt.subplots_adjust(hspace=.4)

plt.subplot(3, 2, 4)
plt.title("h=0.04")
plt.grid(True)
x = np.arange(0, R, 0.01)
plt.plot(x, 0.0*x, 'k')


N_x = []
FNR = []
FNI = []
for n in np.arange(0, R, 1):
    N_x.append(n)
    FNR.append(F_nr(Func, n))
    FNI.append(F_ni(Func, n))
  

F_B = np.zeros(R, dtype=(complex))
T = []
for m in np.arange(0, R, 1):
    T.append(m*h)
    for n in np.arange(0, R, 1):
        F_B[m] += (FNR[n]+ 1j*FNI[n])*(np.cos((2*np.pi*m*n)/N) + 1j*np.sin((2*np.pi*m*n)/N))


F_B = (1/N)*F_B

plt.plot(N_x, FNR, 'ro', markersize = 1, label = "Real")
plt.plot(N_x, FNI, 'bo', markersize = 1, label = "Imaginary")


N = 32
h = 0.01
m = np.arange(0, N, 1)
t_m = h*m

plt.subplot(3, 2, 5)
plt.title("h=0.01")
plt.grid(True)
x = np.arange(0, R, 0.01)
plt.plot(x, 0.0*x, 'k')


N_x = []
FNR = []
FNI = []
for n in np.arange(0, R, 1):
    N_x.append(n)
    FNR.append(F_nr(Func, n))
    FNI.append(F_ni(Func, n))
  

F_B = np.zeros(R, dtype=(complex))
T = []
for m in np.arange(0, R, 1):
    T.append(m*h)
    for n in np.arange(0, R, 1):
        F_B[m] += (FNR[n]+ 1j*FNI[n])*(np.cos((2*np.pi*m*n)/N) + 1j*np.sin((2*np.pi*m*n)/N))


F_B = (1/N)*F_B

plt.plot(N_x, FNR, 'ro', markersize = 1, label = "Real")
plt.plot(N_x, FNI, 'bo', markersize = 1, label = "Imaginary")


N = 32
h = 1/96
m = np.arange(0, N, 1)
t_m = h*m

plt.subplot(3, 2, 6)
plt.title("h=1/96")
plt.grid(True)
x = np.arange(0, R, 0.01)
plt.plot(x, 0.0*x, 'k')


N_x = []
FNR = []
FNI = []
for n in np.arange(0, R, 1):
    N_x.append(n)
    FNR.append(F_nr(Func, n))
    FNI.append(F_ni(Func, n))
  

F_B = np.zeros(R, dtype=(complex))
T = []
for m in np.arange(0, R, 1):
    T.append(m*h)
    for n in np.arange(0, R, 1):
        F_B[m] += (FNR[n]+ 1j*FNI[n])*(np.cos((2*np.pi*m*n)/N) + 1j*np.sin((2*np.pi*m*n)/N))


F_B = (1/N)*F_B

plt.plot(N_x, FNR, 'ro', markersize = 2, label = "Real")
plt.plot(N_x, FNI, 'bo', markersize = 1, label = "Imaginary")



# N = 32
# h = 1/96
# m = np.arange(0, N, 1)
# t_m = h*m

# fig8 = plt.figure()

# plt.title("Plots of Fourier components")
# x = np.arange(0, R, 0.01)
# plt.plot(x, 0.0*x, 'k')

# plt.grid(True)

# N_x = []
# FNR = []
# FNI = []
# for n in np.arange(0, R, 1):
#     N_x.append(n)
#     FNR.append(F_nr(Func, n))
#     FNI.append(F_ni(Func, n))
  

# F_B = np.zeros(R, dtype=(complex))
# T = []
# for m in np.arange(0, R, 1):
#     T.append(m*h)
#     for n in np.arange(0, R, 1):
#         F_B[m] += (FNR[n]+ 1j*FNI[n])*(np.cos((2*np.pi*m*n)/N) + 1j*np.sin((2*np.pi*m*n)/N))


# F_B = (1/N)*F_B

# plt.plot(N_x, FNR, 'ro', markersize = 1, label = "Real")
# plt.plot(N_x, FNI, 'bo', markersize = 1, label = "Imaginary")




# fig3 = plt.figure()
# plt.grid(True)
# plt.title("Plot of Fourier back transform")
# plt.plot(x, 0.0*x, 'k')


# plt.plot(T, F_B)

# plt.legend()


# N = 128
# h = 0.0347
# m = np.arange(0, N, 1)
# t_m = h*m

# fig4 = plt.figure()
# plt.grid(True)
# plt.title("Plot of Fourier components")
# x = np.arange(0, R, 0.01)
# plt.plot(x, 0.0*x, 'k')


# N_x = []
# FNR = []
# FNI = []
# for n in np.arange(0, R, 1):
#     N_x.append(n*h)
#     FNR.append(F_nr(Func, n))
#     FNI.append(F_ni(Func, n))
  

# F_B = np.zeros(R, dtype=(complex))
# T = []
# for m in np.arange(0, R, 1):
#     T.append(m*h)
#     for n in np.arange(0, R, 1):
#         F_B[m] += (FNR[n]+ 1j*FNI[n])*(np.cos((2*np.pi*m*n)/N) + 1j*np.sin((2*np.pi*m*n)/N))


# F_B = (1/N)*F_B

# plt.plot(N_x, FNR, 'ro', markersize = 1, label = "Real")
# plt.plot(N_x, FNI, 'bo', markersize = 1, label = "Imaginary")
# plt.legend()


# fig5 = plt.figure()
# plt.grid(True)
# plt.title("Plot of Fourier back transform")
# plt.plot(x, 0.0*x, 'k')


# plt.plot(T, F_B)

# plt.legend()


plt.show()
