class Sortable:
	def __init__(self, name:str, score:int, doubt:int, image_path:str=""):
		self.name = name
		self.score = score
		self.doubt = doubt
		self.image_path = image_path

	def print(self,show_image_path:bool=False):
		if not show_image_path:
			print(f"{self.name} [{self.score} ~{self.doubt}] ")
		else:
			print(f"{self.name} [{self.score} ~{self.doubt}]  ({self.image_path})")

	def rename(self, new_name:str):
		self.name = new_name
	
	def update_score(self, variation:int):
		self.score += variation
	
	def update_doubt(self, variation:int):
		self.doubt += variation

if __name__ == "__main__":
	pass