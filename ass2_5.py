import numpy as np 
import matplotlib.pyplot as plt 
x=np.linspace(0,10,101)
h=10.0/(len(x)-1)
g=-10

'''
two coupled differential equation:
du/dx=g (solution is linear in x, hence Euler forward method will give accurate result)
dy/dx=u (solution is quadratic in x, hence Euler mid-point method will give accurate result)

'''
def f(Y,U,X):
	return -10
def g(U):
	return U

y=[0]*len(x)


u=[0]*len(x)

#boundary condition

y[0]=0


#two initial guess for u[0](Bisection method)
alpha=70 ##make sure that y[last]>0
beta=40 ##make sure that y[last]<0


flag=10 #initial arbitrary non zero number to enter the loop
while abs(flag)>=0.000000001:
	u[0]=(alpha+beta)/2
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
	
	flag=y[len(x)-1]
	#print(flag)
	#break
	if flag>0:
		alpha=u[0]
	else:
		beta=u[0]		
	plt.plot(x,y,color='green', linestyle='dashed')

#drawing numerical solution
plt.plot(x,y,'b-o', linestyle='dashed',label="Numerical solution")

#drawing exact solution
y1=[0]*len(x)
for k in range(len(x)):
	y1[k]=-5*x[k]*(x[k]-10)
plt.plot(x,y1,color='black', linestyle='solid',label="exact solution")	


# setting x and y axis range 
plt.ylim(0,150) 
plt.xlim(0,10) 
 
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('Shooting method') 		
plt.legend()
plt.show()	