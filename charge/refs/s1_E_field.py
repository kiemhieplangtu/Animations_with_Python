import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def norm(v):
	# A     = np.linalg.norm( v, axis=1 )
	# vnorm = np.zeros_like(v)
	# for i in range(len(vnorm)):
	# 	vnorm[i] = v[i]/A[i]

	if(np.sum(v**2) == 0.):
		return v*0.

	return v / np.sqrt(np.sum(v**2))


def vec_dot(n,v):
	# nr,nc = v.shape
	# ret   = np.zeros(nr)
	# for i in range(nr):
	# 	ret[i] = np.dot(n, v[i])

	return np.dot(n, v[i])


def vec_dott(v,n):
	nr,nc = v.shape
	ret   = np.zeros(nr)
	for i in range(nr):
		ret[i] = np.dot(v[i], n)

	return ret		


def cal_lambda(t,phi):
	v     = get_vel(t)
	gamma = 1. / np.sqrt( 1. - v[0][0]**2 )
	vnorm = norm(v)
	vec_n = np.array( [np.cos(phi), np.sin(phi)] ).T

	a = vec_n + (gamma-1.)*np.dot(vec_n, vnorm.T)*vnorm + gamma*v
	b = gamma*(np.dot(v, vec_n.T)+1.)[0]

	for i in range( len(phi) ):
		a[i,:] = a[i,:]/b[i]

	return a



# def get_pos(t):
# 	return np.array( [ [0.9*np.sin(np.pi*t)/np.pi, 0.] ] )


# def get_vel(t):
# 	return np.array( [ [0.9*np.cos(np.pi*t), 0.] ] )




def get_pos(t):
	if(t<0.):
		return np.array( [ [t/np.sqrt(2.), 0.] ] )
	if(t<1.):
		return np.array( [ [1. + t/np.sqrt(2.) - np.sqrt(1.+t**2), 0.] ] )
	if(t>=1.):
		return np.array( [ [1. + 1./np.sqrt(2.) - np.sqrt(2.), 0.] ] )


def get_vel(t):
	if(t<0.):
		return np.array( [ [1./np.sqrt(2.), 0.] ] )
	if(t<1.):
		return np.array( [ [1./np.sqrt(2.) - t/np.sqrt(1.+t**2), 0.] ] )
	if(t>=1.):
		return np.array( [ [0., 0.] ] )





# def get_pos(t):
# 	if(t<0.):
# 		return np.array( [ [0., 0.] ] )
# 	if(t<1.):
# 		return np.array( [ [np.sqrt(1.+t**2)-1., 0.] ] )
# 	if(t>=1.):
# 		return np.array( [ [np.sqrt(2.) -1. + (t-1.)/np.sqrt(2.), 0.] ] )


# def get_vel(t):
# 	if(t<0.):
# 		return np.array( [ [0., 0.] ] )
# 	if(t<1.):
# 		return np.array( [ [t/np.sqrt(1.+t**2), 0.] ] )
# 	if(t>=1.):
# 		return np.array( [ [1./np.sqrt(2.), 0.] ] )




phi    = np.arange(0., 360., 15.)*np.pi/180.

t      = -10.
p      = get_pos(t)[0]

tarray = np.arange(t-15., t, 0.1)

nrow   = len(phi)
ncol   = 2                    # x and y
ndepth = len(tarray)


dat = np.zeros( (nrow, ncol, ndepth) )
for (i,xt) in enumerate(tarray):
	# a = get_pos(xt)         # [1x2] -> 1st column: x, 2nd column: y
	# b = cal_lambda(t,phi)   # [24x2] -> 1st column: x, 2nd column: y for 24 values of phi
	x = get_pos(xt) + (t-xt)*cal_lambda(xt,phi)
	dat[:,:,i] = x




fig = plt.figure(figsize=(10,10))
ax  = fig.add_subplot(111)
for i in range(nrow):
	# ax.plot(dat[:,0,:], dat[:,1,:])
	ax.plot(dat[i,0,:], dat[i,1,:], 'k-')


points = plt.plot(p[0], p[1], 'ro', markersize=10)

def update(t, points):
	p      = get_pos(t)[0]
	tarray = np.arange(t-15., t, 0.1)

	print ('t:', t)

	ax.clear()

	points = plt.plot(p[0], p[1], 'ro', markersize=10)

	dat = np.zeros( (nrow, ncol, ndepth) )
	for (i,xt) in enumerate(tarray):
		x = get_pos(xt) + (t-xt)*cal_lambda(xt,phi)
		dat[:,:,i] = x

	for i in range(nrow):
		ax.plot(dat[i,0,:], dat[i,1,:], 'k-')

	ax.set_xlim(-5., 5.)
	ax.set_ylim(-5., 5.)

	return points



ani = animation.FuncAnimation(fig, update, frames=np.arange(-3., 11., 0.1), fargs=(points), interval=1, repeat=False)


ax.set_xlim(-5., 5.)
ax.set_ylim(-5., 5.)
ax.grid()
plt.show()