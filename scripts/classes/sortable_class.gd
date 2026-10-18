class_name Sortable extends Resource

@export var name: String
@export var score: int
@export var doubt: int
@export var last_updated: String
@export var description: String
@export var image_buffer: PackedByteArray

var in_combat := false:
	set(new_value):
		print("in_combat of ", name, " switched to ", new_value)
		in_combat = new_value
		if in_combat:
			print("Cleared history, new doubt")
			contest_history = []
			doubt = GlickoBrain.compute_doubt_since_last_update(self)
		else:
			print("compute history, update last_updated")
			GlickoBrain.compute_tournament_result(self)
			last_updated = Time.get_datetime_string_from_system(false, true)

var image_texture: ImageTexture = null
var contest_history: Array[ContestResult]


func _init(parameters: Dictionary = {}) -> void:
	name = parameters.get("name","Unnamed")
	score = parameters.get("score",Config.DEFAULT_SCORE)
	doubt = parameters.get("doubt",Config.MAX_DOUBT)
	last_updated = parameters.get("last_updated","")
	description = parameters.get("description","")
	image_buffer = parameters.get("image_buffer",Config.DEFAULT_IMAGE_BUFFER)


func fight(opponent: Sortable, result: float) -> void:
	if not in_combat:
		print("Self not in combat ! attempting correction")
		self.in_combat = true
	if not opponent.in_combat:
		print("Opponent not in combat ! attempting correction")
		opponent.in_combat = true
	
	var self_contest_result := ContestResult.new(
			opponent.score,
			opponent.doubt,
			result,
	)
	contest_history.append(self_contest_result)
	
	var opponent_contest_result := ContestResult.new(
			score,
			doubt,
			1.0-result,
	)
	opponent.contest_history.append(opponent_contest_result)


func get_texture() -> ImageTexture:
	if not image_texture:
		var temp_image = Image.new()
		temp_image.load_png_from_buffer(image_buffer)
		image_texture = ImageTexture.create_from_image(temp_image)
	
	return image_texture


func export_line(separator: String = "\t", with_description: bool = false) -> String:
	var output_array = [name, score, doubt, last_updated]
	if with_description:
		output_array.append(description)
	
	return separator.join(output_array)

func print_in_console() -> void:
	print("%s : %s (%s)" % [name, score, doubt])
	print("Last updated : %s" % last_updated)
	print("'"+description+"'")
