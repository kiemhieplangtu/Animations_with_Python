import sys
from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0)







# Define Constants
e           = 1. # 1.6e-19
oofpez      = 9.e9
scalefactor = 1.e3

muzofp      = 1.# 1.e-7 # mu_0/(4*pi)
deltat      = 5.e-20 # second
t           = 0.
Q           = e

# Create a vector as a row
o     = np.array([0., 0., 0.])
c_pos = np.array([-20., 0., 0.])
v_vec = np.array([10., 0., 0.])

o_pos = np.array([0., 10., 0.])
o_vec = o_pos - c_pos
A     = np.linalg.norm(o_vec)
r_hat = o_vec / A

VR    = np.cross(v_vec, r_hat)
B_vec = scalefactor * muzofp * Q * VR / A**2

X, Y, Z = zip(c_pos,o_pos)


## Second location
o_pos1 = np.array([0., 0., 6.])
o_vec1 = o_pos1 - c_pos
A1     = np.linalg.norm(o_vec1)
r_hat1 = o_vec1 / A1

VR1    = np.cross(v_vec, r_hat1)
B_vec1 = scalefactor * muzofp * Q * VR1 / A1**2

X1, Y1, Z1 = zip(c_pos, o_pos1)


## Sphere for the charge
phi        = np.linspace(0, np.pi, 60)
theta      = np.linspace(0, 2*np.pi, 60)
phi, theta = np.meshgrid(phi, theta)
r          = 5.
boxsize    = 30.

# The Cartesian coordinates of the unit sphere
x = r * np.sin(phi) * np.cos(theta) - 20.
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

vx = np.zeros_like(x) + v_vec[0]
vy = np.zeros_like(y) + v_vec[1]
vz = np.zeros_like(z) + v_vec[2]




# Set the aspect ratio to 1 so our sphere looks spherical
fig = plt.figure(figsize=(10,10))
ax  = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z,  rstride=1, cstride=1)
points = ax.plot_surface(x, y, z, color='b')


arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0)
ax.add_artist(Arrow3D(X,Y,Z, **arrow_prop_dict))

arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0)
ax.add_artist(Arrow3D(X1,Y1,Z1, **arrow_prop_dict))

# X, Y, Z = zip(o,r_hat)
# arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color='r', shrinkA=0, shrinkB=0)
# ax.add_artist(Arrow3D(X,Y,Z, **arrow_prop_dict))

# X, Y, Z = zip(o,B_vec)
# arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color='b', shrinkA=0, shrinkB=0)
# ax.add_artist(Arrow3D(X,Y,Z, **arrow_prop_dict))


def update_points(t, x, y, z, points):

    x = x + vx * t
    y = y + vy * t
    z = z + vz * t

    c_pos = np.array([-20. + v_vec[0] * t, 0., 0.])

    o_vec = o_pos - c_pos
    A     = np.linalg.norm(o_vec)
    r_hat = o_vec / A

    VR    = np.cross(v_vec, r_hat)
    B_vec = scalefactor * muzofp * Q * VR / A**2
    X, Y, Z = zip(o_pos, B_vec)


    o_vec1 = o_pos1 - c_pos
    A1     = np.linalg.norm(o_vec1)
    r_hat1 = o_vec1 / A1

    VR1    = np.cross(v_vec, r_hat1)
    B_vec1 = scalefactor * muzofp * Q * VR1 / A1**2
    X1, Y1, Z1 = zip(o_pos1, B_vec1)



    print 't:', t

    ax.clear()

    points = ax.plot_surface(x, y, z, color= 'b')
    ax.add_artist(Arrow3D(X,Y,Z, mutation_scale=20, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0))
    ax.add_artist(Arrow3D(X1,Y1,Z1, mutation_scale=20, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0))


    ax.set_xlim(-boxsize, boxsize)
    ax.set_ylim(-boxsize, boxsize)
    ax.set_zlim(-boxsize, boxsize)

    return points

ani = animation.FuncAnimation(fig, update_points, frames=np.arange(0.0, 5., 0.1), fargs=(x, y, z, points), interval=2, repeat=False)

# ax.grid(False)


ax.set_xlim3d(-boxsize, boxsize)
ax.set_ylim3d(-boxsize, boxsize)
ax.set_zlim3d(-boxsize, boxsize)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()

# while (x < 20.):
# 	pass