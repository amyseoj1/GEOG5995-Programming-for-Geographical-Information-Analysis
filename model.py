# Author: Amy Seo
# Practical 5: copy this into your model.py file.


import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework


num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20 # Practical 7: Communication 

f = open("/Users/appleseo/Downloads/GEOG5995/GEOG5995-Programming-for-Geographical-Information-Analysis/in.txt")


environment = []
rowlist = [] 
for line in f:
  
    value = str.split(line,",")


    for num in value:
        rowlist.append(float(num))
    environment.append(rowlist)
print(rowlist)
print(environment)

agents = []

# Make the agents.
for i in range(num_of_agents):  
    #agents.append(agentframework.Agent())
    agents.append(agentframework.Agent(environment,agents, neighbourhood))
    


# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# Plot 

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)

# Animation figure

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True	

def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0]  = (agents[i][0] + 1) % 99 
        else:
            agents[i][0]  = (agents[i][0] - 1) % 99
        
        if random.random() < 0.5:
            agents[i][1]  = (agents[i][1] + 1) % 99 
        else:
            agents[i][1]  = (agents[i][1] - 1) % 99 
        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        #print(agents[i][0],agents[i][1])

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
















# Plot agents moving
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.imshow(environment)

# Animation/Behaviour

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

