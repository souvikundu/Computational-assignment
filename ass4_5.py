import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

x1 = np.random.rand(10000)
x2 = np.random.rand(10000)
'''x1 and x2 uniformly istributed random numbers between 0 and 1 ensures 
y1 and y2 will have normal distribution with mean at 0 and variance=1'''
y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

plt.hist(y1,bins=20, density=True, label="Histogram plot")
plt.xlim([-5,5])

X=np.linspace(-5,5,101)
Y=1/np.sqrt(2*np.pi)*np.exp(-X**2/2)
plt.plot(X,Y,label=r'$y=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^{2}}{2}}$')

plt.xlabel("x")
plt.ylabel("PDF")
plt.title("PDF of normal distribution using Box-Muller method")
plt.legend()
plt.show()


