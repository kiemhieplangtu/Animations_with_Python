import numpy as np
import math as math
import matplotlib
import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def line_eq(p1, p2):
	if( np.abs(float(p2[0] - p1[0])) < 1.e-4 ):
		return None, None

	m = (p2[1] - p1[1]) / float(p2[0] - p1[0])
	b = p2[1] - (m * p2[0])
	return m, b


def x(v,t,phi):
	return (t)*v*np.sin(phi)**2 + (t)*np.cos(phi)*np.sqrt( 1.-v**2*np.sin(phi)**2 )


def y(v,t,phi):
	return -(t)*v*np.sin(phi)*np.cos(phi) + (t)*np.sin(phi)*np.sqrt( 1.-v**2*np.sin(phi)**2 )




def ext_points(x0, y0, xlist, ylist):
	for i,(xi,yi) in enumerate(zip(xlist,ylist)):
		m, b = line_eq( (x0,y0), (xi,yi) )
		if(m == None):
			xi = x0
			yi = yi >= 0. and 99. or -99.
		else:
			xi = xi >= 0. and 99. or -99.
			yi = m*xi + b

		xlist[i] = xi
		ylist[i] = yi

	return xlist,ylist
		


def connect_point(x0, y0, xlist, ylist):
	for xi,yi in zip(xlist,ylist):
		ax1.plot([x0, xi], [y0, yi], 'k-', lw=1.)


def draw_line(xc,yc,xlist,ylist):
	for xci,yci,xi,yi in zip(xc,yc,xlist,ylist):
		ax1.plot([xci, xi], [yci, yi], 'k-', lw=1.)




def circle(r):
	# theta goes from 0 to 2pi
	theta = np.linspace(0, 2*np.pi, 100)

	# the radius of the circle
	# r = np.sqrt(xc[0]**2+yc[0]**2)

	# compute x1 and x2
	x1 = r*np.cos(theta)
	x2 = r*np.sin(theta)

	ax1.plot(x1, x2, 'r-', lw=1.5)




def update(val):
	ax1.clear()
	ax1.axis([-30., 80., -50., 50.])
	t  = time.val
	v0 = vv0.val
	v1 = vv1.val
	# l.set_xdata(v0*(t - 10.) )

	xt  = x(v0, t-tbreak, phi)
	yt  = y(v0, t-tbreak, phi)
	
	xc  = x(v0, t-tbreak, phi)
	yc  = y(v0, t-tbreak, phi)

	xt1 = x(v1, t-tbreak, phi)
	yt1 = y(v1, t-tbreak, phi)

	x0 = v0*(t-tbreak)
	y0 = 0.

	xt, yt = ext_points(x0, y0, xt, yt)

	ax1.plot(v0*(t-tbreak), y0, 'ro', markersize=10)
	ax1.plot(0., 0., 'rx', markersize=10) # Location of acceleration

	if(t<tbreak):
		connect_point(x0, y0, xt, yt)
	else:
		circle(np.sqrt(xc[0]**2+yc[0]**2))
		connect_point(x0, y0, xt1, yt1)
		draw_line(xc, yc, xt1, yt1)
		draw_line(xc, yc, xt, yt)

	fig.canvas.draw_idle()






### MAIN ###
phi = np.arange(0., 2.*np.pi, np.pi/6.)

v0  = 0.5 # unit of c
v1  = 0.7 # unit of c

t0     = 0.1
tbreak = 20.
x0     = v0*(t0-tbreak)
y0     = 0.

xt     = x(v0, t0-tbreak, phi)
yt     = y(v0, t0-tbreak, phi)

xt, yt = ext_points(x0, y0, xt, yt)




## Plot 
matplotlib.use('TkAgg')
 
root   = Tk.Tk()
root.wm_title("Embedding in TK")
root.minsize(width=100, height=100)
root.geometry('1000x920+0+0')

fig    = plt.Figure()
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

ax1    = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.25)

 
ax1.axis([-30., 80., -50., 50.])
 
ax1_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
ax2_value = fig.add_axes([0.12, 0.14, 0.78, 0.03])
ax3_value = fig.add_axes([0.12, 0.09, 0.78, 0.03])

vv0  = Slider(ax2_value, 'v0', 0.1, 0.5,  valinit=0.5, valstep=0.1)
vv1  = Slider(ax3_value, 'v1', 0.6, 0.9,  valinit=0.7, valstep=0.1)
time = Slider(ax1_value, 't', 0.1, 100., valinit=0.1, valstep=0.1)

ax1.plot(x0, y0, 'ro', markersize=10)
ax1.plot(0., 0., 'rx', markersize=10) # location at acceleration
connect_point(x0, y0, xt, yt)
 
 
time.on_changed(update)
vv0.on_changed(update)
vv1.on_changed(update)
 
Tk.mainloop()