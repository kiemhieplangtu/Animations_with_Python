import sys
import tkinter as tk
import numpy   as np

import matplotlib.pyplot as plt

# from PIL             import Image
# from pylab           import *
from matplotlib      import animation
from math            import tau
from scipy.integrate import quad




def func(t, time_table, x_table, y_table):
    return np.interp(t, time_table, x_table) + 1j*np.interp(t, time_table, y_table)




def fourier_series(t, coef_list, order=5):
    s      = np.array( [(coef_list[i,0]+1j*coef_list[i,1]) *np.exp(-n*1j*t) for (i,n) in enumerate(range(-order, order+1)) ])
    series = np.sum( s, axis = 0 )
    return series.real, series.imag




def coef_list(time_table, x_table, y_table, order=5):
    coef_list = []
    for n in range(-order, order+1):
        real_coef = quad(lambda t: np.real(func(t, time_table, x_table, y_table) * np.exp(-n*1j*t)), 0, tau, limit=100, full_output=1)[0]/tau
        imag_coef = quad(lambda t: np.imag(func(t, time_table, x_table, y_table) * np.exp(-n*1j*t)), 0, tau, limit=100, full_output=1)[0]/tau
        coef_list.append([real_coef, imag_coef])
    return np.array(coef_list)


def update_center(coef, dt):
    new_center = []
    for i, j in enumerate(range(-order, order + 1)):
        dtheta = -j * dt    # to draw in the same direction of the line_func
        xx     = coef[i][0]
        yy     = coef[i][1]
        dr     = [xx*np.cos(dtheta) - yy*np.sin(dtheta), xx*np.sin(dtheta) + yy*np.cos(dtheta)]
        new_center.append(dr)
    return np.array(new_center)

def arrange_circle(order):
    idx = []
    for i in range(1,order+1):
        idx.extend([order+i, order-i])
    return idx




def draw(event):
	global ix, iy
	ix, iy = event.x, event.y

	npoint = 1
	x1, y1 = (ix-npoint), (iy-npoint)
	x2, y2 = (ix+npoint), (iy+npoint)
	c.create_oval(x1,y1,x2,y2, fill='red', outline='red', width=5)
	# c.create_line(x1,y1,x2,y2, fill="#476042", width=3)
	# print(event.x, event.y)
	global coords
	coords.append([ix, -iy])



### ---- MAIN ---- ###

w      = 600
h      = 450
coords = []

master = tk.Tk()
master.title('Draw with mouse')

c = tk.Canvas(master, width=w, height=h, bg='white')

c.pack(expand=True, fill='both')
c.bind('<B1-Motion>', draw)

message = tk.Label(master, text='Press and drag to draw slowly')
message.pack(side='bottom')
master.mainloop()

coords = np.array(coords)

print(coords.shape)


x_table    = coords[:,0]
y_table    = coords[:,1]
time_table = np.linspace(0, tau, len(x_table))

x_table = x_table - min(x_table)
y_table = y_table - min(y_table)
x_table = x_table - max(x_table) / 2.
y_table = y_table - max(y_table) / 2.

if(False):
	plt.plot(x_table, y_table, 'k-')
	plt.show()
	sys.exit()



order = 30 # We need higher order approximation to get better approximation
coef  = coef_list(time_table, x_table, y_table, order)

npoints              = 300
space                = np.linspace(0, tau, npoints) # tau = 2*pi
x_fourier, y_fourier = fourier_series(space, coef, order)


if(False):
	fig, ax = plt.subplots(figsize=(5, 5))
	ax.plot(x_fourier, y_fourier, 'r:')
	ax.plot(x_table, y_table, 'k-')
	ax.set_aspect('equal', 'datalim')

	plt.show()
	sys.exit()



## Plot
fig, ax = plt.subplots(figsize=(10,10))


# Initialize
line        = plt.plot([], [], 'k-', linewidth=2)[0]
radius_line = [plt.plot([], [], 'b-', linewidth=0.5, marker='o', markersize=1)[0] for _ in range(2 * order + 1)]
circles     = [plt.plot([], [], 'r-', linewidth=0.5)[0] for _ in range(2 * order + 1)]

theta       = np.linspace(0., tau, 50) # draw a circle, 50 = number of points of a circle
idx         = arrange_circle(order)
r           = [np.linalg.norm(x) for x in coef]

def animate(i):
    # line of the function
    line.set_data(x_fourier[:i], y_fourier[:i])

    center0 = coef[order]

    dcen    = update_center(coef, float(i)/float(npoints)*tau)

    for j, rad, circle in zip(idx,radius_line,circles):
        new_center = center0 + dcen[j]
        rad.set_data([center0[0], new_center[0]], [center0[1], new_center[1]])
        
        x, y = r[j] * np.cos(theta) + center0[0], r[j] * np.sin(theta) + center0[1]
        circle.set_data(x, y)
        center0 = new_center

ani = animation.FuncAnimation(fig, animate, frames=len(space), interval=100)

ax.set_xlim(-320., 320.)
ax.set_ylim(-300., 300.)
ax.set_aspect('equal')
plt.show()