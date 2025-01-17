from config import *
from modules.controller import Controller
from modules.sortable_class import Sortable

from PIL import ImageTk,Image
import customtkinter



class Window(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		self.controller = Controller()

		self.title("Elo Calculator")
		self.geometry("800x600")

		self.controller.set_collection("test")
		self.controller.load_collection()
		test_sortable = self.controller.pick_random(1)[0]

		button = self.create_sortable_button(test_sortable, False)
		button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")


		my_image = customtkinter.CTkImage(light_image=Image.open(test_sortable.image_path),
                                  size=(300, 300))
		image_label = customtkinter.CTkLabel(self, image=my_image, text="")
		image_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

	def button_callback(self):
		print("button clicked")


	def create_sortable_button(self, sortable:Sortable, toggle:bool):
		my_image = customtkinter.CTkImage(light_image=Image.open(sortable.image_path),
                                  size=(30, 30))
		
		button = customtkinter.CTkButton(self, text=sortable.name, image = my_image, compound=customtkinter.TOP, command=self.button_callback)
		return button


	def submit_match(self):
		winner = self.winner_entry.get()
		loser = self.loser_entry.get()
		try:
			relevance = float(self.relevance_entry.get())
		except ValueError:
			self.display_error("Relevance must be a number.")
			return

		self.controller.add_match(winner, loser, relevance)



def start_ui():
	window = Window()
	window.mainloop()
