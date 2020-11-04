# Author: Amy Jungmin Seo
# Practical 4 using function of Pythagorian code

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
            
            
   
    

    import matplotlib.pyplot as plt
    
    plt.ylim(0, 99)
    plt.xlim(0, 99)
    plt.scatter(agents[i][1],agents[i][0])
    plt.show()
    
    distance_between(agents[i][0], agents[i][1])
