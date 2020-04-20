import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
def f(t,y):
	return (y**2+y)/t

def f1(x,t):
    return ((x**2+x)/t)


##absolute error is better than 10^-4 implies if we take our target accuracy per unit time <10^-5 
##(we take 0.5*10^-5) the condition will be satisfied
h=0.01 ###initial starting step size
delta=0.5*10**(-4)

##implementing RK4 method:
t1=1.0  ##initial t
w1=-2.0  ##initial y
Y=np.array([-2.0])
T=np.array([1.0])

t_final=1 ##initial value to enter the loop
while t_final<=3.0:
	##single step evaluation
	k1=h*f(t1,w1)
	k2=h*f(t1+h/2,w1+k1/2)
	k3=h*f(t1+h/2,w1+k2/2)
	k4=h*f(t1+h,w1+k3)

	##double step evaluation
	g1=2*h*f(t1,w1)
	g2=2*h*f(t1+h,w1+g1/2)
	g3=2*h*f(t1+h,w1+g2/2)
	g4=2*h*f(t1+2*h,w1+g3)

	y2=w1+1/6*(g1+2*g2+2*g3+g4)	

	w1=w1+1/6*(k1+2*k2+2*k3+k4)
	t1=t1+h
	Y=np.append(Y,w1)
	T=np.append(T,t1)

	k1=h*f(t1,w1)
	k2=h*f(t1+h/2,w1+k1/2)
	k3=h*f(t1+h/2,w1+k2/2)
	k4=h*f(t1+h,w1+k3)

	y1=w1+1/6*(k1+2*k2+2*k3+k4)


	##adaptive step size control
	h=h*(30*delta*h/(abs(y1-y2)))**0.25

	t_final=t1

Y_true=odeint(f1,Y[0],T)

##estemating absolute error:
Error=np.zeros(len(T))
for j in range(len(Error)):
	Error[j]=abs(Y[j]-Y_true[j])
absolute_error=max(Error)
print("maximum of absolute error is ",absolute_error)	

with plt.style.context('dark_background'):

    plt.plot(T,Y,'c-o',label = "Adaptive Step Size")
    plt.plot(T,Y_true,'r-o',label="Exact solution")

    plt.legend()
    plt.grid()
    plt.show()
