import random
from ElixirItem import *
from Enemy import *
import data_4
from data_5 import *
from Shop import *
from Home import *
import Quests as quests
import os
import sys


from cities import nircing
from cities import kirt_arrosh


lcwd = os.getcwd()
os.chdir('scripts')

from scripts import underground_club

os.chdir(lcwd)


class Kastomaki():
	def __init__(self):
		self.durak_cards = [Card(6, 'Черви'), Card(6, 'Крести'), Card(6, 'Пики'), Card(6, 'Буби'), \
		Card(7, 'Черви'), Card(7, 'Крести'), Card(7, 'Пики'), Card(7, 'Буби'), \
		Card(8, 'Черви'), Card(8, 'Крести'), Card(8, 'Пики'), Card(8, 'Буби'), \
		Card(9, 'Черви'), Card(9, 'Крести'), Card(9, 'Пики'), Card(9, 'Буби'), \
		Card(10, 'Черви'), Card(10, 'Крести'), Card(10, 'Пики'), Card(10, 'Буби'), \
		Card(11, 'Черви'), Card(11, 'Крести'), Card(11, 'Пики'), Card(11, 'Буби'), \
		Card(12, 'Черви'), Card(12, 'Крести'), Card(12, 'Пики'), Card(12, 'Буби'), \
		Card(13, 'Черви'), Card(13, 'Черви'), Card(13, 'Черви'), Card(13, 'Черви'), ]


	def start_researching(self, l_char, gf):
		print('Выберите направление вашего движеня:')
		print('')
		print('1 - К стене')
		print('2 - В переулок')
		print('3 - В казино**')
		print('4 - В подпольный клуб**')
		print('5 - Пойти в трущобы')
		print('6 - В центр города')
		print('7 - Отправиться в другой город')
		print('8 - Выход')

		ch = gf.player_ask_selection('', 1, 8)

		if ch == 1:
			self.goto_wall(l_char, gf)
		elif ch == 2:
			if 'Ограбление банка (Пролом в лоб)' in l_char.work:
				print('Вы пока не можете сюда пройти')
			elif 'Ограбление банка (Аккуратно по плану) (Вернуться в логово кирианцев)' in l_char.work:
				l_char.work.remove('Ограбление банка (Аккуратно по плану) (Вернуться в логово кирианцев)')
				data_4.work_003_4(l_char, gf)
			elif 'Ограбление банка (Аккуратно по плану) (Вам нужно поспать дома.)' in l_char.work:
				print('Вам требуется отдохнуть дома.')
			elif l_char.find_work(3):
				data_4.start_003(l_char, gf)
			else: pass

		elif ch == 3:
			self.goto_casino(l_char, gf)
		elif ch == 4:
			pass
		elif ch == 5:
			if 'Ограбление банка (Пролом в лоб)' in l_char.work:
				l_char.work.remove('Ограбление банка (Пролом в лоб)')
				quests.bank_work_003(l_char, gf)
			else: self.ghetto(l_char, gf)
		elif ch == 6:
			if 'Прийти к центру города с толпой бедняков' in l_char.work:
				l_char.work.remove('Прийти к центру города с толпой бедняков')
				print('Харон: Ого! Судя по этой толпе, ты неплохой оратор.')
				gf.enter()
				print('Вира(тихим голосом): Прекрасно. Они отвлекут внимание и задержат стражу. Пора за дело.')
				gf.enter()
				gf.update(l_char)
				data_4.work_003_3(l_char, gf)
			else: self.goto_center(l_char, gf)
		elif ch == 8:
			return
		elif ch == 7:
			print('Выберите город:')
			print('1 - Нирсинг')
			print("2 - Кирт'Аррош")
			print('3 - Выход')

			ch = gf.player_ask_selection('', 1, 3)

			if ch == 1:
				l_char.loc = 'Nircing'
				nircing.Nircing().play_menu(l_char, gf)
			elif ch == 2:
				l_char.loc = "Кирт'Аррош"
				kirt_arrosh.KirtArrosh().play_menu(l_char, gf)
			#elif ch == 3: return

	def ghetto(self, l_char, gf):
		print("Вы пришли в трущобы.")
		print("")
		print("1 - Подойти к торговцу контрабандой")
		print("2 - Поболтать с местными жителями.")
		print("3 - Покинуть трущобы")

		if l_char.work == 'Свет в конце тоннеля: Пути выполнения квеста - Отправиться на пост стражи или подкараулить один из патрулей на улице в трущобах.':
			print('4 - Пойти на пост стражи')
			print('5 - Подкараулить один из патрулей.')
			ch = gf.player_ask_selection('', 1, 5)
		else: ch = gf.player_ask_selection('', 1, 3)

		if ch == 1:
			self.kontrabanda_shop(l_char, gf)
		elif ch == 2:
			self.talk_with_homeless(l_char, gf)
		elif ch == 4:
			l_char.work = 'Свет в конце тоннеля: прийти на пост стражи'
			gf.update(l_char)
			quests.AdditionalQuests.light_in_the_end_of_tonnel(l_char, l_char, gf)
		elif ch == 5:
			l_char.work = 'Свет в конце тоннеля: подкараулить один из патрулей на улицах'
			gf.update(l_char)
			quests.AdditionalQuests.light_in_the_end_of_tonnel(l_char, l_char, gf)
		else: return

	def kontrabanda_shop(self, l_char, gf):
		if l_char.work == 'Свет в конце тоннеля: Цель 1.1 - Посетить местного торговца в трущобах.':
			l_char.work = 'Свет в конце тоннеля: Пути выполнения квеста - Отправиться на пост стражи или подкараулить один из патрулей на улице в трущобах.'
		print('Торговец: Ну здравствуй! Что пожелаешь?')
		while True:
			print('')
			print('1 - Метку с изображением волка (60 медяков)')
			print('2 - Отмычки (50-5шт)')
			print('3 - Маска (45)')
			print('4 - Кинжал (70)')
			print("5 - Зелёная книга '3' (90 медяков)")
			print('6 - Поболтать с торговцем')
			print('7 - Спасибо, мне ничего не нужно. (Уйти)')

			ch = gf.player_ask_selection('', 1, 7)

			if ch == 1 and l_char.can_afford(60):
				l_char.invent.append(Item_special('Метка с изображением волка', 200004))
				l_char.mon -= 60
			elif ch == 5 and l_char.can_afford(90):
				l_char.invent.append(Item_special("Зелёная книга '3'", 100003))
				l_char.mon -= 90
			elif ch == 6: self.talk_with_kontr(l_char, gf)
			elif ch == 7:
				print('Торговец: Жду тебя ещё раз!')
				return
			elif ch == 2 and l_char.can_afford(50):
				for i in range(5): l_char.invent.append(Item_special("Отмычка"))
				l_char.mon -= 50
			elif ch == 3 and l_char.can_afford(45):
				l_char.invent.append(Clothes("Маска", 30, hp=0))
				l_char.mon -= 50
			elif ch == 4 and l_char.can_afford(70):
				l_char.weap.append(Weapon('Кинжал', 7, 2, 60))
				l_char.mon -= 70

			gf.update(l_char)


	def talk_with_kontr(self, l_char, gf):
		pass

	def talk_with_homeless(self, l_char, gf):
		pass

	def goto_center(self, l_char, gf):
		pass

	def goto_wall(self, l_char, gf):
		print('1 - Пойти к тракту')
		print('2 - Уйти')

		ch = gf.player_ask_selection('', 1, 2)

		if ch == 1:
			self.tract(l_char, gf)
		else: return

	def tract(self, l_char, gf):
		if l_char.work == 'Свет в конце тоннеля: разобраться с осевшими в лесах близ тракта бандитами (Пойти к стене и к тракту.':
			quests.AdditionalQuests.light_in_the_end_of_tonnel(l_char, l_char, gf)


	'''
	def play_durak(self, l_char, gf):
		stavka = 0
		print('Игрок в карты: ну здравствуй')
		print('Вы: Давай партейку в дурака')
		print('Игрок: Только назови ставку. В слычае победы ты получишь в 2-ю ставку.')
		gf.enter()

		print('Ваш баланс - ', l_char.mon)
		while True:
			try:
				stavka = int(input('Ваша ставка: '))
			except TypeError:
				print('Это не число. Попробуйте ещё раз.')
			if stavka > l_char.mon:
				print('Вы не можете столько поставить, у вас попросту столько нет.')
			else: break

		l_char.mon -= stavka
		#Начало игры


		deck = self.durak_cards
		player_cards = []
		bot_cards = []
		lower_player = 0
		lower_bot = 0
		first = ''

		#fill decks
		for i in range(6):
			card = random.randrange(0, len(deck))
			player_cards.append(deck[card])
			del deck[card]
			card = random.randrange(0, len(deck))
			bot_cards.append(deck[card])
			del deck[card]
		trump = deck[random.randrange(0, len(deck))]

		lower_player = gf.lower_card(player_cards)
		lower_bot = gf.lower_card(bot_cards)

		first = gf.who_first(lower_player, lower_bot)

		gf.start_playing_durak(l_char, gf, first, player_cards, bot_cards)
	'''



	def goto_casino(self, l_char, gf):
		while True:
			print('Добро пожаловать в казино! Здесь вы можете:')
			print("1 - Сыграть в кубики")
			print("2 - Сыграть в рулетку")
			print("3 - Сыграть в Runner")
			print("4 - Выпить")
			print("5 - Покинуть казино")
			
			ch = gf.player_ask_selection('', 1, 5)

			if ch == 1:
				#self.play_durak(l_char, gf)
				self.play_cubes(l_char, gf)
			elif ch == 2: self.play_colors(l_char, gf)
			elif ch == 3: self.play_runner(l_char, gf)
			elif ch == 4:
				print('Выберите напиток')
				print('1 - Водка (40 медяков)')
				print('2 - Красное вино (80 медяков)')
				print('3 - Вино белое заморское (100 медяков)')
				print('4 - Крепкий эль (75 медяков)')
				print('5 - Не пить')
				
				ch = gf.player_ask_selection('', 1, 5)

				if ch == 1 and l_char.can_afford(40):
					print('Вы выпили бутылку водки, вы освежились и подготовили вашу удачу.')
					l_char.mon -= 40
					gf.update(l_char)
				elif ch == 2 and l_char.can_afford(80):
					print('Красное вино оказалось довольно вкусным, вам понравилось, но не более того.')
					l_char.mon -= 80
					gf.update(l_char)
				elif ch == 3 and l_char.can_afford(100):
					print('Заморское вино оказалось невероятно вкусным, вам понравилось и вы захотели ещё!',\
						'Вы отлично освежились и готовы выигрывать крупные суммы.')
					l_char.mon -= 100
					gf.update(l_char)
				elif ch == 4 and l_char.can_afford(75):
					print('Крепкий эль оказался как ни странно со вкусом эля...')
					l_char.mon -= 75
					gf.update(l_char)
				else: return
			else: return


	def play_colors(self, l_char, gf):
		while True:
			print('Добро пожаловать в рулетку')
			print('1 - Правила игры')
			print('2 - Сделать ставку')
			print('3 - Покинуть казино')

			ch = gf.player_ask_selection('', 1, 3)

			if ch == 1:
				print("Есть кольцо, на котором замечены 62 значения, 0, 00, и от 1 до 60. Чётные чила - красные, не чётные чёрные, а нули зелёные. Вы можете сделать ставки на разный выигрыш. Ставки х2: 1-я половина(0-30), 2-я половина (31-00), красное, чёрное. Ставка х50 - зелёное. Ставка х60: Конкретное число.")
			elif ch == 2:
				if l_char.mon == 0:
					print('У вас нет денег!')
					break
				gf.start_colors(l_char, gf)
				break
			else: break



	def play_cubes(self, l_char, gf):
		while True:
			print('1 - Правила игры')
			print('2 - Выбрать ставку')
			print('3 - Покинуть казино')

			ch = gf.player_ask_selection('', 1, 3)

			if ch == 1:
				print('Копмьютер случайно подбрасывает кубики и если выпадает одинаковые числа на всех кубиках, за столько подбросов, сколько вы поставили, вы получаете деньги, в ином случае вы теряете деньги эквивалентно 100 медяков на 1 поставленный кубик. Вы ставите колличество кубиков и то, за какое кол-во подкидываний выпадет одинаковые числа. В случае победы вам выдаётся приз в размере 100 * на кубики делёное на колличество подбрасываний, которое поделено на 5 если больше 10.')
				gf.enter()
			elif ch == 2:
				gf.cubes_start(l_char, gf)
				break
			else: break

	def play_runner(self, l_char, gf):
		while True:
			print('1 - Правила игры')
			print('2 - Выбрать ставку')
			print('3 - Покинуть казино')

			ch = gf.player_ask_selection('', 1, 3)

			if ch == 1:
				print('Вы ставите на число от 1.00 до 9.99, это будет коэффицентом вашей ставки, в случае выигрыша. Выигрываете вы в том случае, если коэффицент на который вы поставили не превосходит выпавший.')
				gf.enter()
			elif ch == 2:
				gf.start_runner(l_char, gf)
				break
			else: break

	def goto_underground_club(self, l_char, gf):
		pass