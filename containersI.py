# Author: Amy Jungmin Seo
# Practical 2
# Our sequence this practical will be:

# shift our coordinates into lists;
# do some analysis on our coordinates;


import random


y0 = random.randint(0,99)
x0 = random.randint(0,99)



agents = []
agents.append([y0,x0])



# do the same thing for y1 and x1

y1 = random.randint(0,99)
x1 = random.randint(0,99)

agents.append([y1,x1])

print(agents)

import operator    # Do this line at the top of the code.
print(max(agents, key=operator.itemgetter(1)))    # Do this line at the bottom.

import matplotlib.pyplot as plt

plt.ylim(0, 99)
plt.xlim(0, 99)
plt.scatter(agents[0][1],agents[0][0])
plt.scatter(agents[1][1],agents[1][0])
plt.show()