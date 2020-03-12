import numpy as np 
import math
np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)

A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
d=3

a,b=np.linalg.eigh(A)
max_value=max(abs(a))
print("true value=", "%.4f" %max_value)

x=np.array([1,0,0]) #choosen vector that will be linear combination of all eigen vector
y=np.array([1,0,0])
A_n1=np.identity(d)
A_n=np.identity(d)
n=1
k=1
while abs(n)>0.01:#accurate within 1%
	A_n=np.matmul(A_n,A)
	A_n1=np.matmul(A_n,A)
	nu=np.dot(np.matmul(A_n1,x),y)
	de=np.dot(np.matmul(A_n,x),y)
	power_value=nu/de
	# power_value_n=power_value**k #gives power_value^k
	power_vector=np.matmul(A_n,x)/(power_value**k)
	n=(power_value-max_value)/max_value
	#n=(power_value-max_value)
	k+=1	
print("approximate value:","%.4f" %power_value)
print("approximate eigen vector:\n", power_vector) #the obtained eigen vector is a scalar multiple of the linalg.eigh eigen vector


