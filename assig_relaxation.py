import numpy as np 
import math
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])

X=np.array([0.0,0.0,0.0,0.0,0.0]) #iterative solution
T=np.array([7.85971307,0.422926408,-0.073592239,-0.540643016,0.010626163]) #initial tolerance
b=np.array([1.0,2.0,3.0,4.0,5.0])

count=0 #no of iteration
w=1.25 #over relaxation
while abs(T[0])>=0.01 or abs(T[1])>=0.01 or abs(T[2])>=0.01 or abs(T[3])>=0.01 or abs(T[4])>=0.01:

	T=np.array([7.85971307,0.422926408,-0.073592239,-0.540643016,0.010626163]) #tolerance
	Y=np.array([0.0,0.0,0.0,0.0,0.0])
	r=np.array([0.0,0.0,0.0,0.0,0.0]) #residual vector
	for i in range(5):
		for j in range(5):
			Y[i]=Y[i]-(A[i,j]*X[j])
			
		r[i]=Y[i]+b[i]
		X[i]=X[i]+w*r[i]/A[i,i]		
		T[i]=T[i]-X[i]
	count=count+1	
print(count)	
	
	

print("no of iteration", count)	
print("Solution vector", X)
print("Tolerance", T)
