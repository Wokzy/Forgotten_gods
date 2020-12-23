from data_4 import *
import random
from data_5 import *
from data_6 import *

# Использовать проверку локации, при запуске диалога.

#gf.dialogs.dialog_001(l_char, gf)

#gf.locations.choose_loc(l_char, gf)

class GameDialogs():
	""" useful game function """
	def __init__(self, name):
		#super(Character, self).__init__()
		self.name = name

	def dialog_001(self, l_char, gf):
		print("---Когда диалог останавливается, нажимайте Enter---")
		print("Вы находитесь в городе Кастомаки")
		print("К вам подходит полный мужчина, лет 40 - 50")
		print("Вы местный?")
		enter = input()
		print("1 - ДА")
		print("2 - Нет")
		ch = int(input())
		while ch < 1 or ch > 2:
			print("Ответ некорректный, повторите!")
			ch = int(input())

		#if ch == 1:
		print("Ты знаешь, где здесь местный рынок?")
		enter = input()
		print("1 - ДА, он вон там, за углом. Указать налево.")
		print("2 - ДА, он вон там, за углом. Указать направо.")
		print("3 - К сожалению нет.")
		ch = int(input())

		while ch < 1 or ch > 3:
			print("Ответ некорректный, повторите!")
			ch = int(input())

		if ch == 1:
			print("Хорошо, спасибо. Мужчина уходит.")
			enter = input()
		elif ch == 2:
			print("Хорошо, спасибо. Мужчина уходит.")
			enter = input()
		elif ch == 3:
			print("Очень жаль. Поможешь мне его найти?")
			enter = input()
			print("1 - ДА, помогу. (7 ед. игрового опыта)")
			print("2 - Нет, прости, не в этот раз. (Отказаться от задания)")
			ch = int(input())

			while ch < 1 or ch > 2:
				print("Ответ некорректный, повторите!")
				ch = int(input())

			if ch == 1:
				work_001(l_char, gf)
			elif ch == 2:
				print("Ладно, извиняюсь за беспокойство. - сказал мужчина и ушёл.")
				enter = input()

		l_char.dialog += 1

		gf.update(l_char)
		#elif ch == 2:



	def dialog_002(self, l_char, gf):
		pass




	def ch_dialog(self, l_char, gf):
		if l_char.dialog == 0:
			self.dialog_001(l_char, gf)
		#gf.locations.choose_loc(l_char, gf)
		#gf.play_menu(l_char, gf, 0)

