import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import time

t1=time.time()
x = np.random.rand(10000)
t2=time.time()
print("Time taken by numpy.random.rand() to produce 10000 random nos: ",(t2-t1))

plt.hist(x,bins=10, density=True, label="Histogram plot")
plt.xticks(np.linspace(0,1,11))

#plotting uniform pdf in the range [0,1]
pdf_x = np.linspace(0,1,101)
pdf_y = np.ones(101)
plt.plot(pdf_x,pdf_y,label="Uniform pdf")

plt.xlabel("Random num(x)")
plt.ylabel("PDF")
plt.title("PDF plot of random number(using numpy) between 0,1")
plt.legend()
plt.show()

