import numpy as np

from config import *

if __name__ == "__main__":
	from sortable_class import Sortable
else:
	from .sortable_class import Sortable


def resolve_match(winner_list:list[Sortable],loser_list:list[Sortable]):
	pass

def _average(sortable_list:list[Sortable])->Sortable:
	average_score = 0
	average_doubt = 0
	for sortable in sortable_list:
		average_score += sortable.score
		average_doubt += sortable.doubt^2
	average_score = average_score/len(sortable_list)
	average_doubt = np.sqrt(average_doubt/len(sortable_list))

	return Sortable("average",average_score,average_doubt,None)


if __name__ == "__main__":
	strong_precise = Sortable("Strong & Precise",500,50,None)
	strong_unclear = Sortable("Strong & Unclear",500,400,None)
	weak_precise = Sortable("Weak & Precise",-500,50,None)
	weak_unclear = Sortable("Weak & Unclear",-500,400,None)

	_average([strong_precise,strong_unclear]).print()