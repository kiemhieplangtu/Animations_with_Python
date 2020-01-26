import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def norm(v):
	A     = np.linalg.norm( v, axis=1 )
	vnorm = np.zeros_like(v)
	for i in range(len(vnorm)):
		vnorm[i] = v[i]/A[i]

	return vnorm


def vec_dot(n,v):
	nr,nc = v.shape
	ret   = np.zeros(nr)
	for i in range(nr):
		ret[i] = np.dot(n, v[i])

	return ret


def vec_dott(v,n):
	nr,nc = v.shape
	ret   = np.zeros(nr)
	for i in range(nr):
		ret[i] = np.dot(v[i], n)

	return ret		


def cal_lambda(t,phi):
	v     = get_vel(t)
	nr, nc = v.shape
	gamma = 1. / np.sqrt( 1. - v**2 )
	vnorm = norm(v)

	vec_n = [ np.cos(phi), np.sin(phi) ]

	temp1 = vec_dot(vec_n, vnorm)
	temp2 = vec_dott(v,vec_n)

	ret = np.zeros_like(v)

	for i in range(nr):
		ret[i] = ( vec_n + temp1[i]*vnorm[i]*(gamma[i] - 1.) + gamma[i]*v[i] ) / gamma[i] / (1. + temp2[i] )


	return ret # (vec_n + (gamma - 1.)*np.dot(vec_n, vnorm)*vnorm + gamma*v) / gamma / (1. + np.dot(v,vec_n) )


def get_pos(t):
	return np.array( [0.*t, 0.8*np.sin(np.pi*t)/np.pi] ).T


def get_vel(t):
	return np.array( [0.*t, 0.8*np.cos(np.pi*t)] ).T


# def get_a(t):
# 	return np.array( [0., -0.8*np.pi*np.sin(np.pi*t)] )      



deg2rad = np.pi/180.
t       = 0.
tt      = t - 15.
tt      = np.arange(t - 15., t, 0.1)

pos     = get_pos(tt)
# vel     = get_vel(t)
# acc     = get_a(t)

phi     = 10. * deg2rad

v     = get_vel(tt)
# vnorm = np.linalg.norm( v )


aaa = cal_lambda(tt,phi)

tdiff = t - tt


aa = np.zeros_like(pos)
for i in range( len(tt) ):
	aa[i] = pos[i] + tdiff[i] * aaa[i]

print aa




plt.plot( aa, aa, 'r.' )
plt.xlim(-5., 5.)
plt.ylim(-5., 5.)
plt.show()