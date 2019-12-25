import sys
import numpy as np
import matplotlib.pyplot as plt

def line_eq(p1, p2):
	if( np.abs(float(p2[0] - p1[0])) < 1.e-4 ):
		return None, None

	m = (p2[1] - p1[1]) / float(p2[0] - p1[0])
	b = p2[1] - (m * p2[0])
	return m, b


def x(v,t,phi):
	return (t-10.)*v*np.sin(phi)**2 + (t-10.)*np.cos(phi)*np.sqrt( 1.-v**2*np.sin(phi)**2 )


def y(v,t,phi):
	return -(t-10.)*v*np.sin(phi)*np.cos(phi) + (t-10.)*np.sin(phi)*np.sqrt( 1.-v**2*np.sin(phi)**2 )




def ext_points(x0, y0, xlist, ylist):
	for i,(xi,yi) in enumerate(zip(xlist,ylist)):
		m, b = line_eq( (x0,y0), (xi,yi) )
		if(m == None):
			xi = x0
			yi = yi >= 0. and 12. or -12.
		else:
			xi = xi >= 0. and 12. or -12.
			yi = m*xi + b

		xlist[i] = xi
		ylist[i] = yi

	return xlist,ylist
		


def connect_point(x0, y0, xlist, ylist):
	for xi,yi in zip(xlist,ylist):
		plt.plot([x0, xi], [y0, yi], 'k-', lw=1.)


def draw_line(xc,yc,xlist,ylist):
	for xci,yci,xi,yi in zip(xc,yc,xlist,ylist):
		plt.plot([xci, xi], [yci, yi], 'k-', lw=1.)




def circle(r):
	# theta goes from 0 to 2pi
	theta = np.linspace(0, 2*np.pi, 100)

	# the radius of the circle
	# r = np.sqrt(xc[0]**2+yc[0]**2)

	# compute x1 and x2
	x1 = r*np.cos(theta)
	x2 = r*np.sin(theta)

	plt.plot(x1, x2, 'r-', lw=1.5)







phi = np.arange(0., 2.*np.pi, np.pi/6.)

# t = [0., 1.5, 2.]
t  = 5.
v0 = 0.5
v1 = 0.75

if(False):
	# Plot of Data 
	plt.plot(x, y, 'ko') 
	plt.xlabel('x') 
	plt.ylabel('y') 
	plt.title("line") 
	plt.show()
	sys.exit()


xt = x(v0, t, phi)
yt = y(v0, t, phi)

xc = x(0.5, t, phi)
yc = y(0.5, t, phi)

xt1 = x(v1, t, phi)
yt1 = y(v1, t, phi)

x0 = v0*(t-10.)
y0 = 0.

xt, yt = ext_points(x0, y0, xt, yt)

plt.figure(figsize=(8,8))


plt.plot(x0, y0, 'ro', markersize=10)
if(t<10.):
	connect_point(x0, y0, xt, yt)
else:
	circle(np.sqrt(xc[0]**2+yc[0]**2))
	connect_point(x0, y0, xt1, yt1)
	draw_line(xc, yc, xt1, yt1)
	draw_line(xc, yc, xt, yt)




plt.xlabel('x') 
plt.ylabel('y')
plt.xlim(-6., 6.)
plt.ylim(-6., 6.)
plt.title("line") 
plt.show()