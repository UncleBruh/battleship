import tkinter as tk

class howtoplaee(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="black")
		self.main_frame.pack(expand=True)

		self.frame_howToPlay = tk.Frame(self.main_frame, width=self.config.side, height=3*self.config.side//8, bg="black")
		self.frame_howToPlay.pack(side="top", fill="x")

		self.label_howToPlay = tk.Label(self.frame_howToPlay, text="How to Play", font=("Arial", 30, "bold"), bg="orange", fg="black")
		self.label_howToPlay.pack(side="top", anchor="nw", pady=5)

		self.scroll_howToPlay = tk.Scrollbar(self.frame_howToPlay)
		self.scroll_howToPlay.pack(side="right", fill="y")

		self.text_howToPlay = tk.Text(self.frame_howToPlay, width=100, height=13, font=("Arial", 14), bg="orange")
		self.howToPlay = """just find the cooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooords"""
		self.text_howToPlay.insert(tk.END, self.howToPlay)
		self.text_howToPlay.pack(pady=5)

		self.text_howToPlay.configure(yscrollcommand=self.scroll_howToPlay.set)
		self.scroll_howToPlay.configure(command=self.text_howToPlay.yview)

		self.button_return = tk.Button(self.main_frame, text="return",font=("Arial",18), command=lambda:self.game.change_frame('login'))
		self.button_return.pack(side="bottom", anchor="se", pady=5)