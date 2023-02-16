#Credit to @AlonNegrin
"""
Created on Tue Wed 26 02:27:59 2023

Bootstrapping - a moderen method to estimate the sampling distribution of 
point processes, which is an alternative to traditional methods.
In bootstrapping we repeatedly draw N observations with replacement 
from the original data to create bootstrap sample. 
By calculating the mean of each resample and repeating this process a large 
number of times, a good approximation of the mean sampling distribution 
can be obtained. 
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import math
import pandas as pd
import numpy as np
import random


car_data = pd.read_csv('car_data.csv', encoding = 'latin-1')
print(car_data.columns)
car_data.head(10)
 
# group the car_data by date - each day in the year is one entry
accidents = car_data.groupby(['Date']).size()
accidents.head(20)
print('Mean:', accidents.mean(), 'std:', accidents.std())
# Bootstrapping to obtain an estimate of the sampling distribution of the mean
# ----------------------------------------------------------------------------

# a function to conduct bootsrap samples
def meanBootstrap(X,numberb):
    '''
    X - input array, numberb - number of bootstrapping samples or resamples
    meanBootstrap computes and returns x - the samples means 
    '''
    x = [0]*numberb
    for i in range(numberb):
        sample = [X[_] for _ in np.random.randint(len(X), size=len(X))]
        #print(sample)
        x[i] = np.mean(sample)
        #print(x[i])
    return x

# lets do a simple example
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # start with this 
# and then comment the line and uncomment the next line
# X = np.random.randn(50) # 50 points from a normal distribution with mu = 0
m2 = meanBootstrap(X, 100) # 100 bootsrap samples
print('The samples means: ', m2)
print("Mean estimate:", np.mean(m2))

# now lets conduct a bootstrapping on the car data
m = meanBootstrap(accidents, 10000)
print("Mean estimate:", np.mean(m))

fig, ax = plt.subplots(1,1, figsize = (12, 3))
plt.ylabel('Frequency')
plt.xlabel('Sample mean value')
plt.hist(m, bins = 50, density = True)
ax.axvline(x = np.mean(m), ymin = 0.0, ymax = 1.0, color = 'red')
plt.show()

# lets apply the Bootstrapping method for obtaining the median
#  
def medBootstrap(X, nbtstrp):
    import numpy as np
    x = [0] * nbtstrp
    for i in range(nbtstrp):
        sample = [X[_] for _ in np.random.randint(len(X), size = len(X))]
        x[i] = np.median(sample)
    return x
 
med = medBootstrap(accidents, 900)
print('Median estimate = ', np.mean(med))
fig, ax = plt.subplots(1, 1, figsize=(12, 3))
plt.hist(med, bins=5, density=True)
plt.ylabel('Frequency')
plt.xlabel('Sample median value')
ax.axvline(x = np.array(med).mean(), ymin = 0, ymax = 1.0, color = 'red')
plt.show()


# computation of the 95% confidence interval of the mean
# Confidence interval is a plausible range of values for the sample parameter 

# a. using the sample mean and standard deviation we will calculate the SE
# and the confidence interval of the mean
m = accidents.mean()
se = accidents.std()/math.sqrt(len(accidents))
# Assuming a normal distribution:
# 95% of the time our estimate will be within 1.96 standard errors 
# of the true mean of the distribution
CI = [m - se*1.96, m + se*1.96] 
print('Confidence interval:', CI)


# b. using bootstrap to compute the standard deviation of the
# sampling distribution of the sample mean.
m = meanBootstrap(accidents, 900)
btstrp_mean = np.mean(m)
btstrp_SE = np.std(m)
print('Mean btstrp estimate = ', btstrp_mean)
print('SE of the estimate = ', btstrp_SE)
btstrpCI = [np.percentile(m,2.5), np.percentile(m, 97.5)]
print('Confidence Interval (95%)', btstrpCI)
    












    