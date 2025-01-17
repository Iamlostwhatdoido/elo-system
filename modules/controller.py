from config import *
from .sortable_class import Sortable
from modules import file_handler as fh, match_result_engine as mre



class Controller:
	def __init__(self):
		self.loaded_sortables : list[Sortable] = []
		self.current_collection : str = None

