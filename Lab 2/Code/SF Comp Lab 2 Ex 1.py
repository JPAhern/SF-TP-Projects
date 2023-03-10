# -*- coding: utf-8 -*-
# 21363697 - ahernjo@tcd.ie
#Linear Pendulum 

import numpy as np
import matplotlib.pylab as plt

k = 0.0
phi = 0.66667
A = 0.0

theta = 1
omega = 0.0
t = 0.0
dt = 0.01
nsteps = []
theta_l = []
omega_l = []

def f(Theta, Omega, T):
    return (-Theta - k*Omega + A*np.cos(phi*T))

def plot_t(a_t, a_o):
    plt.figure(dpi=1200)
    plt.axis([0, 10, -np.pi, np.pi])
    plt.title("Plot Theta (%s) and Omega (%s) against Time" % (a_t, a_o), fontsize=14)
    l = 0
    T = []
    theta_l = []
    omega_l = []
    for i in range(0, 1000, 1):
        theta_l.append(a_t)
        omega_l.append(a_o)
        T.append(l)
        k1a = dt * a_o
        k1b = dt * f(a_t, a_o, l)
        k2a = dt * (a_o + k1b)
        k2b = dt * f(a_t + k1a, a_o + k1b, l + dt)        
        a_t = a_t + (k1a + k2a)/2
        a_o = a_o + (k1b + k2b)/2
        l = l + dt
    plt.xlabel("t (s)", fontsize=12)
    plt.ylabel("Theta", fontsize=12)
    plt.grid(True)
    plt.plot(T, theta_l, markersize=5, label=("Theta"))
    plt.plot(T, omega_l, markersize=5, label=("Omega"))


for i in range(0, 1000, 1):
    nsteps.append(i)
    theta_l.append(theta)
    omega_l.append(omega)
    k1a = dt * omega
    k1b = dt * f(theta, omega, t)
    k2a = dt * (omega + k1b)
    k2b = dt * f(theta + k1a, omega + k1b, t + dt)        
    theta = theta + (k1a + k2a)/2
    omega = omega + (k1b + k2b)/2
    t = t + dt
fig1 = plt.figure(dpi=1200)
plt.axis([0, 1000, -np.pi, np.pi])
plt.title("Plot Theta and Omega against Steps", fontsize=14)
plt.xlabel("nsteps", fontsize=12)
plt.ylabel("Theta", fontsize=12)
plt.grid(True)
plt.plot(nsteps, theta_l, markersize=5, label=("Theta"))
plt.plot(nsteps, omega_l, markersize=5, label=("Omega"))

plt.legend()
plot_t(0.2, 0)
plt.legend()
plot_t(1, 0)
plt.legend()
plot_t(3.14, 0)
plt.legend()
plot_t(0, 1)

plt.legend()
plt.show()