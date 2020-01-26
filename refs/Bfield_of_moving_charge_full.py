import sys
from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d




# Define Constants
e           = 1. # 1.6e-19
oofpez      = 9.e9
scalefactor = 1.e2

muzofp      = 1.# 1.e-7 # mu_0/(4*pi)
deltat      = 5.e-20 # second
t           = 0.
Q           = e



xx    = np.linspace(-30,30,10)
yy    = np.linspace(-30,30,10)
zz    = np.linspace(-30,30,10)
X,Y,Z = np.meshgrid(xx,yy,zz)

c_pos = np.array([-20., 0., 0.])
v_vec = np.array([10., 0., 0.])

XX = X - c_pos[0]
YY = Y - c_pos[1]
ZZ = Z - c_pos[2]
L  = np.sqrt( XX**2 + YY**2 + ZZ**2)

## R_hat
XX_hat = XX/L
YY_hat = YY/L
ZZ_hat = ZZ/L

## cross product [V x R_hat]
XVR = v_vec[1]*ZZ_hat - v_vec[2]*YY_hat
YVR = v_vec[2]*XX_hat - v_vec[0]*ZZ_hat
ZVR = v_vec[0]*YY_hat - v_vec[1]*XX_hat

B_XX = scalefactor * muzofp * Q * XVR / L**2
B_YY = scalefactor * muzofp * Q * YVR / L**2
B_ZZ = scalefactor * muzofp * Q * ZVR / L**2


## Sphere for the charge
phi        = np.linspace(0, np.pi, 60)
theta      = np.linspace(0, 2*np.pi, 60)
phi, theta = np.meshgrid(phi, theta)
r          = 2.
boxsize    = 30.

# The Cartesian coordinates of the unit sphere
x = r * np.sin(phi) * np.cos(theta) - 20.
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)


vx    = np.zeros_like(x) + v_vec[0]
vy    = np.zeros_like(y) + v_vec[1]
vz    = np.zeros_like(z) + v_vec[2]

# ex,ey,ez = E(XX,YY,ZZ)


# Set the aspect ratio to 1 so our sphere looks spherical
fig = plt.figure(figsize=(10,10))
ax  = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z,  rstride=1, cstride=1)
points = ax.plot_surface(x, y, z, color='r')

ax.quiver(X,Y,Z,B_XX,B_YY,B_ZZ,color='b',length=1,normalize=False)


def update_points(t, x, y, z, points):

    x = x + vx * t
    y = y + vy * t
    z = z + vz * t

    c_pos = np.array([-20. + v_vec[0] * t, 0., 0.])

    XX = X - c_pos[0]
    YY = Y - c_pos[1]
    ZZ = Z - c_pos[2]
    L  = np.sqrt( XX**2 + YY**2 + ZZ**2)

    ## R_hat
    XX_hat = XX/L
    YY_hat = YY/L
    ZZ_hat = ZZ/L

    ## cross product [V x R_hat]
    XVR = v_vec[1]*ZZ_hat - v_vec[2]*YY_hat
    YVR = v_vec[2]*XX_hat - v_vec[0]*ZZ_hat
    ZVR = v_vec[0]*YY_hat - v_vec[1]*XX_hat

    B_XX = scalefactor * muzofp * Q * XVR / L**2
    B_YY = scalefactor * muzofp * Q * YVR / L**2
    B_ZZ = scalefactor * muzofp * Q * ZVR / L**2    


    print 't:', t

    ax.clear()

    points = ax.plot_surface(x, y, z, color= 'b')
    ax.quiver(X,Y,Z,B_XX,B_YY,B_ZZ,color='b',length=1,normalize=False)


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