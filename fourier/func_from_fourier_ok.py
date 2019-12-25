import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation



def fourier_series(period, N):
	"""Calculate the Fourier series coefficients up to the Nth harmonic"""
	result = []
	T      = len(period)
	t      = np.arange(T)
	for n in range(N+1):
	    an = 2/T*(period * np.cos(2*np.pi*n*t/T)).sum()
	    bn = 2/T*(period * np.sin(2*np.pi*n*t/T)).sum()
	    result.append((an, bn))
	return np.array(result)



def reconstruct(P, anbn):
    result = 0.
    t = np.arange(P)
    for n, (a, b) in enumerate(anbn):
        if n == 0:
            a = a/2
        result = result + a*np.cos(2*np.pi*n*t/P) + b * np.sin(2*np.pi*n*t/P)
    return result




def showHarmonics(period, N):
    """Calculate the Fourier Series up to N harmonics, and show the reconstructed signal."""
    F = fourier_series(period, N+1)
    plt.subplot(231)
    plt.stem(F[:,0], use_line_collection=True)
    plt.subplot(234)
    plt.stem(F[:,1], use_line_collection=True)
    plt.subplot(132)
    T = len(period)
    t = np.arange(T)/T
    result = 0
    for n, (an, bn) in enumerate(F):
        if n == 0:
            an = an/2.
        cos_part = an*np.cos(2*np.pi*n*t)
        sin_part = bn*np.sin(2*np.pi*n*t)
        plt.plot(t, cos_part)
        plt.plot(t, sin_part)
        result = result + cos_part + sin_part
    plt.subplot(133)
    t2 = np.arange(2*T)/T
    plt.plot(t2, np.tile(period, 2))
    plt.plot(t2, np.tile(result, 2))
    plt.show()
    plt.close('all')



func1 = lambda t: (abs((t%1)-0.25) < 0.25).astype(float) - (abs((t%1)-0.75) < 0.25).astype(float)
func2 = lambda t: t % 1
func3 = lambda t: (abs((t%1)-0.5) < 0.25).astype(float) + 8*(abs((t%1)-0.5)) * (abs((t%1)-0.5)<0.25)
func4 = lambda t: ((t%1)-0.5)**2

Fs = 10000

if(False):
	t  = np.arange(-1.5, 2, 1/Fs)
	plt.subplot(221); plt.plot(t, func1(t))
	plt.subplot(222); plt.plot(t, func2(t))
	plt.subplot(223); plt.plot(t, func3(t))
	plt.subplot(224); plt.plot(t, func4(t))

	plt.show()
	plt.close('all')
	sys.exit()




t_period = np.arange(0., 1., 1./Fs)
if(False):
	F = fourier_series(func1(t_period), 20)
	plt.subplot(121)
	plt.stem(F[:,0], use_line_collection=True)
	plt.subplot(122)
	plt.stem(F[:,1], use_line_collection=True)
	plt.show()
	plt.close('all')
	sys.exit()

if(True):
	F = fourier_series(func1(t_period), 100)
	plt.plot(t_period, func1(t_period), label='Original', lw=2)
	plt.plot(t_period, reconstruct(len(t_period), F[:20,:]), label='Reconstructed with 20 Harmonics')
	plt.plot(t_period, reconstruct(len(t_period), F[:100,:]), label='Reconstructed with 100 Harmonics')
	plt.legend(loc='upper left')
	plt.show()
	plt.close('all')
	sys.exit()

# showHarmonics(func1(t_period), 50)
# showHarmonics(func2(t_period), 50)
# showHarmonics(func3(t_period), 50)
# showHarmonics(func4(t_period), 50)



fig    = plt.figure(figsize=(10,10))

period = func1(t_period)
F      = fourier_series(period, 1)
plt.subplot(231)
plt.stem(F[:,0], use_line_collection=True)
plt.subplot(234)
plt.stem(F[:,1], use_line_collection=True)
plt.subplot(132)

T      = len(period)
t      = np.arange(T)/T
result = 0
for n, (an, bn) in enumerate(F):
    if n == 0:
        an = an/2
    cos_part = an*np.cos(2*np.pi*n*t)
    sin_part = bn*np.sin(2*np.pi*n*t)
    plt.plot(t, cos_part)
    plt.plot(t, sin_part)
    result = result + cos_part + sin_part

plt.subplot(133)
t2 = np.arange(2*T)/T
plt.plot(t2, np.tile(period, 2))
plt.plot(t2, np.tile(result, 2))


def update(i):
	print ('t:', i)
	fig.suptitle('N = ' + str(i), fontsize=16)

	F = fourier_series(period, i)

	plt.subplot(231)
	plt.stem(F[:,0], use_line_collection=True)
	plt.title('An')

	plt.subplot(234)
	plt.stem(F[:,1], use_line_collection=True)
	plt.title('Bn')

	plt.subplot(132)
	T      = len(period)
	t      = np.arange(T)/T
	result = 0
	for n, (an, bn) in enumerate(F):
	    if n == 0:
	        an = an/2
	    cos_n = an*np.cos(2*np.pi*n*t)
	    sin_n = bn*np.sin(2*np.pi*n*t)
	    plt.plot(t, cos_n)
	    plt.plot(t, sin_n)
	    result = result + cos_n + sin_n
	plt.title('cos_n and sin_n')

	plt.subplot(133)
	plt.cla()
	# plt.title('N = ' + str(i))
	t2 = np.arange(2*T)/T
	plt.plot(t2, np.tile(result, 2))
	plt.plot(t2, np.tile(period, 2))
	plt.title('Result')



# ani = animation.FuncAnimation(fig, update, frames=np.arange(-3., 11., 0.1), fargs=(points), interval=1, repeat=False)
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 50, 1), interval=1, repeat=False)


# ax.set_xlim(-5., 5.)
# ax.set_ylim(-5., 5.)
# ax.grid()
plt.show()