# Author: Amy Jungmin Seo
# Practical 3

# This practical we're going to use control flow statements to rework our code 
# to remove all the repeats. While we do so, we'll also increase the number of 
# agents we can locate, and sort out an issue with boundaries we skipped over 
# last time.


 
num_of_agents = 10
num_of_iterations = 100
agents = []

import random

for i in range(num_of_agents):
        
        agents.append([random.randint(0,100),random.randint(0,100)])

for j in range(num_of_iterations): 

    for i in range(num_of_agents):
    
        if random.random() < 0.5:
         
            agents[i][0] = (agents[i][0] + 1) % 100
            
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            


        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
            
            
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
            
            
    dist = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
    print(dist)
    

    import matplotlib.pyplot as plt
    
    plt.ylim(0, 99)
    plt.xlim(0, 99)
    plt.scatter(agents[i][1],agents[i][0])
    plt.show()
    
     
    
        
# End -----------------------------------------------------------------------