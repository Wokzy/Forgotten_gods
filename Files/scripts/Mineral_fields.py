import random
import os
from datetime import datetime
from ElixirItem import Pick



class Ore():
	def __init__(self, name, mining_type, minimal_pick, recomended_pick, cost, information='None'):
		self.name = name
		self.mining_type = mining_type
		self.minimal_pick = minimal_pick
		self.recomended_pick = recomended_pick
		self.cost = cost
		self.information = information


class MineralFields():

	def __init__(self, l_char, gf):
		self.loc = l_char.loc
		self.located_fields = []

		if self.loc == "Кирт'Аррош":
			self.located_fields = [self.init_iron, self.init_rock, self.init_redstone]

	def start(self, l_char, gf):
		print('Добро пожаловать на рудники, здесь вы можете покупать/продавать/добывать различную руду.')
		while True:
			print('1 - Информация')
			print('2 - Зайти в управляющее здание')

			ch = gf.player_ask_selection('', 1, 2)

			if ch == 1:
				print('Налог за добытую руду - 5% от стоимости добытой руды.')
				print('Коммисия за продажу руды - 2% от всей стоимости')
				print('Стоимости  руд за 1 кг: ')
				for i in range(len(self.located_fields)):
					print(self.located_fields[i].name + ' - ' + str(self.located_fields[i].cost))
				gf.enter()
			elif ch == 2:
				print('Вы заходите в управляющее здание.')
				print('Информатор: Добрый день, вам помочь?')

				print('1 - Да.')
				print('2 - Нет, спасибо!')

				ch = gf.player_ask_selection('', 1, 2)

				if ch == 2:
					print('Информатор: Ну чтож, прощайте.')
					continue

				print('1 - Заказать кирку(и)')
				print('2 - Купить руду')
				print('3 - Продать руду')
				print('4 - Отправиться добывать')
				print('5 - Личное предприятие.')

				ch = gf.player_ask_selection('', 1, 5)

				if ch == 1:
					self.buy_pick(l_char, gf)
				elif ch == 2:
					self.buy_minerals(l_char, gf)
				elif ch == 3:
					self.sell_minerals(l_char, gf)
				elif ch == 4:
					self.mine_minerals(l_char, gf)
				elif ch == 5:
					self.own_company(l_char, gf)

		'''
		print('Вот, что вы пожете покупать/продавать/добывать:')
		print('')
		for i in range(len(self.located_fields)):
			print(str(i+1) + ' - ' + self.located_fields[i].name)

		ch = gf.player_ask_selection('', 1, len(self.located_fields))
		'''



	def buy_pick(self, l_char, gf):
		print('Здесь вы можете купить кирки:')
		print('1 - Деревянные кирки')
		print('2 - Каменные кирки')
		print('3 - Железные кирки')
		print('4 - Дробилки')
		print('5 - Кристаллические кирки')
		print('6 - Магические кирки')
		print('7 - Выход')

		ch = gf.player_ask_selection('', 1, 7)

		if ch == 1:
			gf.buy_tree_pick(l_char, gf)
		elif ch == 2:
			gf.buy_rock_pick(l_char, gf)
		elif ch == 3:
			gf.buy_iron_pick(l_char, gf)
		elif ch == 4:
			pass
		elif ch == 5:
			pass
		elif ch == 6:
			pass
		return


	def init_iron(self, l_char, gf):
		try:
			iron_cost = l_char.mining_list['iron']
		except KeyError:
			iron_cost = 3.6584
			l_char.mining_list['iron'] = iron_cost
		iron_info = "Железо, подвид - сталь, добывать достаточно сложно."
		ore = Ore('Железо', 'Kg', 'Каменная_кирка_++', 'Дробилка', iron_cost, iron_info)

		return ore

	def init_redstone(self, l_char, gf):
		try:
			redstone_cost = l_char.mining_list['redstone']
		except KeyError:
			redstone_cost = 3231060.1856
			l_char.mining_list['redstone'] = redstone_cost
		redstone_info = "Редстоун - очень редкий и трудно добываемый камень, пеемущественно используется в драгоценностях. 1 Sol = 0.0001 кг (стоимость идёт за килограмм)"
		ore = Ore('Редстоун', 'Sols', 'Железная_кирка_++', 'Дробилка_2400+', redstone_cost, redstone_info)

		return ore

	def init_rock(self, l_char, gf):
		try:
			rock_cost = l_char.mining_list['rock']
		except KeyError:
			rock_cost = 1.4665
			l_char.mining_list['rock'] = rock_cost
		rock_info = "Обыкновенный камень, широко используется в строительстве домов и зданий."
		ore = Ore('Булыжник', 'Kg', 'Деревянная_кирка', 'Каменная_кирка_+', rock_cost, rock_info)

		return ore