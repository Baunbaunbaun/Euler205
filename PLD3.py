
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


# In[9]:

# answer to Euler problem 205

# Colins 6 dice of 6 sides
die_Colin = {1,2,3,4,5,6}; # sides of the die
die_c = 6 # nr sides
amount_Colin = 6
# nr of possibilities is 46656
posi_Colin = len(die_Colin)**amount_Colin
# list of zeroes
posi_sums_Colin = np.zeros(37)

# Peters 9 dice of 4 sides
die_Peter = {1,2,3,4}; # sides of the die
die_p = 4 # nr sides
amount_Peter = 9
# nr of possibilities is 262144
posi_Peter = len(die_Peter)**amount_Peter
# list of zeroes
posi_sums_Peter = np.zeros(37)

# amount of all possible combinations
posi_all = posi_Colin*posi_Peter

# get all possible dice results
for d1 in die_Colin:
    for d2 in die_Colin:
        for d3 in die_Colin:
            for d4 in die_Colin:
                for d5 in die_Colin:
                    for d6 in die_Colin:
                        index = d1+d2+d3+d4+d5+d6
                        posi_sums_Colin[index] += 1 

# get all possible dice results
for d1 in die_Peter:
    for d2 in die_Peter:
        for d3 in die_Peter:
            for d4 in die_Peter:
                for d5 in die_Peter:
                    for d6 in die_Peter:
                        for d7 in die_Peter:
                            for d8 in die_Peter:
                                for d9 in die_Peter:
                                    index = d1+d2+d3+d4+d5+d6+d7+d8+d9
                                    posi_sums_Peter[index] += 1    
        
count = 0
# x is Colins roll from 6 to 36
for x in np.arange(die_c,37):
    count += np.sum(posi_sums_Peter[x+1:37])*posi_sums_Colin[x]

print("\nThe probability that Peter wins over Colin is %1.7f" % (1-(count/posi_all)))

