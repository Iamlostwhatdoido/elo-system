from config import *

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
		self.doubt = min(max(self.doubt + self.doubt_modification,MINIMUM_DOUBT),DEFAULT_DOUBT)
		self.doubt_modification = 0

	def display(self,show_image_path:bool=False):
		print(f"{self.name} [{self.score} {self.score_modification:+}] ~{self.doubt} {self.doubt_modification:+} ",end="")
		if show_image_path :
			print(f"({self.image_path})")
		else:
			print("")
	