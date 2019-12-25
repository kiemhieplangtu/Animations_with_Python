import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

TWOPI = 2*np.pi

fig, ax = plt.subplots()

plt.plot([0., 0.], [-1., 1.], 'k:')

ax = plt.axis([-1., 1., -1, 1])

dot, = plt.plot([0], [np.sin(0)], 'ro')

radius = 1.
def animate(i):
	x = radius*np.cos(i)
	y = radius*np.sin(i)
	dot.set_data(x, y)
	return dot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI, 0.1), \
                                      interval=50, blit=True, repeat=True)

plt.show()