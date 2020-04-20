from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


#given functions:
def f1(t,y):
	return(t*np.exp(3*t)-2*y)
def f2(t,y):
	return(1-(t-y)**2)
def f3(t,y):
	return(1+y/t)
def f4(t,y):
	return(np.cos(2*t)+np.sin(3*t))


#The exact Solutions obtained from mathematica:
def y_exact1(t):
	return((5*t-1)*np.exp(3*t)/25+np.exp(-2*t)/25)
def y_exact2(t):
	return((1-3*t+t**2)/(-3+t))
def y_exact3(t):
	return(t*2+t*np.log(t))
def y_exact4(t):
	return(np.sin(2*t)/2-np.cos(3*t)/3+8/6)


##solution of first eqn:
a1=0
b1=1
y1_0=0
t=np.linspace(a1,b1,11)

exact_sol1=np.zeros(len(t))
for i in range(len(t)):
	exact_sol1[i]=y_exact1(t[i]) 


num_sol1=solve_ivp(f1,[a1, b1], [y1_0],t_eval=t)

error1=np.zeros(11)
for j in range(11):
	error1[j]=abs(exact_sol1[j]-num_sol1.y[0][j])
print("Maximum absolute error is", max(error1))

fig1,ax1=plt.subplots()
plt.plot(num_sol1.t,num_sol1.y[0],'r-o',label='Numerical solution(solve_ivp)')
plt.plot(t,exact_sol1,color='blue', label='Exact solution from mathematica')
ax1.set_xlabel(r'$t$',fontsize=16)
ax1.set_ylabel(r'$y$',fontsize=16)
ax1.text(0.4,1.75, r"$\dot{y}=te^{3t}-2y$", fontsize=14)
plt.legend()
plt.grid()



##Solution of second equation
a2=2
b2=3
y2_0=1
t=np.linspace(a2,b2,11)

exact_sol2=np.zeros(len(t))
for i in range(len(t)):
	exact_sol2[i]=y_exact2(t[i]) 

num_sol2=solve_ivp(f2,[a2, b2], [y2_0],t_eval=t)


error2=np.zeros(10) #here we omitted the last point as exact solution blows up at t=3
for j in range(10):
	error2[j]=abs(exact_sol2[j]-num_sol2.y[0][j])
print("Maximum absolute error is", max(error2))

fig2,ax2=plt.subplots()
plt.plot(num_sol2.t,num_sol2.y[0],'r-o',label='Numerical solution(solve_ivp)')
plt.plot(t,exact_sol2,'b', label='Exact solution from mathematica')
ax2.set_xlabel(r'$t$',fontsize=16)
ax2.set_ylabel(r'$y$',fontsize=16)
ax2.text(2,-2, r"$\dot{y}=1-(t-y)^2$", fontsize=14)
plt.legend()
plt.grid()



#Solution of Third equation by scipy
a3=1
b3=2
y3_0=2
t=np.linspace(a3,b3,11)

exact_sol3=np.zeros(len(t))
for i in range(len(t)):
	exact_sol3[i]=y_exact3(t[i]) 

num_sol3=solve_ivp(f3,[a3, b3], [y3_0],t_eval=t)

error3=np.zeros(11)
for j in range(11):
	error3[j]=abs(exact_sol3[j]-num_sol3.y[0][j])
print("Maximum absolute error is", max(error3))


fig3,ax3=plt.subplots()
plt.plot(num_sol3.t,num_sol3.y[0],'r-o', label='Numerical solution(solve_ivp)')
plt.plot(t,exact_sol3,'b', label='Exact solution from mathematica')
ax3.set_xlabel(r'$t$',fontsize=16)
ax3.set_ylabel(r'$y$',fontsize=16)
ax3.text(1.2,4, r"$\dot{y}=1+y/t$", fontsize=14)
plt.legend()
plt.grid()



#Solution of Fourth equation
a4=0
b4=1
y4_0=1
t=np.linspace(a4,b4,11)

exact_sol4=np.zeros(len(t))
for i in range(len(t)):
	exact_sol4[i]=y_exact4(t[i]) 

num_sol4=solve_ivp(f4,[a4, b4], [y4_0],t_eval=t)

error4=np.zeros(11)
for j in range(11):
	error4[j]=abs(exact_sol4[j]-num_sol4.y[0][j])
print("Maximum absolute error is", max(error4))


fig4,ax4=plt.subplots()
plt.plot(num_sol4.t,num_sol4.y[0],'r-o', label='Numerical solution(solve_ivp)')
plt.plot(t,exact_sol4,'b', label='Exact solution from mathematica')
ax4.set_xlabel(r'$t$',fontsize=16)
ax4.set_ylabel(r'$y$',fontsize=16)
ax4.text(0.6,1.40, r"$\dot{y}=\cos2t+\sin3t$", fontsize=16)
plt.legend()
plt.grid()

plt.show()

