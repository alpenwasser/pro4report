#!/usr/bin/env python3

# coding: utf-8

# In[25]:

import numpy as np
import matplotlib.pyplot as plt
#get_ipython().magic('matplotlib inline')

def open_csv_pia(csv, start, stop, scale_f, scale_L):
    f = []
    L = []
    with open(csv, 'r') as csvfile:
        i = 0
        for line in csvfile:
            i+=1
            if i > (start - 1) and i < (stop + 1):
                split = line.split('\t')
                f.append(float(split[0]) * scale_f)
                L.append(float(split[1]) * scale_L)
    return (f, L)

def open_csv_pc(csv, start, stop, scale_x, scale_y):
    x = []
    y = []
    with open(csv, 'r') as csvfile:
        i = 0
        for line in csvfile:
            i+=1
            if i > (start - 1) and i < (stop + 1):
                split = line.split(';')
                x.append(float(split[0]) * scale_x)
                y.append(float(split[1]) * scale_y)
    return (x, y)


plt.rc('text',usetex=True)
plt.rc('font',family='serif',size=11)
plt.rc('legend',fontsize=9)
plt.rc('axes',labelsize=9,titlesize=11)
plt.rc('xtick',labelsize=9)
plt.rc('ytick',labelsize=9)
plt.rc('savefig',transparent=True)
plt.rc('lines',linewidth=0.5)
plt.rc('axes',linewidth=0.5)
plt.rc('patch',linewidth=0.5) # For legend box line


factor_mega = 1000 * 1000

f_1, L_1 = open_csv_pia('1LAYER.TXT', 22, 222, 1, factor_mega)
f_1_stray, L_1_stray = open_csv_pia('1LSTRAY.TXT', 22, 222, 1, factor_mega)
f_multi, L_multi = open_csv_pia('MULTILAY.TXT', 22, 222, 1, factor_mega)

plt.figure(num=1, figsize=(5.5, 2), facecolor='w', edgecolor='k')
plt.subplots_adjust(bottom=0.2,top=0.90,left=0.10,right=0.95)
plt.plot(f_1, L_1)
plt.plot(f_1_stray, L_1_stray)
plt.plot(f_multi, L_multi)
plt.title(r'Frequenzgang Induktivit\"at')
plt.xlabel('f [Hz]')
plt.xscale('log')
plt.xlim([1e4, 1e8])
plt.ylabel('$L_s(f) [\mu H]$')
plt.ylim([-250, 250])
plt.legend([r'$L_{\mathrm{1 Layer}}(f)$', r'$L_{\mathrm{stray, 1 Layer}}(f)$', r'$L_{\mathrm{multi-Layer}}(f)$'], loc='lower left')
plt.savefig('../../images/fsk-meas/frequency_sweep_Ls.pgf')


factor_mili = 1e-3

f_1, L_1 = open_csv_pia('1LAYER.TXT', 229, 429, 1, factor_mili)
f_1_stray, L_1_stray = open_csv_pia('1LSTRAY.TXT', 229, 429, 1, factor_mili)
f_multi, L_multi = open_csv_pia('MULTILAY.TXT', 229, 429, 1, factor_mili)

plt.figure(num=2, figsize=(5.5,2),  facecolor='w', edgecolor='k')
plt.subplots_adjust(bottom=0.2,top=0.90,left=0.10,right=0.95)
plt.plot(f_1, L_1)
plt.plot(f_1_stray, L_1_stray)
plt.plot(f_multi, L_multi)
plt.title(r'Frequenzgang $R_{\mathrm{series}}$')
plt.xlabel('f [Hz]')
plt.xscale('log')
plt.xlim([1e4, 1e8])
plt.ylabel('$R_s(f) [k\Omega]$')
#plt.ylim([-250, 250])
plt.legend(['$R_{\mathrm{1 Layer}}(f)$', '$R_{\mathrm{stray, 1 Layer}}(f)$', r'$R_{\mathrm{multi-Layer}}(f)$'], loc='upper left')
plt.savefig('../../images/fsk-meas/frequency_sweep_Rs.pgf')
#plt.show()


# In[28]:

factor_mili = 1e-3

I_inc, L1_inc = open_csv_pc('1_layer_power_choke_test.csv', 29, 115, 1, 1)
I_sec, L1_sec = open_csv_pc('1_layer_power_choke_test.csv', 230, 318, 1, 1)

plt.figure(num=3, figsize=(5.5, 2), dpi=80, facecolor='w', edgecolor='k')
plt.subplots_adjust(bottom=0.2,top=0.90,left=0.10,right=0.95)
plt.plot(I_inc, L1_inc)
plt.plot(I_sec, L1_sec)
plt.title('Power choke test')
plt.xlabel('I [A]')
#plt.xlim([1e4, 1e8])
plt.ylabel('$L(I) [\mu H]$')
#plt.ylim([-250, 250])
plt.legend(['L_inc(I)', 'L_sec(I)'], loc='lower left')
plt.savefig('../../images/fsk-meas/power_choke_I.pgf')
#plt.show()


