import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from scipy.optimize import minimize
import emcee
import corner
import urllib.request
import re



def log_likelihood(theta, x, y, yerr):
	a, b, c = theta
	model = a*x**2 + b*x + c
	var = yerr**2
	# negative ln L
	return 0.5 * np.sum((y - model) ** 2 / var + np.log(2 * np.pi * var))

def log_prior(theta):
	a, b, c = theta
	if -200<a<200 and -500.0 < b < 500 and -500< c < 500.0 :
		return 0.0
	else:
		return -np.inf

def log_posterior(theta, x, y, yerr):
	lp = log_prior(theta)
	if not np.isfinite(lp):
		return -np.inf
	return lp - log_likelihood(theta, x, y, yerr)

data=np.loadtxt("ass4.txt",delimiter='&')
x=data[:, 1]
y=data[:, 2]
sigma_y=data[:, 3]


guess = (1.0,1.0,1.0)
soln = minimize(log_likelihood, guess, args=(x, y, sigma_y))

nwalkers, ndim = 50, 3
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim)


sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior, args=(x, y, sigma_y))
sampler.run_mcmc(pos, 4000)

samples = sampler.get_chain()

fig,ax=plt.subplots(3)
fig.suptitle("Marcov chain of a,b,c")

ax[0].plot(samples[:, :, 0]) # a values
ax[0].set_xlabel("step")
ax[0].set_ylabel("a")

ax[1].plot(samples[:, :, 1]) # a values
ax[1].set_xlabel("step")
ax[1].set_ylabel("b")


ax[2].plot(samples[:, :, 2]) # a values
ax[2].set_xlabel("step")
ax[2].set_ylabel("c")

Flat_sample=sampler.get_chain(discard =200, thin=20, flat=True)
medians = np.median(Flat_sample, axis=0)
a_true, b_true, c_true = medians
fig1 = corner.corner(Flat_sample, labels=["a","b","c"], truths=[a_true, b_true, c_true])
fig1.suptitle("Posterior distribution of a,b,c")


fig2 = plt.figure()
fig2.suptitle("Best fit and additional 200 fits of the model")

X = np.linspace(0,300,601)
Y_best = a_true*X**2+b_true*X+c_true

#plotting random 200 fits from posteriors
for i in range(200):
	j = np.random.randint(len(Flat_sample))
	rand_posterior = Flat_sample[j]
	a,b,c = rand_posterior[:3]
	Y_rand = a*X**2+b*X+c
	plt.plot(X,Y_rand,'b')

#plotting best fit
plt.plot(X,Y_best,'g',label="Best fit")
plt.errorbar(x,y,sigma_y,fmt=".k",capsize=3,label="Experimental data with error bars") #showing data
plt.xlabel("x")
plt.ylabel("y")
plt.legend()	



plt.show()