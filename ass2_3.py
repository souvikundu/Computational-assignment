import numpy as np 
import matplotlib.pyplot as plt 
x=np.linspace(0,1,101)
h=1.0/(len(x)-1)

'''
two coupled differential equation:
du/dx=f(y,u,x)=2u-y+x*e^x-x
dy/dx=g(u)=u
'''

y=[0]*len(x)
u=[0]*len(x)
u[0]=0
y[0]=0

def f(Y,U,X):
	return 2*U-Y+X*np.exp(X)-X
def g(U):
	return U

##implementing RK4 method
for i in range(len(x)-1):
	k1=h*f(y[i],u[i],x[i])
	l1=h*g(u[i])
	k2=h*f(y[i]+l1/2,u[i]+k1/2,x[i]+h/2)
	l2=h*g(u[i]+k1/2)
	k3=h*f(y[i]+l2/2,u[i]+k2/2,x[i]+h/2)
	l3=h*g(u[i]+k2/2)
	k4=h*f(y[i]+l3,u[i]+k3,x[i]+h)
	l4=h*g(u[i]+k3)
	u[i+1]=u[i]+(k1+2*k2+2*k3+k4)/6
	y[i+1]=y[i]+(l1+2*l2+2*l3+l4)/6

	
plt.plot(x,y)
plt.show()	

