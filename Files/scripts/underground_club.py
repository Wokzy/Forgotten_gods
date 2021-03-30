import random
from ElixirItem import *


class UndergroundClub:
	def __init__(self):
		pass

	def check_card(self, l_char, card:str='Золотая карта'):
		for i in l_char.invent:
			if card in i:
				return True
		return False

	def EnterClub(self, l_char, gf):
		while True:
			print("")
			print('Вас встречает охранник: "Пропуск или оплата."')
			print('1 - Заплатить 80 медяков')
			print('2 - Предъявить пропуск/карту.')
			print('3 - Уйти')
			
			ch = gf.player_ask_selection("", 1, 3)

			if ch == 1:
				if l_char.mon >= 80:
					print('Охранник даёт вам пройти')
					l_char.mon -= 80
				else:
					print('У вас не хватает денег.')
					continue
			elif ch == 2:
				t = False
				for i in l_char.invent:
					if 'карта' in i.name or 'Пропуск в подпольный клуб' in i.name:
						t = True
				if t: print(' - Конечно, проходите. - говорит охранник.')
				elif not t:
					print('У вас нет карты/пропуска!')
					continue
			else: return

			self.club_menu(l_char, gf)

	def duel(self, l_char, gf):
		print('Как хотите, вы сказали руководителю ринга,', \
			'что хотите начать бой и вам подобрали соперника.')
		hitpts = random.randint(20, 60)
		dmg = random.randint(2, 5)
		win = hitpts*dmg
		gf.battle(enemyes=[Enemy(hp=hitpts, \
			damage=dmg, name='Враг')])
		print('Вы победили соперника и получили', win, "медяков")
		l_char.mon += win

	def club_menu(self, l_char, gf):
		while True:
			print('Добро пожаловать в клуб, здесь вы можете:')
			print('1 - Устроить дуэль')
			print('2 - Поболтать с местными')
			print('3 - Покинуть клуб')
			
			if self.check_card(l_char=l_char):
				print('4 - Выбрать музыку')
				ch = gf.player_ask_selection('', 1, 4)
			else: ch = gf.player_ask_selection('', 1, 3)

			if ch == 3:
				return
			elif ch == 1:
				self.duel(l_char, gf)
			elif ch == 2:
				self.speak(l_char, gf)
			elif ch == 4: self.choose_music()

			gf.update(l_char)

	def speak(self, l_char, gf):
		n = 1
		t = []
		for i in range(1):
			if l_char.find_work('Разговор в подпольном клубе про Баталии.'):
				t.append('Разговор в подпольном клубе про Баталии.')
				print(n, '- Сказать: "Ну и кто тут из вас самый сильный? "')
				n += 1
		ch = gf.player_ask_selection('', 1, n)
		said = t[n-1]