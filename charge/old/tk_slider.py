from tkinter import *

from matplotlib.figure import Figure

def show_values():
    # print (w1.get(), w2.get())
    print (w2.get())
    sel = "Value = " + str(w2.get())
    label.config(text = sel)

root = Tk()
menu = Menu(root)
root.config(menu=menu)

# try fiddling with these root.geometry values
root.title('My tkinter size experiment')
root.minsize(width=100, height=100)
root.geometry('1000x920+0+0')

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New")
subMenu.add_command(label="Open File...")
subMenu.add_command(label="Close")
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

editMenu = Menu(menu)
menu.add_cascade(label="?",menu=editMenu)
editMenu.add_command(label="Check For Updates")
editMenu.add_command(label="Change log")
editMenu.add_command(label="About")


w2 = Scale(root,length=500, from_=0, to=200,tickinterval=50, resolution=0.1, orient=HORIZONTAL)
w2.set(23)
w2.pack(anchor=CENTER)
btn = Button(root, text='Show', command=show_values)
btn.pack(anchor=CENTER)

label = Label(root)  
label.pack()


## Figure within Tk
figure = Figure(figsize=(5, 4), dpi=100)
plot = figure.add_subplot(1, 1, 1)

plot.plot(0.5, 0.3, color="red", marker="o", linestyle="")

x = [ 0.1, 0.2, 0.3 ]
y = [ -0.1, -0.2, -0.3 ]
plot.plot(x, y, color="blue", marker="x", linestyle="")


root.mainloop()



# from tkinter import *  
  
# def select():  
#    sel = "Value = " + str(v.get())  
#    label.config(text = sel)  
     
# top = Tk()  
# top.geometry("500x300")  
# v = DoubleVar()  
# scale = Scale( top, length=200, width=10, variable = v, from_ = 1, to = 50, resolution=0.1, orient = HORIZONTAL)  
# scale.pack(anchor=CENTER)  
  
# btn = Button(top, text="Value", command=select)  
# btn.pack(anchor=CENTER)  
  
# label = Label(top)  
# label.pack()  
  
# top.mainloop()  