import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

def g(x):
	return 1.5*np.exp(-x)

def f(x):
	return np.sqrt(2/np.pi)*np.exp(-x**2/2)

n=10000

x = np.random.rand(n)#n uniformly distributed random num between 0,1

x = -np.log(x) #x: n random num distributed according to exp(-x) for x>=0

X = np.array([]) #set of random number distributed according to sqrt(2/pi)*exp(-x**2/2)

#rejection method:
for i in x:
	if np.random.rand()*g(i) <= f(i):
		X = np.append(X,i)

#effectively after x>5 P(x)=0 assumed:
plt.hist(X, range=(0.0,5.0), bins=20, density=True, label="Histogram plot")		

y = np.linspace(0,5,101)
Y = np.sqrt(2/np.pi)*np.exp(-y**2/2)
plt.plot(y,Y,label=r"$y=\sqrt{\frac{2}{\pi}}e^{-\frac{x^{2}}{2}}$")

plt.xlabel("x")
plt.ylabel("PDF")
plt.title(r"PDF of $y=\sqrt{\frac{2}{\pi}}e^{-\frac{x^{2}}{2}}$ using rejection method")
plt.legend()
plt.show()

