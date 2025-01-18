import random
from config import *
from .sortable_class import Sortable
from modules import file_handler as fh, match_result_engine as mre



class Controller:
	def __init__(self):
		self.loaded_sortables : list[Sortable] = []
		self.current_collection : str = None
		self.information :str = "# controller initialized"


	def set_collection(self, collection_name:str):
		self.current_collection = collection_name
		self.loaded_sortables : list[Sortable] = []
		self.information :str = f"The {collection_name} collection was selected"
	

	def load_collection(self):
		self.loaded_sortables = fh.load(self.current_collection)
		self.information :str = f"Loaded {len(self.loaded_sortables)} elements"
	

	def save_collection(self):
		fh.save(self.current_collection,self.loaded_sortables)
	

	def pick_random(self, number:int) -> list[Sortable]:
		return random.sample(self.loaded_sortables,number)
	

	def resolve_match(self, winners:list[Sortable], losers:list[Sortable]):
		mre.resolve_match(winners,losers)