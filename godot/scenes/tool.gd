extends Node2D

var test_arena := Arena.new()

func _ready() -> void:
	test_arena.name = "TestArena"
	
	var pokemons = FileManager.load_from_images("D:/[02] Code/03 Sandbox/temp/glicko-sorter/Collection")
	
	test_arena.add_sortable(pokemons)
	test_arena.start_tournament()
	
	
	set_random_poke()

func set_random_poke() -> void:
	$Right.displayed = test_arena.contenders.values().pick_random()
	$Right.update_visual()
	$Left.displayed = test_arena.contenders.values().pick_random()
	$Left.update_visual()


func _on_left_button_pressed() -> void:
	$Left.displayed.fight($Right.displayed,1.0)
	$Left.displayed.in_combat = false
	$Right.displayed.in_combat = false
	set_random_poke()



func _on_right_button_pressed() -> void:
	$Right.displayed.fight($Left.displayed,1.0)
	set_random_poke()



func _on_middle_button_pressed() -> void:
	$Right.displayed.fight($Left.displayed,0.5)
	set_random_poke()


func _on_save_button_pressed() -> void:
	test_arena.end_tournament()
	test_arena.export_tsv("D:/[02] Code/03 Sandbox/temp/glicko-sorter/test.tsv")
	test_arena.start_tournament()
