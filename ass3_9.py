#assignment 3
#qn-9
#By Souvik Kundu

import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
	if abs(x)<1:
		return 1
	else:
		return 0
def dft(num_arr):
	l=len(num_arr)
	num_dft=np.zeros(l)
	for i in range(l):
		for j in range(l):
			num_dft[i]+=num_arr[j]*np.exp(-1j*2*np.pi*j*i/l)
		num_dft[i]=1/np.sqrt(l)*num_dft[i]
	return num_dft

def idft(num_arr):
	l=len(num_arr)
	num_idft=np.zeros(l)
	for i in range(l):
		for j in range(l):
			num_idft[i]+=num_arr[j]*np.exp(1j*2*np.pi*j*i/l)
		num_idft[i]=1/np.sqrt(l)*num_idft[i]
	return num_idft		

x_min=-10
x_max=10

n=250
m=2*n+1
##two function g and h we want to convolve
g=np.zeros(m)
h=np.zeros(m)

##sampleing of two function:
X=np.linspace(x_min,x_max,m)
dx=(x_max-x_min)/(2*n)
for i in range(m):
	g[i]=f(x_min+i*dx)
	h[i]=f(x_min+i*dx)

##evaluating DFT of two functions
g_dft=dft(g)
h_dft=dft(h)
f_dft=np.asarray(g_dft)*np.asarray(h_dft)
K=np.fft.fftfreq(m, d=dx)
dk=K[1]-K[0]
X1=np.fft.fftfreq(m, d=dk)
##IDFT and convolution
f=np.asarray(idft(f_dft))
f=dx*np.sqrt(m)*f
plt.plot(X,g,label='box function')
plt.plot(X1,f,label='convolution')
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.legend()
plt.show()