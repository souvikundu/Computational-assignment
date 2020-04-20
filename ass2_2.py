import numpy as np 
import matplotlib.pyplot as plt 
h=0.1
step=int((2-1)/0.1)+1
t=np.linspace(1,2,step)

#Euler solution plot
y=[0]*len(t)
y[0]=1
def f(Y,T):
	return Y/T-(Y/T)**2
for i in range(1,len(t)):
	y[i]=y[i-1]+h*f(y[i-1],t[i-1])
plt.plot(t,y, label="euler")

#exact solution plot
z=[0]*len(t)
z[0]=1
for j in range(1,len(t)):
	z[j]=t[j]/(1+np.log(t[j]))
plt.plot(t,z, label="exact")

plt.xlabel("t")
plt.ylabel("y")

#absolute and relative error
abs_error=np.array([])
rtv_error=np.array([])
for k in range(len(t)):
	abs_error=np.append(abs_error,abs(z[k]-y[k]))
	rtv_error=np.append(rtv_error,abs((z[k]-y[k])/z[k]))

print("absolute error at each evaluation point is ",abs_error)
print("Relative error at each evaluation point is ",rtv_error)

plt.legend()		
plt.show()	

