# Author: Amy Jungmin Seo
# Practical 5 agentframework 
# Goal: To start this process, make yourself a blank agentframework.py file
# in the same directory as your model.py. Open it up in Spyder, and define 
# inside it an Agent class, with an __init__ method. Don't forget that all 
# object methods have to have a parameter label to assign to the object when 
# it is sent in; usually called self.

import random
import operator
import matplotlib.pyplot

class Agent(): 
    def __init__(self):
      self.x = random.randint(0,99)
      self.y = random.randint(0,99)

# Next, make a move() method within the Agent class (remember not to make it 
# inside __init__: it needs to be its own method).
      
    def move(self):
        if random.randint(0,1) < 0.5:
            self.x = self.x + 1
        else: 
            self.x = self.x - 1
            
        if random.randint(0,1) < 0.5:
            self.y = self.y + 1
        else: 
            self.y = self.y - 1
                

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
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


matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
        

