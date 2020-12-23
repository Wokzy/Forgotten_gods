import random
from ElixirItem import *
from Enemy import *




def battle_with_man(l_char, gf, man):
	print("Мужик вырывается и стоит перед вами")
	print("Оружия под рукой у вас не оказалось, поэтому прийдётся драться в рукопашку.")

	while True:
		gf.update(l_char)

		print("1 - Ударить противника в голову")
		print("2 - Ударить противника в тело")
		print("3 - Ударить противника по рукам")
		print("4 - Ударить противника по ногам")

		ch = gf.player_ask_selection("", 1, 4)

		if ch == 1:
			print("Вы нанесли удар в голову")
			man.hp -= random.randrange(l_char.s-1, l_char.s+3)
			print("Вы примерно нанесли " + str(l_char.s) + " единиц урона")
			print("У мужика осталось " + str(man.hp) +  " единиц жизней")
			gf.enter()
		elif ch == 2:
			print("Вы нанесли удар в тело")
			man.hp -= random.randrange(l_char.s-1, l_char.s+2)
			print("Вы примерно нанесли " + str(l_char.s) + " единиц урона")
			print("У мужика осталось " + str(man.hp) +  " единиц жизней")
			gf.enter()
		elif ch == 3:
			print("Вы нанесли удар в руки")
			man.hp -= random.randrange(l_char.s-1, l_char.s+1)
			print("Вы примерно нанесли " + str(l_char.s) + " единиц урона")
			print("У мужика осталось " + str(man.hp) +  " единиц жизней")
			gf.enter()
		elif ch == 4:
			print("Вы нанесли удар по ногам")
			man.hp -= random.randrange(l_char.s-1, l_char.s+2)
			print("Вы примерно нанесли " + str(l_char.s) + " единиц урона")
			print("У мужика осталось " + str(man.hp) +  " единиц жизней")
			gf.enter()

		if man.die_enemy(gf, l_char) == 1:
			gf.update(l_char)
			break

		max_ = 0
		if l_char.l >= 2:
			max_ = 8
		else:
			max_ = 7

		hit = random.randrange(1, max_)

		if hit == 1:
			print("Вас ударили критическим ударом в тело")
			if l_char.s >= 2:
				print("Вы постарались заблокировать удар, но он оказался нереально сильным.")
				print("Вы ослабили удар в два раза.")
				l_char.hits += 1
			else:
				l_char.hits -= 2
		elif hit == 2 or hit == 3:
			print("Вас ударили обычным ударом.")
			if l_char.s >= 2:
				print("Вы успешно заблокировали удар.")
				print("Урон от удара вы не получили.")
			else:
				l_char.hits += 1
		else:
			print("Мужик замахнулся, но не попал")


	print("1 - Обыскать мужика")
	print("2 - Уйти")

	ch = gf.player_ask_selection("", 1, 2)

	if ch == 1:
		print("Вы начали обыскивать мужика")
		find_mon = gf.find_some_money(76)
		print("Вы нашли " + str(find_mon) + " медяка(-ов)")
		l_char.mon += find_mon

	print("Также вы нашли 'Gold' карту с пропуском в какой-то подпольный клуб.")

	item = Item_standart("'Gold' карта с пропуском в подпольный клуб", 1200, 1001)
	l_char.invent.append(item)

	
	gf.update(l_char)



def buy_dragon_misson(l_char, gf, man):
	item = RedDragonItem("Красный дракон 0.5", 64, 18)

	if l_char.can_afford(item.price):
		l_char.buy_item(item, item.code)
		gf.update(l_char)
	else:
		battle_with_man(l_char, gf, man)





def beer_battle_misson(l_char, gf, big_man):
	

	print("")
	print("Мужик хватает вас за шиворот и прижимает к полу, держа за шею.")
	gf.enter()
	print("Вы начинаете задыхаться")

	l_char.hits += 1

	gf.enter()
	print("1 - Попробовать вырваться")
	print("2 - Добровольно сдаться")

	ch = gf.player_ask_selection("", 1, 2)

	if ch == 1:
		if l_char.s >= 3:
			print("Вы оказались довольно сильны и заломали руку мужика, вырвав её из под шеи.")
			big_man.hp -= 2
			battle_with_man(l_char, gf, big_man)


		
	elif ch == 2:
		buy_dragon_misson(l_char, gf, big_man)

	print("")




