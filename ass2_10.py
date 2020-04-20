import numpy as np
import matplotlib.pyplot as plt
def f(z,x):
    return (1/(z**2+x**2*(1-z)**2))
def t(z):
	return z/(1-z)  ##as z=1 the original function blows up we take t=10^6 as the order of infinity
def z(t):
	return t/(t+1.0)

a=0
b=1
h=0.01
N=int((b-a)/h)+1
X=np.zeros(N)
Z=np.linspace(a,b,N)
X[0]=1

for j in range(N-1):
	k1=h*f(Z[j],X[j])
	k2=h*f(Z[j]+h/2,X[j]+k1/2)
	k3=h*f(Z[j]+h/2,X[j]+k2/2)
	k4=h*f(Z[j]+h,X[j]+k3)
	X[j+1]=X[j]+(k1+2*k2+2*k3+k4)/6	

figure1,ax1=plt.subplots()
plt.plot(Z,X,color='c',label="X-Z plot(Z=changed time variable)")
ax1.set_xlabel(r'$z$',fontsize=16)
ax1.set_ylabel(r'$x$',fontsize=16)
ax1.text(400, 1.6, r"$\frac{dx}{dz}=\frac{1}{z^2+x^2 \ (1-z)^2}$", fontsize=16)

plt.grid()
plt.legend()


T=np.zeros(N)
for i in range(N-1):
	T[i]=t(Z[i])
T[N-1]=3.5*10**6	
##as t=3.5*10^6,z approximately 1(we take O(10^6) of t to be infinity)
print("the value of x at" r"$t=x(t=3.5\times 10^6)$" "is", X[N-1])

figure2,ax2=plt.subplots()
plt.semilogx(T,X,color='r',label="X-T plot(T=original time variable)")
ax2.set_xlabel(r'$t$',fontsize=16)
ax2.set_ylabel(r'$x$',fontsize=16)
ax2.text(400, 1.6, r"$\frac{dx}{dt}=\frac{1}{x^2+t^2}$", fontsize=16)
ax2.text(400,1.3,r"$x(t=3.5\times 10^6)=2.144818$",fontsize=12)	

plt.grid()
plt.legend()
plt.show()