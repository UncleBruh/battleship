import tkinter as tk
import sys

from config import Config
from game_statistic import Game_Statistic
from ship import Ship
from player import Player
from board import Board
from loginpage import login
from howtoplaylmao import howtoplaee
from restart import youwin


class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config
		self.ship = Game.ship

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_board()
		self.create_howtoplaylmao()
		self.create_restart()
		self.create_loginpage()

	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_loginpage(self):
		self.pages["login"] = login(self.container, self)

	def create_howtoplaylmao(self):
		self.pages['howtoplaee'] = howtoplaee(self.container, self)

	def create_restart(self):
		self.pages['youwin'] = youwin(self.container, self)

	def change_frame(self, page):
		page = self.pages[page]
		page.tkraise()



	def exit(self):
		sys.exit()

class Battleship:

	def __init__(self):
		self.config = Config()
		self.game_statistic = Game_Statistic()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			return True	
		return False

	def button_clicked(self, pos_x, pos_y):
		#print(pos_x, pos_y)
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages['board'].change_img_button(pos_x, pos_y, win)
		if win:
			print("You Win!!!")
			#self.window.destroy()
			self.window.change_frame("youwin")


	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()