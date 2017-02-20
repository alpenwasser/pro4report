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
A    = 1.5

x = sp.Symbol('x')
#func1 = 1/2 * (2 + sp.cos(2*w1*x) + sp.cos(2*w2*x) + 2*sp.cos((w1+w2)*x) + 2*sp.cos((w1-w2)*x))
ask_mod_lo    = A1 * sp.sin(w * x)
ask_mod_hi    = A2 * sp.sin(w * x)
ask_mod_hi_2  = A2 * sp.sin(w * x + np.pi/2) # Short-circuit version
ask_mod_lo_ld    = sp.lambdify(x,ask_mod_lo, modules=['numpy'])
ask_mod_hi_ld    = sp.lambdify(x,ask_mod_hi, modules=['numpy'])
ask_mod_hi_ld_2  = sp.lambdify(x,ask_mod_hi_2, modules=['numpy'])

fsk_carrier = A * sp.sin(w * x - sp.pi/2)
fsk_mod_lo  = A * sp.sin((w - deltaW) * x - sp.pi/2)
fsk_mod_hi  = A * sp.sin((w + deltaW) * x - sp.pi/2)
fsk_carrier_ld = sp.lambdify(x,fsk_carrier, modules=['numpy'])
fsk_mod_lo_ld  = sp.lambdify(x,fsk_mod_lo, modules=['numpy'])
fsk_mod_hi_ld  = sp.lambdify(x,fsk_mod_hi, modules=['numpy'])

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
ax1 = fig1.add_subplot(511)
ax1.plot([   0,  4*T], [0,0], color='blue')
ax1.plot([ 4*T,  4*T], [0,1], color='grey')
ax1.plot([ 4*T,  8*T], [1,1], color='magenta')
ax1.plot([ 8*T,  8*T], [1,0], color='grey')
ax1.plot([ 8*T, 12*T], [0,0], color='blue')
ax1.plot([12*T, 12*T], [0,1], color='grey')
ax1.plot([12*T, 16*T], [1,1], color='magenta')
ax1.set_ylim([-0.1,1.1])
ax1.set_xlim([0,16*T])
ax1.set_title("Daten")
ax1.set_ylabel('Symbol')
ax1.set_xlabel('Zeit')
ax1.get_xaxis().set_ticks([]);
ax1.get_yaxis().set_ticks([0,1]);

# Modulated Signal, FSK
ax2 = fig1.add_subplot(512)
ax2.plot(t_lo_1, fsk_mod_lo_ld(t_lo_1), label=r"Tr\"agerfrequenz", color='blue')
ax2.plot(t_hi_1, fsk_mod_hi_ld(t_hi_1), label=r"Tr\"agerfrequenz", color='magenta')
ax2.plot(t_lo_2, fsk_mod_lo_ld(t_lo_2), label=r"Tr\"agerfrequenz", color='blue')
ax2.plot(t_hi_2, fsk_mod_hi_ld(t_hi_2), label=r"Tr\"agerfrequenz", color='magenta')
ax2.set_ylim([-1.1 * A, 1.1 * A])
ax2.set_xlim([0,16*T])
ax2.set_title(r"Moduliertes Signal, FSK")
ax2.set_ylabel('Spannung')
ax2.set_xlabel('Zeit')
ax2.get_xaxis().set_ticks([]);
ax2.get_yaxis().set_ticks([]);

# Modulated Signal, ASK
ax3 = fig1.add_subplot(513)
ax3.plot(t_lo_1, ask_mod_lo_ld(t_lo_1), label=r"Tr\"agerfrequenz", color='blue')
ax3.plot(t_hi_1, ask_mod_hi_ld(t_hi_1), label=r"Tr\"agerfrequenz", color='magenta')
ax3.plot(t_lo_2, ask_mod_lo_ld(t_lo_2), label=r"Tr\"agerfrequenz", color='blue')
ax3.plot(t_hi_2, ask_mod_hi_ld(t_hi_2), label=r"Tr\"agerfrequenz", color='magenta')
ax3.set_ylim([-1.1 * A2, 1.1 * A2])
ax3.set_xlim([0,16*T])
ax3.set_title(r"Moduliertes Signal, ASK")
ax3.set_ylabel('Spannung')
ax3.set_xlabel('Zeit')
ax3.get_xaxis().set_ticks([]);
ax3.get_yaxis().set_ticks([]);


