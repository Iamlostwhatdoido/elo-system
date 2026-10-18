class_name FileManager extends Node


static func save_arena(arena: Arena) -> void:
	ResourceSaver.save(arena, Config.SAVE_PATH+arena.name+".res")

static func load_arena(arena_name: String) -> Arena:
	return ResourceLoader.load(Config.SAVE_PATH+arena_name+".res")


static func create_buffer_from_image(image_path) -> PackedByteArray:
	var image := Image.load_from_file(image_path)
	return image.save_png_to_buffer()



static func load_sortables_from_tsv(file_path: String) -> Array[Sortable]:
	var file := FileAccess.open(file_path,FileAccess.READ)
	
	if not file:
		return []
	
	var sortable_list: Array[Sortable] = []
	
	while !file.eof_reached():
		var line: PackedStringArray = file.get_line().split("\t")
		
		if line.size() == 1:
			break
		
		var new_sortable_param := {
			"name" = line[0],
			"score" = int(line[1]),
			"doubt" = int(line[2]),
		}
		
		sortable_list.append(Sortable.new(new_sortable_param))
	
	file.close()
	
	return sortable_list

static func load_from_images(dir_path: String) -> Array[Sortable]:
	var dir := DirAccess.open(dir_path)
	if dir == null:
		push_error("Impossible d'ouvrir le répertoire : " + dir_path)
		return []
	
	var sortables: Array[Sortable] = []
	dir.list_dir_begin()
	var file_name: String = dir.get_next()
	
	
	while file_name != "":
		if file_name.get_extension() not in ["png","jpg","jpeg"]:
			file_name = dir.get_next()
			continue
		
		var file_path := dir_path + "/" + file_name
		var image := Image.load_from_file(file_path)
		if image != null:
			var param : Dictionary = {
				"name" : file_name.get_basename(),
				"image_buffer" : image.save_png_to_buffer(),
			}
			sortables.append(Sortable.new(param))
		file_name = dir.get_next()
	
	return sortables

static func deposit_sortable_images(
			_sortables: Array[Sortable],
			_deposit_path: String,
	) -> void:
		pass
