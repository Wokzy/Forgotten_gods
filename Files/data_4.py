from data_5 import *
from Enemy import *
from GameFunctions import *
import random
from ElixirItem import *
from Teammates import *
import Quests as quests


def work_001(l_char, gf):
	gf.update(l_char)

	print("Хорошо, куда пойдём?")
	enter = input()
	print("1 - Налево, за угол.")
	print("2 - Направо, за угол.")
	print("3 - Прямо, налево.")
	print("4 - Прямо, направо.")
	print("5 - Просто прямо")
	ch = int(input())

	while ch < 1 or ch > 5:
		print("Выбор некорректный, пожалуйста повторите.")
		ch = int(input())


	if ch == 1:
		print("Зайдя налево за угол, вы нашли бар и несколько сидящих рядом с ним")
		print("напившихся мужиков. Рынка здесь не оказалось.")
		print("Нажмите Enter для продолжения.")
		enter = input()
		work_001(l_char)
	elif ch == 2:
		print("Зайдя направо за угол, вы увидели огромную толпу людей, проход")
		print("между зданиями был узкий, а людей много, поэтому вы ничего не увидели.")
		print("Нажмите Enter для продолжения.")
		enter = input()
		print("1 - Попробовать прорваться через толпу и поискать рынок.")
		print("2 - Развернуться и пойти обратно.")
		ch = int(input())
		
		while ch < 1 or ch > 2:
			print("Выбор некорректный, пожалуйста повторите.")
			ch = int(input())


		if ch == 1:
			print("Спустя некоторое время вы прорвались через толпу и")
			print("увидели табличку с перечёрнутой надписью 'Кастомаки'.")
			print("Нажмите Enter для продолжения.")
			enter = input()
			work_001(l_char)
		elif ch == 2:
			work_001(l_char)
	elif ch == 3:
		print("Вы пошли прямо, налево и увидели несколько прилавков с продуктами.")
		print("Нажмите Enter для продолжения.")
		enter = input()
		print("1 - Пройти посмотреть дальше.")
		print("2 - Сказать - Вот он и рынок. (Завершить задание, 5 - exp)")
		print("3 - Вернуться обратно.")
		ch = int(input())

		while ch < 1 or ch > 3:
			print("Выбор некорректный, пожалуйста повторите.")
			ch = int(input())

		if ch == 1:
			print("Вы проходите дальше и видите огромную табличку - ГОРОДСКОЙ РЫНОК.")
			print("Нажмите Enter для продолжения.")
			enter = input()
			print("Мужик вас очень благодарит: 'Я у вас в долгу!'")
			l_char.exp += 7
			print("Получено 7 ед. игрового опыта!")
			
		elif ch == 2:
			print("Спасибо тебе огромное! - говорит мужик и уходит.")
			print("Нажмите Enter для продолжения.")
			enter = input()
			l_char.exp += 5
			print("Получено 5 ед. игрового опыта.")

		l_char.work_end += 1

	elif ch == 4:
		print("Зайдя направо за угол вы увидели огромного мужика.")
		print("	")
		gf.enter()
		print("ИЭ! ..жик ты чего здесь забыл?")
		print("Проваливай!")
		gf.enter()

		print("1 - попытаться что-то сказать")
		print("2 - Уйти")

		ch = gf.player_ask_selection("", 1, 2)


		if ch == 1:
			print("...Вы попытались что-то вякнуть...")
			print("")
			print("- Каво? У тебя есть претензии? - сказал мужик.")
			print("Силач откинул вас на 3 метра, вы упали и получили серьёзный ушиб")
			l_char.hits += 1

			gf.update(l_char)

			work_001(l_char, gf)
		elif ch == 2:
			work_001(l_char, gf)

	elif ch == 5:
		print("Вы пошли прямо.")
		print("Вы всё шли, шли и шли, так ничего и не найдя.")
		print("")


#--------------------------------------------------------------------------------
'''
def get_player_input(l_char, _min, _max):

	ch = int(input())

	while ch < _min or ch > _max:
		print("Выбор некорректный, пожалуйста повторите.")
		ch = int(input())

	return ch
'''
#--------------------------------------------------------------------------------

def player_go_to_forest(l_char, gf, kill_enemy):

	wolf = Enemy("Wolf", 10, 2)
	#wolf.hp = 10

	print("Вы идёте к лесу.")
	print("Перед вами тропа.")
	gf.enter()
	print("Другово пути идти вы не видите и по этому идёте по тропе.")
	gf.enter()
	print("Внезапно на вас нападает волк.")
	print("Он ловкий меткий, но довольно слабый.")
	gf.enter()
	print("Оружия у вас не оказалось, поэтому придётся отбиваться кулаками.")

	

	while kill_enemy != 1:
		print("1 - Ударить волка кулаком")
		print("2 - Ударить волка ногой")
		print("3 - Подождать атаки волка, а потом контратаковать.")
		ch = gf.player_ask_selection("", 1, 3)

		if ch == 1:
			print("Вы пытаетесь ударить волка кулаком, но волк оказался крайне ловким и увернулся.")
			if wolf.die_enemy(gf, l_char) == 1:
				kill_enemy += 1

				print("Вам выпала из волка его шкура.")

				item = Item_standart("Шкура волка 12 медяков", 12, 100001)
				l_char.invent.append(item)
				gf.autosave(l_char)
				return 0

			gf.enter()
		elif ch == 2 and l_char.m < 2:
			print("Вы целитесь по волку, но вы оказались не сильно метким и не попали.")
			print("Вам ранил ногу волк.")
			l_char.hits += 1
			gf.enter()
			
			if l_char.die() == 1:
				l_char.hits = 0
				return 0
		elif ch == 2 and l_char.m >= 2:
			print("Вы оказались довольно метким и зарядили волку по морде!")
			wolf.hp -= 3

			if wolf.die_enemy(gf, l_char) == 1:
				kill_enemy += 1

				print("Вам выпала из волка его шкура.")

				item = Item_standart("Шкура волка 12 медяков", 12, 100001)
				l_char.invent.append(item)
				gf.autosave(l_char)
				return 0

			gf.enter()
			print("Волк упал, но быстро поднялся.")
			gf.enter()
		elif ch == 3 and l_char.exp < 7:
			print("Вы подождали атаки волка и постарались её отбить.")
			print("Так как вы не очень тактичен, вы получили урон и ударили в ответ.")
			l_char.hits += 1

			if l_char.die() == 1:
				l_char.hits = 0
				return 0

			wolf.hp -= 3
		elif ch == 3 and l_char.exp >= 7:
			print("Вы подождали атаки волка и постарались её отбить.")
			print("Вы оказались крайне такчины и ударили волка критичиским ударом.")


			wolf.hp -= 6

			if wolf.die_enemy(gf, l_char) == 1:
				kill_enemy = 1

				print("Вам выпала из волка его шкура.")

				item = Item_standart("Шкура волка 12 медяков", 12, 100001)
				l_char.invent.append(item)
				gf.autosave(l_char)
				return 0




	
	gf.autosave(l_char)
	return 0


