import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

t=np.linspace(0,5,51)
y=2*np.exp(-2*t)
X=np.loadtxt("random.txt")

plt.hist(X,bins=20,range=(0,5),density=True,label="Density histogram")
plt.plot(t,y,'--',label=r"Exponential PDF($\mu=0.5$)")
plt.legend()
plt.show()