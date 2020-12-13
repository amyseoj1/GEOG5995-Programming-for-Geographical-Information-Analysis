
# Author: Amy Seo 

# Agent Based Model Framework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
            
            

class Agent():
    def __init__(self, environment, agents, neighbourhood):
        self.environment = environment
        self.agents = agents
        self.neigbourhood= neighbourhood
        self.store = 0 # We'll come to this in a second.
    
    

def eat(self): # can you make it eat what is left?
    if self.environment[self.y][self.x] > 10:
       self.environment[self.y][self.x] -= 10
       self.store += 10
       
       
       
def move(self):
        if random.randint(0,1) < 0.5:
            self.x = self.x + 1
        else: 
            self.x = self.x - 1
            
        if random.randint(0,1) < 0.5:
            self.y = self.y + 1
        else: 
            self.y = self.y - 1
                    
# build our share_with_neighbours(neighbourhood) method in Agent.            

def share_with_neighbours(self, neighbourhood):
    for agent in self.agents:
        if agent==self: 
        
            distance = self.distance_between(agent)
            
        if distance <= neighourhood: 
            sum = self.store + agent.store
            average = int(sum/2)
            self.store = average
            agent.store = average
