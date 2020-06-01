import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

def compare(n,dim):
	k=0
	for i in range(dim):
		k+=X[i,n]**2
	return k	

N=100000

##I have written a general code to find the volume of d dimensional sphere
dim=2
X=np.random.rand(N)
## X is a 2d array whose each column denotes a single point on x-y plane(uniformly distributed[0,1])
for j in range(dim-1):
	X = np.vstack((X,np.random.rand(N)))

count=0
for n in range(N):
	if compare(n,dim)<=1:
		count+=1
Area=2**dim*(count/N)
print("Volume of unit sphere in", dim,"dimension= ", Area)

##repeted same code with dim=10:
dim=10
X=np.random.rand(N)
## X is a 2d array whose each column denotes a single point on 10 dim plane(uniformly distributed[0,1])
for j in range(dim-1):
	X = np.vstack((X,np.random.rand(N)))


count=0
for n in range(N):
	if compare(n,dim)<=1:
		count+=1
Area=2**dim*(count/N)
print("Volume of unit sphere in", dim,"dimension= ", Area)