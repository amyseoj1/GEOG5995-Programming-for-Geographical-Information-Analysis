# -*- coding: utf-8 -*-
# Author: Amy Jungmin Seo
# Practical 1
# Goals: 

# 1. builds a series of agents in space
# 2. each agent will have a list of the other agents so they can communicate;
# 3. each agent will know about the environment it is in and be able to query/change the environment;
# 4. agents will move around the environment eating it, but checking first that other agents aren't already in the neighbourhood;
#    the environment will contain data from a file;
# 5. we'll display the environment and other data after the model has run;
# 6. we'll be able to save the environment as results of the model.

# import random

import random

# Make a y variable.

y0 = 50


# Make a x variable.

x0 = 50


# Change y and x based on random numbers.


if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
    
if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    
    
print(y0, x0)
    
# Make a second set of y and xs, and make these change randomly as well.

if random.random() < 0.5:
    y1 = y0 + 1
else:
    y1 = y0 - 1
    
    
if random.random() < 0.5:
    x1 = x0 + 1
else:
    x1 = x0 - 1
    
print(y1,x1)


# Work out the distance between the two sets of y and xs.

# Assign p0 and p1

import math

p0 = [x0,y0]
p1 = [x1,y1]


distance = math.sqrt(((p0[0]-p1[0])**2)+((p0[1]-p1[1])**2))


print(distance)
