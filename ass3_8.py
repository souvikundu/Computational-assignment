#assignment 3
#qn-8
#By Souvik Kundu

import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

def z_func(x,y):
 return np.exp(-(x**2+y**2))
x_min=-100
x_max=100
y_min=-100
y_max=100

n=200
m=2*n+1
x=np.linspace(x_min,x_max,m)
y=np.linspace(y_min,y_max,m)

dx=(x_max-x_min)/(2*n)
dy=(y_max-y_min)/(2*n)

X,Y=np.meshgrid(x,y) # grid of point
Z=z_func(X,Y) # evaluation of the function on the grid

kx=2*np.pi*np.fft.fftfreq(m,d=dx)
ky=2*np.pi*np.fft.fftfreq(m,d=dy)

Kx,Ky=np.meshgrid(kx,ky)
Z_fft=np.fft.fft2(Z,norm="ortho")
factor=np.exp(-1j*Kx*x_min)*np.exp(-1j*Ky*y_min)

Z_fft=dx*dy*factor*m/(2*np.pi)*Z_fft ##by numpy.fft.fft2

Z_Aft=0.5*np.exp(0.25*(-Kx**2-Ky**2)) #Analytical solution

fig=plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
surf=ax1.plot_surface(Kx,Ky,np.real(Z_fft),cmap=cm.RdBu,linewidth=0, antialiased=False)
ax1.text2D(0.05, 0.95, "numpy.fft.fft2", transform=ax1.transAxes)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)

ax1.set_xlabel('kx',fontsize=14)
ax1.set_ylabel('ky',fontsize=14)
ax1.set_zlabel(r'$\tilde{Z_n}$',fontsize=14)

ax2 = fig.add_subplot(122, projection='3d')
surf1=ax2.plot_surface(Kx,Ky,Z_Aft,cmap=cm.hot,linewidth=0, antialiased=False)
ax2.text2D(0.05, 0.95, "analytical soln.", transform=ax2.transAxes)
ax2.zaxis.set_major_locator(LinearLocator(10))
ax2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf1, shrink=0.5, aspect=5)

ax2.set_xlabel('kx',fontsize=14)
ax2.set_ylabel('ky',fontsize=14)
ax2.set_zlabel(r'$\tilde{Z_a}$',fontsize=14)

plt.show()
