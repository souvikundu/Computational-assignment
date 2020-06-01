import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import time



a = 1664525
c = 1013904223
m = 4294967296
x = 1
n = 10000


randoms = []
t1=time.time()
for i in range(n):
	x = float((a*x+c)%m)
	randoms.append(x/m)
t2=time.time()

print("Time taken by linear congruential generator to produce 10000 random nos: ",(t2-t1))
plt.hist(randoms,bins=10,density=True,label="Histogram plot")
plt.xticks(np.linspace(0.1,1,10))

#plotting uniform pdf in the range [0,1]
pdf_x = np.linspace(0,1,101)
pdf_y = np.ones(101)
plt.plot(pdf_x,pdf_y,label="Uniform pdf")

plt.xlabel("Random num")
plt.ylabel("PDF")
plt.title("PDF plot of uniform random number between 0,1")
plt.legend()
plt.show()
