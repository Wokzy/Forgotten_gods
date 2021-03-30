import random
import data_4

# Importing quests files
from quests_files import fisher_and_pirates
from quests_files import light_iteo_tonnel


class PlotQuests:
	def __init__(self):
		self.a = None


class AdditionalQuests:
	def __init__(self):
		self.a = None


	def light_in_the_end_of_tonnel(self, l_char, gf):
		if l_char.work == 'Свет в конце тоннеля':
			l_char.helpers = []
			light_iteo_tonnel.start(l_char, gf)
		elif l_char.work == 'Свет в конце тоннеля: прийти на пост стражи':
			l_char.helpers = []
			light_iteo_tonnel.go_to_post(l_char, gf)
		elif l_char.work == 'Свет в конце тоннеля: подкараулить один из патрулей на улицах':
			l_char.helpers = []
			light_iteo_tonnel.wait_for_patrol(l_char, gf)
			return
		elif 'Свет в конце тоннеля: разобраться с осевшими в лесах близ тракта бандитами (Пойти к стене и к тракту.' in l_char.work:
			l_char.helpers = []
			light_iteo_tonnel.near_tract(l_char, gf)
			if '(__)' in l_char.work:
				light_iteo_tonnel.lie_after_coop(l_char, gf)
			else: light_iteo_tonnel.dialog_3(l_char, gf)

	def swimming_with_fisher(self, l_char, gf):
		fisher_and_pirates.check(l_char, gf)



























''' Old or Special Quests without class: '''
def bank_work_003(self, l_char, gf):
		print('Вы приходите в трущобы')
		gf.enter()
		print('Небольшие, покосившиеся халупы буквально лезут друг на друга.')
		gf.enter()
		print('Здесь живёт бедная половина населения Варнии.')
		gf.enter()
		print('Это люди, работавшие на заводах, бывшие строителями до тех пор,', \
		'пока их места не заняли големы.')
		gf.enter()
		print('Они потребляли меньше ресурсов и не требовали платы.')
		gf.enter()
		print('Вскоре обедневший рабочий класс погряз в долгах, от чего люто ненавидел банки.')
		gf.enter()
		print('За этим вы и пришли.')
		gf.enter()
		print('Навстречу вам выходят несколько бедняков.')
		gf.enter()
		print('Они удивлены появлением относительно богато одетого человека в трущобах,', \
		'но вместе с тем в их взглядах читалась зависть и ненависть.')
		gf.enter()
		print('Один из бедняков подходит к вам и просит милостыни.')
		gf.enter()
		print('Бедняк: Прошу, господин, подайте на пропитание!')
		gf.enter()

		print('1 - Отойди, гнусное создание. От тебя смердит!')
		print('2 - *Бросить 40 медяков* Вот тебе деньги. И я знаю, где достать больше, намного больше...')

		ch = gf.player_ask_selection('', 1, 2)

		if ch == 1:
			print('Бедняк: Очередной сноб... Нечего тебе было сюда приходить.')
			data_4.battle_003_4(l_char, gf)
			gf.enter()
			print('Расскажи хотьзачем ты сюда пришёл.')
			gf.enter()
			print('Вы: Я знаю, где можно раздобыть много денег.')
			gf.enter()
			print('Бедняк: И где же?')
			gf.enter()
			print('Вы: В банке Арринхоупа!')
			gf.enter()
			print('Неужели вам не надоело копошиться в собственных долгах,', \
			'оставаясь в грязных лапах бедности!?')
			gf.enter()
			print('Неужели вы не готовы сражаться за свою судьбу?!')
			gf.enter()
			print('Богачи наняли големов. Они отбросили вас умирать в грязи!')
			gf.enter()
			print('Пора отомстить, братья! Пора показать им, что вы не намерены молча терпеть пинки!')
			gf.enter()
			print('Смерть врагу!')
			gf.enter()
			print('Толпа: Смерть! Сметь! СМЕРТЬ!')
			gf.enter()
			print('Вы: За мной, братья! Эта ночь запомниться миру надолго! ')
			gf.enter()
			l_char.work.append('Прийти к центру города с толпой бедняков')
			gf.update(l_char)
		elif ch == 2:
			if l_char.mon >= 40:
				print("Вы бросили 40 медяков")
				l_char.mon -= 40
			else:
				print("40 медяков у вас не оказалось, поэтому вы бросили все деньги, что у вас были.")
				l_char.mon = 0
			print('Бедняк: Спасибо господин! И где же?')
			gf.enter()
			print('Вы: В банке Арринхоупа!')
			gf.enter()
			print('Неужели вам не надоело копошиться в собственных долгах,', \
			'оставаясь в грязных лапах бедности!?')
			gf.enter()
			print('Неужели вы не готовы сражаться за свою судьбу?!')
			gf.enter()
			print('Богачи наняли големов. Они отбросили вас умирать в грязи!')
			gf.enter()
			print('Пора отомстить, братья! Пора показать им, что вы не намерены молча терпеть пинки!')
			gf.enter()
			print('Смерть врагу!')
			gf.enter()
			print('Толпа: Смерть! Сметь! СМЕРТЬ!')
			gf.enter()
			print('Вы: За мной, братья! Эта ночь запомниться миру надолго! ')
			gf.enter()
			l_char.work.append('Прийти к центру города с толпой бедняков')
			gf.update(l_char)