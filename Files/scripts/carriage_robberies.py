from scripts import Prison
from ElixirItem import *
from Enemy import *
import data_4
import os
import sys
import random


def carriage_robbery_bread(self, l_char, gf):
		gf.server_units.remove('Торговец хлебом')

		print('Вы поджидаете и налетаете на торговца хлебом. Он машет кулаками и брыкается.')
		gf.enter()

		gf.battle(gf, l_char, [Enemy('Торговец хлебом', 10, 1, 0.5)])

		print('Торговец падает на колени и говорит:')
		print('ХВАТИТ! ХВАТИТ! ХВАТИТ! Сеньор, я сдаюсь, с-сдаюсь. Прошу, смилуйтесь!!! Я отдам вам весь свой товар! Молю!')

		print('1 - Смиловаться')
		print('2 - Смиловаться и попросить 30 медяков.')
		print('3 - Я хочу твоей смерти, *Злобный смех')

		ch = gf.player_ask_selection('', 1, 3)

		if ch == 1 or ch == 2:
			l_char.exp += 5
			print('Вы: Я не стану тебя убивать, мне не нужны лишние трупы...')
			print('Торговец: Благодарю вас Государь, спасибо вам!!')
			gf.enter()
			if ch == 2:
				print('Вы: Не спеши, мне нужны 30 медяков.')
				gf.enter()
				print('Торговец: Конечно! *начинает искать деньги...')
				gf.enter()
				if random.randint(1, 2) == 2:
					print('У меня нет 30-ти медяков..')
					print('')
					print('1 - Убить торговца.')
					print('2 - Смиловаться вновь.')

					ch = gf.player_ask_selection('', 1, 2)

					if ch == 1:
						print('Вы: К сожалению тебе придётся умереть... Вы быстро лишаете жизни бедняка.')
					elif ch == 2:
						print('Вы: Ладно, денег у меня хватает, обойдусь.')
				else:
					print('Торговец протягивает вам 30 медяков.')
					l_char.mon += 30
		elif ch == 3:
			print('Вы быстро лишаете жизни бедняка.')

		gf.enter()

		print('1 - Обыскать повозку')
		print('2 - Уйти')

		ch = gf.player_ask_selection('', 1, 2)

		if ch == 1:
			print('Там вы обнаруживаете только хлеб и одежку бедняка, которую вы забираете себе.')
			l_char.invent.append(Clothes('Поношеная куртка', 15))

		gf.update(l_char)
		return

def carriage_robbery_kontr(l_char, gf):
	print('Вы делаете налёт на контрабандиста.')
	gf.enter()
	print('Контрабандист достаёт револьвер и целится прямо вам в грудь, вам приходится встать на месте.')
	gf.enter()
	print('Он же: Чееееел, что за выкрутасы? Ограбить меня хотел?? Нет уж дружок, так просто это не сделать.')
	gf.enter()

	print('1 - Прыгнуть на незнакомца')
	print('2 - Ойойойойой, прости, я тебя перепутал с другим человеком, грабить тебя я совсем не собирался.')
	print('3 - Конечно!')

	ch = gf.player_ask_selection('', 1, 3)

	if ch == 1 or ch == 3:
		if ch == 1:
			print('Вы наскакиваете на контрабандиста, выбиваете у него из рук пистолет и наносите критический урон!')
			gf.enter()

			gf.battle(gf, l_char, [Enemy('Контрабандист', 12, 1, 3)])
		elif ch == 3:
			print('Контрабандист: Ну, чтож, тогда получай!!!')
			gf.enter()

			gf.battle(gf, l_char, [Enemy('Контрабандист', 25, 1, 5)])

			l_char.exp += 25

		print('Вы убили контрабандиста.')
		gf.enter()

		print('1 - Обыскать повозку')
		print('2 - Уйти ни с чем.')

		if ch == 1:
			print('Вы нашли и взяли: 70 медяков, небольшую книжку с изображением огня, отмычки и маску, а также вы подобрали револьвер, который на вас контрабандист.')
			l_char.invent.append(Item_special("Книжка с изображением огня"))
			l_char.invent.append(Clothes("Маска", 30, hp=0))
			l_char.invent.append(Item_special("Отмычка"))
			l_char.mon += 70
			l_char.weap.append(Weapon('Револьвер поношеный', 7, 7, 30))
			l_char.exp += 5

		gf.update(l_char)
		return
	elif ch == 2:
		print('Контрабандист: Ну ладно, лихач, проходи, поверю тебе.')
		gf.enter()
		gf.update(l_char)
		return


def carriage_robbery_beer_drinks(l_char, gf):
	