#------------------------------------------------------------------------------------------------------------


def battle_with_troll(l_char, troll, gf):
	enemy_kill = 0

	while enemy_kill != 1:

		gf.update(l_char)

		print("1 - Ударить противника в голову")
		print("2 - Ударить противника в тело")
		print("3 - Ударить противника в руки")
		print("4 - Ударить противника в ноги")

		ch = gf.player_ask_selection("", 1, 4)

		if ch == 1:
			if l_char.m < 3:
				print(l_char.miss())
			elif l_char.m >= 3:
				print("Вы попали по Троллю")
				troll.hp -= l_char.take_weap.hit + random.randrange(3) + l_char.s
				print("И примерно нанесли - " + str(l_char.take_weap.hit))
				print("Жизни тролля - " + str(troll.hp))
				enemy_kill = troll.die_enemy(gf, l_char)

				gf.enter()
		elif ch == 2:
			if l_char.m < 1:
				print(l_char.miss())
				print(l_char.m)
			elif l_char.m >= 1:
				print("Вы попали по Троллю")
				troll.hp -= l_char.take_weap.hit + l_char.s
				print("И примерно нанесли - " + str(l_char.take_weap.hit))
				print("Жизни тролля - " + str(troll.hp))
				enemy_kill = troll.die_enemy(gf, l_char)

				gf.enter()
		elif ch == 3:
			if l_char.m < 2:
				print(l_char.miss())
			elif l_char.m >= 2:
				print("Вы попали по Троллю")
				troll.hp -= l_char.take_weap.hit + random.randrange(2) + l_char.s
				print("И примерно нанесли - " + str(l_char.take_weap.hit))
				print("Жизни тролля - " + str(troll.hp))
				enemy_kill = troll.die_enemy(gf, l_char)

				gf.enter()
		elif ch == 4:
			if l_char.m < 2:
				print(l_char.miss())
			elif l_char.m >= 2:
				print("Вы попали по Троллю")
				troll.hp -= l_char.take_weap.hit + random.randrange(1) + l_char.s
				print("И примерно нанесли - " + str(l_char.take_weap.hit))
				print("Жизни тролля - " + str(troll.hp))
				enemy_kill = troll.die_enemy(gf, l_char)

				gf.enter()

		r_ch = random.randrange(1, 8)
		
		if r_ch == 1:
			print("Вас сильным ударом в туловище отбросил на 10 метров Тролль")
			gf.enter()
			l_char.hits += 2
			#if l_char.die == 1:
			#	return 0

			print("Вы довольно сильно ранены.")
			gf.enter
		elif r_ch == 2:
			print("Вас Значительно не плохо ударил Тролль")
			gf.enter()
			l_char.hits += 1
			#if l_char.die == 1:
			#	return 0

			print("Вы получили серьёзный ушиб.")
			gf.enter()
		elif r_ch == 3 or r_ch == 4 or r_ch >= 5:
			print("Тролль замахнулся, но не попал.")
			gf.enter()
			l_char.hits += 0
			if l_char.die == 1:
				return 0

			print("Ваше состояние не изменилось.")
			gf.enter()




def player_go_to_cave(l_char, gf):
	

	print("При входе в пещеру вы натыкаетесь на стену, ")
	print("исписанную непонятными надписями.")
	gf.enter()
	print("Приглядевшись, вы видите, что это молитвы древним богам.")
	gf.enter()

	touch = 0

	while touch != 1:
		ch = gf.player_ask_selection("1 - Осмотреться вокруг, 2 - внимательно осмотреть стену.", 1, 2)

		if ch == 1:
			print("Вы осматриваетесь и из чего-то существенного видите только камень.")
			ch = gf.player_ask_selection("1 - Взять камень, 2 - ничего не делать", 1, 2)

			if ch == 1:
				print("Камень находится в вашем инвентаре.")
				item = Weapon("Камень", 2, 3, 1, 200001, 0)
				l_char.weap.append(item)

				gf.update(l_char)

		elif ch == 2:
			touch = 1

	print("Вы касаетесь стены и она внезапно рушится.")
	print("Вдруг, откуда не возьмись появляется тролль")
	
	troll = Enemy("Troll", 38, 2)

	l_char.search_weapon()

	gf.enter()



	l_char.choose_weap(gf)
	gf.enter()

	battle_with_troll(l_char, troll, gf)

	l_char.return_weap()


	ch = gf.player_ask_selection("1 - Обыскать пещеру, 2 - Уйти", 1, 2)

	if ch == 1:
		print("Вы начинаете обыскивать пещеру.")
		gf.enter()
		some_money = gf.find_some_money(50)
		print("Вы находите " + str(some_money) + " медяков")
		l_char.add_money(some_money)
		gf.enter()

		print("Вы находите странную книгу. Она находится в вашем инвентаре.")
		item = Item_special("Красная книга '2'", 100002)
		l_char.invent.append(item)
	else:
		gf.autosave(l_char)
		return 0

	gf.autosave(l_char)
	return 0




#---------------------------------------------------------------------------------------------------



def player_go_to_chirch(l_char, gf):

	print("Вы идёте к храму...")
	print("Нажмите Enter для продолжения.")
	enter = input()

	print("Вдруг в своей голове ты начинаешь слышать три разных голоса...")
	print("Вспомни меня... - голос 1.")
	print("Мы умираем - голос 2.")
	print("Ты должен идти на север - голос 3.")
	print("Найди Элерика... - голос 1.")

	print("Нажмите Enter для продолжения.")
	enter = input()

	return 1

