import numpy as np
import matplotlib.pyplot as plt
# The ordinary differential equation
def g(x,y):
	return -9.0*y
def f(x,y):
    return -20*(y-x)**2+2*x

a=0 #initial value of x
b=1 #final value of x
h= 0.01 # step-size
N=int((b-a)/h)+1

#for problem 1.1
x=np.linspace(a,b,N)
y=np.zeros(N)
y[0]=2.71828

#for problem 1.2
X=np.linspace(a,b,N)
Y=np.zeros(N) 
Y[0]=1.0/3
for i in range(N-1):
	k=y[i]+h*g(x[i],y[i])
	y[i+1]=y[i]+h*g(x[i],k)
    

    
for i in range(N-1):
	k=Y[i]+h*f(X[i],Y[i])
	Y[i+1]=Y[i]+h*f(X[i+1],k)

fig1,ax1=plt.subplots()
plt.plot(x,y)
ax1.set_xlabel(r'$x$',fontsize=16)
ax1.set_ylabel(r'$y$',fontsize=16)
ax1.set_title("Backward Euler’s Method for problem 1.1 with h=0.01")
#plt.legend()
plt.grid()
   
fig2,ax2=plt.subplots()
plt.plot(X,Y)
ax2.set_xlabel(r'$x$',fontsize=16)
ax2.set_ylabel(r'$y$',fontsize=16)
ax2.set_title("Backward Euler’s Method for problem 1.2 with h=0.01")
#plt.legend()
plt.grid()
plt.show()
