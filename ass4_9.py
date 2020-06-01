import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
#from scipy import norm 

def f(x):
	if 3<x<7:
		return 1
	else :
		return 0

N=10000
x0=5 #initial x we choose so that PDF converges quickly
X=[] ##good x choices
X_all=[] ## all x choices

x0=5 #choosed st. easily converges

for i in range(N):
    x1=x0+np.random.standard_normal()
    X_all.append(x1)
    r=np.random.rand()
    if f(x0)==0:
       x0=x1  
    elif f(x1)/f(x0)>r :
       x0=x1
    X.append(x0)


step=np.linspace(1,N,N)
fig1,ax1=plt.subplots()
plt.plot(step,X_all,'o',label="all points")
plt.plot(step,X,label="marcov chain")
ax1.set_xlabel("step")
ax1.set_ylabel("x")
plt.legend()
plt.title('Marcov chain')

pdf_x = np.linspace(3,7,11)
pdf_y = np.ones(11)*0.25
fig2,ax2=plt.subplots()
plt.hist(X,bins=20,range=(0,10),density=True,label="Histogram plot")
plt.plot(pdf_x,pdf_y,'--',label="Uniform PDF")
plt.plot()
ax2.set_xlabel("x")
ax2.set_ylabel("PDF")
plt.legend()
plt.title('Density plot')

plt.show()