# Modulated Signal, OOK, Oscillator
ax4 = fig1.add_subplot(514)
ax4.plot([0, 4*T], [0,0] , color='blue')
ax4.plot(t_hi_1, ask_mod_hi_ld(t_hi_1), label=r"Tr\"agerfrequenz", color='magenta')
ax4.plot([8*T, 12*T], [0,0], color='blue')
ax4.plot(t_hi_2, ask_mod_hi_ld(t_hi_2), label=r"Tr\"agerfrequenz", color='magenta')
ax4.set_ylim([-1.1 * A2, 1.1 * A2])
ax4.set_xlim([0,16*T])
ax4.set_title(r"Moduliertes Signal, OOK, Oszillator")
ax4.set_ylabel('Spannung')
ax4.set_xlabel('Zeit')
ax4.get_xaxis().set_ticks([]);
ax4.get_yaxis().set_ticks([]);

# Modulated Signal, Short-Circuit
ax5 = fig1.add_subplot(515)
ax5.plot([   0,  4*T], [960,960], color='blue')
ax5.step([ 4*T + T/2 * 0,  4*T + T/2    ], [960,900], color='magenta')
ax5.step([ 4*T + T/2 * 1,  4*T + T/2 * 2], [900,960], color='magenta')
ax5.step([ 4*T + T/2 * 2,  4*T + T/2 * 3], [960,900], color='magenta')
ax5.step([ 4*T + T/2 * 3,  4*T + T/2 * 4], [900,960], color='magenta')
ax5.step([ 4*T + T/2 * 4,  4*T + T/2 * 5], [960,900], color='magenta')
ax5.step([ 4*T + T/2 * 5,  4*T + T/2 * 6], [900,960], color='magenta')
ax5.step([ 4*T + T/2 * 6,  4*T + T/2 * 7], [960,900], color='magenta')
ax5.step([ 4*T + T/2 * 7,  4*T + T/2 * 8], [900,960], color='magenta')
ax5.plot([ 8*T, 12*T], [960,960], color='blue')
ax5.step([12*T + T/2 * 0, 12*T + T/2    ], [960,900], color='magenta')
ax5.step([12*T + T/2 * 1, 12*T + T/2 * 2], [900,960], color='magenta')
ax5.step([12*T + T/2 * 2, 12*T + T/2 * 3], [960,900], color='magenta')
ax5.step([12*T + T/2 * 3, 12*T + T/2 * 4], [900,960], color='magenta')
ax5.step([12*T + T/2 * 4, 12*T + T/2 * 5], [960,900], color='magenta')
ax5.step([12*T + T/2 * 5, 12*T + T/2 * 6], [900,960], color='magenta')
ax5.step([12*T + T/2 * 6, 12*T + T/2 * 7], [960,900], color='magenta')
ax5.step([12*T + T/2 * 7, 12*T + T/2 * 8], [900,960], color='magenta')
ax5.set_ylim([890,970])
ax5.set_xlim([0,16*T])
ax5.set_title(r"Moduliertes Signal, OOK, Kurzschluss \"uber Modul")
ax5.set_ylabel('Spannung')
ax5.set_xlabel('Zeit')
ax5.get_xaxis().set_ticks([]);
ax5.get_yaxis().set_ticks([]);


fig1.subplots_adjust(bottom=0.05,top=0.95,left=0.10,right=0.95,hspace=0.45)
#fig1.set_figwidth(5.314) # Textwidth
fig1.set_figwidth(5.1)
# fig1.set_figheight(6.5)
fig1.set_figheight(8)
#fig1.subplots_adjust(bottom=0.01,top=0.99,left=0.05,right=0.99)
fig1.savefig('../images/python/modulation.pgf')

#plt.show()