#--------------------------------------------------------------------------------

def return_funk_mission(l_char, gf):
	player_went_to_forest = 0
	player_went_to_cave = 0
	player_went_to_chirch = 0
	
	kill_enemy = 0
	funk = 0
	print("  ")
	print("  ")
	print("  ")
	print("Время клонится к закату.")
	print("Нажмите Enter для продолжения.")
	enter = input()
	print("  ")
	print("Внезапно в голове у вас сильно помутнело и вас начало клонить в сон.")
	print("Вы сильно пытались устоять на ногах, но вас сломило, вы упали на пол и уснули.")
	print("Нажмите Enter для продолжения.")
	enter = input()
	print("Вам начинает сниться сон....")
	print("Нажмите Enter для продолжения.")
	enter = input()

	

	while funk == 0:
		
		print("Перед вами 3 тропы:")
		print("1 - К лесу")
		print("2 - В пещеру")
		print("3 - К храму")
		print("Куда пойдёте?")

		ch = gf.player_ask_selection("", 1, 3)

		if ch == 3 and player_went_to_chirch == 0:
			funk = player_go_to_chirch(l_char, gf)
			player_went_to_chirch = 1
		elif ch == 1 and player_went_to_forest == 0:
			funk = player_go_to_forest(l_char, gf, kill_enemy)
			player_went_to_forest = 1
		elif ch == 2 and player_went_to_cave == 0:
			funk = player_go_to_cave(l_char, gf)
			player_went_to_cave = 1
		else:
			print("Вы уже ходили по этой тропе.")
			gf.enter()

	gf.enter()
	print("Вы внезапно просыпаетесь, думая, что это - просто страшный кошмар.")
	print("Но вот на ваших глазах перед вами появляются все те предметы, которые")
	print("вы нашли во время сна, и переносятся в ваш инвентарь.")

	l_char.work_end += 1
	l_char.work_finish.append(1)
	gf.update(l_char)

	gf.play_menu(l_char, gf, 0)

#=====================================================================================================================

def end_005(l_char, gf):
	print('Вы приходите в бар садитесь за стол.')
	gf.enter()
	print('Торговец - Меня к стати зовут Хильгримм, а вас как.')
	gf.enter()
	print('Вы - ' + l_char.name + '. Приятно познакомиться.')
	gf.enter()

	print('Хильгримм: Хорошо, что ты им задал. Давно не встречал такого смелого воина.')
	gf.enter()
	print('Я думаю, что ты можешь сравниться с героями древности. ')
	gf.enter()
	print('Но это я думаю, а уверен я в том, что надо выпить!')

	gf.enter()
	print('')
	print('1 - Согласиться.')
	print('2 - Не пить.')

	ch = gf.player_ask_selection('', 1, 2)

	if ch == 1:
		print('Вы начали пить и быстро вырубились.')
		gf.enter()
		print('Вы проснулись на полу трактира. Рядом лежит револьвер а с ним записка')
		gf.enter()
		print('"Прошу принять его в оплату за ваш подвиг. Уверен, такому храброму войну он \
			сослужит добрую службу. Я проснулся в этом трактире на заре и уже уезжаю. \
			Вас я будить не стал. -Хильгримм Годрисон."')
		gf.enter()
		print('Вы встаёте из-за стола улыбаетесь и уходите. Ваша голова раскалываетяс от похмелья.')
		gf.enter()
		l_char.weap.append(Weapon("Револьвер обычный", 10, 1, 190, 68, 9))
	else:
		print('Хильгримм: А это зря!!')
		gf.enter()
		print('Купец выпивает очень много и пьянеет')
		gf.enter()
		print('1 - Попробовать обокрасть')
		print('2 - Уйти')

		ch = gf.player_ask_selection('', 1, 2)

		if ch == 1:
			if l_char.l >= 2:
				print('Вы успешно украли 200 медяков')
				l_char.mon += 200
			else: print('У вас ничего не получилось, но Хильгримм ничего не заметил.')


	gf.enter()
	print('Задание выполнено! Вы получили 100 единиц опыта.')
	l_char.exp += 100
	l_char.work_finish.append(5)
	gf.update(l_char)
	gf.enter()


#=====================================================================================================================

def battle_005_2(l_char, gf):
	global money
	print('Вы с купцом движитесь к повозке, купец находится позади вас. \n \
		Вы слезаете с лошади и говорите: "Я привёл вам купца, а теперь умрите!!!" \n \
		Купец расстреливает каждого из бандитов с шестизарядного револьвера.')

	gf.enter()

	print('1 - Обыскать бандитов')
	print('2 - Не обыскивать бандитов')

	ch = gf.player_ask_selection('', 1, 2)

	if ch == 1:
		print('Вы нашли Ржавую саблю (не годится как оружие), метку с волком и 60 медяков.')
		l_char.invent.append(Item_standart('Ржавая сабля (не годится как оружие)', 8, 200002))
		l_char.invent.append(Item_special('Метка с изображением волка', 200004))
		l_char.mon += 60
		gf.update(l_char)


	if money == 1:
		print('Купец вас сердечно благодарит, даёт вам в уплату 80 медяков \
			и предлагает вам сходить в бар за его счёт, вы конечно же соглашаетесь')
		l_char.mon += 80
		gf.enter()
		gf.update(l_char)
	elif money != 1:
		print('Купец вас сердечно благодарит \
			и предлагает вам сходить в бар за его счёт, вы конечно же соглашаетесь')
		gf.enter()
		gf.update(l_char)

	gf.enter()
	end_005(l_char, gf)



