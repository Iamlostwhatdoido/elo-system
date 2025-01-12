import numpy as np

class item:
    def __init__(self, name, score,deviation):
        self.name = name
        self.score = score
        self.deviation = deviation


def grader(deviation,D):
    return 1/np.sqrt(1+99*(deviation/D)**2)

def duel2(item1:item,item2:item,comparison):
    D = 400
    BASE = 9
    Q = np.log(BASE)/D
    PRECISE = 10

    grader = lambda x : 1/np.sqrt(1+3*(Q*x/np.pi)**2)

    G1 = grader(item1.deviation)
    G2 = grader(item2.deviation)

    E1 = 1/(1+np.power(BASE,G2*(item2.score - item1.score)/D))
    E2 = 1/(1+np.power(BASE,G1*(item1.score - item2.score)/D))

    D1 = G2*abs(item2.score - item1.score)
    D2 = G1*abs(item2.score - item1.score)

    S1 = comparison(item1.name,item2.name)
    S2 = 1 - S1
    
    item1.score += round(item1.deviation*G2*(S1-E1))
    item2.score += round(item2.deviation*G1*(S2-E2))

    item1.deviation = round(((PRECISE-G2)/PRECISE)*item1.deviation*(1-abs(S1-E1)) + abs(S1-E1)*np.sqrt(item1.deviation**2+G2*D1**2))
    item2.deviation = round(((PRECISE-G1)/PRECISE)*item2.deviation*(1-abs(S2-E2)) + abs(S2-E2)*np.sqrt(item2.deviation**2+G1*D2**2))



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
    
