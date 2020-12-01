# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:46:57 2020

@author: schkorf1
"""

'''
Simple Monte Carlo Example

'''

from dice import *
import numpy as np
import matplotlib.pyplot as plt
import time
import random as rnd

# Check to see that the dice are working
# Roll each one many times and make sure the distributions are uniform

nTrials=100000

die1Vals=np.zeros(nTrials)
die2Vals=np.zeros(nTrials)
die3Vals=np.zeros(nTrials)
die4Vals=np.zeros(nTrials)

my_cum_weights=[1./6.,2./6.,3./6.,4./6.,5./6.,6./6.]


#%%
tic = time.perf_counter()
for ii in range(nTrials):
    die1Vals[ii]=diev1()

toc = time.perf_counter()
print(f"Simulation took {toc - tic:0.4f} seconds")


#%%
tic = time.perf_counter()
for ii in range(nTrials):
    die2Vals[ii]=diev2(my_cum_weights)

toc = time.perf_counter()
print(f"Simulation took {toc - tic:0.4f} seconds")


#%%
tic = time.perf_counter()
for ii in range(nTrials):
    die3Vals[ii]=diev3(my_cum_weights)

toc = time.perf_counter()
print(f"Simulation took {toc - tic:0.4f} seconds")


#%%
tic = time.perf_counter()
die4Vals=rnd.choices([1,2,3,4,5,6],cum_weights=my_cum_weights,k=nTrials)
toc = time.perf_counter()
print(f"Simulation took {toc - tic:0.4f} seconds")


#%%

plt.figure()
plt.hist(die1Vals)
plt.figure()
plt.hist(die2Vals)
plt.figure()
plt.hist(die3Vals)
plt.figure()
plt.hist(die4Vals)



#%% Distribution of sum of n rolls

nTrials=100000
nRolls=3

sumVals=np.zeros(nTrials)
tmpVals=np.zeros(nRolls)

tic = time.perf_counter()
# MC Trial Loop
for ii in range(nTrials):
    # Roll loop
    for jj in range(nRolls):
        tmpVals[jj]=diev2(my_cum_weights)
        
    #print(tmpVals)
    sumVals[ii]=sum(tmpVals)

toc = time.perf_counter()
print(f"Simulation took {toc - tic:0.4f} seconds")


plt.figure()
plt.hist(sumVals,range(nRolls,6*nRolls+2))







