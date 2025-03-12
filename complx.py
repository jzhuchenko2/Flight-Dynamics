import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import control as ctrl

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
plt.figure()
plt.semilogx(w, phase)
plt.show()

#controlllllll
A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]]) #for specific dh/du

system = ctrl.ss(A, B, C, D) #c state-space system

t, y = ctrl.step_response(system) # sim response to a step input
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Step Response')
plt.show()


############################
# Root locus plot
ctrl.root_locus(system)
plt.show()
ctrl.nyquist(system)
plt.show()

# pid controller
Kp = 1.0
Ki = 0.1
Kd = 0.01

pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

plant = ctrl.TransferFunction([1], [1, 2, 1])
