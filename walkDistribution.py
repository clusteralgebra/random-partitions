
import random
import numpy as np
import math
import matplotlib.pyplot as plt

def randInt(n):
    return random.randint(0, n)

def push(partition):
    l = len(partition)
    if l == 0:
        return [1]
    while(True):
        i = randInt(l)
        if (i == l):
            partition.append(1)
            return partition
        if (i == 0 or partition[i-1] > partition[i]):
            partition[i] += 1
            return partition
def recursive_gen(N):
    if N == 1:
        return [1]
    prev = gen(N-1)
    l = len(prev)
    temp = True
    while(True):
        i = randInt(l)
        if (i == l):
            prev.append(1)
            return prev
        if (i == 0 or prev[i-1] > prev[i]):
            prev[i] += 1
            return prev
        
def gen(N):
    ans = []
    for i in range(N):
        ans = push(ans)
    return ans

def draw(N):
    y = (1/math.sqrt(N)) * np.array(gen(N))
    x = (1/math.sqrt(N)) * np.arange(1,len(y)+1)
    plt.scatter(x, y, s=0.1, color='blue', marker='o', label='Scatter')
    #plt.plot(x, y, color='green', linestyle='-', marker='o', label='Line')

    # Add titles and labels
    plt.title('Random Partitions L^1 Plancherel')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.gca().set_aspect('equal', adjustable='box')
    # Add a legend
    plt.legend()

    # Display the plot
    plt.show()



print(draw(5000000))


                        
        


