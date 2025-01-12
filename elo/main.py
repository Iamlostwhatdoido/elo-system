import elo_system as elo
import comparison as cpr


with open("elo/previous_rank.txt","r") as file:
    rank_input = [e.split("\t") for e in file.read().splitlines()]

for e in rank_input:
    e[1] = int(e[1])

def update_rank(fights,specific = None):

    if specific != None:
        new_order = elo.update_specific(rank_input,specific,fights,cpr.compare2)
    else:
        new_order = elo.update_random(rank_input,fights,cpr.compare2)

    with open('elo/updated_rank.txt', 'w') as outfile:
        outfile.write('\n'.join(e[0]+'\t'+str(e[1]) for e in new_order))

update_rank(20,0)
