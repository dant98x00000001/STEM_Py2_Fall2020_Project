"""
File defining a few different "dice"

Import the random package
See
https://docs.python.org/3/library/random.html
for more information

Created on Mon Nov 30 14:23:47 2020

@author: schkorf1
"""

import random as rnd
import numpy  as np

#%% Die version 1
def diev1():
    # Generate a random number U(0,1)
    rv=rnd.random()
    # Check to see if it's in the first interval
    if rv<=1./6.:
        dieVal=1
    # Check to see if it's in the next interval
    elif rv<=2./6.:
        dieVal=2
    elif rv<=3./6.:
        dieVal=3
    elif rv<=4./6.:
        dieVal=4
    elif rv<=5./6.:
        dieVal=5    
    else:
        dieVal=6
        
    # Return the die value
    return dieVal


#%% Die version 2
def diev2(cum_weights):
    # Generate a random number U(0,1)
    rv=rnd.random()
    # Initialize iVal
    iVal=1
    # Loop over each cumulative weight
    for cutoff in cum_weights:
        # If the rv is <= the threshold
        if rv<=cutoff:
            # Then return iVal
            return iVal
        # Otherwise, Increment iVal
        else:
            iVal += 1


#%% Die Version 3
def diev3(cum_weights):
    # Create a numpy array
    cum_weights=np.array(cum_weights)
    
    # Generate a random number U(0,1)
    rv=rnd.random()
    
    return np.sum(rv>cum_weights)+1