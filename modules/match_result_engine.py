import numpy as np
from config import *
from .sortable_class import Sortable

CORRECTION = np.log(EXPECTANCY_BASE)/STANDARD_GAP

def resolve_duel(winner:Sortable,loser:Sortable, is_draw:bool):
	
	winner_pertinence = _pertinence(winner.doubt)
	loser_pertinence = _pertinence(loser.doubt)

	winner_expectancy = _expectancy(winner.score, loser.score, loser_pertinence)
	loser_expectancy = _expectancy(loser.score, winner.score, winner_pertinence)

	if is_draw:
		winner_score_points = round(winner.doubt*loser_pertinence*(0.5 - winner_expectancy))
		loser_score_points = round(loser.doubt*winner_pertinence*(0.5 - loser_expectancy))
	else:
		winner_score_points = round(winner.doubt*loser_pertinence*(1-winner_expectancy))
		loser_score_points = round(loser.doubt*winner_pertinence*(0-loser_expectancy))
	
	winner.update_score(winner_score_points)
	# winner.update_doubt()

	loser.update_score(loser_score_points)
	# loser.update_doubt()


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