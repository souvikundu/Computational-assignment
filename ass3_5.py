#assignment 3
#qn-5
#By Souvik Kundu

import numpy as np 
import matplotlib.pyplot as plt 
import math
import time
p=100
N=np.zeros(p)
n=1
def dft_time(num_arr):
	l=len(num_arr)
	num_dft=np.zeros(l)
	start=time.time()
	for i in range(l):
		for j in range(l):
			num_dft[i]+=num_arr[j]*np.exp(-1j*2*np.pi*j*i/l)
		num_dft[i]=1/np.sqrt(l)*num_dft[i]
	end=time.time()
	return end-start

def fft_time(num_arr):
	start=time.time()
	num_fft=np.fft.fft(num_arr,norm='ortho')
	end=time.time()
	return end-start

DFT_time=np.zeros(p)
FFT_time=np.zeros(p)
for i in range(p):
	N[i]=n #n 
	num_arr=np.linspace(1,n,n) #chosen arbitrary n numbers like this with dx=1
	DFT_time[i]=dft_time(num_arr)
	st=time.time()
	num_fft=np.fft.fft(num_arr,norm='ortho')
	en=time.time()
	FFT_time[i]=fft_time(num_arr)
	n=n+1
plt.plot(N,DFT_time,label='Without using fft')
plt.plot(N,FFT_time,label='Using fft')

plt.xlabel('n')
plt.ylabel('Time')
plt.legend()
plt.grid()
plt.show()