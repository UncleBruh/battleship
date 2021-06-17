import tkinter as tk

class youwin(tk.Frame):

	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="orange")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.battleship_title = tk.Label(self, text="YOU WIN !", font=("Times New Roman", 50), bg="orange", fg="Blue")
		self.battleship_title.pack(pady=40)
		

		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="orange")
		self.main_frame.pack(expand=True)

		self.button_play = tk.Button(self.main_frame, text="Preview", font=("Arial", 18), command=lambda:self.game.change_frame("board"))
		self.button_play.pack(pady=5)

		self.button_restarts = tk.Button(self.main_frame, text=" Restart the Board ",font=("Arial",18), command=lambda:self.game.create_board())
		self.button_restarts.pack(pady=5, anchor="n")

		self.button_exit = tk.Button(self.main_frame, text="Exit", font=("Arial", 18), command=lambda:self.game.exit())
		self.button_exit.pack(pady=5)