#=====================================================================================================================
def battle_005_3(l_char, gf):

	bandit_01 = Enemy("Бандит первый", 20, 1)
	bandit_02 = Enemy("Бандит второй", 20, 1)
	bandit_03 = Enemy("Бандит третий", 20, 1)
	bandit_05 = Enemy("Бандит пятый", 20, 1)

	enemyes = []
	enemyes.append(bandit_01)
	enemyes.append(bandit_02)
	enemyes.append(bandit_03)
	enemyes.append(bandit_05)

	bandit_main = Enemy("Глава бандитов", 32, 1)
	enemyes.append(bandit_main)

	gf.battle(gf, l_char, enemyes)
	gf.update(l_char)

	print('Вы успешно сразились с бандитами')
	gf.enter()

	print('1 - Обыскать бандитов')
	print('2 - Не обыскивать бандитов')

	ch = gf.player_ask_selection('', 1, 2)

	if ch == 1:
		print('Вы нашли Ржавую саблю (не годится как оружие) и 60 медяков.')
		l_char.invent.append(Item_standart('Ржавая сабля (не годится как оружие)', 8, 200002))
		l_char.mon += 60
		gf.update(l_char)
		gf.enter()
	print('')
	print('1 - Обыскать купца')
	print('2 - Уйти')

	ch = gf.player_ask_selection('', 1, 2)
	if ch == 1:
		print('Вы нашли Обычный револьвер и 200 медяков.')
		l_char.weap.append(Weapon("Револьвер обычный", 10, 1, 190, 68, 9))
		l_char.mon += 200
		gf.update(l_char)
		gf.enter()

	print('Задание успешно завершено! Вы получили 100 опыта.')
	l_char.exp += 100
	l_char.work_finish.append(5)
	gf.update(l_char)



#=====================================================================================================================


def target_005_2(l_char, gf, bd=0):

	print('Вам необходимо отправиться обратно к купцу и снова с ним поговорить.')
	gf.enter()

	if bd == 0:
		if money == 1:
			print('Купец вас сердечно благодарит, даёт вам в уплату 80 медяков \
				и предлагает вам сходить в бар за его счёт, вы конечно же соглашаетесь')
			l_char.mon += 80
			gf.enter()
			gf.update(l_char)
			end_005(l_char, gf)
		elif money != 1:
			print('Купец вас сердечно благодарит \
				и предлагает вам сходить в бар за его счёт, вы конечно же соглашаетесь')
			gf.enter()
			gf.update(l_char)
			end_005(l_char, gf)
	elif bd != 0:
		print('1 - Сказать о прячущихся бандитах')
		print('2 - Не сказать о прячущихся бандитах')

		ch = gf.player_ask_selection("", 1, 2)

		if ch == 1:
			print('Купец достаёт револьвер и говорит: \"Выдвигаемся!\"')
			battle_005_2(l_char, gf)
		elif ch == 2:
			print('Вы отправились с купцом к его товару, но вдруг неожиданно для купца \
				из-за кустов появляются бандиты и нападают на купца, тот успел выстрельнуть из револьвера \
				и убить 4-того бандита.')
			gf.enter()
			print('Бандиты говорят: Слушай, а почему бы нам не убить тебя и не забрать у тебя всё?..\
				начинается драка.')
			battle_005_3(l_char, gf)





#=====================================================================================================================

def battle_005_1(l_char, gf, bandits):
	global bd
	bd = bandits


	bandit_01 = Enemy("Бандит первый", 20, 1)
	bandit_02 = Enemy("Бандит второй", 20, 1)
	bandit_03 = Enemy("Бандит третий", 20, 1)
	bandit_04 = Enemy("Бандит четвёртый", 20, 1)
	bandit_05 = Enemy("Бандит пятый", 20, 1)

	enemyes = []
	enemyes.append(bandit_01)
	enemyes.append(bandit_02)
	enemyes.append(bandit_03)
	enemyes.append(bandit_04)
	enemyes.append(bandit_05)

	if bd == 6:
		bandit_main = Enemy("Глава бандитов", 32, 1)
		enemyes.append(bandit_main)

	gf.battle(gf, l_char, enemyes)












def start_005(l_char, gf, m):
	global money
	money = m
	print("Необходимо отправиться к воротам!")

	while l_char.loc_town != 3:
		print("1 - Пойти направо")
		print("2 - Пойти налево")
		print("3 - Пойти прямо")
		print("4 - Спросить у торговца - куда идти.")

		ch = gf.player_ask_selection("", 1, 4)

		if ch == 1:
			print("Вы пошли направо и дошли до своего дома.")
			gf.enter()
		elif ch == 3:
			print("Вы пошли прямо и зашли в переулок, в который возможно когда-то уже заходили.")
			gf.enter()
		elif ch == 2:
			print("Вы пошли налево и наткнулоись на стойку лошадей. Продавца небыло на месте и вам пришлось взять одну.")
			gf.enter()
			l_char.loc_town = 3
		elif ch == 4:
			print("Торговец: Вроде надо налево. Там лошадей взять можно.")
			gf.enter()

	print("Вы Прискакали к стене.")
	gf.enter()


	while True:

		print("1 - Пойти на север")
		print("2 - Пойти на запад")
		print("3 - Пойти на восток")

		ch = gf.player_ask_selection("", 1, 3)

		if ch == 1:
			print("Вы собирались пойти на север, как вспомнили, что вы просто вернётесь домой.")
			gf.enter()
		elif ch == 2:
			print("Вы пошли на запад")
			gf.enter()
			break
		elif ch == 3:
			print("Вы пошли на восток но нам была только стена, только стена и ещё встречалась стена.")
			gf.enter()


	print("Вы выходите на тракт и идёте по нему")
	gf.enter()
	print('Идёте...')
	gf.enter()
	print('Идёте...')
	gf.enter()
	print('Идёте...')
	gf.enter()

	print("Вдруг вы замечаете разбитую повозку и сидящих рядом с ней бандитов.")
	gf.enter()
	print("Один из них вскакивает")
	gf.enter()

	#----------------------------------------------

	print("Главарь бандитов: О! Гляди, парни, кажется, у нас тут герой нашёлся! ")
	print("Даю дружеский совет: вали отсюда. ")
	gf.enter()

	print("1 - И не подумаю. Умрите!")
	print("2 - Господа, мы можем договориться! ")

	ch = gf.player_ask_selection("", 1, 2)

	if ch == 1:
		battle_005_1(l_char, gf, 6)
	elif ch == 2:
		print("Главарь бандитов заинтересованно смотрит на игрока: и что ты можешь нам предложить? ")
		print("Бандит подходит ближе.")
		gf.enter()

		print("1 - Смерть!")
		print("2 - Вы притаитесь в кустах, а я приведу сюда торговца. Убьём его и разделим то, что у него есть.")

		ch = gf.player_ask_selection("", 1, 2)

		if ch == 1:
			print("Вы быстро убиваете главаря.")
			battle_005_1(l_char, gf, 5)
			target_005_2(l_char, gf, 0)
		elif ch == 2:
			print("Главарь: Хм, а ты прав. Я согласен.")

		target_005_2(l_char, gf, 6)





