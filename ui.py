from modules.controller import Controller
import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = Controller()

        self.title("Elo Calculator")
        self.geometry("800x600")

        self.winner_entry = tk.Entry(self)
        self.loser_entry = tk.Entry(self)
        self.relevance_entry = tk.Entry(self)

        self.submit_button = tk.Button(self, text="Ajouter Match", command=self.submit_match)

        self.message_label = tk.Label(self, text="", fg="red")

        # Placement des widgets
        self.winner_entry.pack()
        self.loser_entry.pack()
        self.relevance_entry.pack()
        self.submit_button.pack()
        self.message_label.pack()

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
