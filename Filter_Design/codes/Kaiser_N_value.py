import math
import numpy as np
delta = 0.15
del_omega = 0.05*np.pi
A = -20*math.log10(delta)
N = (A-8)/(4.57*del_omega)
print(f"Value of A is {A}")
print(f"Smallest value of N is {N}")
