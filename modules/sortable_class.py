class Sortable:
	def __init__(self, name:str, score:int, doubt:int):
		self.name = name
		self.score = score
		self.doubt = doubt
		
	def rename(self, new_name:str):
		self.name = new_name
	
	def update_score(self, variation:int):
		self.score += variation
	
	def update_doubt(self, variation:int):
		self.doubt += variation