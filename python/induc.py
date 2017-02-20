#!/usr/bin/env python3

import numpy as np

# Calculate Inductance of Rectangle
a = 10                      # length
b = 3
#b = np.sqrt(2*5)
#bInner = 2
#bOuter = 5
d = np.sqrt(a**2 + b**2)    # diagonal
s = 4e-6                    # section surface of wire
rho = np.sqrt(s/np.pi)      # radius of wire
mu0 = 4*np.pi*1e-7          # electromagnetic constant

# Terms for Inductance Calculation
A = (a+b)*np.log(2*a*b/rho)
B = a*np.log(a+d)
C = b*np.log(b+d)
D = 7/4 * (a+b)
E = 2*(d+rho)

# Inductance
Lrect = mu0/np.pi * (A - B - C - D + E)

print("Panel Array Rectangle Inductance: ", Lrect*1e6, "muH")


# Calculate Inductance of Two-Wire Setup
dw = 20e-3 # distance between wires
l  = 20    # length of single wire

Lwire = mu0*l/np.pi * (np.log(dw/rho)+1/4)
print("Dual-Wire Inductance: ", Lwire*1e6, "muH")

# Calculate Inductance of PV Panel Wiring
# Middle wires
lPV = 1.5
dPV = 125e-3
LPVmiddle = mu0*lPV/(2*np.pi) * (np.log(dPV/rho) + 1/4-np.log(4/3))
LPVouter  = mu0*lPV/(2*np.pi) * (np.log(dPV/rho) + 1/4-np.log(3/2))
LPV2nd    = mu0*lPV/(2*np.pi) * (np.log(dPV/rho) + 1/4-np.log(8/3))

#print(LPVmiddle)
#print(LPV2nd)
#print(LPVouter)

LPVPanel = (LPVmiddle + LPVouter + LPV2nd)*2*20
print("Total Panel Wiring Inductance: ", LPVPanel*1e6, "muH")

print("Total Inductance of DC Line: ", (Lrect + Lwire + LPVPanel)*1e6, "muH");

# Inductance of Piece of Wire interacting with Signal Coil
lInteract = 10e-3
muCopper = 1.256629e-6
Linteraction = mu0/(2*np.pi)*(np.log(2*lInteract/rho)-1+muCopper/4)
print("Interactive Inductance:", Linteraction, "muH")
