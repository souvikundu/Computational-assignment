import numpy as np 
import math
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
A=np.array([[5,-2],[-2,8]])

Q,R=np.linalg.qr(A)
print("QR decomposition of A:")
print(" Q=", Q)
print("R=", R)

a,b=np.linalg.eigh(A)
eigh_value1=a[1]
eigh_value2=a[0]



#condition inside the while loop is when off diagonal elements are zero(I have taken the O(10^-10) as zero with respect to the minimum of eigen values which are O(1))
while abs(A[0,1])>=10**-10 or abs(A[1,0])>=10**-10:
	Q,R=np.linalg.qr(A)
	A=np.matmul(R,Q)
qr_value1=A[0,0]
qr_value2=A[1,1]

print("eigen values obtained from QR decomposition:", qr_value1,qr_value2)	
print("eigen values obtained from linalg.eigh package:", eigh_value1,eigh_value2)