def beer_mission(l_char, gf):
	print("Войдя в бар вы случайно задели стол и опрокинули Красный дракон.")
	gf.enter()
	print("Все внезапно обернулись на звуки разбившегося стекла и резко попрятались.")
	gf.enter()
	print("- Я тут не причём. - писклявым голосом сказал бармен и побежал с криком 'ААААА!!!'")
	gf.enter()
	print("Из-за стола, на котором была разлита выпивка, встал огромный мужик и щёлкнул костяшками пальцев.")
	gf.enter()
	print("- Тебе крышка произнёс он.")
	gf.enter()

	gf.update(l_char)

	big_man = Enemy("Сильный мужик", 21, 1)

	print("1 - Купить новую выпивку")
	print("2 - Драться")
	print("3 - Убежать")
	print("4 - Попробовать договориться")

	ch = gf.player_ask_selection("", 1, 4)

	if ch == 1:
		print("1 - Сказать: 'Только не бей, сейчас куплю бутылку твоего красного дракона.'")
		print("2 - Сказать: 'Не быкуй лучше, если хочешь, чтобы я тебе купил ещё дракона'")

		ch = gf.player_ask_selection("", 1, 2)

		if ch == 1:
			print("Только не бей, сейчас куплю бутылку твоего красного дракона. - говорите вы")
			print("Давай жду... - сказал Мужик")
			buy_dragon_misson(l_char, gf, big_man)
		elif ch == 2:
			print("Не быкуй лучше, если хочешь, чтобы я тебе купил ещё дракона - говорите вы")
			print("Ох, ну ты напросился... - сказал Мужик")
			beer_battle_misson(l_char, gf, big_man)
	elif ch == 2:
		beer_battle_misson(l_char, gf, big_man)
	elif ch == 3:
			print("Вы резко дёрнулись в сторону двери и побежали. Внезапно вы на что-то наступили.")
			print("Вы поскальзнулись и упали. Вы быстро встали, но мужик был уже перед вами.")
			gf.enter()
			beer_battle_misson(l_char, gf, big_man)
	elif ch == 4:
		print("1 - Сказать: 'Слушай мужик, я просто шёл мимо и задел твой напиток случайно...'")
		print("2 - Сказать: 'Ты жить хочешь?  Если да, то давай-ка вали от сюда.'")

		ch = gf.player_ask_selection("", 1, 2)

		if ch == 1:
			print("За нечайно бьют отчаянно! - произнёс мужик.")
			beer_battle_misson(l_char, gf, big_man)
		elif ch == 2:
			print("Размечтался! - произнёс мужик.")
			beer_battle_misson(l_char, gf, big_man)
	l_char.work_finish.append(2)


#===================================================================================
#----------------------------------------------------------------
#===================================================================================

class Beer():

	"""docstring for Beer"""
	def __init__(self):
		self.buy_invent = []



#-------------------------------------------------

	def show_intro(self):
		print("1 - Купить выпивку")
		print("2 - Купить напиток")
		print("3 - Поболтать с барменом")
		print("4 - Поболтать с чуваком за столом.")
		print("5 - Выйти")


	def beer_enter(self, l_char, gf):


		print("Вы вошли в бар")
		print("")

		if l_char.find_work(2):
			beer_mission(l_char, gf)

		print("Выберите продукцию:")

		self.show_intro()

		ch = gf.player_ask_selection("", 1, 4)

		if ch == 1:
			self.buy_drink_sp(l_char, gf)
		elif ch == 2:
			self.buy_drink(l_char, gf)
		elif ch == 3:
			self.talk_with_barmen(l_char, gf)
		elif ch == 4:
			self.talk_with_men(l_char, gf)
		elif ch == 5:
			gf.update(l_char)
			return


