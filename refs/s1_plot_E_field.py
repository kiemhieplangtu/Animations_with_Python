import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

TWOPI = 2.*np.pi
c     = 1.
v     = 0.2
dmax  = 50.

fig, ax = plt.subplots(figsize=(10,10))

# plt.plot([-1., 1.], [0., 0.], 'k:')

plt.axis([-dmax, dmax, -dmax, dmax])

dot,  = plt.plot([0], [0.], 'ro')
line, = plt.plot([0., 0.], [0., 0.], 'b-')

xangle = [0., np.pi/4., np.pi/2., 3.*np.pi/4., np.pi, 5.*np.pi/4., 3.*np.pi/2., 7.*np.pi/4., 2.*np.pi]
nlines = len(xangle)
xangle = np.array(xangle)




def run(t):
	if(t < dmax):
		d  = c * t
		xi = d * np.cos(xangle)
		yi = d * np.sin(xangle)

		x  = np.zeros( (nlines,2) )
		y  = np.zeros( (nlines,2) )

		for i in range(nlines):
			x[i,:] = [0., xi[i]]
			y[i,:] = [0., yi[i]]

	
		line.set_data(x, y)

	else:
		xc = v * (t-tmax)
		yc = 0.
		dot.set_data(xc, yc)

	return line, dot,

# create animation using the run() function
tmax = dmax
ani = ani.FuncAnimation(fig, run, frames=np.arange(0., 2.*tmax, 0.5), interval=50, blit=True, repeat=False)



# def animate(i):
# 	x = dmax*np.cos(i)
# 	y = dmax*np.sin(i)
# 	dot.set_data(x, y)
# 	return dot,

# # create animation using the animate() function
# myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI, 0.1), \
#                                       interval=50, blit=True, repeat=True)


plt.show()