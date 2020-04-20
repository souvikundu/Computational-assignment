import numpy as np
import matplotlib.pyplot as plt

a=0
b=10
h=0.1
N=int((b-a)/h)+1

T=np.linspace(0,10,N) 
X=np.zeros(N) ##X[0], X[100] satisfies the boundary condition
X[0]=0.0
X[N-1]=0.0


## we have N-2 linear eqn(A*X=B) with N-2 unknoown(x1,x2,x3....) which we have to solve by iterative technique
## using Gauss seidal iterative technique to find the correct solution in between
##### we will check the tollerence w.r.t. original solution in each step to end iteration

#forming A matrix & B array:
l=N-2
A=np.zeros((l,l))
for i in range(1,l-1):
    A[i,i-1]=1.0
    A[i,i]=-2.0
    A[i,i+1]=1.0
A[0,0]=-2.0
A[0,1]=1.0
A[l-1,l-2]=1.0
A[l-1,l-1]=-2.0

B=np.array([])
for j in range(l):
    B=np.append(B,-10*h**2)

x_exact=np.linalg.solve(A,B)

X_true=np.zeros(N)
for m in range(1,N-1):
    X_true[m]=x_exact[m-1]

X_iterative=np.ones(l) ##initial guess solution
tollerence=x_exact ## initial tollerence

count=0
while 2==2:
    tollerence=x_exact #tolerance
    
    for i in range(l):
        y=0    
        for j in range(l):
            if j!=i:
                y+=-(A[i,j]*X_iterative[j])/A[i,i]
        X_iterative[i]=y+B[i]/A[i,i]       
    tollerence=tollerence-X_iterative

    count=count+1
    if all(abs(m) <= 0.1 for m in tollerence):
        break
    if count%500.0==0.0:
        for m in range(1,N-1):
            X[m]=X_iterative[m-1]
        plt.plot(T,X, color='blue')
    
print(max(tollerence)) 
print(count)    
for m in range(1,N-1):
    X[m]=X_iterative[m-1]
plt.plot(T,X,'b-o',label=("Solution by relaxation method", count))
plt.plot(T,X_true, label="exact solution", color='black')       

plt.xlabel("t")
plt.ylabel("x")   
plt.legend()
plt.show()
     



