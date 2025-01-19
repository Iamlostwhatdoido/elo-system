from config import *
from modules.controller import Controller
from modules.sortable_class import Sortable

from numpy import sqrt as np_sqrt
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


	def openInputMenu(self):
		menu = InputMenu(
			master=self,
			can_cancel = (self.controller.current_collection != None))
		menu.grid(row=0, column=0, sticky="nsew")

	
	def openSetupMenu(self):
		menu = SetupMenu(master=self)
		menu.grid(row=0, column=0, sticky="nsew")


	def openMatchMenu(self):
		menu = MatchMenu(master=self, contestants=self.controller.pick_sortables())
		menu.grid(row=0, column=0, sticky="nsew")


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
		
		change_button = customtkinter.CTkButton(header_frame, text="Change", width=80, command=self.change_event)
		change_button.grid(row=2, column=1, padx=10, pady=(10,20))

		reload_button = customtkinter.CTkButton(header_frame, text="Reload", width=80, command=self.reload_event)
		reload_button.grid(row=2, column=2, padx=0, pady=(10,20))

		save_button = customtkinter.CTkButton(header_frame, text="Save", width=80, command=self.save_event)
		save_button.grid(row=2, column=3, padx=10, pady=(10,20))

		main_frame = customtkinter.CTkFrame(self,height=100,width=200)
		main_frame.grid(row=2, column=1)

		mode_droplist = customtkinter.CTkComboBox(main_frame, width=150,
											values=master.controller.mode_list,
											variable=master.controller.current_mode,
											command=self.mode_choice_event)
		mode_droplist.grid(row=0,column=0, padx=10, pady=10)

		size_droplist = customtkinter.CTkComboBox(main_frame, width=150, 
											values=master.controller.size_list,
											variable=master.controller.current_size,
											command=self.size_choice_event)
		size_droplist.grid(row=1,column=0, padx=10, pady=(0,10))

		start_button = customtkinter.CTkButton(main_frame, text="Start", width=150, command=self.start_match)
		start_button.grid(row=2, column=0, padx=10, pady=(0,10))

	def change_event(self):
		self.master.openInputMenu()

	def reload_event(self):
		self.master.controller.load_collection()
		self.info_label.configure(text=self.master.controller.information)

	def save_event(self):
		self.master.controller.save_collection()
		self.info_label.configure(text=self.master.controller.information)
	
	def mode_choice_event(self,choice):
		self.master.controller.update_mode(choice)
	
	def size_choice_event(self,choice):
		self.master.controller.update_size(choice)
	
	def start_match(self):
		self.master.openMatchMenu()


class MatchMenu(customtkinter.CTkFrame):
	def __init__(self, master:Window, contestants : list[Sortable], **kwargs):
		super().__init__(master, fg_color='transparent', **kwargs)

		self.contestants = contestants
		self.columnconfigure(0,weight=1)
		self.rowconfigure(1,weight=1)

		participants_number = len(contestants)
		row_number = int(np_sqrt(participants_number))
		columns_number = int(participants_number/row_number)
		self.winner_list = [False]*participants_number

		image_size = int(320/max(row_number*1.5,columns_number))

		header_frame = customtkinter.CTkFrame(self, fg_color='transparent')
		header_frame.grid(row=0, column=0, sticky="nsew")
		header_frame.columnconfigure(0,weight=1)

		save_button = customtkinter.CTkButton(header_frame, text="Save", width=60, command=self.save_event)
		save_button.grid(row=0, column=1, padx=5, pady=10)

		stop_button = customtkinter.CTkButton(header_frame, text="Stop", width=60, command=self.stop_event)
		stop_button.grid(row=0, column=2, padx=5, pady=10)

		
		match_frame = customtkinter.CTkFrame(self, fg_color='transparent')
		match_frame.grid(row=1, column=0, sticky="nsew")
		match_frame.grid_columnconfigure((0, columns_number+1), weight=1)
		match_frame.grid_rowconfigure(0, weight=1)
		match_frame.grid_rowconfigure(row_number+1, weight=2)

		for row in range(row_number):
			for column in range(columns_number):
				index = column + row*row_number
				sortable_button = SortableButton(match_frame,index,self.contestants[index],image_size)
				sortable_button.grid(row=row+1, column=column+1)
		
		submit_button = customtkinter.CTkButton(self, text="Submit", width=60, command=self.submit_event)
		submit_button.grid(row=2, column=0, padx=5, pady=(20,50))

	
	def save_event(self):
		self.master.controller.save_collection()

	def stop_event(self):
		self.master.openSetupMenu()
	
	def toggle_index(self, index:int):
		self.winner_list[index] = not self.winner_list[index]

	def submit_event(self):
		winners = []
		losers = []
		for i, contestant in enumerate(self.contestants):
			if self.winner_list[i]:
				winners.append(contestant)
			else:
				losers.append(contestant)
		self.master.controller.resolve_match(winners,losers)
		self.master.openMatchMenu()


class SortableButton(customtkinter.CTkFrame):
	def __init__(self, master, associated_index:int, associated_sortable : Sortable, image_size:int, **kwargs):
		super().__init__(master, fg_color='transparent', **kwargs)

		self.index = associated_index
		self.button_toggled = False
		display_image = customtkinter.CTkImage(light_image=Image.open(associated_sortable.image_path),
								  size=(image_size, image_size))
		self.button = customtkinter.CTkButton(
			self,
			width=10,
			text=associated_sortable.name, 
			image = display_image, compound=customtkinter.TOP, 
			command=self.button_event,
			border_spacing=10,
			fg_color="#2b2b2b",
			hover_color="#4f4f4f",
			text_color="#ffffff")
		self.button.grid(row=0, column=0, padx = int(image_size/4), pady=int(image_size/8))

	def button_event(self):
		self.master.master.toggle_index(self.index)
		self.button_toggled = not self.button_toggled
		if self.button_toggled:
			self.button.configure(
				fg_color="#1c822f",
				hover_color="#17a63e")
			
		else:
			self.button.configure(
				fg_color="#2b2b2b",
				hover_color="#4f4f4f")