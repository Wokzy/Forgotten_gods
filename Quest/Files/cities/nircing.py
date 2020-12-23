import random
import os

from ElixirItem import *
from Enemy import *

from Shop import *
from data_5 import *

from Home import *
import Quests as quests

from cities import kirt_arrosh




class Nircing:
	def __init__(self):
		self.fish_1_2 = [Fish('Дикий морской окунь', 10), Fish('Кафельник', 12), \
		Fish('Атлантический большеголов', 9), Fish('Королевская макрель', 15), Fish('Рувета', 11), \
		Fish('Голубой тунец', 14), Fish('Красный луциан', 7)]
		self.fish_3_5 = [Fish('Пикша', 25), Fish('Рыба неизвестная', 20), Fish('Рыба неизвестная', 19), \
		Fish('Рыба неизвестная', 28)]
		self.fish_6_8 = [Fish('Рыба дорогая', 70), Fish('Красная рыба', 75), Fish('Лосось', 65), \
		Fish('Кто?', 50)]


	def play_menu(self, l_char, gf):
		l_char.loc = 'Nircing'
		l_char.loc_town = 0
		if Shack('Нирсинг', 20000, 0) not in l_char.buildings:
			l_char.buildings.append(Shack('Нирсинг', 20000, 0))

		while True:
			print("Вы находитесь в игровом меню города Нирсинга:")
			print("1 - Выбрать локацию")
			print("2 - Посмотреть текущие миссии")
			print("3 - Сохранение")
			print("4 - Информация по персонажу")
			print("5 - Взаимодействовать с предметами из инвентаря.")
			print('6 - Выбрать город, куда отправиться')
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
				#gf.play_menu(l_char, gf, 0)
			elif ch == 7:
				gf.update(l_char)
				exit()


	def choose_city(self, l_char, gf):
		print('Выберите город, куда хотите отправиться:')
		print('1 - Кастомаки')
		print("2 - Кирт'Аррош")
		print('3 - не отправляться')

		if ch == 1:
			l_char.loc = 0
			return True
		elif ch == 2:
			kirt_arrosh.KirtArrosh().play_menu(l_char, gf)
			return True
		else: return False

	def choose_loc(self, l_char, gf):
		print('Выберите локацию:')
		print('1 - Лачуга')
		print('2 - Магазин')
		print('3 - Отправиться к заливу')
		print('4 - Пойти в центр')
		print('5 - Узнать чем промышляют местные бандиты')
		print('6 - Выйти')

		ch = gf.player_ask_selection('', 1, 6)

		if ch == 1:
			for i in range(len(l_char.buildings)):
				g = l_char.buildings[i]

				if g.code == 0 and l_char.loc == 'Nircing' and g.loc == 'Нирсинг':
					g.home_enter(l_char, gf)
					break
		elif ch == 2:
			shop_loc2 = Shop("The shop (loc 2)");
			gf.fill_shop_loc2(shop_loc2)

			#shop_loc2.player_enter(l_char);

			shop_loc_2(l_char, gf, shop_loc2)
			self.choose_loc(l_char, gf)
		elif ch == 3:
			self.bay(l_char, gf)
		elif ch == 4:
			pass
		elif ch == 5:
			pass
		elif ch == 6:
			return


	def bay(self, l_char, gf):
		while True:
			print('Добро пожаловать в залив!')
			print('')
			print('1 - Отправиться на рыбалку')
			print('2 - Купить удочку')
			print('3 - Пойти поплавать')
			print('4 - Взять подводное снаряжение на прокат и отправиться бороздить просторы залива. ',\
			'(40 медяков) (Есть шанс найти что-нибудь и получить опыт с предметом)')
			print('5 - Покинуть залив')

			ch = gf.player_ask_selection('', 1, 5)

			if ch == 1: self.fishing(l_char, gf)
			elif ch == 2: self.buy_udochka(l_char, gf)
			elif ch == 3: self.swimming(l_char, gf)
			elif ch == 4: self.diving(l_char, gf)
			elif ch == 5: return

	def buy_udochka(self, l_char, gf):
		print('Приветствую! - говорит продовец удочек.')
		while True:
			print('Выбирайте, что купить:')
			print('1 - обычную удочку - 100')
			print('2 - удочку с особой приманкой -', 35*5)
			print('3 - палку рыбацкую - 50')
			print('4 - продвинутую удочку -', 45*5)
			print('5 - супер удочку -', 300)
			print('i - Информация о товарах')
			print('q - Выход')

			ch = gf.player_ask_selection_iq('', 1, 5)
			udochka = None

			if ch == 1: udochka = Udochka('Обычная удочка', 3, 100)
			elif ch == 2: udochka = Udochka('Удочка с особой приманкой', 4, 35*5)
			elif ch == 3: udochka = Udochka('Палка рыбацкая', 1, 50)
			elif ch == 4: udochka = Udochka('Продвинутая удочка', 6, 45*5)
			elif ch == 5: udochka = Udochka('Супер удочка', 8, 300)
			elif ch == -1:
				print('Обычная удочка - Название говорит само за себя, обычная удочка для простенькой рыбёшки.')
				print('Удочка с особой приманкой - Улучшеная приманка, спектр рыб увеличивается.')
				print('Палка рыбацкая - если вы решили заключить пари, то если ваш соперник проиграет, пусть попробует выловить на эту удочку рыбёшку.')
				print('Продвинутая удочка - Крутая приманка, удобный хват, футуристичный дизайн, лёгко ловить, всё это про продвинутую удочку')
				print('Супер удочка - "Умная рыба та, что не ведётся на приманку.", с этой удочкой умных рыб не бывает...')
			else: return None

			if l_char.mon >= udochka.price:
				l_char.mon -= udochka.price
				l_char.invent.append(udochka)
				print('Вы успешно приобрели удочку! Удачной рыбалки!')
				gf.update(l_char)
				return
			else:
				print('У вас не достаточно денег, чтобы купить эту удочку.')
				gf.enter()
				continue

	def fishing(self, l_char, gf):
		k = False
		for i in l_char.invent:
			if i.__class__.__name__ == 'Udochka':
				k = True
				break

		if k:
			print('1 - Взять удочку на прокат или 2 - пойти со совоей удочкой')
			ch = gf.player_ask_selection('', 1, 2)

			if ch == 1: udochka = self.get_udochka(l_char, gf)
			else:
				g = 0
				lst = []
				for i in l_char.invent:
					if i.__class__.__name__ == 'Udochka':
						g += 1
						print(g, ' - ', i.name)
						lst.append(i)
				ch = gf.player_ask_selection('', 1, g)
				udochka = lst[ch-1]
		else:
			print('У вас нет удочки, Поэтому вам нужно взять на прокат.')
			gf.enter()
			udochka = self.get_udochka(l_char, gf)

		if udochka == None: return

		print('Вы отправились рыбачить')
		fish = None
		print(udochka.chance)
		if udochka.chance <= 2: fish = random.choice(self.fish_1_2)
		elif udochka.chance >= 3 and udochka.chance <= 5: fish = random.choice(self.fish_3_5)
		else: fish = random.choice(self.fish_6_8)

		print('Вы поймали рыбу: ' + fish.name, '.Её стоимость - ', fish.price)
		l_char.invent.append(fish)
		for i in l_char.invent:
			if i == udochka:
				if i.work == 0:
					print('Ваша удочка сломалась от старости.')
					l_char.invent.remove(i)
				i.work -=1
				break
		gf.update(l_char)



	def get_udochka(self, l_char, gf):
		while True:
			print('Добро пожаловать, здесь вы можете взять на прокат удочки.')
			print('')
			print('1 - Взять обычную удочку - 20')
			print('2 - Взять удочку с особой приманкой - 35')
			print('3 - Взять палку - 10')
			print('4 - Взять продвинутую удочку - 45')
			print('5 - Взять супер удочку - 60')
			print('i - Информация о товарах')
			print('q - Выход')

			ch = gf.player_ask_selection_iq('', 1, 5)
			udochka = None

			if ch == 1: udochka = Udochka('Обычная удочка', 3, 20)
			elif ch == 2: udochka = Udochka('Удочка с особой приманкой', 4, 35)
			elif ch == 3: udochka = Udochka('Палка рыбацкая', 1, 10)
			elif ch == 4: udochka = Udochka('Продвинутая удочка', 6, 45)
			elif ch == 5: udochka = Udochka('Супер удочка', 8, 60)
			elif ch == -1:
				print('Обычная удочка - Название говорит само за себя, обычная удочка для простенькой рыбёшки.')
				print('Удочка с особой приманкой - Улучшеная приманка, спектр рыб увеличивается.')
				print('Палка рыбацкая - если вы решили заключить пари, то если ваш соперник проиграет, пусть попробует выловить на эту удочку рыбёшку.')
				print('Продвинутая удочка - Крутая приманка, удобный хват, футуристичный дизайн, лёгко ловить, всё это про продвинутую удочку')
				print('Супер удочка - "Умная рыба та, что не ловится на удочку.", с этой удочкой умных рыб не бывает...')
				continue
			else: return None

			if l_char.mon >= udochka.price:
				l_char.mon -= udochka.price
				gf.update(l_char)
				return udochka
			else:
				print('У вас не достаточно денег, чтобы взять данную удочку на прокат.')
				gf.enter()
				continue


	def swimming(self, l_char, gf):
		if l_char.find_work('Заплыв на лодке с Рыбаком.'):
			quests.AdditionalQuests().swimming_with_fisher(l_char, gf)
		else:
			print('Голос в вашей голове: "Я думаю, что вы поняли, что не стоит рисковать."')
			gf.enter()

	def diving(self, l_char, gf):
		pass