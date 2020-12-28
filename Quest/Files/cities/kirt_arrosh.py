import random
import os

from ElixirItem import *
from Enemy import *

from Shop import *
from data_5 import *

from Home import *
import Quests as quests

from cities import nircing



class KirtArrosh():
	def __init__(self):
		self.a = None

	def play_menu(self, l_char, gf):
		l_char.loc_town = 0
		l_char.loc = "Кирт'Аррош"

		while True:
			print("Вы находитесь в игровом меню города Кирт'Аррош:")
			print("1 - Выбрать локацию")
			print("2 - Посмотреть текущие миссии")
			print("3 - Сохранение")
			print("4 - Информация по персонажу")
			print("5 - Взаимодействовать с предметами из инвентаря.")
			print('6 - Выбрать город, куда отправиться.')
			print("7 - Выход из игры")

			ch = gf.player_ask_selection("", 1, 7)

			if ch == 1:
				self.choose_loc(l_char, gf)
				gf.enter()
			elif ch == 2:
				print("Ваши текущие миссии - " + ', '.join(l_char.work))
			elif ch == 3:
				gf.save_st(l_char)
			elif ch == 4:
				gf.get_player_info(l_char)
				gf.enter()
			elif ch == 5:
				gf.work_inventory(l_char, gf)
			elif ch == 6:
				if self.choose_city(l_char, gf):
					return
				else: continue
			elif ch == 7:
				gf.update(l_char)
				exit()


	def choose_city(self, l_char, gf):
		print('Выберите город, куда хотите отправиться:')
		print('1 - Кастомаки')
		print('2 - Нирсинг')
		print('3 - не отправляться')

		if ch == 1:
			l_char.loc = 0
			return True
		elif ch == 2:
			nircing.Nircing().play_menu(l_char, gf)
			return True
		else: return False

	def choose_loc(self, l_char, gf):
		pass
		# TODO !