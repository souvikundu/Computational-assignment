import numpy as np
import matplotlib.pyplot as plt
def f1(t,u1,u2,u3):
    return u1+2*u2-2*u3+np.exp(-t)
def f2(t,u1,u2,u3):
	return u2+u3-2*np.exp(-t)
def f3(t,u1,u2,u3):
	return u1+2*u2+np.exp(-t)
a=0
b=1
h=0.01
N=int((b-a)/h)+1

T=np.linspace(a,b,N)
U1=np.zeros(N)
U2=np.zeros(N)
U3=np.zeros(N)
U1[0]=3
U2[0]=-1
U3[0]=1

for i in range(N-1):
	k1=h*f1(T[i],U1[i],U2[i],U3[i])
	l1=h*f2(T[i],U1[i],U2[i],U3[i])
	m1=h*f3(T[i],U1[i],U2[i],U3[i])

	k2=h*f1(T[i]+h/2,U1[i]+k1/2,U2[i]+l1/2,U3[i]+m1/2)
	l2=h*f2(T[i]+h/2,U1[i]+k1/2,U2[i]+l1/2,U3[i]+m1/2)
	m2=h*f3(T[i]+h/2,U1[i]+k1/2,U2[i]+l1/2,U3[i]+m1/2)

	k3=h*f1(T[i]+h/2,U1[i]+k2/2,U2[i]+l2/2,U3[i]+m2/2)
	l3=h*f2(T[i]+h/2,U1[i]+k2/2,U2[i]+l2/2,U3[i]+m2/2)
	m3=h*f3(T[i]+h/2,U1[i]+k2/2,U2[i]+l2/2,U3[i]+m2/2)

	k4=h*f1(T[i]+h,U1[i]+k3,U2[i]+l3,U3[i]+m3)
	l4=h*f2(T[i]+h,U1[i]+k3,U2[i]+l3,U3[i]+m3)
	m4=h*f3(T[i]+h,U1[i]+k3,U2[i]+l3,U3[i]+m3)

	U1[i+1]=U1[i]+(k1+2*k2+2*k3+k4)/6
	U2[i+1]=U2[i]+(l1+2*l2+2*l3+l4)/6
	U3[i+1]=U3[i]+(m1+2*m2+2*m3+m4)/6

plt.plot(T,U1,color='black',label="U1")
plt.plot(T,U2,color='red',label="U2")
plt.plot(T,U3,color='green',label="U3")

plt.legend()
plt.grid()
plt.show()


