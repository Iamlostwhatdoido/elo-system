from sortable_class import Sortable
import os


if not os.path.exists('./data'):
    print(f"Erreur : file_handler n'as pas trouvé de /data dans le projet")
elif not os.path.exists('./data/unknown.png'):
	print(f"Erreur : file_handler n'as pas trouvé de unknown.png dans /data")


def check_collection_validity(collection_path:str) -> int:
	if not os.path.exists(collection_path):
		print(f"Erreur : /{collection_path} introuvable")
		return 1
	elif not os.path.exists(collection_path+"/save.tsv"):
		print(f"Erreur : save.tsv introuvable dans /{collection_path}")
		return 2
	elif not os.path.exists(collection_path+"/image"):
		print(f"Erreur : /image introuvable dans /{collection_path}")
		return 3
	else:
		return 0


def generate_missing_png(collection:str):
	collection_path = "./data/"+ collection
	if check_collection_validity(collection_path) != 0:
		return
	
	
	with open(collection_path+"/save.tsv","r") as save_file:
		name_list = []
		for line in save_file.readlines()[1:]:
			line_content_list = line.strip().split("\t")
			name_list.append(line_content_list[0])
	
	for name in name_list:
		if not os.path.exists(collection_path+"/image/"+name+".png"):
			os.system("cp ./data/unknown.png "+"'"+collection_path+"/image/"+name+".png'")


def clear_untracked_png(collection:str):
	collection_path = "./data/"+ collection
	if check_collection_validity(collection_path) != 0:
		return

	with open(collection_path+"/save.tsv","r") as save_file:
		name_list = []
		for line in save_file.readlines()[1:]:
			line_content_list = line.strip().split("\t")
			name_list.append(line_content_list[0])
	
	file_list = os.listdir(collection_path+"/image")
	
	for file in file_list:
		if not file[:-4] in name_list:
			os.remove(collection_path+"/image/"+file)


def add_untracked_png(collection:str,default_score:int,default_doubt:int):
	collection_path = "./data/"+ collection
	if check_collection_validity(collection_path) != 0:
		return

	sortable_list = load(collection)
	name_list = []
	for sortable in sortable_list:
		name_list.append(sortable.name)
	
	file_list = os.listdir(collection_path+"/image")
	
	with open(collection_path+"/save.tsv","a") as save_file:
		for file in file_list:
			if not file[:-4] in name_list:
				save_file.write("\n"+file[:-4]+"\t"+str(default_score)+"\t"+str(default_doubt))


def generate_collection(collection:str,default_score:int,default_doubt:int):
	collection_path = "./data/"+ collection
	if not os.path.exists(collection_path):
		os.mkdir(collection_path)
	if not os.path.exists(collection_path+"/image"):
		os.mkdir(collection_path+"/image")
	if not os.path.exists(collection_path+"/save.tsv"):
		with open(collection_path+"/save.tsv", "w") as save_file:
			save_file.write("Name"+"\t"+"Score"+"\t"+"Doubt")

	add_untracked_png(collection,default_score,default_doubt)

def load(collection:str) -> list[Sortable]:
	collection_path = "./data/"+ collection
	if check_collection_validity(collection_path) != 0:
		return
	
	with open(collection_path+"/save.tsv","r") as save_file:
		sortable_list=[]
		for line in save_file.readlines()[1:]:
			line_content_list = line.strip().split("\t")
			new_sortable = Sortable(
				line_content_list[0],
				line_content_list[1],
				line_content_list[2],
			)
			sortable_list.append(new_sortable)

	return sortable_list


def save(collection:str,sortable_list:list[Sortable]):
	collection_path = "./data/"+ collection
	if check_collection_validity(collection_path) != 0:
		return
	
	with open(collection_path+"/save.tsv", "w") as save_file:
		save_file.write("Name"+"\t"+"Score"+"\t"+"Doubt"+"\n")
		save_file.write('\n'.join(e.name+'\t'+str(e.score)+'\t'+str(e.doubt) for e in sortable_list))





if __name__ == "__main__":
	generate_collection("test",0,400)