def work_005(l_char, gf):
	gf.update(l_char)
	money = 1

	if l_char.find_work(6) == False:
		print("Ну что, передумали?")

		print("1 - Да")
		print("2 - Нет")

		ch = gf.player_ask_selection("", 1 , 2)

		if ch == 1:
			money = 3
			start_005(l_char, gf, money)
			return
		else:
			return

	print("Вы подходите к торговцу, который что-то крайне возмущённо говорит.")
	gf.enter()
	print("Торговец: Эти Варнийцы ещё хуже Анрогоцев! Жадные ублюдки!")
	gf.enter()
	print("Они отобрали у меня 90% товара и назвали это пошлиной!")
	gf.enter()
	print("Подумать только... ")
	print("Какая к дьяволу пошлина, это настоящий грабёж!")
	gf.enter()
	print("Теперь вся поездка не окупится! Мне даже не на что добраться до дома!")
	gf.enter()

	print("1 - Вступить в разговор")
	print("2 - Уйти, будто ничего небыло")

	ch = gf.player_ask_selection("", 1, 2)

	if ch == 2:
		return
	

	print("Вы: Простите, сир, из какой вы страны?")
	print("Торговец: Из Локрии.")
	gf.enter()
	print("Вы: в таком случае, пошлина должна быть не более 10%. ")
	print("Она такова ещё со времён Расцвета Магии. Скорее всего, ")
	print("вы просто наткнулись на бандитов, прикинувшихся стражей. ")
	gf.enter()
	print("Торговец: Вот чёрт! Вы похожи на воина, добрый человек. ")
	print("Не могли бы вы помочь мне вернуть мой товар? ")
	gf.enter()

	print("1 - Конечно, но не бесплатно.")
	print("2 - Безусловно!")
	print("3 - У меня пока нет времени.")

	ch = gf.player_ask_selection("", 1, 3)

	if ch == 1:
		print("Ох, спасибо. Буду ждать вас.")
		start_005(l_char, gf, money)
	elif ch == 2:
		print("Ох, спасибо. Буду ждать вас.")
		money = 2
		start_005(l_char, gf, money)
	elif ch == 3:
		print('Эх, очень жаль. Что ж, может вы ещё передумаете... ')
		print("Я предлагаю вам плату в 50% от моего товара!")
		gf.enter()

		print("1 - Я согласен!")
		print("2 - Вы меня не убедили.")

		ch = gf.player_ask_selection("", 1, 2)

		if ch == 1:
			pass
		else:
			print("Прощайте.")
			l_char.work_end.append(6)
			gf.update(l_char)
			return


#=====================================================================================================================
def battle_003_1(l_char, gf):
	gf.battle(gf, l_char, [Enemy('Охранник подвала', 25, 1),])
	print('Вы успешно прорвались через охранника')
	gf.enter()

def battle_003_2(l_char, gf):
	gf.battle(gf, l_char, [Enemy('Глава банды Кирианцев - Харон', 55, 1),])
	print('Вы победили в бою против Главы банды и получили 70 ед. опыта')
	l_char.exp += 70
	gf.update(l_char)
	gf.enter()

def battle_003_4(l_char, gf):
	enemyes = []
	enemyes.append(Enemy('Бедняк 1', 15, 1))
	enemyes.append(Enemy('Бедняк 2', 15, 1))
	enemyes.append(Enemy('Бедняк 3', 15, 1))
	enemyes.append(Enemy('Бедняк посильнее', 20, 1))

	gf.battle(gf, l_char, enemyes)
	print('Вы сразили всех бедняков, что на вас напали.')
	if l_char.hits > 1: l_char.hits -= 2

def battle_003_5(l_char, gf):
	enemyes = []
	enemyes.append(Enemy('Охранник с ружьём', 20, 1, 4))
	enemyes.append(Enemy('Охранник с саблей', 25, 1, 2))
	enemyes.append(Enemy('Охранник с алебардой', 25, 3))
	enemyes.append(Enemy('Капитан охраны (вооружён револьвером)', 40, 1, 2))

	gf.battle(gf, l_char, enemyes)

def battle_003_7(l_char, gf):
	enemyes = []
	enemyes.append(Enemy('Стражник с мечом', 30, 1, 4))
	enemyes.append(Enemy('Стражник с аркебузой', 20, 1, 6))
	enemyes.append(Enemy('Стражник с гизармой', 30, 1, 5))

	gf.battle(gf, l_char, enemyes)



def work_003_check_metka(l_char, gf):
	if l_char.find_item('Метка с изображением волка'):
		print('Вы: Конечно! Вы показываете метку с изображением волка')
		return True
	else:
		print('Эмм... какую метку?')
		gf.enter()
		print("Харон: Без метки тебя бы не пропустили... В любом случае, лишние уши нам ни к чему.")
		gf.enter()
		print("Вам придётся драться с Хароном.")
		battle_003_2(l_char, gf)
		return False

