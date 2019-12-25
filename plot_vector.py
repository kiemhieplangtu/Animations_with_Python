import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if(False):
	p0 = [0.799319, -3.477045e-01, 0.490093]
	p1 = [0.852512, 9.113778e-16, -0.522708]
	p2 = [0.296422, 9.376042e-01, 0.181748]

	origin = [0,0,0]
	X, Y, Z = zip(origin,origin,origin) 
	U, V, W = zip(p0,p1,p2)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.quiver(X,Y,Z,U,V,W,arrow_length_ratio=0.2)

	boxsize    = 1.
	ax.set_xlim(-boxsize, boxsize)
	ax.set_ylim(-boxsize, boxsize)
	ax.set_zlim(-boxsize, boxsize)

	plt.show()


if(False):
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.set_xlim3d(-30, 30.)
	ax.set_ylim3d(-30, 30.)
	ax.set_zlim3d(-30, 30.)

	a = np.array([-20., 0., 0.])
	b = np.array([20., 0., 0.])

	x = b - a
	L = np.linalg.norm(x)

	ax.quiver(0, 0, 0, 1, 1, 1, length = L, normalize = True)

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	plt.show()



# vectors=np.array( [ [0,0,1,1,-2,0], [0,0,2,1,1,0],[0,0,3,2,1,0],[0,0,4,0.5,0.7,0]]) 
vectors=np.array( [ [-10, 0, 0, 0, 0, 6], ]) 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for vector in vectors:
    v = np.array([vector[3],vector[4],vector[5]])
    vlength=np.linalg.norm(v)
    ax.quiver(vector[0],vector[1],vector[2],vector[3],vector[4],vector[5],
            pivot='tail',length=vlength,arrow_length_ratio=0.3/vlength)

boxsize = 30.
ax.set_xlim3d(-boxsize, boxsize)
ax.set_ylim3d(-boxsize, boxsize)
ax.set_zlim3d(-boxsize, boxsize)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()