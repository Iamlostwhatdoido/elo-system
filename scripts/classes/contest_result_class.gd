class_name ContestResult extends Resource

@export var result: float
@export var opponent_score: int
@export var relevancy: float

func _init(input_score:int, input_doubt: int, input_result: float) -> void:
	opponent_score = input_score
	relevancy = GlickoBrain.compute_relevancy(input_doubt)
	result = input_result
