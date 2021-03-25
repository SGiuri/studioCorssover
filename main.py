from math import pi, sqrt, atan, cos

v_picco = 50  # volt
L1 = 15e-3  # 15 x 10 alla -3 - (mH)
R1 = 1.3  # Ohm

C1 = 10e-6  # Farad

L2 = 0.32e-3  # H
R2 = 8  # Ohm

frequenze = range(1,100000,1) # Hz
potenze_apparenti = []
potenze = []
# ZC1 e' in parallelo con ZL2R2 e entrambe sono
# in serie a ZL1R1
for frequenza in frequenze:

    omega = 2 * pi * frequenza

    Z_R1L1 = R1 + omega * L1 * 1j

    Z_R2L2 = R2 + omega * L2 * 1j
    Z_C1 = -1j / (omega * C1)

    Z_C1_R2L2 = (Z_R2L2 * Z_C1) / (Z_R2L2 + Z_C1)

    Zeq = Z_R1L1 + Z_C1_R2L2

    I = v_picco / Zeq

    I_picco = sqrt(I.real ** 2 + I.imag ** 2)
    I_phase = atan(I.imag / I.real)
    I_phase_deg = I_phase * 360 / (2 * pi)

    Pa = (v_picco / sqrt(2)) * (I_picco / sqrt(2))
    P = Pa * cos(I_phase)
    potenze_apparenti.append(Pa)
    potenze.append(P)

#print("Potenze apparenti [VA] = ", potenze_apparenti)

#print("Potenze [W] = ",potenze)

#print("Z_R1L1 = ", Z_R1L1, " Ohm")
#print("Z_R2L2 = ", Z_R2L2, " Ohm")
#print("Z_C1 = ", Z_C1, " Ohm")
#print("Z_C1_R2L2 = ", Z_C1_R2L2, " Ohm")
#print("Zeq = ", Zeq, " Ohm")
#print("I = ", I, " A")
#print("I_picco = ", I_picco, " A")
#print("I_phase = ", I_phase, " rad")
#print("I_phase_deg = ", I_phase_deg, " deg")
#print("Pa = ", Pa, " VA")
#print("P = ", P, " W")

#import numpy as np
import matplotlib.pyplot as plt

x = frequenze
y = potenze
ya = potenze_apparenti

fig, ax = plt.subplots()

line1, = ax.plot(x, y, label='potenze [W]')
line2, = ax.plot(x, ya, label='potenze app [VA]')
plt.semilogx()
plt.xlabel("frequenza [Hz]",fontsize=12)
plt.ylabel("potenze",fontsize=12)
plt.title("Analisi potenze Crossover",fontsize=16)
ax.legend()
plt.show()
plt.savefig("AnalisiPotenze.png")