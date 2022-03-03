import numpy as np
import matplotlib.pyplot as plt

def sinfract(x, f, n, k=4):
    if n == 0:
        return 0
    return np.sin(2*np.pi*f*x) + (1/k)*sinfract(x, f*k, n-1, k)
            
x = np.linspace(-np.pi, np.pi, 10000)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

freq = 1/6
n = 30

# plot the function
#plt.plot(x,sinfract(x, freq, 1), 'b-')
plt.plot(x,sinfract(x, freq, n, 4), 'b-')

# show the plot
plt.show()