def work_003_dialog_8(l_char, gf):
	print('Вира:(оборачиваясь и выхватывая лук): Какого чёрта! Что ты творишь?!')
	gf.enter()
	print('Кирианец: Ваша война и этот поход безнадёжны. Вы бы всё равно умерли, а так мне за это ещё и заплатят.')
	gf.enter()
	print('Эй, ты! Вы проиграли. Присоединяйся, и мы разделим награду.')
	gf.enter()

	print('1 - Пошёл ты...')
	print('2 - Я согласен.')

	ch = gf.player_ask_selection('', 1, 2)

	if ch == 2:
		print('Кирианец убивает Виру, после чего в комнату вбегает капитан стражи.')
		gf.enter()
		print('Капитан(смотрит на труп Виры): Отличная работа. А это ещё кто?')
		gf.enter()
		print('Кирианец: Всё в порядке. Это мой коллега.')
		gf.enter()
		print('Капитан кивает и протягивает игроку и кирианцу мешки с монетами.')

		print('1 - Обыскать трупы')
		print('2 - Продолжить')

		ch = gf.player_ask_selection('', 1, 2)

		if ch == 1:
			print('Вы нашли:')
			print('Кожаный доспех, Клинок одиночный, Лук средний,')
			print('Клинки боевые, Усыпляющий дротик (можно использовать в определённых квестовых ситуациях.)')

			l_char.invent.append(Clothes("Кожаный доспех", 80, 117, 10))
			l_char.weap.append(Weapon("Клинок одиночный", 3, 9, 65, 76, 0))
			l_char.weap.append(Weapon("Лук средний", 6, 0, 210, 49, 1))
			l_char.weap.append(Weapon("Клинки боевые", 7, 9, 145, 77, 0))
			l_char.invent.append(Item_special('Усыпляющий \
дротик( можно использовать в определённых квестовых ситуациях.', 200003))


		print('Квест завершён, Вы получили 370 опыта и 150 медяков')
		l_char.exp += 370
		l_char.mon += 150
		l_char.work_finish.append(3)
		gf.update(l_char)
		return


	print('Кирианец стреляет вам в руку и вы теряете оружие.')
	gf.enter()
	print('1 - Прыгнуть на кирианца и закрыть Виру собой. (Начать особый квест)')
	print('2 - Подхватить оружие и прыгнуть в окно.')

	ch = gf.player_ask_selection('', 1, 2)

	if ch == 2:
		print("Вира успевает прокричать «Беги в Кирт'аррош», \
вы выпрыгиваете в окно и приземляетесь на какой-то торговый латок, который забыли свернуть. \
Вы спрыгиваете с него, и воспользовавшись всеобщей суматохой, сбегаете и срываете маску. \
К счастью, стража не успевает заметить вас.")
		gf.enter()
		print('Квест завершён, Вы получили 300 опыта')
		l_char.exp += 300
		l_char.work_finish.append(3)
		gf.update(l_char)
		return


	print('Вы прыгаете на кирианца, пуля прошивает вам бок.')
	gf.enter()
	print('Вы падаете на землю, захлёбываясь собственной кровью.')
	gf.enter()
	print('Последнее, что вы видит — вскакивающая Вира. Кирианка ловко перерезает горло своему бывшему союзнику')
	gf.enter()
	print('После чего в ваших глазах мутнеет.')
	print('Квест завершён, Вы получили 300 опыта...')
	gf.enter()
	l_char.exp += 300
	l_char.work_finish.append(3)
	l_char.work = 'Свет в конце тоннеля'
	gf.update(l_char)
	return

#=====================================================================================================================
def work_003_4(l_char, gf):
	l_char.helpers.append(TeamMate('Вышибала, вооружён ружьём.', 20, 4))
	l_char.helpers.append(TeamMate('Харон', 30, 2))
	l_char.helpers.append(TeamMate('Солдат', 15, 2))
	l_char.helpers.append(TeamMate('Солдат', 15, 2))
	l_char.helpers.append(TeamMate('Вира(вооружена луком и ножами для ближнего боя)', 15, 1, ['Ярость']))
	gf.update(l_char)

	print('Вира: Отлично. Мы тебя ждали.')
	gf.enter()
	print('Отряд инспекторов  в основном двигается по главным улицам.')
	gf.enter()
	print('Пытаться перехватить их там - самоубийство.')
	gf.enter()
	print('В один момент они свернут в Грегсвилль — район неподалёку от трущоб.')
	gf.enter()
	print('Стражи там значительно меньше, да и лишних глаз не будет.')
	gf.enter()
	print('Перехватим их там. Следуй за мной.')
	gf.enter()
	print('Преодолев сеть из улиц, поворотов и площадей, вы и кирианский отряд добираетесь до Грегсвилля.')
	gf.enter()
	print('Вира говорит, что вы должены спрятаться за поворотом и заблокировать выход инспекторам.')
	gf.enter()
	print('На горизонте появляется нужный отряд, Вира даёт отмашку, и кирианцы прячутся, пусть и не слишком хорошо.')
	gf.enter()
	print('Видно, что эти воины не привыкли скрываться. ')
	gf.enter()
	print('Сидя в своём укрытии, вы слышите разговор двоих солдат:')
	gf.enter()
	print('- Слушайте, капитан, а что, ежели мы, ну, немного позаимствуем у этих банкиров...')
	gf.enter()
	print('Зарплату-то нам крохотную платят, а в Локрии, я слыхал, она побольше будет.')
	gf.enter()
	print('-Заткнись! Не стоит говорить об этом на улице. А что и у кого заимствовать, я сам разберусь.')
	gf.enter()
	print('Ещё раз заикнёшься об этом — под трибунал пущу, ясно тебе.')
	gf.enter()
	print('Третий голос: Постойте-ка капитан. Видите вон тех ребят. Как-то странно они стоят. Небось засаду готовят.')
	gf.enter()
	print('Капитан: Сейчас прове...')
	gf.enter()
	print('Вира метким выстрелом убивает капитана')
	gf.enter()

	battle_003_7(l_char, gf)

	print('Бой завершился успешно!')
	gf.enter()
	print('Кирианцы скидывают трупы в трущобы (они расположены ниже основных районов), \
предварительно надев униформу инспекторов и направляются в банк.')
	gf.enter()
	print('Там их спокойно пропускают, и они проходят на второй этаж.')
	gf.enter()
	print('У входа в хранилище стоит двое охранников.')
	gf.enter()
	print('Охранник: Эй, господа, предъявите удостоверение. Мы не можем вас так просто пропустить.')
	gf.enter()
	print('1 - Удостоверение?')
	print('2 - Попробовать подкупить охранников за 100 медяков')
	print('3 - Попробовать подкупить охрану за 1000 медяков.')
	if l_char.s >= 3:
		print('4 - Вот чёрт! Смотри! (резко ударить обернувшегося охранника)')
		ch = gf.player_ask_selection('', 1, 4)
	else:
		ch = gf.player_ask_selection('', 1, 3)

	if ch == 4:
		print('Вы вырубаете охранника ловким ударом, забираете ключ и входите в хранилище.')
		gf.enter
	elif ch == 1:
		print('Охранник: Ага, значит, проникаем незаконно? Вали их!')
		gf.enter()
		print('Вира резко выпускает стрелу в одного из охранников, второго убивает Харон ударом в шею.')
		gf.enter()
		print('Однако на крики сбегаются охранники снизу.')
		gf.enter()
		print('Харон бросается к лестнице, чтобы их задержать и бросает на лестницу бомбу.')
		gf.enter()
		print('Охранники погибают, но в Харона попадает несколько пуль, и он умирает.')
		for i in range(len(l_char.helpers)):
			g = l_char.helpers[i]
			if g.name == 'Харон':
				del l_char.helpers[i]
				break
		gf.update(l_char)
		gf.enter()
		print('Вира берёт ключ с трупа охранника у входа и вбегает в хранилище.')
	elif ch == 2:
		print('Охранник: Нас таким не купишь! Бей их!')
		gf.enter()
		print('Вира резко выпускает стрелу в одного из охранников, второго убивает Харон ударом в шею.')
		gf.enter()
		print('Однако на крики сбегаются охранники снизу.')
		gf.enter()
		print('Харон бросается к лестнице, чтобы их задержать и бросает на лестницу бомбу.')
		gf.enter()
		print('Охранники погибают, но в Харона попадает несколько пуль, и он умирает.')
		for i in range(len(l_char.helpers)):
			g = l_char.helpers[i]
			if g.name == 'Харон':
				del l_char.helpers[i]
		gf.update(l_char)
		gf.enter()
		print('Вира берёт ключ с трупа охранника у входа и вбегает в хранилище.')
	elif ch == 3:
		print('Охранник: Меня не купи... * Глядит на деньги * Эм... Ладно, проходите. Только быстро.')
		gf.enter()


	print('Вира хватает связку ключей, лежащую на столе неподалёку и начинает вскрывать ячейки.')
	gf.enter()
	print('Награбленное кирианцы складывают в мешки и выбрасывают из окна в повозку, стоящую там.')
	gf.enter()
	print('Внезапно раздаётся выстрел и Харон умирает.')
	gf.enter()
	if ch == 3:
		print('Вира тихо говорит: Нам не нужны лишние глаза.')
		gf.enter()
		print('Она и Харон подходят к выходу и резко убивают двоих охранников.')
		gf.enter()
		print('Пуля попадает Харону в сердце... Он умирает...')
		for i in range(len(l_char.helpers)):
			g = l_char.helpers[i]
			if g.name == 'Харон':
				del l_char.helpers[i]
		gf.update(l_char)
		gf.enter()
	work_003_dialog_8(l_char, gf)



