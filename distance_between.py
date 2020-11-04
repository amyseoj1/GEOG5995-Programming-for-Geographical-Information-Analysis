# Author: Amy Jungmin Seo
# Practical 4 

# This practical, we're going to build some functions into our system. 
# First, though, let's review the code we have so we're all roughly in the 
# same place. Here's a version of the code that should (broadly) match what 
# you have.


def distance_between(agents_row_a, agents_row_b):
    
    answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
    print(answer)