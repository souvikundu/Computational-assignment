import numpy as np 
import math
import time

np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
m=int(input("No of rows: "))
n=int(input("No of columns: "))
# A=np.zeros((m,n))
# print("enter the matrix input rowwise:")
# for i in range(m):
# 	print("entries for row",i+1)
# 	for j in range(n):
# 		A[i,j]=input()
start=time.time()
A1=np.transpose(A)
A_1=np.dot(A,A1) #A*A_T=U*S*S_T*U_T
A_2=np.dot(A1,A) #A_T*A=V*S_T*S*V_T
S,U=np.linalg.eigh(A_1)
S1,V=np.linalg.eigh(A_2)
U_s=np.zeros((m,m))
V_s=np.zeros((n,n))
for i in range(m):
	for j in range(m):
		U_s[i,j]=U[i,m-1-j]
for i in range(n):
	for j in range(n):
		V_s[j,i]=V[i,n-1-j]
S2=np.ones(n)
for i in range(n):
	S2[i]=math.sqrt(S1[n-1-i])



end=time.time()
time1=end-start
start=time.time()
u,s,vh=np.linalg.svd(A)
end=time.time()
time2=end-start

print("Manual computation:\n","U\n",U_s,"\nS\n",S2,"\nVh\n", V_s,"\ntime taken:",time1)
print("from linalg.svd:\n","U\n",u,"\nS\n",s,"\nVh\n", vh,"\ntime taken:",time2)