import random
from config import *
from .sortable_class import Sortable
from modules import file_handler as fh, match_result_engine as mre



class Controller:
	def __init__(self):

		self.size_list = [2,3,4,6,9,12,16,20]
		self.mode_list = ['Random','Highest Doubt']

		self.current_mode = self.mode_list[0]
		self.current_size = self.size_list[0]
		self.current_collection : str = None

		self.loaded_sortables : list[Sortable] = []
		self.information :str = "# controller initialized"


	def clear_loaded(self):
		self.loaded_sortables : list[Sortable] = []


	def set_collection(self, collection_name:str):
		self.current_collection = collection_name
	

	def load_collection(self):
		fh.generate_collection(self.current_collection)
		fh.add_untracked_png(self.current_collection)
		self.loaded_sortables = fh.load(self.current_collection)
		self.information :str = f"Loaded {len(self.loaded_sortables)} elements"
	

	def save_collection(self):
		fh.save(self.current_collection,self.loaded_sortables)
		fh.generate_missing_png(self.current_collection)
		self.information :str = f"Saved {len(self.loaded_sortables)} elements"
	

	def pick_sortables(self) -> list[Sortable]:
		if self.current_size > len(self.loaded_sortables):
			print("Error, not enough elements loaded")
			return []
		return random.sample(
			self.loaded_sortables,
			self.current_size)
	

	def resolve_match(self, winners:list[Sortable], losers:list[Sortable]):
		mre.resolve_match(winners,losers)