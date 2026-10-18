extends Node2D

@export var displayed: Sortable

func _init(sortable: Sortable = Sortable.new()) -> void:
	displayed = sortable

func _ready() -> void:
	update_visual()


func update_visual() -> void:
	$Panel/TextureRect.texture = displayed.get_texture()
