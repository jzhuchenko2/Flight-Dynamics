import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

z1 = complex(2, 3)  # 2 + 3j
z2 = 4 + 5j


z_sum = z1 + z2
z_diff = z1 - z2
z_prod = z1 * z2
z_quot = z1 / z2

print(f"Sum: {z_sum}, Difference: {z_diff}, Product: {z_prod}, Quotient: {z_quot}")

conjugate_a = a.conjugate()

num = [1, 1]
den = [1, 2, 2]
system = signal.TransferFunction(num, den)

#plot
w, mag, phase = signal.bode(system)
plt.figure()
plt.semilogx(w, mag)  # Bode magnitude plot
