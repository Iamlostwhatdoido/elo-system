import numpy as np
from config import *
from .sortable_class import Sortable

CORRECTION = np.log(EXPECTANCY_BASE)/STANDARD_GAP

def resolve_duel(subject:Sortable,opponent:Sortable, result:float) -> Sortable:
	print(f"\n!MATCH")
	subject.print()
	print(f"VS")
	opponent.print()
	print(f"result : {result}")

	opponent_pertinence = _pertinence(opponent.doubt)
	print(f" - opp. pert : {opponent_pertinence}")

	subject_expectancy = _expectancy(subject.score, opponent.score, opponent_pertinence)
	print(f" - win exp : {subject_expectancy}")

	score_points = round(subject.doubt * opponent_pertinence * (result-subject_expectancy))
	print(f" - scored points : {score_points}")

	new_score = subject.score + score_points
	new_doubt = subject.doubt

	return Sortable(subject.name,new_score,new_doubt,subject.image_path)


def resolve_match(winner_list:list[Sortable],loser_list:list[Sortable]) -> list[Sortable]:
	total_len = len(winner_list)+len(loser_list) - 1

	winner_result = (len(loser_list) + 0.5 * (len(winner_list)-1) )/total_len
	loser_result = 0.5 * (len(loser_list)-1) / total_len

	print(winner_result)
	print(loser_result)

	outlist = []
	for winner in winner_list:
		average_list = loser_list + [sortable for sortable in winner_list if sortable != winner]
		outlist.append(resolve_duel(winner,_average(average_list),winner_result))
	for loser in loser_list:
		average_list = winner_list + [sortable for sortable in loser_list if sortable != loser]
		outlist.append(resolve_duel(loser,_average(average_list),loser_result))
	return outlist

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