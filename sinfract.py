import numpy as np
import matplotlib.pyplot as plt
import sys

def sinfract(x, a, f, n, k=4):
    if n == 0:
        return 0
    return a*np.sin(2*np.pi*f*x) + sinfract(x, a/k, f*k, n-1, k=k)
            
x = np.linspace(0, 10, 10000)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

period = float(sys.argv[1])
n = float(sys.argv[2])
k = float(sys.argv[3])

# plot the function
plt.plot(x,sinfract(x, 1, 1/period, n, k), 'b-')

# show the plot
plt.show()

