from ElixirItem import *

# Список основных переменных:
# s - сила
# m - меткость
# mg - магия
# u - удача
# l - ловкость
# vs - восприятие
# mon - деньги
# exp - игровой опыт
# upgr - очки для прокачки навыков
# weap - список с оружием
# awards - список с наградами
# loc - локация персонажа


def new_game(l_char, gf):
	#change = []
	#s, m, mg, u, l, vs, mon, exp, upgr, weap, awards
	print("Создайте себе персонажа:")
	print(" ")
	print("Кем ваш персонаж будет, выберите и введите:")
	print("1 - Лучник - 1 сила, 3 меткость, 0 магия, 1 удача, 1 ловкость, 2 восприятие.")
	print("2 - Мечник - 3 сила, 2 - меткость, 0 магия, 1 удача, 2 ловкость, 1 восприятие")
	print("3 - Странник - 2 сила, 2 - меткость, 0 магия, 2 удача, 1 ловкость, 2 восприятие")
	print("4 - Ассасин - 2 сила, 2 - меткость, 0 магия, 2 удача, 4 ловкость, 3 восприятие")
	pers = gf.player_ask_selection("", 1, 4)


	if pers == 1:
		l_char.s += 1
		l_char.m += 3
		l_char.mg += 0
		l_char.u += 1
		l_char.l += 1
		l_char.vs += 2
		l_char.ability.append('Быстрая стрельба')
		print("Ваш персонаж - Лучник!")
	elif pers == 2:
		l_char.s += 3
		l_char.m += 2
		l_char.mg += 0
		l_char.u += 1
		l_char.l += 2
		l_char.vs += 1
		l_char.ability.append('Боевое безумие')
		print("Ваш персонаж - Мечник!")
	elif pers == 3:
		l_char.s += 2
		l_char.m += 2
		l_char.mg += 0
		l_char.u += 2
		l_char.l += 1
		l_char.vs += 2
		l_char.ability.append('Древнее знание')
		print("Ваш персонаж - Странник!")
	elif pers == 4:
		l_char.s += 2
		l_char.m += 2
		l_char.mg += 0
		l_char.u += 2
		l_char.l += 4
		l_char.vs += 3
		l_char.ability.append('Дымовая завеса')
		print("Ваш персонаж - Ассасин!")

	print("Ваш персонаж успешно создан!")
	print("Нажмите Enter для продолжения.")
	enter = input()

	print("Выберите, откуда вы будете родом:")
	print("	")
	print("1 - Нортгард - Могучие холодные севера, обитают самые жестокие и самые сильные.")
	print("2 - Варния - торговое государство на востоке")
	print("3 - Локрия - Западное государство, технологического развития")
	print("4 - Нирсинг - вольный город на севере")
	print("5 - Анрог - Пришедшее в упадок Южное королевство")
	print("6 - Потомок давно поверженых Локрией родов Кирианцев")
	print("	")

	ch = gf.player_ask_selection("", 1, 6)

	if ch == 1:
		l_char.rod = "Нортгардовец"

		item = Item_standart("Тяжёлая меховая куртка", 190, 99)
		l_char.invent.append(item)

		item = Item_standart("Шапка меховая, ручной работы", 90, 100)
		l_char.invent.append(item)

		item = Item_standart("Штаны кожаные", 140, 101)
		l_char.invent.append(item)

	elif ch == 2:
		l_char.rod = "Варниец"

		item = Item_standart("Длиные хитоны", 70, 101)
		l_char.invent.append(item)

	elif ch == 3:
		l_char.rod = "Локриец"

		item = Item_standart("Лёгкая рубаха белого цвета", 60, 101)
		l_char.invent.append(item)

		item = Item_standart("Брюки синие", 80, 101)
		l_char.invent.append(item)

		item = Item_standart("Шляпа ковбойская", 57, 101)
		l_char.invent.append(item)

	elif ch == 4:
		l_char.rod = "Нирсингиец"

		item = Item_standart("Тяжёлая меховая куртка", 190, 99)
		l_char.invent.append(item)

		item = Item_standart("Шапка меховая, ручной работы", 90, 100)
		l_char.invent.append(item)

		item = Item_standart("Штаны кожаные", 140, 101)
		l_char.invent.append(item)
	elif ch == 5:
		l_char.rod = 'Анрогиец'
		item = Item_standart("Длиные хитоны", 70, 101)
		l_char.invent.append(item)
	elif ch == 6:
		l_char.rod = 'Кирианец'
		item = Weapon("Нож охотничий", 6, 1, 60, 73, 0)
		l_char.invent.append(item)




	print("Введите имя вашего персонажа:")
	l_char.name = str(input())



	return l_char

