from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
	return np.vstack((y[1], -np.exp(-2*y[0])))
def bc1(ya, yb):
	return np.array([ya[0], yb[0]-np.log(2)])

def f2(x, y):
	return np.vstack((y[1], y[1]*np.cos(x)-y[0]*np.log(y[0]) ))
def bc2(ya, yb):
	return np.array([ya[0]-1, yb[0]-np.exp(1)])

def f3(x, y):
	return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])*np.cos(x)**(-1) ))
def bc3(ya, yb):
	return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])

def f4(x, y):
	return np.vstack((y[1], 0.5*(1-y[1]**2-y[0]*np.sin(x))  ))
def bc4(ya, yb):
	return np.array([ya[0]-2, yb[0]-2 ])

#Solution of first equation
a1=1
b1=2
h=0.01
N1=int((b1-a1)/h)+1

X_1=np.linspace(a1,b1,N1)
Y_1 = np.zeros((2,N1))
Y_1[0]=0

sol_1=solve_bvp(f1,bc1,X_1,Y_1) #solution from solve_bvp
y1=np.log(X_1) #solution from mathematica

error1=np.zeros(N1)
for j in range(N1):
	error1[j]=abs(y1[j]-sol_1.sol(X_1)[0][j])

print("Reason for arguing my numerical solution is correct is:")	
print("Maximum absolute error for first one is", max(error1))

fig1,ax1=plt.subplots()
plt.plot(X_1,sol_1.sol(X_1)[0],'.',label="Using solve_bvp")
plt.plot(X_1,y1,'black',label="Using Mathematica")
ax1.set_xlabel(r'$t$',fontsize=16)
ax1.set_ylabel(r'$y$',fontsize=16)
plt.legend()
ax1.text(1.6, 0.2, r"$y''=-e^{-2y}$", fontsize=12)
plt.grid()


#Solution of second equation by scipy
a2=0
b2=np.pi/2
h=0.01
N2=int((b2-a2)/h)+1

X_2=np.linspace(a2,b2,N2)
Y_2 = np.zeros((2,N2))
Y_2[0]=1

sol_2 =solve_bvp(f2, bc2, X_2, Y_2) #solution from solve_bvp
y2=np.exp(np.sin(X_2)) #solution from mathematica

error2=np.zeros(N2)
for j in range(N2):
	error2[j]=abs(y2[j]-sol_2.sol(X_2)[0][j])
print("Maximum absolute error for second one is", max(error2))

fig2,ax2=plt.subplots()
plt.plot(X_2,sol_2.sol(X_2)[0],'.',label="Using solve_bvp")
plt.plot(X_2,y2,'black',label="Using Mathematica")
ax2.set_xlabel(r'$t$',fontsize=16)
ax2.set_ylabel(r'$y$',fontsize=16)
plt.legend()
ax2.text(1.0,1.25, r"$y''=y'\cos x-y\ln y$", fontsize=12)
plt.grid()


#Solution of third equation by scipy
a3=np.pi/4
b3=np.pi/3
h=0.01
N3=int((b3-a3)/h)+1

X_3=np.linspace(a3,b3,N3)
Y_3=np.zeros((2,N3))
Y_3[0]=2**(-(1.0/4))

sol_3=solve_bvp(f3,bc3,X_3,Y_3) #solution from solve_bvp
y3=np.sqrt(np.sin(X_3)) #solution from mathematica

error3=np.zeros(N3)
for j in range(N3):
	error3[j]=abs(y3[j]-sol_3.sol(X_3)[0][j])
print("Maximum absolute error for third one is", max(error3))

fig3,ax3=plt.subplots()
plt.plot(X_3,sol_3.sol(X_3)[0],'.',label="Using solve_bvp")
plt.plot(X_3,y3,'black',label="Using Mathematica")
ax3.set_xlabel(r'$t$',fontsize=16)
ax3.set_ylabel(r'$y$',fontsize=16)
plt.legend()
ax3.text(0.92, 0.85, r"$y''=-(2y'^3+y^2y')\sec(x)$", fontsize=12)
plt.grid()


#Solution of fourth equation by scipy
a4=0
b4=np.pi
h=0.1
N4=int((b4-a4)/h)+1

X_4=np.linspace(a4,b4,N4)
Y_4=np.zeros((2,N4))
Y_4[0]=2.0

sol_4=solve_bvp(f4,bc4,X_4,Y_4) #solution from solve_bvp
y4=np.sin(X_4)+2  #solution from mathematica

error4=np.zeros(N4)
for j in range(N4):
	error4[j]=abs(y4[j]-sol_4.sol(X_4)[0][j])
print("Maximum absolute error for fourth one is", max(error4))

fig4,ax4=plt.subplots()
plt.plot(X_4,sol_4.sol(X_4)[0],'.',label="Using solve_bvp")
plt.plot(X_4,y4,'black',label="Using Mathematica")
ax4.set_xlabel(r'$t$',fontsize=16)
ax4.set_ylabel(r'$y$',fontsize=16)
plt.legend()
ax4.text(1.25, 2.25, r"$y''=\frac{1}{2}-\frac{y'^2}{2}-y \ \frac{\sin(x)}{2}$", fontsize=12)
plt.grid()

plt.show()

