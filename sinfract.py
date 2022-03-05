import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.io.wavfile import write

def sinfract(x, a, f, n, k=4):
    if n == 0:
        return 0
    return a*np.sin(2*np.pi*f*x) + sinfract(x, a/k, f*k, n-1, k=k)

def sinfractl(x, a, f, n, k=4):
    y = np.zeros(len(x))
    for i in range(0, int(n)):
        y += a*np.sin(2*np.pi*f*x)
        f = f*k
        a = a/k
    return y
            
seconds = 5
x = np.linspace(0, seconds, 44100*seconds)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

freq = float(sys.argv[1])
n = float(sys.argv[2])
k = float(sys.argv[3])
amp = float(sys.argv[4])

data = sinfractl(x, amp, freq, n, k)

# plot the function
plt.plot(x, data, 'b-')

# show the plot
plt.show()

print('writing sound file...')

scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('output.wav', 44100, scaled)
