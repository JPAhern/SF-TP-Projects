# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:03:49 2022

@author: ahernjo
Comp Lab 3
"""

import numpy as np
import matplotlib.pylab as plt


B = 1.6*10**-4 # N s m^-2
C = 0.25 # N s^2 m^-4

def f(DxV):
    return B*DxV + C*(DxV**2)

def f_lin(DxV):
    return B*DxV

def f_quad(DxV):
    return C*(DxV**2)

R = 4*10**-4
S = 1*10**-6

# fig1 = plt.figure(dpi=1200)
# plt.title("Plot of f_lin(x) against DxV", fontsize=14)
# x = np.arange(0, R, S)
# plt.plot(x, f_lin(x), 'b')
# plt.plot(x, 0.0*x, 'k')
# plt.xlabel("DxV", fontsize=12)
# plt.ylabel("f_lin(DxV)", fontsize=12)
# plt.grid(True)

# fig2 = plt.figure(dpi=1200)
# plt.title("Plot of f(x) against DxV", fontsize=14)
# x = np.arange(0, R, S)


# plt.plot(x, f_lin(x), label = "Linear")
# plt.plot(x, f_quad(x), label = "Quadratic")
# plt.plot(x, f(x), label = "Both")
# plt.plot(x, 0.0*x, 'k')
# plt.xlabel("DxV", fontsize=12)
# plt.ylabel("f(x)", fontsize=12)
# plt.grid(True)

# plt.legend(loc = 'upper left')

# fig3 = plt.figure(dpi=1200)
# plt.title("Plot of f_quad(x) against DxV", fontsize=14)
# x = np.arange(0, R, S)
# plt.plot(x, f(x), 'b')
# plt.plot(x, 0.0*x, 'k')
# plt.xlabel("DxV", fontsize=12)
# plt.ylabel("f(DxV)", fontsize=12)
# plt.grid(True)

#Linear dominates until DxV > ~10^-5


#Baseball DxV = 0.35 Quadratic
#Oil Drop DxV = 7.5 x10^-11 Linear
#Rain Drop DxV = 1x10^-3 Both 

R = 1*10**-2

fig, ax1 = plt.subplots(dpi = 1200)
ax2 = ax1.twinx()
plt.title("Plot of bV and c$V^2$ against DxV", fontsize=14)
x = np.arange(0, R, S)
ax1.plot(x, 0.0*x, 'k')

ax1.plot(x, f_lin(x), label = "Linear")
ax1.plot(x, f_quad(x), 'r', label = "Quadratic")


ax1.set_xlabel("DxV ($m^2s^{-1}$)", fontsize=12)
ax1.set_ylabel("bV (N) and c$V^2$ (N)")
ax2.set_ylabel("bV + c$V^2$ (N)")
ax2.plot(x, f(x), 'y', label = "Both")

ax1.grid()
fig.legend(loc = 'upper left', bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.show()
