import numpy as np
from scipy.signal import convolve
import matplotlib.pyplot as plt

def f(t):
return np.exp(-t) * (t >= 0)
