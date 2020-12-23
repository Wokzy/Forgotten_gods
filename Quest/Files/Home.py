import random
import keyboard
import turtle


class Home():

	def __init__(self, loc, price, code):
		self.loc = loc
		self.invent = []
		self.price = price
		self.trade_price = 0
		self.code = code

		self.sleep = ["бегающих в лесу синих кроликах", "пустоте", "летающих оранжевых верблюдах",
						"Пожилых ежах", "Великую войну", "Восстании паровых машин", 
						"зомби апокалипсисе", "вашей мечте", "бомже, который сидел у вашего дома."]



	def home_enter(self, l_char, gf):
		for i in range(len(l_char.buildings_invents)):
			g = l_char.buildings_invents[i]

			if i == self.code:
				del l_char.buildings_invents[i]

		l_char.buildings_invents.append(self.invent)


		l_char.loc_town = 1

		quit = 0



		print("Вы зашли в дом.")

		gf.enter()

		while quit != 1:
			gf.update(l_char)

			print("Выберите действие:")
			print("")
			print("1 - отправиться в кладовую")
			print("2 - отдохнуть на диване")
			print("3 - Подойти к доске с планом")
			print("4 - Выйти из дома")
			
			ch = gf.player_ask_selection("", 1, 4)

			if ch == 1:
				self.home_invent(l_char, gf)
			elif ch == 2:
				self.chill(l_char, gf)
			elif ch == 3:
				self.board_for_plan(l_char, gf)
			elif ch == 4:
				quit = 1



	def home_invent(self, l_char, gf):
		print("Выберите действие:")
		print("1 - Посмотреть составляющее кладовки")
		print("2 - Изъять предметы из кладовки")
		print("3 - Положить предметы в кладовку")
		print("4 - Выход из кладовки")

		ch = gf.player_ask_selection("", 1, 4)

		if ch == 1:
			if len(self.invent) == 0:
				print("В вашей кладовки ничего нет. Вы можете положить туда что-нибудь.")
				gf.enter()
			else:
				print("Составляющее вашей кладовки:")
				for i in range(len(self.invent)):
					g = self.invent[i]

					print(str(g.name))

				gf.enter()

		elif ch == 2:
			if len(self.invent) == 0:
				print("В вашей кладовки ничего нет. Вы можете положить туда что-нибудь.")
				gf.enter()
			else:
				print("Выберите предмет из кладовки:")
				for i in range(len(self.invent)):
					g = self.invent[i]

					print(str(i+1) + " - " + str(g.name))

				ch = gf.player_ask_selection("", 1, len(self.invent))

				ch_item = self.invent[ch-1]

				if ch_item.__class__.__name__ == 'Weapon': l_char.weap.append(ch_item)
				else: l_char.invent.append(ch_item)

				del self.invent[ch-1]
		elif ch == 3:
			print("1 - положить обычный предмет")
			print("2 - положить оружие")

			ch = gf.player_ask_selection("", 1, 2)

			if ch == 1:
				self.put_item(l_char, gf)
			elif ch == 2:
				self.put_weapon(l_char, gf)



	def chill(self, l_char, gf):
		print("Вы ложитесь отдыхать на диван.")

		gf.enter()

		print("Вам приснился сон о " + self.sleep[random.randrange(0, len(self.sleep))])
		print("Также вы отлично выспались и не чувствуете усталости")

		if l_char.work == 'Ограбление банка (Аккуратно по плану) (Вам нужно поспать дома.)':
			l_char.work = 'Ограбление банка (Аккуратно по плану) (Вернуться в логово кирианцев)'

		l_char.sleep = 0

		gf.enter()



	def put_item(self, l_char, gf):
		print("Выберите предмет:")
		print(" ")

		ch = gf.choose_invent_item(l_char)

		ch_item = l_char.invent[ch-1]

		self.invent.append(ch_item)
		print("Предмет находится в кладовой")

		del l_char.invent[ch-1]


	def put_weapon(self, l_char, gf):
		print("Выберите предмет:")
		print(" ")

		ch = gf.choose_weapon_item(l_char)

		ch_item = l_char.weap[ch-1]

		self.invent.append(ch_item)
		print("Оружие находится в кладовой")

		del l_char.weap[ch-1]




	def board_for_plan(self, l_char, gf):
		t = turtle.Turtle()
		t.speed(0)
		t.pensize(2)

		print('')
		print('Бинды для клавиш:')
		print('W, A, S, D - передвижение по доске')
		print('X, C - Поднять, опустить перо')
		print('P - Выход из рисования')
		print('')

		while True:
			if keyboard.is_pressed('w'):
				t.forward(10)
			elif keyboard.is_pressed('a'):
				t.left(10)
			elif keyboard.is_pressed('s'):
				t.back(10)
			elif keyboard.is_pressed('d'):
				t.right(10)
			elif keyboard.is_pressed('x'):
				t.penup()
			elif keyboard.is_pressed('c'):
				t.pendown()
			elif keyboard.is_pressed('p'):
				break



