import tkinter as tk 


class login(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)



		#CREATE MAIN FRAME
		self.battleship_title = tk.Label(self, text="BATTLESHIP", font=("Times New Roman", 50), bg="black", fg="Blue")
		self.battleship_title.pack(pady=40)
		

		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="black")
		self.main_frame.pack(expand=True)

		self.button_play = tk.Button(self.main_frame, text="   Play   ", font=("Arial", 18), command=lambda:self.game.change_frame('board'))
		self.button_play.pack(pady=5)

		self.button_howtoplaylmao = tk.Button(self.main_frame, text="  How to Play  ",font=("Arial",18), command=lambda:self.game.change_frame('howtoplaee'))
		self.button_howtoplaylmao.pack(pady=5, anchor="n")
		

		self.button_exit = tk.Button(self.main_frame, text="Exit", font=("Arial", 18), command=lambda:self.game.exit())
		self.button_exit.pack(pady=5)






		
	