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
A    = 1.5

x = sp.Symbol('x')
#func1 = 1/2 * (2 + sp.cos(2*w1*x) + sp.cos(2*w2*x) + 2*sp.cos((w1+w2)*x) + 2*sp.cos((w1-w2)*x))
fsk_carrier = A * sp.sin(w * x - sp.pi/2)
fsk_mod_lo  = A * sp.sin((w - deltaW) * x - sp.pi/2)
fsk_mod_hi  = A * sp.sin((w + deltaW) * x - sp.pi/2)
fsk_carrier_ld = sp.lambdify(x,fsk_carrier, modules=['numpy'])
fsk_mod_lo_ld  = sp.lambdify(x,fsk_mod_lo, modules=['numpy'])
fsk_mod_hi_ld  = sp.lambdify(x,fsk_mod_hi, modules=['numpy'])
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
plt.rc('lines', linewidth=0.5)
plt.rc('axes',linewidth=0.5)

fig1 = plt.figure(num=1,figsize=(10,15))
#fig1.suptitle(r'Frequenzanteile bei Intensit\"at einer Schwebung')

# Data
ax1 = fig1.add_subplot(211)
ax1.plot([   0,  4*T], [0,0], color='blue')
ax1.plot([ 4*T,  4*T], [0,1], color='grey')
ax1.plot([ 4*T,  8*T], [1,1], color='magenta')
ax1.plot([ 8*T,  8*T], [1,0], color='grey')
ax1.plot([ 8*T, 12*T], [0,0], color='blue')
ax1.plot([12*T, 12*T], [0,1], color='grey')
ax1.plot([12*T, 16*T], [1,1], color='magenta')
ax1.set_ylim([-0.1,1.1])
ax1.set_title("Daten")
ax1.set_ylabel('Symbol')
ax1.set_xlabel('Zeit (s)')

# Carrier Frequency
# ax2 = fig1.add_subplot(312)
# ax2.plot(t, fsk_carrier_ld(t), label=r"Tr\"agerfrequenz", color="green")
# ax2.set_ylim([-1.1 * A, 1.1 * A])
# ax2.set_title(r"Tr\"agerfrequenz")

# Modulated Signal
ax3 = fig1.add_subplot(212)
ax3.plot(t_lo_1, fsk_mod_lo_ld(t_lo_1), label=r"Tr\"agerfrequenz", color='blue')
ax3.plot(t_hi_1, fsk_mod_hi_ld(t_hi_1), label=r"Tr\"agerfrequenz", color='magenta')
ax3.plot(t_lo_2, fsk_mod_lo_ld(t_lo_2), label=r"Tr\"agerfrequenz", color='blue')
ax3.plot(t_hi_2, fsk_mod_hi_ld(t_hi_2), label=r"Tr\"agerfrequenz", color='magenta')
ax3.set_ylim([-1.1 * A, 1.1 * A])
ax3.set_title(r"Moduliertes Signal")
ax3.set_ylabel('Spannung (V)')
ax3.set_xlabel('Zeit (s)')

# Modulated Signal + DC component
#ax4 = fig1.add_subplot(414)
#ax4.plot(t_lo_1, fsk_mod_lo_ld(t_lo_1) + 960, label=r"Tr\"agerfrequenz", color='blue')
#ax4.plot(t_hi_1, fsk_mod_hi_ld(t_hi_1) + 960, label=r"Tr\"agerfrequenz", color='magenta')
#ax4.plot(t_lo_2, fsk_mod_lo_ld(t_lo_2) + 960, label=r"Tr\"agerfrequenz", color='blue')
#ax4.plot(t_hi_2, fsk_mod_hi_ld(t_hi_2) + 960, label=r"Tr\"agerfrequenz", color='magenta')
#ax4.plot([0,16*T],[0,0],color='white')
#ax4.set_title(r"Moduliertes Signal auf Leitung mit DC-Anteil")

fig1.subplots_adjust(bottom=0.15,top=0.95,left=0.15,right=0.95,hspace=0.65)
#fig1.set_figwidth(5.314) # Textwidth
fig1.set_figwidth(4.5)
# fig1.set_figheight(6.5)
fig1.set_figheight(3.5)
#fig1.subplots_adjust(bottom=0.01,top=0.99,left=0.05,right=0.99)
fig1.savefig('../images/python/fsk.pgf')

#plt.show()
