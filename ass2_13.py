import numpy as np 
import matplotlib.pyplot as plt 

def f(t,u,y):
	return t*np.log(t)+2*u/t-2*y/t**2
def g(u):
	return u
def exact(t):
	return 7*t/4.0+t**3/2*np.log(t)-3/4.0*t**3

a=1
b=2
h=0.001
N=int((b-a)/h)+1
T=np.linspace(a,b,N)	
Y=np.zeros(N)
Y_e=np.zeros(N)
U=np.zeros(N)
Y[0]=1
U[0]=0

for i in range(N-1):
	U[i+1]=U[i]+f(T[i],U[i],Y[i])*h ##using euler forward method
	Y[i+1]=Y[i]+(g(U[i])+g(U[i+1]))*h/2 ###using euler mid-point method

for j in range(N):
	Y_e[j]=exact(T[j])



plt.plot(T,Y,'r-o',label="Using Euler method")
plt.plot(T,Y_e,color='blue',label="Analytical solution")	
plt.legend()
plt.xlabel(r'$t$',fontsize=16)
plt.ylabel(r'$y$',fontsize=16)
plt.show()