#-----------------------------------------------------




	def buy_from_beer(self, l_char, gf, ch, tag):
		if tag == 1:
			if ch == 1:
				item = Item_standart("Виски", 15, 5001)
			elif ch == 2:
				item = Item_standart("Водка", 20, 5002)
			elif ch == 3:
				item = Item_standart("Крепкий эль", 10, 5003)
			elif ch == 4:
				item = Item_standart("Белый дракон", 28, 5004)
			elif ch == 5:
				item = Item_standart("Красный дракон", 64, 5005)
		elif tag == 2:
			if ch == 1:
				item = Item_standart("Морковный сок", 10, 5006)
			elif ch == 2:
				item = Item_standart("Лимончелло", 12, 5007)
			elif ch == 3:
				item = Item_standart("'Жигулёвское'", 20, 5008)
			elif ch == 4:
				item = Item_standart("'Балтика'", 25, 5009)
			elif ch == 5:
				item = Item_standart("'Дикая' смесь дракона", 110, 50010)


		if l_char.can_afford(item.price):
			l_char.buy_item(item, item.code)
			gf.update(l_char)




	def drink_sp_info(self):
		print("Виски - поднимет настроение в любой грустной ситуации.")
		print("")
		print("Водка - Напиток с фентезийных земель с незабываемым вкусом.")
		print("")
		print("Белый дракон - 'напиток, похожий на красный дракон', подробное описание на прилавках рынка.")
		print("")
		print("Красный дракон - 'напиток, известный в мире своей крепкостью', подробное описание на прилавках рынка.")
		print("")



		

	def buy_drink_sp(self, l_char, gf):
		quit = 0

		while quit != 1:

			gf.update(l_char)


			print("Выберите выпивку:")
			print("")
			print("1 - Виски - 20 медяков")
			print("2 - Водка - 15 медяков")
			print("3 - Крепкий эль - 12 медяков")
			print("4 - Белый дракон - 24 медяка")
			print("5 - Красный дракон - 35 медяков")
			print("6 - Информация о продуктах")
			print("7 - Выход")

			ch = gf.player_ask_selection("", 1, 7)

			if ch == 7:
				quit = 1
			elif ch == 6:
				self.drink_sp_info()
			else:
				self.buy_from_beer(l_char, gf, ch, 1)



	def drinks_info(self):
		print("Морковный сок - напиток, поднимающий имунитет, для людей, которые предпочитают")
		print("здоровое питание.")
		print("")
		print("Лимончелло - смесь чистого спирта и сока лимона. 'Взбодрит, да не по детски!'.")
		print("")
		print("'Жигулёвское' - напиток с фентезийных земель, который затягивает, от него почти")
		print("не возможно оторваться. Так бар и зарабатывает.")
		print("")
		print("'Балтика' - Пародия напитка 'Жигулёвское', только без такого крепкого вкуса.")
		print("")
		print("'Дикая' смесь дракона - смесь обсалютно всех спиртых напитков, имеющихся в")
		print("этом баре. Сильно замароженный и продержанный в таком состоянии в течении")
		print("16-ти дней.")
		print("")



	def buy_drink(self, l_char, gf):

		while True:
			print("Выбирайте напиток:")
			print("")
			print("1 - Морковный сок")
			print("2 - Лимончелло (Присудствует спирт)")
			print("3 - 'Жигулёвское'")
			print("4 - 'Балтика'")
			print("5 - 'Дикая' смесь дракона")
			print("6 - Информация о продуктах")
			print("7 - Выход")

			ch = gf.player_ask_selection("", 1, 7)

			if ch == 7:
				break
			elif ch == 6:
				self.drinks_info()
			else:
				self.buy_from_beer(l_char, gf, ch, 2)




	def barmen_dialogs(self, l_char, gf):
		if l_char.find_dialog(1):
			print("Прикинь! Тут я как-то на днях встретил мужика, набухавшегося такого,")
			print("сразу видно, с похмелья! Так вот значит он идёт с бутылкой Крепкого Эля,")
			print("пошатывается и такой...")
			gf.enter()
			print("Как упадёт. Ну тут я не сдержался от смеха, подошёл и давай предлагать")
			print("свою помощь.")
			gf.enter()
			print("В этот день я никуда не торопился, поэтому уделил этому замечательному")
			print("мужчине немного времени. Так вот.")
			gf.enter()
			print("Я к нему подхожу, говорю - 'Молодой! Помощь не нужна'.")
			print("Ну он такой: 'Я сам... Сам я встану... я... Встану щас... Сам..'")
			gf.enter()
			print("Я стою, ржу, давлюсь от смеха.")
			gf.enter()
			print("И снова спрашиваю: 'Мужик ну тебе прям точно помощь не нужна?'")
			gf.enter()
			print("Он уже на серьёзных щах начал мне доказывать, что он обойдётся без меня.")
			print("Посдавил бутылку, потянулся и встал.")



			print("1 - 'Да ну!'")
			print("2 - 'Афигеть!'")

			ch = gf.player_ask_selection("", 1, 2)

			if ch == 1:
				print("Да ну! - говорите вы.")
			elif ch == 2:
				print("Афигеть! - говорите вы.")


			print("Прикинь!! Я и сам сначала думал, что у него нет шансов вообще.")
			print("Но ты не спеши радоваться так сильно!")
			gf.enter()
			print("Вот он встал, пошатнулся пару раз, потянулся за бутылкой и опять")
			print("навернулся!")
			gf.enter()
			print("Тут уже начал собиваться народ, и больше я не увидел.")


			print("1 - Расскажи, что дальше было.")
			print("2 - Блин, прикольная история, чего только с людьми не бывает.")

			ch = gf.player_ask_selection("", 1, 2)

			if ch == 1:
				print("Дальше опять случились чудеса - он встал и пошёл дальше, куда глаза глядят.")
			elif ch == 2:
				print("Что правда, то правда.")

			l_char.dialogs.append(1)
			gf.update(l_char)

			return

		elif l_char.find_dialog(2):
			print("Собираюсь я как-то на рынок, беру деньги, пресчитал их два раза даже,")
			print("подумал заранее, что буду брать и отправился на сам рынок.")
			gf.enter()
			print("Иду, иду, вроде всё нормально.")
			gf.enter()
			print("Захожу на рынок, беру красный дракон.")

			print("1 - Я смотрю ты мажор.")
			print("2 - Выпить вдруг решил по среди бела дня?")

			ch = gf.player_ask_selection("", 1, 2)

			if ch == 1:
				print("Да вот как-то деньги внепно появились, ну я сразу на рынок., за покупками!")
			elif ch == 2:
				print("Ну-у-у. Красный дракон - это не просто выпивка, это целый напиток.")
				print("Так сказал Конфуций в свои времена.")

			print("Собственно слушай дальше.")
			gf.enter()
			print("Вот я уже у столика, расплачиваюсь, а тут вдруг медяков двух не хватает.")
			gf.enter()
			print("Ну! - думаю я, - Может из кармана не достал?")
			print("Смотрю в карман, там тоже нет.")
			gf.enter()
			print(" - Может договоримся, у меня тут медяков 2-х не хватает. - сказал я.")
			gf.enter()
			print("Но тот чувак оказался не таким уж дружелюбным, заставил доплачивать.")
			gf.enter()
			print('Я ему говорю: "Посчитай, может у меня и хватает."')
			gf.enter()
			print("Благо в тот день у меня были мелкие монеты и продавец считал долго.")
			gf.enter()
			print("Он начинает считать, досчитывает до 24-ёх и я ему начинаю рассказывать про")
			print("нынешнюю экономику, он отвлекается, удивляется новостям, придуманным мною")
			print("сейчас и спрашивает, сколько он насчитал уже. Я ему говорю 26.")
			gf.enter()
			print("Так я остался с Красным Драконом.")

			gf.enter()


			l_char.dialogs.append(2)
			gf.update(l_char)

			return

		elif l_char.find_dialog(2) == False:
			print("Диалоги с барменом больше не доступны.")

			gf.enter()
			gf.update(l_char)

			return







	def talk_with_barmen(self, l_char, gf):
		print("Вы подходите к бармену.")

		print("1 - Сказать: 'Здравствуй, как жизнь?'")
		print("2 - Сказать: 'Ох, здарова, живётся тяжело последнее время, как сам?'")
		print("3 - Сказать: 'ШЫНДЫР МЫНДЫР!'")
		print("4 - Сказать: 'Здарова! Что нового расскажешь?'")
		print("5 - Уйти")

		ch = gf.player_ask_selection("", 1, 5)

		if ch == 5:
			return
		elif ch == 1:
			print("Да так. Знаешь живётся не плохо.")
		elif ch == 2:
			print("Живу не плохо, последнее время много заработал.")
		elif ch == 3:
			print("Ну здравствуй, расхититель гробниц фараона.")
		elif ch == 4:
			print("")


		gf.enter()
		self.barmen_dialogs(l_char, gf)




	def talk_with_men(self, l_char, gf):

		print('1 - Сказать: "Приветствую"')
		print('2 - Сказать: "Здравствуй мил человек."')
		print('3 - Сказать: "ШЫНДЫР МЫНДЫР"')
		print('4 - Сказать: "Чики бряк"')
		print('5 - Сказать: "Коничива"')
		

		ch = gf.player_ask_selection("", 1, 5)

		if ch == 1:
			print('"Ну здарова!" - сказал человек за столом.')
			self.man_dialogs(l_char, gf)
		elif ch == 2:
			print('"Взаимно."')
			self.man_dialogs(l_char, gf)
		elif ch == 3:
			print("Здравствуй, расхититель гробниц фараона.")
			self.man_dialogs(l_char, gf)
		elif ch == 4:
			print('"4ku BPuKu B DAMKu"')
			self.man_dialogs(l_char, gf)
		elif ch == 5:
			print("Коничив....")
			self.man_dialogs(l_char, gf)




	def man_dialogs(self, l_char, gf):

		if l_char.find_dialog(8):

			print("Ты был хоть раз в учебном лагере?")

			print("1 - Да")
			print("2 - Нет")

			ch = gf.player_ask_selection("", 1, 2)


			if ch == 1:
				print("Значит скорее всего ты знаешь, какие мучения надо пройти, чтобы научиться ")
				print("владеть огнестрельным оружием.")
			elif ch == 2:
				print("Ох, ты не знаешь, что стоит преодолеть, чтобы научиться")
				print("владеть огнестрельным оружием.")
			l_char.dialogs.append(8)
		else: print('Диалоги больше не доступны')