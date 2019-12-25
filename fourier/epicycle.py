import sys
import numpy            as np
from scipy.signal       import square
from matplotlib         import animation
from matplotlib         import pyplot as plt
from matplotlib.patches import ConnectionPatch





def fourier_series(fnc, N):
  """Calculate the Fourier series coefficients up to the Nth harmonic"""
  result = []
  T      = len(fnc)
  t      = np.arange(T)  # [0, 1, 2, ... ]
  for n in range(N+1):
      an = 2./T*(fnc * np.cos(2.*np.pi*n*t/T)).sum()
      bn = 2./T*(fnc * np.sin(2.*np.pi*n*t/T)).sum()
      result.append((an, bn))
  return np.array(result)



def reconstruct(size, coeffs):
  result = 0.
  t      = np.arange(size)  # [0, 1, 2, ... ]
  for n, (a, b) in enumerate(coeffs):
    if n == 0:
      a = a/2.
    result = result + a*np.cos(2.*np.pi*n*t/size) + b * np.sin(2.*np.pi*n*t/size)
  return result


def element_i(size, n, an, bn):
  result = 0.
  t      = np.arange(size)  # [0, 1, 2, ... ]
  return an*np.cos(2.*np.pi*n*t/size) + bn*np.sin(2.*np.pi*n*t/size)




def fourier_series_complex(fnc, N):
  """Calculate the Fourier series coefficients an, bn up to the Nth harmonic"""
  result = []
  T      = len(fnc)
  t      = np.arange(T)  # [0, 1, 2, ... ]
  for n in range(N+1):
    c_plusn  = 2./T * (fnc * np.exp(-2j*np.pi*n*t/T)).sum()
    c_minusn = 2./T * (fnc * np.exp(2j*np.pi*n*t/T)).sum()
    result.append((c_plusn, c_minusn))
  return np.array(result)



def reconstruct_cn(size, coeffs):
  cp    = coeffs[:,0]
  cm    = coeffs[:,1]
  order = len(cp) - 1

  result = 0.
  t      = np.arange(size)  # [0, 1, 2, ... ]3

  for i in range(order+1):
    if(i < 0 ):
      result = result + cm[i]*np.exp(-2j*np.pi*i*t/size)
    elif(i == 0):
      result = result + cp[i]/2.
    else:
      result = result + cp[i]*np.exp(2j*np.pi*i*t/size)
  
  return result



## --------------- MAIN ------------- ##

func1 = lambda t: (abs((t%1)-0.25) < 0.25).astype(float) - (abs((t%1)-0.75) < 0.25).astype(float)
func2 = lambda t: t % 1
func3 = lambda t: (abs((t%1)-0.5) < 0.25).astype(float) + 8*(abs((t%1)-0.5)) * (abs((t%1)-0.5)<0.25)
func4 = lambda t: ((t%1)-0.5)**2

nxpoints = 500
N        = 30
t        = np.linspace(0., 1., nxpoints, endpoint=True)
# sq_wave  = square(2.*np.pi*t)
func     = func2(t)

# AiBi     = fourier_series(func, 50)
Cn       = fourier_series_complex(func, N)


if(False):
  plt.figure(figsize=(10., 10.))
  plt.plot(t, func, label='Original', lw=2)
  plt.plot(t, reconstruct_cn(len(t), Cn).real, label='Reconstructed with Cn - real')
  # plt.plot(t, reconstruct(len(t), AiBi[:20,:]), label='Reconstructed with 20 Harmonics')
  # plt.plot(t, reconstruct(len(t), AiBi[:50,:]), label='Reconstructed with 50 Harmonics')
  plt.legend(loc='upper left')
  plt.show()
  plt.close('all')


  plt.figure(figsize=(10., 10.))
  plt.plot(t, reconstruct_cn(len(t), Cn).imag, label='reconstruct with Cn - imag')
  # plt.plot(t, reconstruct(len(t), AiBi[:20,:]), label='Reconstructed with 20 Harmonics')
  # plt.plot(t, reconstruct(len(t), AiBi[:50,:]), label='Reconstructed with 50 Harmonics')
  plt.legend(loc='upper left')
  plt.show()
  plt.close('all')

  sys.exit()


  plt.subplot(121)
  plt.stem(AiBi[:,0], use_line_collection=True)
  plt.ylim(-1.,1.5)

  plt.subplot(122)
  plt.stem(AiBi[:,1], use_line_collection=True)
  plt.ylim(-1.,1.5)
  plt.show()
  plt.close('all')
  sys.exit()


harm   = range(-1, 10) # Change this for different function, some functions need negative values
an_lst = []
bn_lst = []
cn_lst = []
n_harm = len(harm)
sq_mat = np.zeros((n_harm, nxpoints), dtype = np.complex_)

