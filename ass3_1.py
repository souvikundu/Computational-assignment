#assignment 3
#qn-1
#By Souvik Kundu

import numpy as np 
import matplotlib.pyplot as plt 
import math

def f(x):
	if x!=0:
		return np.sin(x)/x
	else:
		return 1
def rect(k):#FT of sinc function
	if abs(k)<=1:
		return np.sqrt(np.pi/2)
	else:
		return 0

			
x_min=-500
x_max=500

n=612
m=2*n+1
F=np.zeros(m)
X=np.linspace(x_min,x_max,m)
h=(x_max-x_min)/(2*n)

for i in range(m):
	F[i]=f(x_min+i*h)

#FT using numpy
F_dft=np.fft.fft(F,norm='ortho')
K=np.fft.fftfreq(m,d=h)
K=2*np.pi*K
factor=np.exp(-1j*K*x_min)
F_ft=h*np.sqrt(m/(2*np.pi))*factor*F_dft


#analytical FT
F_fte=np.zeros(m)
for k in range(m):
	F_fte[k]=rect(K[k])



plt.plot(K,F_ft,label="numerical solution")
plt.plot(K,F_fte,label="analytical solution")

plt.xlabel("k")
plt.ylabel("FT of Sinc(x)")
plt.grid()
plt.legend()

plt.show()


