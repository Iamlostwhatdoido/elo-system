from config import *
from modules.controller import Controller
from modules.sortable_class import Sortable

from PIL import ImageTk,Image
import customtkinter


def start_ui():
	window = Window()
	window.mainloop()


class Window(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		self.controller = Controller()
		self.title("Elo Calculator")
		self.geometry("800x600")
		self.grid_columnconfigure((0, 1, 2), weight=1)


		self.controller.set_collection("test")
		self.controller.load_collection()
		self.test_sortable = self.controller.pick_random(1)[0]

		self.collection_frame = CollectionFrame(master=self)
		self.collection_frame.grid(row=0, column=0, padx=0, pady=0, sticky="ew", columnspan=3)


	def button_callback(self):
		print("button clicked")
		self.big_image_label.grid_forget()


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


class CollectionFrame(customtkinter.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, fg_color='transparent', **kwargs)
		self.grid_columnconfigure(0, weight=1)


		self.input_frame = customtkinter.CTkFrame(master=self,height=300)
		self.input_frame.grid_columnconfigure((0,4), weight=1)

		self.input_entry = customtkinter.CTkEntry(self.input_frame, placeholder_text="Enter Collection's name", width=200)
		self.input_entry.grid(row=0, column=1, padx=10, pady=20)
		self.load_button = customtkinter.CTkButton(self.input_frame, text="Load", width=80,command=self.load_event)
		self.load_button.grid(row=0, column=2, padx=10, pady=20)
		self.cancel_button = customtkinter.CTkButton(self.input_frame, text="Cancel", width=80,command=self.cancel_event)
		self.cancel_button.grid(row=0, column=3, padx=0, pady=20)
		
		self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


		self.header_frame = customtkinter.CTkFrame(master=self,height=300)
		self.header_frame.grid_columnconfigure(0, weight=1)

		self.collection_label = customtkinter.CTkLabel(self.header_frame, text="None", justify="center", font=("",36))
		self.collection_label.grid(row=0, column=0, padx=10, pady=(20,0))
		self.info_label = customtkinter.CTkLabel(self.header_frame, text="Found 5678 items", justify="center", font=("",16))
		self.info_label.grid(row=1, column=0, padx=10, pady=(10,0))
		self.change_button = customtkinter.CTkButton(self.header_frame, text="Change", width=80,command=self.change_event)
		self.change_button.grid(row=2, column=0, padx=10, pady=(10,20))
		self.reload_button = customtkinter.CTkButton(self.header_frame, text="Reload", width=80,command=self.load_event)
		self.reload_button.grid(row=2, column=0, padx=10, pady=(10,20))
		self.save_button = customtkinter.CTkButton(self.header_frame, text="Save", width=80,command=self.save_event)
		self.save_button.grid(row=2, column=0, padx=10, pady=(10,20))
		
		self.header_frame.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")
		self.header_frame.grid_forget()

	def cancel_event(self):
		pass
	
	def change_event(self):
		print(f"Simulated changing collection !")
	
	def load_event(self):
		self.collection_label.configure(text=self.input_entry.get())
		print(f"Simulated loading of {self.input_entry.get()} !")

	def save_event(self):
		pass

