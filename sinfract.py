import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.io.wavfile import write
from scipy.special import iv

def bessel(x, n, f, fm, beta):
    y = np.zeros(len(x))
    for i in range(1, int(n)):
        #y += iv(i, beta)*np.cos(np.pi*((f+i*(fm/(i**(i-1))))**i)*x) 
        y += iv(i, beta)*np.cos(np.pi*((f+i*fm)**i)*x) 
    return y

def sinfract(x, n, a, f, s):
    y = np.zeros(len(x))
    for i in range(0, int(n)):
        y += a*np.cos(2*np.pi*f*x)
        a = a/s
        f = f*s
    return y

def weierstrass(x, n, a, b, f=1):
    y = np.zeros(len(x))
    for i in range(0, int(n)):
        y += (a**i)*np.cos(f*(b**i)*np.pi*x)
    return y

