from sortable_class import Sortable
import os


if not os.path.exists('./data'):
    print(f"file_handler n'as pas trouvé de /data dans le projet")
elif not os.path.exists('./data/unknown.png'):
	print(f"file_handler n'as pas trouvé de unknown.png dans /data")

def generate_missing_png(collection:str):
	collection_path = "./data/"+ collection
	if not os.path.exists(collection_path):
		print(f"/{collection} introuvable dans /data")
	if not os.path.exists(collection_path+"/save.tsv"):
		print(f"save.tsv introuvable dans /{collection}")
	if not os.path.exists(collection_path+"/image"):
		print(f"/image introuvable dans /{collection}")
	
	with open(collection_path+"/save.tsv","r") as file:
		name_list = []
		for line in file.readlines()[1:]:
			line_content_list = line.strip().split("\t")
			name_list.append(line_content_list[0])
	
	for name in name_list:
		if not os.path.exists(collection_path+"/image/"+name+".png"):
			os.system("cp ./data/unknown.png "+"'"+collection_path+"/image/"+name+".png'")


def load(collection:str) -> list[Sortable]:
	collection_path = "./data/"+ collection
	if not os.path.exists(collection_path+"/save.tsv"):
		print(f"'{collection}/save.tsv' introuvable dans /data")
	
	with open(collection_path+"/save.tsv","r") as file:
		
		
		sortable_list=[]
		for line in file.readlines()[1:]:
			line_content_list = line.strip().split("\t")
			new_sortable = Sortable(
				line_content_list[0],
				line_content_list[1],
				line_content_list[2],
			)
			sortable_list.append(new_sortable)

	return sortable_list



if __name__ == "__main__":
	generate_missing_png("test")