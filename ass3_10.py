#assignment 3
#qn-10
#By Souvik Kundu

import numpy as np 
import matplotlib.pyplot as plt 
import math
import urllib.request

with urllib.request.urlopen('http://theory.tifr.res.in/~kulkarni/noise.txt') as response:
	data=[]
	for line in response:
		data.append(float(line))

Noise=np.array(data)
l=len(Noise)
X=np.linspace(1,l,l)
dx=1

fig1,ax1=plt.subplots()
ax1.plot(X,Noise)
ax1.set_xlabel('n')
ax1.set_ylabel('Noise')
ax1.set_title('Noise vs data-count graph')

Noise_dft=np.fft.fft(Noise,norm='ortho')
K=np.fft.fftfreq(l,d=dx)
K=2*np.pi*K
fig2,ax2=plt.subplots()
ax2.plot(K,Noise_dft)
ax2.set_title('DFT of Noise vs K graph')
ax2.set_xlabel('K')
ax2.set_ylabel('Noise_DFT')
   

Power_noise=np.zeros(len(K))
for i in range(len(K)):
	Power_noise[i]=abs(Noise_dft[i])**2/len(K)

fig3,ax3=plt.subplots()
ax3.plot(K,Power_noise)
ax3.set_xlabel('K')
ax3.set_ylabel('Power spectra')
ax3.set_title("Power spectra using periodogram")


##making 10 equal bin of k amd binning the data of power spectra(Power_noise)
K_span=int((max(K)-min(K)))
n_bin=10
width=K_span/n_bin
lower_bound=min(K)
upper_bound=max(K)

K1=np.linspace(lower_bound,upper_bound,n_bin+1)
Power_bin=np.zeros(n_bin)
K_bin=np.zeros(n_bin)

for i in range(n_bin):
	count=0
	for j in range(len(K)):
		if K1[i]<=K[j]<K1[i+1]:
			Power_bin[i]+=Power_noise[j]
			count+=1
	Power_bin[i]=Power_bin[i]/count	
	K_bin[i]=K1[i]+(K1[i+1]-K1[i])/2


fig4,ax4=plt.subplots()
ax4.bar(K_bin,Power_bin,width)
ax4.set_xlabel("Binned K")
ax4.set_ylabel("Binned power spectra")
ax4.set_title("Plot of binned power spectra for noise")


plt.show()

