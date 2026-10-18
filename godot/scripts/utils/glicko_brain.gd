class_name GlickoBrain extends Node

static func compute_doubt_since_last_update(subject: Sortable) -> int:
	if subject.last_updated == "":
		return subject.doubt
	
	var time_then: int 
	time_then = Time.get_unix_time_from_datetime_string(subject.last_updated)
	
	var seconds_elapsed: float = Time.get_unix_time_from_system() - time_then
	var days_elapsed := seconds_elapsed/float(60*60*24)
	
	var new_doubt = sqrt(subject.doubt**2 + Config.TIME_COEF*days_elapsed)
	new_doubt = clamp(roundi(new_doubt), Config.MIN_DOUBT, Config.MAX_DOUBT)
	
	return new_doubt

static func compute_tournament_result(subject: Sortable) -> void:
	var contest_array : Array[ContestResult] = subject.contest_history
	
	var partial_score_sum: float = 0
	var partial_dsquared_sum: float = 0
	
	for contest in contest_array:
		var expected_result: float = _compute_expected_result(subject, contest)
		
		partial_score_sum += contest.relevancy*(contest.result-expected_result)
		partial_dsquared_sum += (contest.relevancy**2) \
				*expected_result*(1-expected_result)
	
	var dsquared: float = 1/((Config.CORRECTION**2)*partial_dsquared_sum)
	
	var score_coef: float = Config.CORRECTION/(1/float(subject.doubt**2)+1/dsquared)
	
	subject.score = subject.score + roundi(score_coef*partial_score_sum)
	subject.doubt = roundi((1/float(subject.doubt**2)+1/dsquared)**(-0.5))

static func compute_relevancy(doubt: int) -> float:
	return (1 + 3*(Config.CORRECTION*doubt/PI)**2)**(-0.5)

static func _compute_expected_result(subject: Sortable, contest: ContestResult) -> float:
	var score_gap: int = subject.score - contest.opponent_score
	var expectancy_power: float = -contest.relevancy*score_gap/Config.STANDARD_GAP
	
	return 1/(1+Config.EXPECTANCY_BASE**(expectancy_power))


#
#
#func _compute_period_Dsquared(subject: Sortable,
		#opponent_array: Array[Sortable]) -> float:
	#var sum: float = 0
	#
	#for opponent in opponent_array:
		#var expected_result: float = _compute_expected_result(subject, opponent)
		#var relevancy: float = compute_relevancy(opponent.doubt)
		#sum += (relevancy**2)*expected_result*(1-expected_result)
	#
	#var Dsquared: float = 1/((Config.CORRECTION**2)*sum)
	#
	#return Dsquared
