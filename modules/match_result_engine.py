import numpy as np
from config import *
from .sortable_class import Sortable

CORRECTION = np.log(EXPECTANCY_BASE)/STANDARD_GAP


def resolve_match(winner_list:list[Sortable],loser_list:list[Sortable]) -> list[Sortable]:
	for winner in winner_list:
		for opponent in loser_list:
			_duel_calculation(winner,opponent,1)
		for opponent in winner_list:
			if opponent == winner : continue
			_duel_calculation(winner,opponent,0.5)
	
	for loser in loser_list:
		for opponent in loser_list:
			if opponent == loser : continue
			_duel_calculation(loser,opponent,0.5)
		for opponent in winner_list:
			_duel_calculation(loser,opponent,0)
	
	for winner in winner_list:
		winner.update()
	for loser in loser_list:
		loser.update()


def _duel_calculation(subject:Sortable,opponent:Sortable, result:float):
	opponent_pertinence = _pertinence(opponent.doubt)
	subject_expectancy = _expectancy(subject.score, opponent.score, opponent_pertinence)
	score_points = round(subject.doubt * opponent_pertinence * (result-subject_expectancy))
	subject.score_modification += score_points


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