#=====================================================================================================================
def work_003_3(l_char, gf):
	l_char.helpers.append(TeamMate('Вышибала, вооружён ружьём.', 20, 4))
	l_char.helpers.append(TeamMate('Харон', 30, 2))
	l_char.helpers.append(TeamMate('Солдат', 15, 2))
	l_char.helpers.append(TeamMate('Солдат', 15, 2))
	l_char.helpers.append(TeamMate('Вира(вооружена луком и ножами для ближнего боя)', 15, 1, ['Ярость']))
	gf.update(l_char)

	print('Вы(подходя к воротам банка): А они крепкие. Ну и что вы собрались с ними делать?')
	gf.enter()
	print('Харон: Пусть технологии и причинили много зла, за одну вещь их стоит благодарить.')
	gf.enter()
	print('Игрок: И за что же?')
	gf.enter()
	print('Харон: За взрывчатку.')
	gf.enter()
	print('Харон бросает бомбу в ворота и кричит остальным пригнуться.')
	gf.enter()
	print('Бедняки бросаются на стражу, а вы и кирианцы бежите в банк.')
	battle_003_5(l_char, gf)
	print('Вы и ваши союзники вбегаете на второй этаж банка.')
	gf.enter()
	print('Внезапно разадётся выстрел!')
	gf.enter()
	print('Вира падает на колени.')
	gf.enter()
	print('Пуля попадает Харону в сердце и он умирает.')
	for i in l_char.helpers:
		if i.name == 'Харон':
			i.hp = 0
	gf.update(l_char)
	gf.enter()

	#dialog 8
	work_003_dialog_8(l_char, gf)



#=====================================================================================================================
def work_003_2(l_char, gf):
	print('Харон: Раз ты новичок, полагаю, тебя стоит ввести в курс дела.')
	gf.enter()
	print('К сожалению, мы не можем начать открытое восстание против Локрии.')
	gf.enter()
	print('Поэтому мы вынуждены действовать в других странах и более скрытно, \
хотя по мне- надо просто собраться и перерезать врагам глотки.')
	gf.enter()
	print('Но к делу. В этом городе, неподалёку от площади есть отделение банка Арринхоупа, \
основанного локрийцами.')
	gf.enter()
	print('Разграбив его, мы хоть как-то снизим их доход.')
	gf.enter()
	print('Вира: Вот только с планом ограбления вышла заминка.')
	gf.enter()
	print('Эти идиоты хотят рваться в банк открыто, просто убивая всех. \
Я же предлагаю проникнуть в банк скрытно.')
	gf.enter()
	print('Вы: у вас есть что-то вроде командира? Пусть он решает.')
	gf.enter()
	print('Харон: Кирианцы- вольный народ. Мы решаем всё вместе.')
	gf.enter()
	print('Вышло так, что ровно половина из нас поддерживает открытую атаку, а вторая половина- скрытное проникновение.')
	gf.enter()
	print('От себя скажу: мы кирианцы, а не какие-то локрийкие крысы, чтобы прятаться и скрываться.')
	gf.enter()
	print('Вира: в общем, решающий голос за тобой.')

	print('1 - Кирианцы куда лучше сражаются открыто. Мы нападём на банк.')
	print('2 - Нас слишком мало, чтобы нападать открыто. Я согласен с Вирой.')

	ch = gf.player_ask_selection('', 1, 2)

	if ch == 1:
		print('Харон: Отлично! Нам потребуются люди.')
		gf.enter()
		print('Идеальная армия для штурма банка-  толпа мятежных бедняков.')
		gf.enter()
		print('Отправляйся в трущобы и подыми народ. Приводи их в полночь на Площадь Освобождения.')
		gf.enter()
		l_char.work.append('Ограбление банка (Пролом в лоб)')
		gf.update(l_char)
		return
	elif ch == 2:
		print('Вира:Хорошо. Нам нужно подготовиться.')
		gf.enter()
		print('В Варнии для проверки банков существуют особые отряды стражи- лиггеры.')
		gf.enter()
		print('Устроим засаду на такой отряд, заберём их форму, и нас пропустят к ячейкам.')
		gf.enter()
		print('Сегодня как раз день проверки. Нужно перехватить отряд.')
		gf.enter()
		print('Я прослежу за ними и сообщу тебе, когда они будут проходить там, где их удобнее взять.')
		gf.enter()
		print('Жди меня здесь вечером.')
		print('Вам требуется отдохнуть дома.')
		gf.enter()
		l_char.work.append('Ограбление банка (Аккуратно по плану) (Вам нужно поспать дома.)')
		gf.update(l_char)
		return



