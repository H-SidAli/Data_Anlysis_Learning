# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # creating the numpy array 
# # if the obtained number is 6 we roll the dice again 
# def sum_of_steps():
#     dice = np.empty(0)
#     for i in range(100):
#         rand = np.random.randint(1,7)
#         if rand == 6:
#             rand = np.random.randint(1,7)
#         elif (rand == 1 or rand == 2 ):
#             rand = -1 
#         else:
#             rand = 1 
#         dice = np.append(dice, rand, axis=None)
#     print(dice)
#     return np.sum(dice)

# def simulation(n_times):
#     won = 0 
#     for i in range(n_times):
#         sum = sum_of_steps()
#         if sum >= 60:
#             won = won + 1 
    
#     probability = round((won / n_times), 2)
#     return probability

# print(sum_of_steps())

import numpy as np
import matplotlib.pyplot as plt

# Creating the numpy array
# If the obtained number is 6 we roll the dice again
def sum_of_steps():
    dice = [0]
    for i in range(100):
        rand = np.random.randint(1, 7)
        if rand == 6:
            rand = np.random.randint(1, 7)
        elif rand == 1 or rand == 2:
            rand = -1
        else:
            rand = 1
        rand = rand + dice[-1]
        if rand < 0:
            rand = 0
        if np.random.rand() <= 0.005:
            rand = 0 
        
        dice.append(rand)
    return dice

def simulation(n_times):
    won = 0
    walks = []
    for i in range(n_times):
        sum_list = sum_of_steps()
        total_steps = sum_list[-1]
        walks.append(sum_list)
        if total_steps >= 60:
            won = won + 1

    probability = round((won / n_times), 2)
    
    np_arr = np.array(walks)
    plt.plot(np_arr.T)
    plt.show()
    return probability

print(simulation(1000))