# In[29]:

SUdt_inc, L2_inc = open_csv_pc('1_layer_power_choke_test.csv', 130, 179, 1, 1)
SUdt_sec, L2_sec = open_csv_pc('1_layer_power_choke_test.csv', 331, 382, 1, 1)

plt.figure(num=4, figsize=(5.5, 2), dpi=80, facecolor='w', edgecolor='k')
plt.subplots_adjust(bottom=0.30,top=0.90,left=0.15,right=0.95)
plt.plot(SUdt_inc, L2_inc)
plt.plot(SUdt_sec, L2_sec)
plt.title('Power choke test')
plt.xlabel('$\int Udt [Vs]$')
#plt.xlim([1e4, 1e8])
plt.ylabel('$L(\int Udt) [\mu H]$')
#plt.ylim([-250, 250])
plt.legend(['$L_{inc}(\int Udt)$', '$L_{sec}(\int Udt)$'], loc='lower left')
plt.savefig('../../images/fsk-meas/power_choke_SUdt.pgf')
#plt.show()


# In[30]:

from math import pi

f = np.logspace(3, 12, 1000)
C = 1e6
omega = 2 * pi * f
Z = [abs(1/(o*C)) for o in omega]

#plt.figure(num=5, figsize=(5.5, 2), dpi=80, facecolor='w', edgecolor='k')
#plt.subplots_adjust(bottom=0.1,top=0.90,left=0.10,right=0.95)
#plt.plot(f, Z)
#plt.title('Impedance of a cap')
#plt.xlabel('$f [Hz]$')
##plt.xlim([1e4, 1e8])
#plt.ylabel('$Z(f) [\Omega]$')
##plt.ylim([-250, 250])
#plt.legend(['$Z(f) [\Omega]$'], loc='upper left')
#plt.savefig('cap.pgf')
##plt.show()
#print('This sucks!')


# In[83]:

#from scipy.constants import mu_0
#import numpy as np
#import numpy as np
#import matplotlib.pyplot as plt
##get_ipython().magic('matplotlib inline')
#
#x = 20
#L = L1_sec[x] * 1e-6
#print('L is %f' % L)
#I = I_sec[x]
#print('I is %f' % I)
#N = 30
#print('N is %f' % N)
#V_m = N * I
#print('$V_m$ is %f' % V_m)
#A = 4e-3 * 12e-3
#print('A is %f' % A)
#r = 6e-3
#print('r is %f' % r)
#l_c = 2 * r * pi
#print('$l_c$ is %f' % l_c)
#l_g = 0.5e-3
#print('$l_g$ is %f' % l_g)
## R_c = l_c / (mu_0 * u_r * A) # u_r = ?
#R_g = l_g / (mu_0 * A * 1.35)# u_r = 1 (A0 * 13.5 == 0.5mm + on each side)
#
#print('$R_g$ is %f' % R_g)
## V_m / Psi = R_m = R_c + R_g
## Psi = L * I
## V_m / (L * I) - R_g = R_c
#u_r = l_c / ((V_m / ((L * I) / N) - R_g) * mu_0 * A)
#print('$u_r$ is %f' % u_r)
#
#x = np.linspace(1.2, 1.3, num=1000)
#R_g = l_g / (mu_0 * A * x) # u_r = 1
#u_r = l_c / ((V_m / ((L * I) / N) - R_g) * mu_0 * A)
#
#plt.figure(num=1, figsize=(5.5, 2), dpi=80, facecolor='w', edgecolor='k')
#plt.subplots_adjust(bottom=0.1,top=0.90,left=0.10,right=0.95)
#plt.plot(x, u_r)
#plt.title('$\mu_r$')
#plt.xlabel('$A / A_0 = p$')
##plt.xlim([1e4, 1e8])
#plt.ylabel('$\mu_r$')
##plt.ylim([-250, 250])
#plt.legend(['$\mu_r$'], loc='upper left')
#plt.savefig('mu_r.pgf')
##plt.show()
#
#x = np.linspace(1.3, 1.6, num=1000)
#R_g = l_g / (mu_0 * A * x) # u_r = 1
#u_r = l_c / ((V_m / ((L * I) / N) - R_g) * mu_0 * A)
#
#plt.figure(num=1, figsize=(5.5, 2), dpi=80, facecolor='w', edgecolor='k')
#plt.subplots_adjust(bottom=0.1,top=0.90,left=0.10,right=0.95)
#plt.plot(x, u_r)
#plt.title('$\mu_r$')
#plt.xlabel('$A / A_0 = p$')
##plt.xlim([1e4, 1e8])
#plt.ylabel('$\mu_r$')
##plt.ylim([-250, 250])
#plt.legend(['$\mu_r$'], loc='upper left')
#plt.savefig('mu_r.pgf')
##plt.show()
