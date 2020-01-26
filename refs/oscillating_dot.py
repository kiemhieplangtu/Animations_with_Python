import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

TWOPI = 2*np.pi

fig, ax = plt.subplots()

plt.plot([0., 0.], [-1., 1.], 'k:')

ax = plt.axis([-0.5, 0.5, -1, 1])

dot, = plt.plot([0], [np.sin(0)], 'ro')

def animate(i):
    dot.set_data(0., np.cos(i))
    return dot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI, 0.1), \
                                      interval=50, blit=True, repeat=True)

plt.show()