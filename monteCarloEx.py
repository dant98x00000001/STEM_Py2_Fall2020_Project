"""
File with a simple Monte Carlo example


Created on Tue Dec  1 14:46:57 2020

@author: schkorf1
"""

# This line will import the three dice functions I wrote in dice.py
from dice import *
# Import other useful stuff
import numpy as np
import matplotlib.pyplot as plt
import time
import random as rnd


#%% Check to see that the dice are working
# Select the number of trials
nTrials=100000

# Initialize result arrays (preallocate for speed)
die1Vals=np.zeros(nTrials)
die2Vals=np.zeros(nTrials)
die3Vals=np.zeros(nTrials)
die4Vals=np.zeros(nTrials)

# Define the cumulative weitght list
my_cum_weights=[1./6.,2./6.,3./6.,4./6.,5./6.,6./6.]


# Roll each die many times and make sure the distributions are uniform
#%% Roll diev1
# Capture the start time
tic = time.perf_counter()
# Roll die nTrials times
for ii in range(nTrials):
    die1Vals[ii]=diev1()

# Capture the finish time
toc = time.perf_counter()
# Print the total time
print(f"Simulation took {toc - tic:0.4f} seconds")


#%% Roll diev2
tic = time.perf_counter()
for ii in range(nTrials):
    die2Vals[ii]=diev2(my_cum_weights)

toc = time.perf_counter()
print(f"Simulation took {toc - tic:0.4f} seconds")


#%% Roll diev3
tic = time.perf_counter()
for ii in range(nTrials):
    die3Vals[ii]=diev3(my_cum_weights)

toc = time.perf_counter()
print(f"Simulation took {toc - tic:0.4f} seconds")


#%% Try the choices function from the random module
tic = time.perf_counter()
die4Vals=rnd.choices([1,2,3,4,5,6],cum_weights=my_cum_weights,k=nTrials)
toc = time.perf_counter()
print(f"Simulation took {toc - tic:0.4f} seconds")


#%% Plot all the results
# All the plots should show pretty uniform results if the cumulative weights
# were uniform
plt.figure()
plt.hist(die1Vals)
plt.figure()
plt.hist(die2Vals)
plt.figure()
plt.hist(die3Vals)
plt.figure()
plt.hist(die4Vals)
# Use plt.close('all') to close all figure windows at once


#%% Monte Carlo Example: Distribution of sum of n rolls

# Specify number of trials
nTrials=100000
# Specify number of rolls in each trial
nRolls=3

# Initialize storage arrays
sumVals=np.zeros(nTrials)
tmpVals=np.zeros(nRolls)

# Capture start time
tic = time.perf_counter()

# Monte Carlo Trial Loop
# Loop over each trial
for ii in range(nTrials):
    # Roll a die nRolls times and store the result of each roll in tmpVals
    for jj in range(nRolls):
        tmpVals[jj]=diev2(my_cum_weights)
    
    # Sum the results of nRolls and store that result in sumVals
    sumVals[ii]=sum(tmpVals)

# Capture finish time
toc = time.perf_counter()
# Print simulation time
print(f"Simulation took {toc - tic:0.4f} seconds")

# Plot a historgram of sumVals
plt.figure()
# The second argument of hist defines the bin edges, including the left edge
# of the first bin and the right edge of the last bin. See documentation for
# more information, https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.hist.html
plt.hist(sumVals,range(nRolls,6*nRolls+2))







