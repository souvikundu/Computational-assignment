import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

A=np.array([ [0.2,  0.1,  1.0, 1.0,  0.0],[0.1,  4.0, -1.0, 1.0, -1.0],[1.0, -1.0, 60.0, 0.0, -2.0],[1.0,  1.0,    0, 8.0,  4.0],[0,   -1.0, -2.0, 4.0,  700]])
b=np.array([1., 2., 3., 4., 5.])

T=np.array([7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163])	#true solution
X=np.zeros(5)		#intial guess of the solution
r=b-np.dot(A,X)
p=r
count=0

while any(abs(X - T) > 0.01):		#infinite loop

	alpha=np.inner(r, r)/ np.inner(p, np.dot(A,p))
	X=X + alpha*p
	r_new=r -alpha*np.dot(A,p)
	beta=np.inner(r_new, r_new) / np.inner(r, r)
	p=r_new + beta*p
	r=r_new

	# print(x)
	count+=1
	# if(all(abs(X - T) < 0.01)):	#if desired tolerance reached then break
	#  	break

print("no of iteration", count)	
print("Solution vector", X)