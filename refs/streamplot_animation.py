import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


nx, ny = .02, .02
x = np.arange(-15, 15, nx)
y = np.arange(-10, 10, ny)
X, Y = np.meshgrid(x, y)
dy = -1 + Y**2
dx = np.ones(dy.shape)

dyu = dy / np.sqrt(dy**2 + dx**2)
dxu = dx / np.sqrt(dy**2 + dx**2)

color = dyu
fig, ax = plt.subplots()
stream = ax.streamplot(X,Y,dxu, dyu, color=color, density=2, cmap='jet',arrowsize=1)
ax.set_xlabel('t')
ax.set_ylabel('x')

def animate(iter):
    ax.collections = [] # clear lines streamplot
    ax.patches = [] # clear arrowheads streamplot
    dy = -1 + iter * 0.01 + Y**2
    dx = np.ones(dy.shape)
    dyu = dy / np.sqrt(dy**2 + dx**2)
    dxu = dx / np.sqrt(dy**2 + dx**2)
    stream = ax.streamplot(X,Y,dxu, dyu, color=color, density=2, cmap='jet',arrowsize=1)
    print(iter)
    return stream

anim =   animation.FuncAnimation(fig, animate, frames=50, interval=10, blit=False, repeat=False)
# anim.save('./animation.gif', writer='imagemagick', fps=60)
plt.show()