from config import *

if __name__ == "__main__":
	from sortable_class import Sortable
else:
	from .sortable_class import Sortable

import os


if not os.path.exists("."+DATA_PATH):
    print(f"Erreur : file_handler n'as pas trouvé {"."+DATA_PATH}")
elif not os.path.exists("."+DATA_PATH+UNKNOWN_FILE):
	print(f"Erreur : file_handler n'as pas trouvé {UNKNOWN_FILE}")


def check_collection_validity(collection_path:str) -> int:
	if not os.path.exists(collection_path):
		print(f"Erreur : {collection_path} introuvable")
		return 1
	elif not os.path.exists(collection_path+SAVE_FILE):
		print(f"Erreur : {SAVE_FILE} introuvable dans {collection_path}")
		return 2
	elif not os.path.exists(collection_path+IMAGE_PATH):
		print(f"Erreur : {IMAGE_PATH} introuvable dans {collection_path}")
		return 3
	else:
		return 0


def generate_missing_png(collection:str):
	collection_path = "."+DATA_PATH+"/"+collection
	if check_collection_validity(collection_path) != 0:
		return
	
	
	with open(collection_path+SAVE_FILE,"r") as save_file:
		name_list = []
		for line in save_file.readlines()[1:]:
			line_content_list = line.strip().split("\t")
			name_list.append(line_content_list[0])
	
	for name in name_list:
		if not os.path.exists(collection_path+IMAGE_PATH+"/"+name+".png"):
			os.system("cp "+"."+DATA_PATH+UNKNOWN_FILE+" '"+collection_path+IMAGE_PATH+"/"+name+".png'")


def clear_untracked_png(collection:str):
	collection_path = "."+DATA_PATH+"/"+collection
	if check_collection_validity(collection_path) != 0:
		return

	with open(collection_path+SAVE_FILE,"r") as save_file:
		name_list = []
		for line in save_file.readlines()[1:]:
			line_content_list = line.strip().split("\t")
			name_list.append(line_content_list[0])
	
	file_list = os.listdir(collection_path+IMAGE_PATH)
	
	for file in file_list:
		if not file[:-4] in name_list:
			os.remove(collection_path+IMAGE_PATH+"/"+file)


def add_untracked_png(collection:str):
	collection_path = "."+DATA_PATH+"/"+collection
	if check_collection_validity(collection_path) != 0:
		return

	sortable_list = load(collection)
	name_list = []
	for sortable in sortable_list:
		name_list.append(sortable.name)
	
	file_list = os.listdir(collection_path+IMAGE_PATH)
	
	with open(collection_path+SAVE_FILE,"a") as save_file:
		for file in file_list:
			if not file[:-4] in name_list:
				save_file.write("\n"+file[:-4]+"\t"+str(DEFAULT_SCORE)+"\t"+str(DEFAULT_DOUBT))


def generate_collection(collection:str):
	collection_path = "."+DATA_PATH+"/"+collection
	if not os.path.exists(collection_path):
		os.mkdir(collection_path)
	if not os.path.exists(collection_path+IMAGE_PATH):
		os.mkdir(collection_path+IMAGE_PATH)
	if not os.path.exists(collection_path+SAVE_FILE):
		with open(collection_path+SAVE_FILE, "w") as save_file:
			save_file.write("Name"+"\t"+"Score"+"\t"+"Doubt")

	add_untracked_png(collection)


def load(collection:str) -> list[Sortable]:
	collection_path = "."+DATA_PATH+"/"+collection
	if check_collection_validity(collection_path) != 0:
		return
	
	with open(collection_path+SAVE_FILE,"r") as save_file:
		sortable_list=[]
		for line in save_file.readlines()[1:]:
			line_content_list = line.strip().split("\t")
			new_sortable = Sortable(
				line_content_list[0],
				line_content_list[1],
				line_content_list[2],
				collection_path+IMAGE_PATH+"/"+line_content_list[0]+".png"
			)
			sortable_list.append(new_sortable)

	return sortable_list


def save(collection:str,sortable_list:list[Sortable]):
	collection_path = "."+DATA_PATH+"/"+collection
	if check_collection_validity(collection_path) != 0:
		return
	
	with open(collection_path+SAVE_FILE, "w") as save_file:
		save_file.write("Name"+"\t"+"Score"+"\t"+"Doubt"+"\n")
		save_file.write('\n'.join(e.name+'\t'+str(e.score)+'\t'+str(e.doubt) for e in sortable_list))





if __name__ == "__main__":
	test_list = load("test")

	for test in test_list:
		test.print(show_image_path=True)