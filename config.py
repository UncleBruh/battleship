import json

class Config:

	def __init__(self):

		self.app_title = "Battleship"

		#GAME CONFIG
		self.row = 5
		self.column = 5

		#WINDOW CONFIG
		base = 125
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+500"




		#IMG BUTTON PATH
		self.init_img_btn = "img/init_img.png"
		self.final_img_btn = "img/final_img.png"
		self.win_img_btn = "img/win_img.png"


	def load_data(self):
		pass

	def save_data(self):
		pass



