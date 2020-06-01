import numpy as np
import math
import scipy

def probability_2dice(n):
	if n <=7:
		return (n-1)/36.0
	else:
		return (13-n)/36

		

def V(A):
	N=0
	for i in range(len(A)):
		N+=A[i]
	v=0	
	for j in range(11):
		v+=(A[j]-N*probability_2dice(j))**2/(N*probability_2dice(j+2))

	return v

def test_randomness(c):
	if c<0.01 or c>0.99:
		print("not sufficiently random")
	elif 0.01<=c<0.05 or 0.99>=c>0.95:
		print("suspect")
	elif 0.05<=c<0.1 or 0.9<c<=0.95:
		print("almost suspect")
	elif 0.1<=c<=0.9:
		print("suffeciently random")
		

		



Obs_count1=np.array([4,10,10,13,20,18,18,11,13,14,13])
Obs_count2=np.array([3,7,11,15,19,24,21,17,13,9,5])

print(V(Obs_count2))

c1 = 1.0-scipy.stats.chi2.cdf(V(Obs_count1), 10.0)
c2 = 1.0-scipy.stats.chi2.cdf(V(Obs_count2), 10.0)

print("The first set of observation is:"/n)
test_randomness(c1)

print("The second set of observation is:"/n)
test_randomness(c2)

