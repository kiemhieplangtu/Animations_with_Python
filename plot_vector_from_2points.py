import matplotlib.pyplot as plt
import numpy as np
import math, sys
from mpl_toolkits.mplot3d import Axes3D

if(False):
	a = [2.0, 4.0]
	b = [8.0, 8.0]

	head_length = 0.7

	dx = b[0] - a[0]
	dy = b[1] - a[1]

	vec_ab = [dx,dy]

	vec_ab_magnitude = math.sqrt(dx**2+dy**2)

	dx = dx / vec_ab_magnitude
	dy = dy / vec_ab_magnitude

	vec_ab_magnitude = vec_ab_magnitude - head_length

	ax = plt.axes()

	ax.arrow(a[0], a[1], vec_ab_magnitude*dx, vec_ab_magnitude*dy, head_width=0.5, head_length=head_length, fc='lightblue', ec='black')

	plt.scatter(a[0],a[1],color='black')
	plt.scatter(b[0],b[1],color='black')

	ax.annotate('A', (a[0]-0.4,a[1]),fontsize=14)
	ax.annotate('B', (b[0]+0.3,b[1]),fontsize=14)

	plt.grid()

	plt.xlim(0,10)
	plt.ylim(0,10)

	plt.title('How to plot a vector in matplotlib ?',fontsize=10)

	# plt.savefig('how_to_plot_a_vector_in_matplotlib_fig2.png', bbox_inches='tight')
	plt.show()
	plt.close()

	sys.exit()


if(True):
	a = np.array([-20., 0., 0.])
	b = np.array([0., 0., 0.])
	x = b - a
	L = np.linalg.norm(x)

	A = np.array( np.append(a, b, axis=None) )

	X, Y, Z, U, V, W = zip(A)
	print X, Y, Z, U, V, W 


	# Set the aspect ratio to 1 so our sphere looks spherical
	fig = plt.figure(figsize=(10,10))
	ax  = fig.add_subplot(111, projection='3d')

	# ax.plot_surface(x, y, z,  rstride=1, cstride=1)
	# points = ax.plot_surface(x, y, z, color='b')

	ax.quiver(X, Y, Z, U, V, W)


	# def update_points(t, x, y, z, points):
	#     # txt.set_text('num={:d}'.format(t))

	#     x = x + vx * t
	#     y = y + vy * t
	#     z = z + vz * t
	#     print('t:', t)

	#     ax.clear()
	#     points = ax.plot_surface(x, y, z,color= 'b')
	#     ax.set_xlim(-boxsize, boxsize)
	#     ax.set_ylim(-boxsize, boxsize)
	#     ax.set_zlim(-boxsize, boxsize)

	#     return points

	# ani = animation.FuncAnimation(fig, update_points, frames=np.arange(0.0, 15., 0.1), fargs=(x, y, z, points), interval=50, repeat=False)

	# ax.grid(False)


	boxsize = 30.
	ax.set_xlim3d(-boxsize, boxsize)
	ax.set_ylim3d(-boxsize, boxsize)
	ax.set_zlim3d(-boxsize, boxsize)

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')


	plt.show()

	sys.exit()




a = [0., 0.]
b = [2., -2.]

A = np.array( np.append(a, b, axis=None) )

X, Y, U, V = zip(A)

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V, units='xy', scale=1)

plt.grid()

ax.set_aspect('equal')

plt.xlim(-5,5)
plt.ylim(-5,5)

plt.title('How to plot a vector in matplotlib ?',fontsize=10)

# plt.savefig('how_to_plot_a_vector_in_matplotlib_fig3.png', bbox_inches='tight')
plt.show()
plt.close()