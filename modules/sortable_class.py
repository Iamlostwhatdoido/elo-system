class Sortable:
	def __init__(self, name:str, score:int, doubt:int, image_path:str):
		self.name = name
		self.score = score
		self.score_modification = 0
		self.doubt = doubt
		self.doubt_modification = 0
		self.image_path = image_path

	def update(self):
		self.score += self.score_modification
		self.score_modification = 0
		self.doubt += self.doubt_modification
		self.doubt_modification = 0

	def display(self,show_image_path:bool=False):
		if not show_image_path:
			print(f"{self.name} [{self.score} {self.score_modification:+}] ~{self.doubt} {self.doubt_modification:+}")
		else:
			print(f"{self.name} [{self.score} ~{self.doubt}]  ({self.image_path})")
	