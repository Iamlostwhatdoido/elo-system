from PIL import Image,ImageTk

class Sortable:
	def __init__(self, name:str, score:int, doubt:int, image_path:str=""):
		self.name = name
		self.score = score
		self.doubt = doubt
		self.image_path = image_path
		self.image = self.load_image(image_path) if image_path != "" else None
	
	def load_image(image_path:str) -> ImageTk:
		try:
			image = Image.open(image_path)
			return ImageTk.PhotoImage(image)
		except Exception as e:
			print(f"Erreur de chargement de l'image : {e}")
			return None

	def print(self):
		print(f"{self.name} [{self.score} ~{self.doubt}]")

	def rename(self, new_name:str):
		self.name = new_name
	
	def update_score(self, variation:int):
		self.score += variation
	
	def update_doubt(self, variation:int):
		self.doubt += variation

if __name__ == "__main__":
	sortable = Sortable("Lol",15,10)

	sortable.print()
	print(sortable.image_path)