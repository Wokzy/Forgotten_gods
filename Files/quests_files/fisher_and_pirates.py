


def nirsing_pirates_start(l_char, gf):
	print('Вы содитесь на лодку с Гилбертом.')



def check(l_char, gf):
	if l_char.find_dialog('Первое плавание в Нирсинге'):
		l_char.dialogs.append('Первое плавание в Нирсинге')
		gf.update(l_char)
		print('Вы решаете поплавать и вот уже собираетесь заходить в воду, как вдруг')
		gf.enter()
		print('Вы оглядываетесь и видите, что люди вокруг удивлённо на вас смотрят, ', \
			"к вам подходит мужчина с удочкой лет 45.")
		gf.enter()
		print('- Эй, парень, ты здесь 1-й раз, или уже перестал бояться пиратов?')
		gf.enter()
		print('1 - Извините, я не понимаю, о каких пиратах идёт речь, я здесь первый раз.')
		print('2 - Пираты мне не страшны.')

		ch = gf.player_ask_selection('', 1, 2)

		if ch == 1:
			print('В заливе Обитают пираты, все, незащищённые высшим уровнем, корабли ', \
				"они топят, забирают груз, берут экипаж в качестве заложников, либо просто его убивают.", \
				"Если захочешь поборроть этих пиратов, приходи сюда, желательно с командой, буду ждать!")
			gf.enter()
			return
		elif ch == 2:
			print(' - Ну раз ты такой бесстрашный, поплыли поборем этих пиратов.', \
				'Меня к стати зовут Гилберт')
			gf.enter()

			print("1 - Поплыли, что мне.")
			print("2 - В другой раз.")

			ch = gf.player_ask_selection('', 1, 2)

			if ch == 1:
				print('Тю. Погнали! Если не удастся решить всё мирным путём, что будет скорее всего', \
					"то я помгу в сражении.")
				gf.enter()
				nirsing_pirates_start(l_char, gf)
				gf.update(l_char)
				return
	else:
		print(' - Ну что, надумал плыть на пиратов? - Гилберт.')
		print('')
		print('1 - Да!')
		print('2 - В другой раз.')

		ch = gf.player_ask_selection('', 1, 2)

		if ch == 1:
			print('')
			nirsing_pirates_start(l_char, gf)
		else: return