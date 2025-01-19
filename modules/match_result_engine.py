import numpy as np
from config import *
from .sortable_class import Sortable

CORRECTION = np.log(EXPECTANCY_BASE)/STANDARD_GAP


def resolve_match(winner_list:list[Sortable],loser_list:list[Sortable],verbose=False) -> list[Sortable]:
	for winner in winner_list:
		opponents = []
		results = []

		for opponent in loser_list:
			opponents.append(opponent)
			results.append(1)
			
		for opponent in winner_list:
			if opponent == winner : continue
			opponents.append(opponent)
			results.append(0.5)

		_duel_calculation(winner,opponents,results,verbose)
		if verbose:
			winner.display()
	
	for loser in loser_list:
		opponents = []
		results = []
		
		for opponent in loser_list:
			if opponent == loser : continue
			opponents.append(opponent)
			results.append(0.5)

		for opponent in winner_list:
			opponents.append(opponent)
			results.append(0)

		_duel_calculation(loser,opponents,results,verbose)
		if verbose:
			loser.display()
	
	for winner in winner_list:
		winner.update()
	for loser in loser_list:
		loser.update()


def _duel_calculation(subject:Sortable,opponents:list[Sortable], results:list[float],verbose=False):

	if verbose:
		print(f'\n\nSubject = {subject.name}')

	match_surprise = 0
	match_informativity = 0
	for i, opponent in enumerate(opponents):
		opponent_pertinence = _pertinence(opponent.doubt)
		subject_expectancy = _expectancy(subject.score, opponent.score, opponent_pertinence)

		match_surprise += _surprise(subject_expectancy,results[i])
		match_informativity += (opponent_pertinence**2)*subject_expectancy*(1-subject_expectancy)
	
	match_informativity *= CORRECTION**2



	score_points = 0
	for i, opponent in enumerate(opponents):
		opponent_pertinence = _pertinence(opponent.doubt)
		subject_expectancy = _expectancy(subject.score, opponent.score, opponent_pertinence)

		score_points += opponent_pertinence * (results[i]-subject_expectancy)

		if verbose:
			print(f' - VS = {opponent.name} (result : {results[i]})')
			print(f'    pertin = {opponent_pertinence}')
			print(f'    expect = {subject_expectancy}')
			print(f'    score/dev = {score_points}')

	if verbose:
		print(f'\n Session result :')
		print(f'    surprise = {match_surprise}')
		print(f'    inform = {match_informativity}')

	new_doubt = _new_doubt(subject.doubt,match_surprise,match_informativity)
	score_points *= new_doubt
	doubt_points = new_doubt - subject.doubt

	subject.score_modification += round(score_points)
	subject.doubt_modification += round(doubt_points)


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


def _surprise(expectancy,result):
	if abs(result-expectancy) < 0.25:
		return 0
	else:
		return ((abs(result-expectancy) - 0.25) / 0.75)**2


def _new_doubt(doubt,match_surprise,match_informativity):
	out_squared = doubt**2
	out_squared += SURPRISE_FACTOR*match_surprise
	out_squared = 1/ (1/out_squared + match_informativity)
	return np.sqrt(out_squared) 
