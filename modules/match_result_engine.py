import numpy as np
from config import *
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