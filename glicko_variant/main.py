import glicko_system as glk
import comparison as cpr


with open("glicko_variant/previous_rank.txt","r") as file:
    rank_input=[]
    for line in file.read().splitlines():
        content = line.split("\t")
        rank_input.append(glk.item(content[0],int(content[1]),int(content[2])))


def update_rank(fights,specific = None):

    if specific != None:
        new_order = glk.update_specific(rank_input,specific,fights,cpr.compare2)
    else:
        new_order = glk.update_random(rank_input,fights,cpr.compare2)

    with open('glicko_variant/updated_rank.txt', 'w') as outfile:
        outfile.write('\n'.join(e.name+'\t'+str(e.score)+'\t'+str(e.deviation) for e in new_order))

update_rank(50,35)
