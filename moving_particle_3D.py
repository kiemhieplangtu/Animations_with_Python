import sys
from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation


fig = plt.figure()
ax  = p3.Axes3D(fig)

q   = [[0.], [0.], [0.]]
v   = [[1.],[ 0.0], [0.0]]

x   = np.array(q[0])
y   = np.array(q[1])
z   = np.array(q[2])
vx  = np.array(v[0])
vy  = np.array(v[1])
vz  = np.array(v[2])

points, = ax.plot(x, y, z, 'ko')
# txt = fig.suptitle('')

def update_points(t, x, y, z, points):
    # txt.set_text('num={:d}'.format(t))

    new_x = x + vx * t
    new_y = y + vy * t
    new_z = z + vz * t
    print('t:', t)

    # update properties
    points.set_data(new_x,new_y)
    points.set_3d_properties(new_z, 'z')

    # return modified artists
    # return points,txt
    return points

ani = animation.FuncAnimation(fig, update_points, frames=np.arange(0.0, 15., 0.1), fargs=(x, y, z, points), interval=50, repeat=False)

ax.set_xlabel('x [pc]')
ax.set_ylabel('y [pc]')
ax.set_zlabel('z [pc]')


boxsize = 50.
ax.set_xlim(-boxsize, boxsize)
ax.set_ylim(-boxsize, boxsize)
ax.set_zlim(-boxsize, boxsize)

plt.show()