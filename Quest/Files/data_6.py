from data_5 import *
#from data_3 import *
from data_4 import *
from Home import *
from Shop import *
import Beer as beer
import Training_camp as TC
import Researching_city as RC

import random




class Neighbour():
	def __init__(self):
		pass



class GameLocations():
	""" useful game function """
	def __init__(self, name):
		self.name = name



	def choose_loc(self, l_char, gf):
		start_work = 0
		if l_char.loc == 0:
			for i in range(len(l_char.work_finish)):
				g = l_char.work_finish[i]
				if g == 1:
					start_work = 1
			if start_work != 1:
				print("Вы находитесь в городе Кастомаки.")
				print("Выберите - куда отправиться:")
				print("1 - Домой (Начать сюжетное задание)")
				print("2 - На рынок")
				print("3 - В бар")
				print("4 - К соседу")
				print("5 - В учебный лагерь")
				print("6 - Исследовать город")
				print("7 - Выход")
				ch = gf.player_ask_selection("", 1, 7)
			else:
				print("Вы находитесь в городе Кастомаки.")
				print("Выберите - куда отправиться:")
				print("1 - Домой")
				print("2 - На рынок")
				print("3 - В бар")
				print("4 - К соседу")
				print("5 - В учебный лагерь")
				print("6 - Исследовать город")
				print("7 - Выход")
				ch = gf.player_ask_selection("", 1, 7)

			if ch == 1:
				l_char.loc_town = 1
				#shop_loc1.player_enter(l_char);

				if start_work != 1:
					return_funk_mission(l_char, gf)
				else:
					for i in range(len(l_char.buildings)):
						g = l_char.buildings[i]

						if g.code == 0 and g.loc == l_char.loc:
							g.home_enter(l_char, gf)
							break
						else:
							print("У вас нет дома в этом городе!")
							gf.enter()
							break
			elif ch == 2:
				l_char.loc_town = 2
				shop_loc2 = Shop("The shop (loc 2)");
				gf.fill_shop_loc2(shop_loc2)

				#shop_loc2.player_enter(l_char);

				shop_loc_2(l_char, gf, shop_loc2)
				self.choose_loc(l_char, gf)
			elif ch == 3:
				l_char.loc_town = 3
				beer.Beer().beer_enter(l_char, gf)
			elif ch == 4:
				l_char.loc_town = 4
				print('Хозяина не оказалось дома, вы ушли')
				gf.enter()
			elif ch == 5:
				l_char.loc_town = 5
				TC.Training_camp().start_training(l_char, gf)
			elif ch == 6:
				l_char.loc_town = 6
				RC.Kastomaki().start_researching(l_char, gf)

