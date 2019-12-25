import sys
import numpy            as np
from scipy.signal       import square
from matplotlib         import animation
from matplotlib         import pyplot as plt
from matplotlib.patches import ConnectionPatch

def bn(n, fnc, t):
   b = fnc*(np.sin(2.*n*np.pi*t))
   return 2.*b.sum()/fnc.size



nxpoints = 500
t        = np.linspace(0., 1., nxpoints, endpoint=False)
sq_wave  = square(2.*np.pi*t)

if(False):
  plt.plot(t, sq_wave)
  plt.show()
  sys.exit()


harm = [1,3,5,7]
bn_lst = []
n_harm = len(harm)
sq_mat = np.zeros((n_harm, nxpoints), dtype = np.complex_)
for idx, i in enumerate(harm): # (1,3,5,7))
# for idx, i in enumerate( range(n_harm) ): # (1,3,5,7))
   bn_lst.append( bn(i, sq_wave, t) )
   sq_mat[idx, :] = bn_lst[idx] * np.exp(1j*2.*np.pi*i*t)
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
N    = n_harm # 6

draw_lst = [ax_1.plot(0,0 )[0] ] +\
           [ax_2.plot(0,0 )[0] ] +\
           [ax_1.plot(0,0 )[0] ] + \
           [ax_1.plot(0,0 )[0] ]
circle_lst = [plt.Circle((0,0), bn_lst[i], alpha = 1, fill = False) for i in range(n_harm)]
con_patch_lst = [ConnectionPatch(xyA=(0,0), xyB=(0,0), coordsA='data', coordsB='data',\
                 axesA=ax_1, axesB=ax_2, zorder=25) ]

# for i in range(4):
#   ax_1.add_patch(circle_lst[i])
#   ax_1.add_artist(con_patch_lst[i])

for i in range(0, n_harm):
  ax_1.add_patch(circle_lst[i])
ax_1.add_artist(con_patch_lst[-1])

ax_2.set_zorder(-1)

def ani(i):
   # for j in range(4):
   #    con_patch_lst[j].remove()
   #    con_patch_lst[j] = ConnectionPatch(xyA=(sq_mat[j, i].real, sq_mat[j, i].imag), xyB=(t[i], sq_mat[j, i].imag), coordsA="data", coordsB="data", axesA=ax_1, axesB=ax_2, zorder=25)
   #    ax_1.add_artist(con_patch_lst[j])
   #    draw_lst[j].set_data(t[:i], sq_mat[j, :i].imag)
   
   for j in range(1, n_harm):
      circle_lst[j].center = (sq_mat_circ[j-1, i].real, sq_mat_circ[j-1, i].imag)
   
   con_patch_lst[-1].remove()
   con_patch_lst[-1] = ConnectionPatch(xyA=(sq_mat_circ[-1, i].real, sq_mat_circ[-1, i].imag),\
    xyB=(t[i], sq_mat_circ[-1, i].imag), coordsA='data', coordsB='data', axesA=ax_1, axesB=ax_2, zorder=25)
   
   ax_1.add_artist(con_patch_lst[-1])
   draw_lst[0].set_data(sq_mat_circ[-1, :i].real, sq_mat_circ[-1, :i].imag)
   draw_lst[1].set_data(t[:i], sq_mat_circ[-1, :i].imag)
   draw_lst[2].set_data([0., sq_mat_circ[0, i].real], [0., sq_mat_circ[0, i].imag])
   draw_lst[3].set_data([sq_mat_circ[-2, i].real, sq_mat_circ[-1, i].real], [sq_mat_circ[-2, i].imag, sq_mat_circ[-1, i].imag])
   return ([])

ani = animation.FuncAnimation(fig, ani, np.arange(0, nxpoints, i), interval=100, blit=True)
ax_1.set_xlim(-2.5, 2.5)
ax_1.set_ylim(-2.5, 2.5)
ax_2.set_xlim(0., 1.)
ax_2.set_ylim(-2.5, 2.5)
plt.show()