#!/usr/bin/env python3

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


n  = 1.6
n2 = 2
IS = 1.6e-6
IS_3 = 1.6e-5
k  = 1.38e-23
T  = 300
q  = 1.609e-19

U = sp.Symbol('U')
#func1 = 1/2 * (2 + sp.cos(2*w1*x) + sp.cos(2*w2*x) + 2*sp.cos((w1+w2)*x) + 2*sp.cos((w1-w2)*x))
vi_pos   = IS * (sp.exp(U/(n*k*T/q)) - 1) + 4
vi_pos_2 = IS * (sp.exp(U/(n2*k*T/q)) - 1) + 4
vi_pos_3 = IS_3 * (sp.exp(U/(n*k*T/q)) - 1) + 4
vi_rev   = IS * (-sp.exp((-U)/(n*k*T/q)) + 1) - 5
vi_rev_2   = IS * (-sp.exp((-U)/(n2*k*T/q)) + 1) - 5
#vi_rev_3   = IS_3 * (-sp.exp((-U)/(n2*k*T/q)) + 1) - 5
vi_pos_lambd  = sp.lambdify(U,vi_pos,modules=['numpy'])
vi_pos_lambd2 = sp.lambdify(U,vi_pos_2,modules=['numpy'])
vi_pos_lambd3 = sp.lambdify(U,vi_pos_3,modules=['numpy'])
vi_rev_lambd  = sp.lambdify(U,vi_rev,modules=['numpy'])
vi_rev_lambd2  = sp.lambdify(U,vi_rev_2,modules=['numpy'])
#vi_rev_lambd3  = sp.lambdify(U,vi_rev_3,modules=['numpy'])

# From 0 to 10 milliseconds
lower        = -0.9
upper        =  0.9
u_pos        = np.linspace(0,upper,300)
u_pos_actual = np.linspace(0.3,upper,300)
u_rev        = np.linspace(lower,0,300)
u_rev_actual = np.linspace(lower,-0.4,300)
u            = np.linspace(-0.4,0.4,300)
u_rev_fill   = np.linspace(-0.2,0.005,500)
u_rev_fill_2 = np.linspace(-0.57,-0.1998,500)

plt.rc('text',usetex=True)
plt.rc('font',family='serif',size=11)
plt.rc('legend', fontsize=9)
plt.rc('axes', labelsize=9, titlesize=11)
plt.rc('xtick', labelsize=9)
plt.rc('ytick', labelsize=9)
plt.rc('savefig', transparent=True)
plt.rc('lines', linewidth=0.5)
plt.rc('axes',linewidth=0.5)

fig1 = plt.figure(num=1)

# Figure
ax1 = fig1.add_subplot(111)
ax1.plot(u_pos_actual, vi_pos_lambd2(u_pos_actual), color="red")
ax1.plot(u_pos_actual, vi_pos_lambd(u_pos_actual), color="blue")
ax1.plot(u_pos_actual, vi_pos_lambd3(u_pos_actual), color="green")
#ax1.plot(u_rev_actual, vi_rev_lambd2(u_rev_actual), color="red")
ax1.plot(u_rev_actual, vi_rev_lambd(u_rev_actual), color="blue")
#ax1.plot(u_rev_actual, vi_rev_lambd3(u_rev_actual), color="green")
ax1.plot(u, 4.525*np.tanh(15*u)-0.5, label=r"Strom", color="blue")

# Axes
ax1.plot([lower,upper],[0,0],color="black")
ax1.plot([0.005,0.005],[-20,20],color="black")
#ax1.arrow(x,y,dx,dy,...)
ax1.arrow(0.7,0,0.1,0, fc="k", ec="k",head_width=2,head_length=0.05,linewidth=0.5)
ax1.arrow(0.005,15,0,2, fc="k", ec="k",head_width=0.05,head_length=2,linewidth=0.5)

# Fill for IS
ax1.fill_between(u_rev_fill,4.525 * np.tanh(15*u_rev_fill)-0.5, 0, color="magenta", alpha="0.5",lw=0)
ax1.fill_between(u_rev_fill_2, vi_rev_lambd(u_rev_fill_2), 0, color="magenta", alpha="0.5",lw=0)

# Tuning
ax1.text(-0.3,1,r"$I_S$",fontsize=9)
ax1.set_title("IV-Kurve einer Diode")
ax1.set_ylim([-20,20])
ax1.set_xlim([lower,upper])
ax1.set_xlabel('Spannung (V)')
ax1.set_ylabel('Strom (A)')
ax1.get_xaxis().set_ticks([])
ax1.get_yaxis().set_ticks([])

fig1.subplots_adjust(bottom=0.1,top=0.90,left=0.1,right=0.9)
fig1.set_figwidth(4.5)
fig1.set_figheight(4)
fig1.savefig('../images/python/diodeVI.pgf')
#fig1.savefig('diodeVI.pgf')

#plt.show()
