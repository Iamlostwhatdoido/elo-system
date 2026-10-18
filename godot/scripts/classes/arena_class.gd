class_name Arena extends Resource

@export var name : String
@export var contenders: Dictionary[String,Sortable]


func add_one_sortable(new_sortable: Sortable) -> void:
	if new_sortable.name in contenders:
		print("%s is already in this arena !" % new_sortable.name)
	else:
		contenders[new_sortable.name] = new_sortable
		#print("Successfully added %s to the arena." % sortable.name)


func append_sortable(input: Variant) -> void:
	if input is Sortable:
		add_one_sortable(input)
	elif input is Array[Sortable]:
		for sortable in input:
			add_one_sortable(sortable)
	else:
		print("Tried to append a %s to an Arena" % type_string(typeof(input)))


func divide_in_pools(_method: int) -> Array[BattlePool]:
	return []


func export_tsv(export_path: String) -> void:
	var file := FileAccess.open(export_path,FileAccess.WRITE)
	var output := []
	for sortable: Sortable in contenders.values():
		output.append(sortable.export_line("\t",false))
	file.store_string("\n".join(output))
