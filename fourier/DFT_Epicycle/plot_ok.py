from presentation import *
import numpy as np

time_table, x_table, y_table = create_close_loop('batman.jpg')
plt.show()
plt.close('all')

order = 30 # We need higher order approximation to get better approximation
coef = coef_list(time_table, x_table, y_table, order)
# print(coef)

space = np.linspace(0, tau, 300) # tau = 2*pi
x_DFT = [DFT(t, coef, order)[0] for t in space]
y_DFT = [DFT(t, coef, order)[1] for t in space]

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x_DFT, y_DFT, 'r--')
ax.plot(x_table, y_table, 'k-')
ax.set_aspect('equal', 'datalim')

plt.show()
sys.exit()


xmin, xmax = xlim()
ymin, ymax = ylim()


anim = visualize(x_DFT, y_DFT, coef, order, space, [xmin, xmax, ymin, ymax])
Writer = animation.writers['html']
writer = Writer(fps=60)
anim.save('batman.html',writer=writer, dpi=150)