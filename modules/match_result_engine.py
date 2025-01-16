import numpy as np
from config import *
from .sortable_class import Sortable

CORRECTION = np.log(EXPECTANCY_BASE)/STANDARD_GAP

def resolve_duel(subject:Sortable,opponent:Sortable, result:float) -> Sortable:
	
	opponent_pertinence = _pertinence(opponent.doubt)
	subject_expectancy = _expectancy(subject.score, opponent.score, opponent_pertinence)
	
	score_points = round(subject.doubt * opponent_pertinence * (result-subject_expectancy))

	new_score = subject.score + score_points
	new_doubt = subject.doubt

	return Sortable(subject.name,new_score,new_doubt,subject.image_path)


def resolve_match(winner_list:list[Sortable],loser_list:list[Sortable]):
	for winner in winner_list:
		resolve_duel(winner,_average(loser_list))
	for loser in loser_list:
		resolve_duel(loser,_average(winner_list))


def _pertinence(doubt:int) -> float:
	return 1/np.sqrt(
		1 + 3*( CORRECTION*doubt/np.pi )**2
		)


def _expectancy(subject_score:int, opponent_score:int,opponent_pertinence:float) -> float:
	return 1 / (
		1 + 
		np.power(
			EXPECTANCY_BASE,
			opponent_pertinence * (opponent_score - subject_score) / STANDARD_GAP
			)
		)


def _average(sortable_list:list[Sortable])->Sortable:
	average_score = 0
	average_doubt = 0
	for sortable in sortable_list:
		average_score += sortable.score
		average_doubt += sortable.doubt**2
	average_score = average_score/len(sortable_list)
	average_doubt = np.sqrt(average_doubt/len(sortable_list))

	return Sortable("average",round(average_score),round(average_doubt),None)