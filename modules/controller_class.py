import random
import copy
from config import *
from .sortable_class import Sortable
from modules import file_handler as fh, match_result_engine as mre


class Controller:
	def __init__(self):

		self.default_size_list = STANDARD_CONTESTANTS_NUMBERS.keys()
		self.size_list = []
		self.mode_list = ['Random','Highest Doubt','Score Density']

		self.current_mode = self.mode_list[0]
		self.current_size = 0
		self.current_collection : str = None

		self.loaded_sortables : list[Sortable] = []
		self.information :str = "# controller initialized"

	def can_run(self) -> bool:
		return (self.current_mode in self.mode_list)*(self.current_size in self.size_list)*(self.loaded_sortables != [])

	def clear_loaded(self):
		self.loaded_sortables : list[Sortable] = []

	def set_collection(self, collection_name:str):
		self.current_collection = collection_name

	def load_collection(self):
		fh.generate_collection(self.current_collection)
		fh.add_untracked_png(self.current_collection)
		self.loaded_sortables = fh.load(self.current_collection)
		self.size_list=[]
		for e in self.default_size_list:
			if int(e) <= len(self.loaded_sortables):
				self.size_list.append(e)
		self.information :str = f"Loaded {len(self.loaded_sortables)} elements"
	
	def save_collection(self):
		# self.loaded_sortables.sort(key = lambda sortable : sortable.name,reverse=False)
		fh.save(self.current_collection,self.loaded_sortables)
		fh.generate_missing_png(self.current_collection)
		self.information :str = f"Saved {len(self.loaded_sortables)} elements"
	
	def update_mode(self, choice):
		self.current_mode = choice
	
	def update_size(self, choice):
		self.current_size = choice

	def pick_sortables(self) -> list[Sortable]:
		if self.current_mode == self.mode_list[0]:
			return random.sample(self.loaded_sortables,	int(self.current_size))
		
		elif self.current_mode == self.mode_list[1]:
			shuffled_list = copy.copy(self.loaded_sortables)
			random.shuffle(shuffled_list)
			
			shuffled_list.sort(key = lambda sortable : sortable.doubt,reverse=True)
			out = (	shuffled_list[ : round(int(self.current_size)/2) ] + 
		  			shuffled_list[    -int(int(self.current_size)/2) : ])
			
			random.shuffle(out)
			return out
		
		elif self.current_mode == self.mode_list[2]:

			sorted_list = copy.copy(self.loaded_sortables)
			sorted_list.sort(key = lambda sortable : sortable.score,reverse=True)
			index = 0
			minimum = sorted_list[0].score - sorted_list[-1].score
			for i in range(len(sorted_list)-int(self.current_size)+1):
				diff = sorted_list[i].score - sorted_list[i+int(self.current_size)-1].score
				if diff == 0:
					index = i
					break
				elif  diff < minimum:
					minimum = diff
					index = i
			return sorted_list[index:index+int(self.current_size)]

		else:
			print("unknown mode")
			return []
		
	

	def resolve_match(self, winners:list[Sortable], losers:list[Sortable]):
		mre.resolve_match(winners,losers,False)