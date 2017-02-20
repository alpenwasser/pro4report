#!/usr/bin/env python3

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# Approx 10 kHz
w = 66e3
deltaW = 33e3

T    = 2 * np.pi / w
T_lo = 2 * np.pi / (w - deltaW)
T_hi = 2 * np.pi / (w + deltaW)
A1    =  5
A2    = 30

x = sp.Symbol('x')
fsk_mod_lo    = A1 * sp.sin(w * x)
fsk_mod_hi    = A2 * sp.sin(w * x)
fsk_mod_hi_2  = A2 * sp.sin(w * x + np.pi/2) # Short-circuit version
fsk_mod_lo_ld    = sp.lambdify(x,fsk_mod_lo, modules=['numpy'])
fsk_mod_hi_ld    = sp.lambdify(x,fsk_mod_hi, modules=['numpy'])
fsk_mod_hi_ld_2  = sp.lambdify(x,fsk_mod_hi_2, modules=['numpy'])
#evalfunc1 = sp.lambdify(x,func1,modules=['numpy'])

# From 0 to 10 milliseconds
t = np.linspace(0,16*T,1000)
t_lo_1 = np.linspace(              0,          4*T, 1000)
t_hi_1 = np.linspace(         4*T, 4*T + 4*T, 1000)
t_lo_2 = np.linspace(4*T + 4*T, 8*T + 4*T, 1000)
t_hi_2 = np.linspace(8*T + 4*T, 8*T + 8*T, 1000)

plt.rc('text',usetex=True)
plt.rc('font',family='serif',size=11)
plt.rc('legend', fontsize=9)
plt.rc('axes', labelsize=9, titlesize=11)
plt.rc('xtick', labelsize=9)
plt.rc('ytick', labelsize=9)
plt.rc('savefig', transparent=True)
plt.rc('lines', linewidth=8)
plt.rc('axes',linewidth=0)


fig1 = plt.figure(num=1,figsize=(10,15))
ax1 = fig1.add_subplot(111)
max = 4.0
# Draw successively narrower lines of differing
# colors onto broader lines.
for i in range(1,int(max)):
    color = (1/max + i/max)
    lineWidth = int(2*(max-i))
    plt.rc('lines', linewidth=lineWidth)
    ln1, = ax1.plot(t_lo_1, fsk_mod_lo_ld(t_lo_1), color=[color,0,0])
    ln1.set_solid_capstyle('round')
    ln2, = ax1.plot(t_hi_1, fsk_mod_hi_ld(t_hi_1), color=[color,0,0])
    ln2.set_solid_capstyle('round')
    ln3, = ax1.plot(t_lo_2, fsk_mod_lo_ld(t_lo_2), color=[color,0,0])
    ln3.set_solid_capstyle('round')

ax1.set_ylim([-1.1 * A2, 1.1 * A2])
ax1.set_xlim([-T,13*T])
fig1.subplots_adjust(bottom=0.05,top=0.95,left=0.10,right=0.90)
fig1.set_figwidth(8.2677)
fig1.set_figheight(2)
ax1.get_xaxis().set_ticks([])
ax1.get_yaxis().set_ticks([])
fig1.savefig('../images/python/title.pgf')

#plt.show()