class Shack(Home):
	def __init__(self, loc, price, code):
		self.loc = loc
		self.invent = []
		self.price = price
		self.trade_price = 0
		self.code = code

		self.sleep = ["бегающих в лесу синих кроликах", "пустоте", "летающих оранжевых верблюдах",
						"Пожилых ежах", "Великих войнах", "Восстании паровых машин", 
						"вашей мечте", "бомже, который сидел у вашего дома.", 
						'Доме получше',]


	def home_enter(self, l_char, gf):
		for i in range(len(l_char.buildings_invents)):
			g = l_char.buildings_invents[i]

			if i == self.code:
				del l_char.buildings_invents[i]

		l_char.buildings_invents.append(self.invent)


		l_char.loc_town = 1

		quit = 0



		print("Вы зашли в лаччугу.")

		gf.enter()

		while quit != 1:
			gf.update(l_char)

			print("Выберите действие:")
			print("")
			print("1 - Отправиться в подпол")
			print("2 - Отдохнуть на сене")
			print("3 - Выйти из дома")
			
			ch = gf.player_ask_selection("", 1, 4)

			if ch == 1:
				self.home_invent(l_char, gf)
			elif ch == 2:
				self.chill(l_char, gf)
			elif ch == 3:
				quit = 1




	def home_invent(self, l_char, gf):
		print("Выберите действие:")
		print("1 - Посмотреть составляющее Подпола")
		print("2 - Вытащить предметы из подпола")
		print("3 - Положить предметы в подпол")
		print("4 - Вылезти из подпола")

		ch = gf.player_ask_selection("", 1, 4)

		if ch == 1:
			if len(self.invent) == 0:
				print("В вашем подполе ничего нет. Вы можете спустить туда что-нибудь.")
				gf.enter()
			else:
				print("Составляющее вашего подпола:")
				for i in range(len(self.invent)):
					g = self.invent[i]

					print(str(g.name))

				gf.enter()

		elif ch == 2:
			if len(self.invent) == 0:
				print("В вашем подполе ничего нет. Вы можете спустить туда что-нибудь.")
				gf.enter()
			else:
				print("Выберите предмет из подпола:")
				for i in range(len(self.invent)):
					g = self.invent[i]

					print(str(i+1) + " - " + str(g.name))

				ch = gf.player_ask_selection("", 1, len(self.invent))

				ch_item = self.invent[ch-1]

				if ch_item.__class__.__name__ == 'Weapon': l_char.weap.append(ch_item)
				else: l_char.invent.append(ch_item)

				del self.invent[ch-1]
		elif ch == 3:
			print("1 - Спустить обычный предмет")
			print("2 - Спустить оружие")

			ch = gf.player_ask_selection("", 1, 2)

			if ch == 1:
				self.put_item(l_char, gf)
			elif ch == 2:
				self.put_weapon(l_char, gf)



	def chill(self, l_char, gf):
		print("Вы ложитесь отдыхать на сено. Вам не очень комфортно, но довольно мягко.")

		gf.enter()

		print("Вам приснился сон о " + self.sleep[random.randrange(0, len(self.sleep))])
		print("Также вы отлично выспались и не чувствуете усталости")

		l_char.sleep = 0

		gf.enter()
		return