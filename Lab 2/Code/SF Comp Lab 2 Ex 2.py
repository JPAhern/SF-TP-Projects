# -*- coding: utf-8 -*-
# 21363697 - ahernjo@tcd.ie
#Non-Linear Pendulum

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

def f_nl(Theta, Omega, T):
    return (-np.sin(Theta) - k*Omega + A*np.cos(phi*T))

def plot_t(a_t, a_o):
    a_t2 = a_t
    a_o2 = a_o
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle("Plot Theta (%s) and Omega (%s) against Time" % (a_t, a_o), fontsize=14)
    ax1.axis([0, 10, -np.pi, np.pi]) 
    ax1.set_title("Linear")
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
    ax1.plot(T, theta_l, markersize=5, label=("Theta"))
    ax1.plot(T, omega_l, markersize=5, label=("Omega"))
    ax1.grid(True)
    
    
    ax2.axis([0, 10, -np.pi, np.pi]) 
    ax2.set_title("Non-Linear")
    l = 0
    T = []
    theta_l = []
    omega_l = []
    for i in range(0, 1000, 1):
        theta_l.append(a_t2)
        omega_l.append(a_o2)
        T.append(l)
        k1a = dt * a_o2
        k1b = dt * f_nl(a_t2, a_o2, l)
        k2a = dt * (a_o2 + k1b)
        k2b = dt * f_nl(a_t2 + k1a, a_o2 + k1b, l + dt)        
        a_t2 = a_t2 + (k1a + k2a)/2
        a_o2 = a_o2 + (k1b + k2b)/2
        l = l + dt
    ax2.plot(T, theta_l, markersize=5, label=("Theta"))
    ax2.plot(T, omega_l, markersize=5, label=("Omega"))
    ax2.grid(True)



def plot_t2(a_t, a_o):
    a_t2 = a_t
    a_o2 = a_o
    fig, (ax1, ax2) = plt.subplots(1, 2, dpi=1200, sharex=True)
    fig.suptitle("Plot Theta (%s) and Omega (%s) against Time" % (a_t, a_o), fontsize=14)
    ax1.axis([0, 40, -np.pi, np.pi]) 
    fig.text(0.5, 0.04, 't(s)', ha='center')
    fig.text(0.04, 0.5, '(radians)', va='center', rotation='vertical')
    ax1.set_title("Theta")
    ax2.axis([0, 40, -np.pi, np.pi]) 
    ax2.set_title("Omega")
    l = 0
    T = []
    theta_l = []
    omega_l = []
    for i in range(0, 4000, 1):
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
    ax1.plot(T, theta_l, markersize=5, label=("Linear"))
    ax2.plot(T, omega_l, markersize=5, label=("Linear"))
    ax1.grid(True)
    
    
    l = 0
    T = []
    theta_l = []
    omega_l = []
    for i in range(0, 4000, 1):
        theta_l.append(a_t2)
        omega_l.append(a_o2)
        T.append(l)
        k1a = dt * a_o2
        k1b = dt * f_nl(a_t2, a_o2, l)
        k2a = dt * (a_o2 + k1b)
        k2b = dt * f_nl(a_t2 + k1a, a_o2 + k1b, l + dt)        
        a_t2 = a_t2 + (k1a + k2a)/2
        a_o2 = a_o2 + (k1b + k2b)/2
        l = l + dt
    ax1.plot(T, theta_l, markersize=5, label=("Non-Linear"))
    ax2.plot(T, omega_l, markersize=5, label=("Non-Linear"))
    ax2.grid(True)




# for i in range(0, 1000, 1):
#     nsteps.append(i)
#     theta_l.append(theta)
#     omega_l.append(omega)
#     k1a = dt * omega
#     k1b = dt * f_nl(theta, omega, t)
#     k2a = dt * (omega + k1b)
#     k2b = dt * f_nl(theta + k1a, omega + k1b, t + dt)        
#     theta = theta + (k1a + k2a)/2
#     omega = omega + (k1b + k2b)/2
#     t = t + dt
# fig1 = plt.figure(dpi=600)
# plt.axis([0, 1000, -np.pi, np.pi])
# plt.title("Plot Theta and Omega against Steps", fontsize=14)
# plt.xlabel("nsteps", fontsize=12)
# plt.ylabel("Theta", fontsize=12)
# plt.grid(True)
# plt.plot(nsteps, theta_l, markersize=5, label=("Theta"))
# plt.plot(nsteps, omega_l, markersize=5, label=("Omega"))


# plot_t(0.2, 0)
# plt.legend()
# # plot_t(1, 0)
# # plt.legend()
# # plot_t(3.14, 0)
# # plt.legend()
# # plot_t(0, 1)
# # plt.legend()


plot_t2(0.2, 0)
plt.legend()
plot_t2(1, 0)
plt.legend()
plot_t2(3.14, 0)
plt.legend()
plot_t2(0, 1)
plt.legend()
plot_t2(3.1415, 0)
plt.legend()


plt.show()