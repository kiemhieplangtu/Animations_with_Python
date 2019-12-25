import numpy as np
import math as math
import matplotlib
import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
matplotlib.use('TkAgg')
 
root = Tk.Tk()
root.wm_title("Embedding in TK")
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
 
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust(bottom=0.25)


def update(val):
    pos = s_time.val
    l.set_ydata(pos * np.sin(l.get_xdata()))
    x = r.get_xdata()
    r.set_ydata(x * np.sin(pos * x))
    fig.canvas.draw_idle()
 
 
def create_values():
    return x_values, y_values
 
 
x_values = np.arange(-20,20,0.1)
y_values=[]
 
for i in range(0, len(x_values)):
    y_values.append(math.sin(x_values[i]))
 
ax1.axis([(-math.pi-1), (math.pi+1), -10, 10])
# ax1.plot(x_values, y_values)
 
ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
s_time = Slider(ax1_value, 'Value', 0, 30, valinit=0)

(l,) = ax1.plot(x_values, y_values)
(r,) = ax2.plot(x_values, y_values)
 
 
s_time.on_changed(update)
 
Tk.mainloop()