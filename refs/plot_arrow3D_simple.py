from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


fig = plt.figure()
ax = fig.gca(projection='3d')


#dibujar punto
ax.scatter([0],[0],[0],color="g",s=100)


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

#m=float(raw_input())
# a = Arrow3D([0,0],[0,1],[0,0], **arrow_prop_dict)
# b = Arrow3D([0,-1],[0,0],[0,0], **arrow_prop_dict)
# c = Arrow3D([0,0],[0,0],[0,1], **arrow_prop_dict)
# d = Arrow3D([0,0],[0,0],[0,-1], **arrow_prop_dict)
# e = Arrow3D([0,1],[0,0],[0,0], **arrow_prop_dict)
# f = Arrow3D([0,0],[0,-0.5],[0,0], **arrow_prop_dict)

ax.add_artist(Arrow3D([0,0],[0,1],[0,0], **arrow_prop_dict))
# ax.add_artist(b)
# ax.add_artist(c)
# ax.add_artist(d)
# ax.add_artist(e)
# ax.add_artist(f)


boxsize = 1.
ax.set_xlim3d(-boxsize, boxsize)
ax.set_ylim3d(-boxsize, boxsize)
ax.set_zlim3d(-boxsize, boxsize)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()