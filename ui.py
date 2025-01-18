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

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)

		self.openInputMenu()

		## For Test
		self.controller.set_collection("test")
		self.controller.load_collection()
		self.test_sortable = self.controller.pick_random(1)[0]

		self.openSetupMenu()

		## tests end


	def openInputMenu(self):
		menu = InputMenu(
			master=self,
			can_cancel = (self.controller.current_collection != None))
		menu.grid(row=0, column=0, sticky="nsew")

	
	def openSetupMenu(self):
		menu = SetupMenu(master=self)
		menu.grid(row=0, column=0, sticky="nsew")


	def openMatchMenu(self):
		pass


class InputMenu(customtkinter.CTkFrame):
	def __init__(self, master:Window, can_cancel:bool=True, **kwargs):
		super().__init__(master, fg_color='transparent', **kwargs)

		self.grid_columnconfigure((0, 2), weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(2, weight=2)

		frame = customtkinter.CTkFrame(self)
		frame.grid(row=1, column=1, padx=0, pady=0)

		self.input_entry = customtkinter.CTkEntry(frame, placeholder_text="Enter Collection's name", width=200)
		self.input_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

		load_button = customtkinter.CTkButton(frame, text="Select", width=95,command=self.load_event)

		if can_cancel:
			load_button.grid(row=1, column=0, padx=(10,5), pady=(0,10))
			cancel_button = customtkinter.CTkButton(frame, text="Cancel", width=95,command=self.cancel_event)
			cancel_button.grid(row=1, column=1, padx=(5,10), pady=(0,10))
		else:
			load_button.configure(width=200)
			load_button.grid(row=1, column=0, padx=10, pady=(0,10), columnspan=2)
		

	def load_event(self):
		new_collection = self.input_entry.get()
		if new_collection != "":
			self.master.controller.clear_loaded()
			self.master.controller.set_collection(new_collection)
			self.master.controller.load_collection()
			self.master.openSetupMenu()
	

	def cancel_event(self):
		self.master.openSetupMenu()


class SetupMenu(customtkinter.CTkFrame):
	def __init__(self, master:Window, **kwargs):
		super().__init__(master, fg_color='transparent', **kwargs)

		self.grid_columnconfigure((0, 2), weight=1)
		self.grid_rowconfigure(1, weight=1)
		self.grid_rowconfigure(3, weight=2)

		header_frame = customtkinter.CTkFrame(self)
		header_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=3)

		header_frame.grid_columnconfigure((0, 4), weight=1)

		title_label = customtkinter.CTkLabel(
			header_frame,
			text=master.controller.current_collection,
			justify="center",
			font=("",36))
		title_label.grid(row=0, column=1, padx = 20, pady = (30,20), columnspan=3)

		self.info_label = customtkinter.CTkLabel(
			header_frame,
			text=master.controller.information,
			font=("",16))
		self.info_label.grid(row=1, column=1, columnspan=3)
		
		change_button = customtkinter.CTkButton(header_frame, text="Change", width=80,command=self.change_event)
		change_button.grid(row=2, column=1, padx=10, pady=(10,20))

		reload_button = customtkinter.CTkButton(header_frame, text="Reload", width=80,command=self.reload_event)
		reload_button.grid(row=2, column=2, padx=0, pady=(10,20))

		save_button = customtkinter.CTkButton(header_frame, text="Save", width=80,command=self.save_event)
		save_button.grid(row=2, column=3, padx=10, pady=(10,20))

		main_frame = customtkinter.CTkFrame(self,height=100,width=200)
		main_frame.grid(row=2, column=1)

	def change_event(self):
		self.master.openInputMenu()

	def reload_event(self):
		self.master.controller.load_collection()
		self.info_label.configure(text=self.master.controller.information)

	def save_event(self):
		self.master.controller.save_collection()
		self.info_label.configure(text=self.master.controller.information)


		
		


class MatchMenu(customtkinter.CTkFrame):
	def __init__(self, master:Window, **kwargs):
		super().__init__(master, fg_color='transparent', **kwargs)
	

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