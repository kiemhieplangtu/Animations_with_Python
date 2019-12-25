from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-30,30,10)
y = np.linspace(-30,30,10)
z = np.linspace(-30,30,10)

x,y,z = np.meshgrid(x,y,z)

# 3d figure
fig = plt.figure()
ax  = fig.gca(projection='3d')

def B(x,y):
    i = 1                                           #Amps in the wire
    mu = 1.26 * 10**(-6)                            #Magnetic constant                       
    mag = (mu/(2*np.pi))*(i/np.sqrt((x)**2+(y)**2)) #Magnitude of the vector B
    by = mag * (np.cos(np.arctan2(y,x)))            #By
    bx = mag * (-np.sin(np.arctan2(y,x)))           #Bx
    bz = z*0                                        #Bz (zero, using the right-hand rule)
    return bx,by,bz

def E(x,y,z):
    Q   = 400.
    r   = np.sqrt(x**2 + y**2 + z**2)
    mag = Q / r**2                                 # Magnitude of the vector E
    ex  = mag * np.cos(np.arctan2(r,x))           # Ex
    ey  = mag * np.cos(np.arctan2(r,y))           # Ey
    ez  = mag * np.cos(np.arctan2(r,z))            # Ez
    return ex,ey,ez

def cylinder(r):
    phi = np.linspace(-2*np.pi,2*np.pi,100)
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    return x,y

# Plot of the fields
ex,ey,ez = E(x,y,z)                                   #Magnetic field
# cx,cy = cylinder(0.2)                               #Wire

# Plot of the 3d vector field
ax.quiver(x,y,z,ex,ey,ez,color='b',length=1,normalize=False)
                                                    #Plot the magnetic field
# for i in np.linspace(-4,4,800):                     #Plot the wire
#     ax.plot(cx,cy,i,label='Cylinder',color='r')

plt.title('E field of a straight wire')
plt.xlabel('x')
plt.ylabel('y')
plt.show()