#=====================================================================================================================
def work_003_1(l_char, gf):
	print('Подозрительный тип: Эй, ты! Тебе здесь не рады. А ну пошёл прочь.')
	gf.enter()

	print('1 - Ладно, ладно успокойся (уйти и отказаться от задания)')
	print('2 - А ну отошёл прочь, придурок. Я пришёл к главарю.')
	print('3 - Ох, зря ты это сделал... Сейчас я научу тебя хорошим манерам!')

	if l_char.find_item('Метка с изображением волка'):
		print('4 - Показать метку с изображением волка')
		ch = gf.player_ask_selection('', 1, 4)
	else:
		ch = gf.player_ask_selection('', 1, 3)

	if ch == 1:
		return False
	elif ch == 3: battle_003_1(l_char, gf)
	else: print('Конечно, проходите!')

	#-----------------------------------


	print('Вы входите в помещение и видите там около пятнадцати человек, одетых в меховые плащи и короткие штаны.')
	if ch == 3:
		print('Харон: Дьявол! Нас обнаружили!')
		battle_003_2(l_char, gf)
		return True
	else:
		print('Главарь Кирианцев: О, новобранец. Что ж, для нас каждый человек на счету.')
		gf.enter()
		print('Какая-то девушка из кирианцев: Харон, не стоит так открыто говорить здесь на Всеобщем. Нас могут услышать.')
		gf.enter()
		print("Харон: Пожалуй, ты права. Ne'ph tarus? Olr dairev humm...")
		gf.enter()

		print('1 - Я не говорю по-кириански или Алькнерски.')
		print('2 - Эм... Ash nazg durbatuluk? ')
		if l_char.rod == 'Кирианец':
			print("3 - Tarh'enn dayor, dannet(Я сам решил к вам присоединится)")
			print("4 - Tirsh, darhen! Os na dor hellcum. (Заткнись, жалкое создание! Ты тут больше не главный.)")
			ch = gf.player_ask_selection('', 1, 4)
		else: ch = gf.player_ask_selection('', 1, 2)

		if ch == 1:
			print("Харон: Что ж, ожидаемо. Нам нужны любые люди.")
			gf.enter()
			print("Вира: Пожалуй, следует его проверить.")
			gf.enter()
			print("Харон: И правда. Эй, новичок, покажи метку.")
			gf.enter()
			if work_003_check_metka(l_char, gf):
				print("Харон: Отлично! Я знал, что без метки сюда не пропускают.")
				gf.enter()
				print("Извини за эти формальности. Вира просто вечно всех в чём-то подозревает.")
				gf.enter()
			else: return True
		elif ch == 2:
			print("Харон(смеясь): Вот, я говорил тебе, Вира! Не может весь отряд состоять из чистокровных кирианцев.")
			gf.enter()
			print("И в Кирт'арроше не каждый сейчас знает древний язык.")
			gf.enter()
			print("Вира: Это не смешно, а подозрительно. Это дело слишком серьёзно, чтоб набирать туда кого попало.")
			gf.enter()
			print("Харон: И правда. Эй, новичок, покажи метку.")
			gf.enter()
			if work_003_check_metka(l_char, gf):
				print("Харон: Отлично! Я знал, что без метки сюда не пропускают.")
				gf.enter()
				print("Извини за эти формальности. Вира просто вечно всех в чём-то подозревает.")
				gf.enter()
			else: return True
		elif ch == 3:
			print("Харон кивает и говорит: Узнаю древний язык.")
			gf.enter()
			print("Если ты его знаешь, нам нечего боятся предательства с твоей стороны.")
			gf.enter()
		elif ch == 4:
			print("Харон: Ash avgur, ha wen tirish, serd! Torn se Kirt'arrosh as wen ger dun ris!\
(сейчас посмотрим, кому придётся заткнуться, пёс! \
Передай в Кирт'аррош, что я не стану никому подчиняться!)")
			gf.enter()
			battle_003_2(l_char, gf)
			return True

	print("Вы входите в доверие к бандитам.")
	work_003_2(l_char, gf)
	return False


#=====================================================================================================================




def start_003(l_char, gf):
	print('Вы отходите в сторону от рыночной площади и сворачиваете в сторону.')
	gf.enter()
	print('Мрак переулка окутывает вас.')
	gf.enter()
	print('Внезапно вы замечаете странного человека, стоящего у входа в какой-то подвал.')
	gf.enter()
	print('Какие-то секунды любопытство борется с опасением.')
	gf.enter()
	print('И вы решаете...')
	gf.enter()

	print('1 - Пройти мимо')
	print('2 - Поговорить с мужчиной (Начать задание "Ограбление по-кириански)"')

	ch = gf.player_ask_selection('', 1, 2)

	if ch == 1:
		gf.update(l_char)
		return
	elif ch == 2:
		if work_003_1(l_char, gf):
			print('Квест успешно завершён! Вы получили 300 опыта!')
			l_char.work_finish.append(3)
			l_char.exp += 300
			gf.update(l_char)
		else:
			gf.update(l_char)
			return

#================================================================================================
