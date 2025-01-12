import numpy as np


def duel2(item1,item2,comparison):
    K = 50
    D = 400

    E = 1/(1+np.power(10,(item1[1] - item2[1])/D))

    result = comparison(item1[0],item2[0])

    diff = round(K*(result-E))

    item1[1] -= diff
    item2[1] += diff


def update_random(array,fights_number,comparison,team_number=1):
    for i in range(fights_number):
        choices = np.random.choice(range(len(array)),2,replace=False)

        duel2(array[choices[0]],array[choices[1]],comparison)
        
    return array

def update_specific(array,specific_rank,fights_number,comparison):

    opponents = list(range(len(array)))
    opponents.pop(specific_rank)

    for i in range(fights_number):
        opponent = np.random.choice(opponents)

        duel2(array[specific_rank],array[opponent],comparison)
    
    return array
    