for idx, i in enumerate(harm):
  if(i > 0):
    cn_lst.append( Cn[i,0] )
    sq_mat[idx, :] = Cn[i,0] * np.exp(2j*np.pi*i*t)
  elif(i == 0):
    cn_lst.append( Cn[i,0] )
    sq_mat[idx, :] = Cn[i,0]/2.
  else:
    cn_lst.append( Cn[i,1] )
    sq_mat[idx, :] = Cn[i,1]*np.exp(-2j*np.pi*i*t)

  # sq_mat[idx, :] =  element_i(len(t), i, AiBi[i,0], AiBi[i,1])

sq_mat_circ = np.add.accumulate(sq_mat, 0)

if(False):
  plt.figure(figsize=(10., 10.))
  plt.plot(t, sq_mat_circ[0].real, label='0', lw=2)
  plt.plot(t, sq_mat_circ[1].real, label='1', lw=2)
  plt.plot(t, sq_mat_circ[2].real, label='2', lw=2)
  plt.plot(t, sq_mat_circ[3].real, label='3', lw=2)
  plt.legend(loc='upper left')
  plt.show()
  plt.close('all')


  plt.figure(figsize=(10., 10.))
  plt.plot(t, sq_mat_circ[0].imag, label='0', lw=2)
  plt.plot(t, sq_mat_circ[1].imag, label='1', lw=2)
  plt.plot(t, sq_mat_circ[2].imag, label='2', lw=2)
  plt.plot(t, sq_mat_circ[3].imag, label='3', lw=2)
  plt.legend(loc='upper left')
  plt.show()
  plt.close('all')

  sys.exit()











fig  = plt.figure(1, figsize=(10,10))
ax_1 = fig.add_subplot(221)
ax_2 = fig.add_subplot(222)

cmap = plt.get_cmap('jet_r')
N    = n_harm


centre_lst = [ ax_1.plot(0., 0., 'k.')[0] for i in range(1, n_harm)] # Centers of circles

draw_lst = [ax_1.plot(0., 0., 'b-')[0] ] +\
           [ax_2.plot(0., 0., 'r-')[0] ] +\
           [ax_1.plot(0., 0.)[0] ] +\
           [ax_1.plot(0., 0., 'r-' )[0] ]    # -> radius line
circle_lst = [plt.Circle((0,0), np.abs(cn_lst[i]), alpha = 1, fill = False) for i in range(n_harm)]
con_patch_lst = [ConnectionPatch(xyA=(0,0), xyB=(0,0), coordsA='data', coordsB='data',\
                 axesA=ax_1, axesB=ax_2, zorder=25) ]


for i in range(0, n_harm):
  ax_1.add_patch(circle_lst[i])
ax_1.add_artist(con_patch_lst[-1])
ax_2.plot(t, func, 'k-', label='Original', lw=1)

ax_2.set_zorder(-1)

def ani(i):
   for j in range(1, n_harm):
      circle_lst[j].center = (sq_mat_circ[j-1, i].imag, sq_mat_circ[j-1, i].real)  # Find the centers for each circle
      centre_lst[j-1].set_data(sq_mat_circ[j-1, i].imag, sq_mat_circ[j-1, i].real)
   
   con_patch_lst[-1].remove() # remove Linked line
   con_patch_lst[-1] = ConnectionPatch(xyA=(sq_mat_circ[-1, i].imag, sq_mat_circ[-1, i].real),\
    xyB=(t[i], sq_mat_circ[-1, i].real), coordsA='data', coordsB='data', axesA=ax_1, axesB=ax_2, zorder=25) # For linked line
   
   ax_1.add_artist(con_patch_lst[-1])                                               # Linked line
   draw_lst[0].set_data(sq_mat_circ[-1, :i].imag, sq_mat_circ[-1, :i].real)         # line in ax1
   draw_lst[1].set_data(t[:i], sq_mat_circ[-1, :i].real)                            # Reconstructed line
   draw_lst[2].set_data([0., sq_mat_circ[0, i].imag], [0., sq_mat_circ[0, i].real]) # -> radius line
   draw_lst[3].set_data([sq_mat_circ[-2, i].imag, sq_mat_circ[-1, i].imag],\
                        [sq_mat_circ[-2, i].real, sq_mat_circ[-1, i].real]) # -> radius line
   return ([])

ani = animation.FuncAnimation(fig, ani, np.arange(0, nxpoints, i), interval=200, blit=True)

ax_1.set_xlim(-2., 2.)
ax_1.set_ylim(-2., 2.)
ax_2.set_xlim(0., 1.)
ax_2.set_ylim(-2., 2.)
plt.show()