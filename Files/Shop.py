from GameFunctions import *
import random


class Shop():
	""" useful game function """
	def __init__(self, name):
		#super(Character, self).__init__()
		self.name = name
		self.ask_str = """ Выберите категорию товаров:\n
			1 - Напитки\n
			2 - Еда\n
			3 - Оружие\n
			4 - Одежда\n
			5 - Специальное\n
			6 - Инвентарь и деньги\n
			7 - Выход\n """

		self.sel_min = 1
		self.sel_max = 7


		self.shop_elixir_items = []
		self.shop_el_items = []
		self.shop_hardel_items = []
		self.shop_whitedragon_items = []
		self.shop_reddragon_items = []
		self.shop_snake_items = []
		self.shop_vodka_items = []
		self.shop_pig_items = []
		self.shop_mutton_items = []
		self.shop_beef_items = []
		self.shop_dragonmeat_items = []
		self.shop_yagodi_items = []
		self.shop_health_grass_items = []
		#-----------------------------------------------------------
		self.shop_bows_items = []
		self.shop_arrows_items = []
		self.shop_pistols_items = []
		self.shop_cold_weapon_items = []
		self.shop_patrons_items = []
		#-----------------------------------------------------------
		self.shop_head_clothes_items = []
		self.shop_top_items = []
		self.shop_bottom_items = []
		self.shop_shoes_items = []
		self.shop_gloves_items = []
		self.shop_bronya_items = []
		self.shop_mechanic_bronya_items = []
		self.shop_konkistodor_items = []
		#------------------------------------------------------------
		self.shop_zelya_items = []
		self.shop_scopes_items = []
		self.shop_dop_for_weapon_items = []
		self.shop_off_noise_items = []

	#gf = GameFunctions()

	def player_enter(self, l_char):
		self.show_intro(l_char)

	def show_drinks_list(self, l_char):

		if (len(self.shop_elixir_items)):
			print("Эликсиры")

		if (len(self.shop_el_items)):
			print("Эли")

		if (len(self.shop_hardel_items)):
			print("Крепкий Эль")


	def show_intro(self, l_char):
		print("Добро пожаловать в магазин!")
		print("Нажмите Enter для продолжения.")
		enter = input()
		print("Выберите категорию товаров:")
		print("1 - Напитки")
		print("2 - Еда")
		print("3 - Оружие")
		print("4 - Одежда")
		print("5 - Специальное")
		print("6 - Продать вещи")

		if l_char.find_work(5): print("7 - Подойти к неподалёку стоящему торговцу")
		#print("i - Инвентарь и деньги")
		print("q - Выход")




	def is_drinks_selected(self, ch):
		return (ch == 1)

	def is_food_selected(self, ch):
		return (ch == 2)

	def is_weapons_selected(self, ch):
		return (ch == 3)

	def is_clothes_selected(self, ch):
		return (ch == 4)

	def is_special_selected(self, ch):
		return (ch == 5)

	def is_sell_selected(self, ch):
		return (ch == 6)

	def is_talk_selected(self, ch):
		return (ch == 7)

	def is_info_selected(self, ch):
		return (ch == -1)




	def is_drink_elixirs_selected(self, ch):
		return (ch == 1)

	def is_drink_el_selected(self, ch):
		return (ch == 2)

	def is_drink_hardel_selected(self, ch):
		return (ch == 3)

	def is_drink_whitedragon_selected(self, ch):
		return (ch == 4)

	def is_drink_reddragon_selected(self, ch):
		return (ch == 5)

	def is_drink_snake_selected(self, ch):
		return (ch == 6)

	def is_drink_vodka_selected(self, ch):
		return (ch == 7)



#============================================================================


	def is_food_pig_selected(self, ch):
		return (ch == 1)

	def is_food_mutton_selected(self, ch):
		return (ch == 2)

	def is_food_beef_selected(self, ch):
		return (ch == 3)

	def is_food_dragonmeat_selected(self, ch):
		return (ch == 4)

	def is_food_yagodi_selected(self, ch):
		return (ch == 5)

	def is_food_health_grass_selected(self, ch):
		return (ch == 6)

	#======================================================================================

	def is_weapon_bows_selected(self, ch):
		return (ch == 1)

	def is_weapon_arrows_selected(self, ch):
		return (ch == 2)

	def is_weapon_pistols_selected(self, ch):
		return (ch == 3)

	def is_weapon_cold_weapon_selected(self, ch):
		return (ch == 4)

	def is_weapon_patrons_selected(self, ch):
		return (ch == 5)

	#======================================================================================

	def is_clothes_Head_clothes_selected(self, ch):
		return (ch == 1)

	def is_clothes_top_selected(self, ch):
		return (ch == 2)

	def is_clothes_bottom_selected(self, ch):
		return (ch == 3)

	def is_clothes_shoes_selected(self, ch):
		return (ch == 4)

	def is_clothes_gloves_selected(self, ch):
		return (ch == 5)

	def is_clothes_bronya_selected(self, ch):
		return (ch == 6)

	def is_clothes_mechanic_bronya_selected(self, ch):
		return (ch == 7)

	def is_clothes_konkistodor_selected(self, ch):
		return (ch == 8)

	#================================================================

	def is_zelya_selected(self, ch):
		return (ch == 1)

	def is_scopes_selected(self, ch):
		return (ch == 2)

	def is_dop_for_weapon_selected(self, ch):
		return (ch == 3)

	def is_off_noise_selected(self, ch):
		return (ch == 4)


	#=================================================================

	def is_trades_selected(self, ch):
		return (ch == 1)

	def is_cancel_trades_selected(self, ch):
		return (ch == 2)






	def add_elixir_item(self, item):
		self.shop_elixir_items.append(item)

	def add_el_item(self, item):
		self.shop_el_items.append(item)

	def add_hardel_item(self, item):
		self.shop_hardel_items.append(item)

	def add_whitedragon_item(self, item):
		self.shop_whitedragon_items.append(item)

	def add_reddragon_item(self, item):
		self.shop_reddragon_items.append(item)

	def add_snake_item(self, item):
		self.shop_snake_items.append(item)

	def add_vodka_item(self, item):
		self.shop_vodka_items.append(item)

	#=============================================================================================

	def add_pig_item(self, item):
		self.shop_pig_items.append(item)

	def add_mutton_item(self, item):
		self.shop_mutton_items.append(item)

	def add_beef_item(self, item):
		self.shop_beef_items.append(item)

	def add_dragonmeat_item(self, item):
		self.shop_dragonmeat_items.append(item)

	def add_yagodi_item(self, item):
		self.shop_yagodi_items.append(item)

	def add_health_grass_item(self, item):
		self.shop_health_grass_items.append(item)

	#=============================================================================================

	def add_bows_item(self, item):
		self.shop_bows_items.append(item)

	def add_arrows_item(self, item):
		self.shop_arrows_items.append(item)

	def add_psitols_item(self, item):
		self.shop_pistols_items.append(item)

	def add_cold_weapon_item(self, item):
		self.shop_cold_weapon_items.append(item)

	def add_patrons_item(self, item):
		self.shop_patrons_items.append(item)
#=====================================================================

	def add_head_clothes(self, item):
		self.shop_head_clothes_items.append(item)

	def add_top(self, item):
		self.shop_top_items.append(item)

	def add_bottom(self, item):
		self.shop_bottom_items.append(item)

	def add_shoes(self, item):
		self.shop_shoes_items.append(item)

	def add_gloves(self, item):
		self.shop_gloves_items.append(item)

	def add_bronya(self, item):
		self.shop_bronya_items.append(item)

	def add_mechanic_bronya(self, item):
		self.shop_mechanic_bronya_items.append(item)

	def add_konkistodor(self, item):
		self.shop_konkistodor_items.append(item)

	#=======================================================================

	def add_zelya(self, item):
		self.shop_zelya_items.append(item)

	def add_scopes(self, item):
		self.shop_scopes_items.append(item)

	def add_dop_for_weapon(self, item):
		self.shop_dop_for_weapon_items.append(item)






	def ask_elixir_selection(self, gf, l_char):

		print("Выбирайте Эликсир:")


		print("1 - Эликсир 0.2. 43 медяка")
		print("2 - Эликсир 0.5. 90 медяков")
		print("3 - Эликсир 1 л. 150 медяков")
		print("4 - Эликсир 5 л. 600 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_el_items)+2)

		return ch





	def ask_el_selection(self, gf, l_char):

		print("Выбирайте Эль:")




		print("1 - Эль 0.2. 3 медяка")
		print("2 - Эль 0.5. 7 медяков")
		print("3 - Эль 1 л. 14 медяков")
		print("4 - Эль 5 л. 26 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_elixir_items)+2)

		return ch




	def ask_hardel_selection(self, gf, l_char):

		print("Выбирайте Крепкий Эль:")




		print("1 - Крепкий Эль 0.2. 12 медяков")
		print("2 - Крепкий Эль 0.5. 27 медяков")
		print("3 - Крепкий Эль 1 л. 43 медяка")
		print("4 - Крепкий Эль 5 л. 114 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_hardel_items)+2)

		return ch




	def ask_whitedragon_selection(self, gf, l_char):

		print("Выбирайте Белый дракон:")




		print("1 - Белый дракон 0.5. 32 медяка")
		print("2 - Белый дракон 1 л. 50 медяков")
		print("3 - Белый дракон 3 л. 120 медяков")
		print("4 - Белый дракон 5 л. 200 медяков")
		print("5 - Белый дракон 10 л. 340 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_whitedragon_items)+2)

		return ch




	def ask_reddragon_selection(self, gf, l_char):

		print("Выбирайте Красный дракон:")



		print("1 - Красный дракон 0.5. 64 медяка")
		print("2 - Красный дракон 1 л. 100 медяков")
		print("3 - Красный дракон 3 л. 280 медяков")
		print("4 - Красный дракон 5 л. 400 медяков")
		print("5 - Красный дракон 10 л. 760 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_reddragon_items)+2)

		return ch




	def ask_snake_selection(self, gf, l_char):

		print("Выбирайте 'Змеиный яд':")




		print("1 - 'Змеиный яд' 0.1. 93 медяка")
		print("2 - 'Змеиный яд' 0.3. 250 медяков")
		print("3 - 'Змеиный яд' 0.5. 400 медяков")
		print("4 - 'Змеиный яд' 1 л. 780 медяков")
		print("5 - 'Змеиный яд' 2 л. 1250 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_snake_items)+2)

		return ch




	def ask_vodka_selection(self, gf, l_char):

		print("Выбирайте Водку:")



		print("1 - Водка 0.5. 52 медяка")
		print("2 - Водка 1 л. 67 медяков")
		print("3 - Водка 2 л. 106 медяков")
		print("4 - Водка 5 л. 299 медяков")
		print("5 - Водка 10 л. 600 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_vodka_items)+2)

		return ch



#------------------------------------------------------------------------------------------------------------------------------------

	def ask_pig_selection(self, gf, l_char):

		print("Выбирайте Свинину:")




		print("1 - кг Свнина 180 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_pig_items)+2)

		return ch


	def ask_mutton_selection(self, gf, l_char):

		print("Выбирайте Баранину:")




		print("1 - кг Баранина 150 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_mutton_items)+2)

		return ch

	def ask_beef_selection(self, gf, l_char):

		print("Выбирайте Говядину:")




		print("1 - кг Говядина 200 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_beef_items)+2)

		return ch


	def ask_dragonmeat_selection(self, gf, l_char):

		print("Выбирайте Мясо драконов:")




		print("1 - кг Мясо драконов 1200 медяков")
		print("i - Информация о продукте")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_dragonmeat_items)+2)

		return ch


	def ask_yagodi_selection(self, gf, l_char):

		print("Выбирайте Ягоды:")

		print("1 - 100 г Клубника 20 медяков")
		print("2 - 100 г Малина 35 медяков")
		print("3 - 100 г Брусника 45 медяков")
		print("4 - 100 г Рябина 45 медяков")
		print("5 - 100 г Харонт 230 медяков")
		print("6 - 100 г Омперонт 200 медяков")
		print("7 - 100 г Венайс 640 медяков")
		print("8 - 15 г Лотрак 750 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_yagodi_items)+2)

		return ch

	def ask_health_garss_selection(self, gf, l_char):

		print("Выбирайте Целебные травы:")

		print("1 - 100 г Паста подорожника 40 медяков")
		print("2 - 100 г Настойка подорожника 80 медяков")
		print("3 - 100 г Факсуфор 140 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_health_grass_items)+2)

		return ch

	#===================================================================================

	def ask_bows_selection(self, gf, l_char):

		print("Выбирайте Луки:")

		print("1 - Лук маленький - 140 медяков")
		print("2 - Лук средний - 210 медяков")
		print("3 - Лук большой 320 медяков")
		print("4 - Лук Снайперский 500 медяков")
		print("5 - Лук Ассасинский 750 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_bows_items)+2)

		return ch

	def ask_arrows_selection(self, gf, l_char):

		print("Выбирайте Стрелы:")

		print("1 - 10 шт. Стрелы обычные с деревянным наконечником - 10 медяков")
		print("2 - 10 шт. Стрелы обычные со стальным наконечником - 22 медяка")
		print("3 - 10 шт. Стрелы обычные с наконечником из валерийской стали - 60 медяков")
		print("	")
		print("4 - 10 шт. Стрелы тонкие с деревянным наконечником - 12 медяков")
		print("5 - 10 шт. Стрелы тонкие со стальным наконечником - 25 медяков")
		print("6 - 10 шт. Стрелы тонкие с наконечником из валерийской стали - 75 медяков")
		print("	")
		print("7 - 10 шт. Стрелы утолщённые с деревянным наконечником - 15 медяков")
		print("8 - 10 шт. Стрелы утолщённые со стальным наконечником - 30 медяков")
		print("9 - 10 шт. Стрелы утолщённые с наконечником из валерийской стали - 90 медяков")
		print("	")
		print("10 - 10 шт. Стрелы удленённые с деревянным наконечником - 15 медяков")
		print("11 - 10 шт. Стрелы удленённые со стальным наконечником - 38 медяков")
		print("12 - 10 шт. Стрелы удленённые с наконечником из валерийской стали - 100 медяков")
		print("	")
		print("13 - 10 шт. Стрелы укороченные с деревянным наконечником - 8 медяков")
		print("14 - 10 шт. Стрелы укороченные со стальным наконечником - 18 медяков")
		print("14 - 10 шт. Стрелы укороченные с наконечником из валерийской стали - 50 медяков")
		print("	")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_arrows_items)+2)

		return ch


	def ask_pistols_selection(self, gf, l_char):

		print("Выбирайте Пистолеты:")
		
		print("1 - Револьвер обычный - 190 медяков")
		print("2 - Револьвер R8 - 360 медяков")
		print("3 - Glock 2 - 280 медяков")
		print("4 - Desert Eagle - 675 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_pistols_items)+2)

		return ch

	def ask_cold_weapon_selection(self, gf, l_char):

		print("Выбирайте Холодное оружие:")
		
		print("1 - Нож короткий - 35 медяков")
		print("2 - Нож охотничий - 60 медяков")
		print("3 - Нож бабочка - 70 медяков")
		print("4 - Нож бабочка модификация 2.0 - 120 медяков")
		print("5 - Клинок одиночный - 65 медяков")
		print("6 - Клинки боевые - 145 медяков")
		print("7 - Стальной меч - 100 медяков")
		print("8 - Меч из Валерийской стали - 400 медяков")
		print("9 - Охотничий клинок - 90 медяков")
		print("10 - Охотничий клинок из Валерийской стали - 290 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_cold_weapon_items)+2)

		return ch

	def ask_patrons_selection(self, gf, l_char):

		print("Выбирайте Патроны:")
		
		print("1 - 10 шт. для Револьвер обычный - 20 медяков")
		print("2 - 10 шт. для Револьвер R8 - 50 медяков")
		print("3 - 10 шт. для Glock 2 - 40 медяков")
		print("4 - 10 шт. для Desert Eagle - 80 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_patrons_items)+2)

		return ch

	#============================================================================================

	def ask_head_clothes_selection(self, gf, l_char):

		print("Выбирайте Головные уборы:")

		print("1 - Бандитская повязка на подбородок чёрного цвета. - 40 медяков")
		print("2 - Бандитская повязка на подбородок белого цвета. - 40 медяков")
		print("3 - Ковбойская шляпа. - 57 медяков")
		print("4 - Элитная Ковбойская шляпа. - 380 медяков")
		print("5 - Повязка на лоб чёрного цвета. - 40 медяков")
		print("6 - Шапка. - 25 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_head_clothes_items)+2)

		return ch

	def ask_top_selection(self, gf, l_char):

		print("Выбирайте Верх:")

		print("1 - Чёрная кожаная куртка - 70 медяков")
		print("2 - Белая кожаная куртка - 90 медяков")
		print("3 - Синяя кожаная куртка - 80 медяков")
		print("4 - Чёрный свитер - 60 медяков")
		print("5 - Серый свитер - 60 медяков")
		print("6 - Белый свитер - 60 медяков")
		print("7 - Лёгкая рубаха белого цвета - 60 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_top_items)+2)

		return ch

	def ask_bottom_selection(self, gf, l_char):

		print("Выбирайте Низ:")

		print("1 - Длинные Хитоны - 70 медяков")
		print("2 - Штаны кожаные - 90 медяков")
		print("3 - Брюки синие - 140 медяков")
		print("4 - Брюки поношеные - 50 медяков")
		print("5 - Брюки красные - 160 медяков")
		print("6 - Брюки чёрные - 140 медяков")
		print("7 - Шорты - 40 медяков")
		print("8 - Штаны меховые - 170 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_bottom_items)+2)

		return ch

	def ask_shoes_selection(self, gf, l_char):

		print("Выбирайте Обувь:")

		print("1 - Сапоги - 70 медяков")
		print("2 - Сапоги укороченые - 40 медяков")
		print("3 - Сандали - 40 медяков")
		print("4 - Тапочки - 30 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_shoes_items)+2)

		return ch

	def ask_gloves_selection(self, gf, l_char):

		print("Выбирайте Перчатки:")

		print("1 - Кожаные - 70 медяков")
		print("2 - Меховые - 90 медяков")
		print("3 - Боевые перчатки - 50 медяков")
		print("4 - Боевые перчатки усиленные - 150 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_gloves_items)+2)

		return ch

	def ask_bronya_selection(self, gf, l_char):

		print("Выбирайте Кожаную броню:")

		print("1 - Кожаный доспех - 80 медяков")
		print("2 - Кираса - 140 медяков")
		print("3 - Мундир - 100 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_bronya_items)+2)

		return ch

	def ask_mechanic_bronya_selection(self, gf, l_char):

		print("Выбирайте Механические доспехи:")

		print("1 - Механический кулак - 4000 медяков")
		print("2 - Механический доспех - 10000 медяков")
		print("3 - Механические ботинки - 2000 медяков")
		print("4 - Механический шлем - 1500 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_mechanic_bronya_items)+2)

		return ch

	def ask_konkistodor_selection(self, gf, l_char):

		print("Выбирайте доспехи Конкистодора:")

		print("1 - Сапоги - 1000 медяков")
		print("2 - Куртка - 3000 медяков")
		print("3 - Перчатки - 500 медяков")
		print("4 - Штаны - 1000 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_konkistodor_items)+2)

		return ch

	#==========================================================================-

	def ask_scopes_selection(self, gf, l_char):

		print("Выбирайте Прицелы:")

		print("1 - Колиматор - 250 медяков")
		print("2 - X2 - 300 медяков")
		print("3 - X3 - 390 медяков")
		print("4 - X4 - 450 медяков")
		print("5 - X6 - 700 медяков")
		print("6 - X8 - 900 медяков")
		print("7 - X15 - 1800 медяков")
		print("8 - Красный прицел - 2200 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_scopes_items)+2)

		return ch

	def ask_dop_for_weapon_selection(self, gf, l_char):

		print("Выбирайте Примочки для оружия:")

		print("1 - Приклад для винтовки - 250 медяков")
		print("2 - Ручка для пистолета - 100 медяков")
		print("3 - Ручка для винтовки - 150 медяков")
		print("4 - Увеличный магазин для револьвера - 200 медяков")
		print("5 - Увеличный магазин для винтовки - 300 медяков")
		print("6 - Стойка для винтовки - 250 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_dop_for_weapon_items)+2)

		return ch

	def ask_off_noise_selection(self, gf, l_char):

		print("Выбирайте Глушители:")

		print("1 - Укороченный глушитель для винтовки - 300 медяков")
		print("1 - Укороченный глушитель для Револьвера R8 - 240 медяков")
		print("1 - Укороченный глушитель для Револьвера - 280 медяков")
		print("1 - Укороченный глушитель для Glock  - 200 медяков")
		print("1 - Удлинённый глушитель для винтовки - 440 медяков")
		print("1 - Удлинённый глушитель для Револьвера - 320 медяков")
		print("1 - Удлинённый глушитель для Glock  - 400 медяков")
		print("i - Информация о продуктах")
		print("q - Выход")

		ch = gf.player_ask_selection_iq("", 1, len(self.shop_off_noise_items)+2)

		return ch









	def get_elixir(self, ch):
		return self.shop_elixir_items[ch-1]

	def get_el(self, ch):
		return self.shop_el_items[ch-1]

	def get_hardel(self, ch):
		return self.shop_hardel_items[ch-1]

	def get_whitedragon(self, ch):
		return self.shop_whitedragon_items[ch-1]

	def get_reddragon(self, ch):
		return self.shop_reddragon_items[ch-1]

	def get_snake(self, ch):
		return self.shop_snake_items[ch-1]

	def get_vodka(self, ch):
		return self.shop_vodka_items[ch-1]

#===================================================================================-------------------

	def get_pig(self, ch):
		return self.shop_pig_items[ch-1]

	def get_mutton(self, ch):
		return self.shop_mutton_items[ch-1]

	def get_beef(self, ch):
		return self.shop_beef_items[ch-1]

	def get_dragonmeat(self, ch):
		return self.shop_dragonmeat_items[ch-1]

	def get_yagodi(self, ch):
		return self.shop_yagodi_items[ch-1]

	def get_health_grass(self, ch):
		return self.shop_health_grass_items[ch-1]

#============================================================================================-------------------------------

	def get_bows(self, ch):
		return self.shop_bows_items[ch-1]

	def get_arrows(self, ch):
		return self.shop_arrows_items[ch-1]

	def get_pistols(self, ch):
		return self.shop_pistols_items[ch-1]

	def get_cold_weapon(self, ch):
		return self.shop_cold_weapon_items[ch-1]

	def get_patrons_weapon(self, ch):
		return self.shop_patrons_items[ch-1]

#=================================================================================================-------------------------------------

	def get_head_clothes(self, ch):
		return self.shop_head_clothes_items[ch-1]

	def get_top(self, ch):
		return self.shop_top_items[ch-1]

	def get_bottom(self, ch):
		return self.shop_bottom_items[ch-1]

	def get_shoes(self, ch):
		return self.shop_shoes_items[ch-1]

	def get_gloves(self, ch):
		return self.shop_gloves_items[ch-1]

	def get_bronya(self, ch):
		return self.shop_bronya_items[ch-1]

	def get_mechanic_bronya(self, ch):
		return self.shop_mechanic_bronya_items[ch-1]

	def get_konkistodor(self, ch):
		return self.shop_konkistodor_items[ch-1]

	#======================================================---------------

	def get_zelya(self, ch):
		return self.shop_zelya_items[ch-1]

	def get_scopes(self, ch):
		return self.shop_scopes_items[ch-1]

	def get_dop_for_weapon(self, ch):
		return self.shop_dop_for_weapon_items[ch-1]

	def get_off_noise(self, ch):
		return self.shop_off_noise_items[ch-1]





	def is_elixir_info(self, ch):
		if (ch == -1):
			return True
		else:
			return False

	def show_elixir_info(self):
		print("Эликсир - как своеобразный энергетик, с помощью него"
			"можно бодорствовать ночью, какуюто часть времени\n"
			"или просто сбить усталость, которая не будет вас тревожить\n"
			"во время действия Эликсира.\n")

	def show_el_info(self):
		print("Эль - всеми возлюбленный алкогольный напиток")
		print("исключительно для тех, кто хочет освежиться,")
		print("после долгой работы или просто так в жару.")
		print("Он известен своими крайне низкими ценами!")

	def show_hardel_info(self):
		print("Крепкий Эль - Идеально подходит для отдыха или")
		print("большой компании людей. Цены на него не маленькие,")
		print("но всё же напиток стоит своих денег.")
		print("  ")

	def show_whitedragon_info(self):
		print("Белый дракон - один из самых крепких напитков во всей")
		print("стране! Он придаёт немного бодрости, желания к работе")
		print("и силы воли!")
		print("Внимание! Не рекомендуется употреблять данный напиток в ")
		print("большом колличестве!")

	def show_reddragon_info(self):
		print("Красный дракон - один из самых крепких напитков во всём мире!")
		print("Он придаёт огромное колличество ярости и сил.")
		print(" ")
		print("Внимание! Не рекомендуется употреблять данный напиток в ")
		print("большом колличестве!")

	def show_snake_info(self):
		print("'Змеиный яд' - яд, активно используемый для смазки деталей")
		print("двигателя, вашей паровой машины. Также он применяем в ")
		print("сфере оружия. Легко воспламеняется, тяжело тушится!")
		print("Внимание! Не употреблять во внутрь!!")
		print("Это ОПАСНО ДЛЯ ВАШЕГО ЗДОРОВЬЯ!!!")

	def show_vodka_info(self):
		print("Водка - ох эта водка, кто же её не любит?")
		print("Крепкий алкоголь, привезённый из Нортгарда. Рецепт его ведом одним лишь северянам,")
		print("и, учитывая, как водка обжигает горло, нечего удивляться,")
		print("что северяне с холодных земель хлещут его, как южане воду.")
		#print("")
		

	def show_pig_info(self):
		print("Хочешь чего-нибудь сытного? Приобретай!")
		print("Нереально вкусная свинина, привезённая с севера, тебе")
		print("однозначно понравится!")

	def show_mutton_info(self):
		print("Кусок зажаренного жирного мяса.")
		print("Насытит вас и восстановит немного ран на вашем теле.")
		print("Очень может пригодиться в бою.")

	def show_beef_info(self):
		print("Кусок идеально приготовленного мяса.")
		print("Насытит вас и восстановит приличное колличество ран на вашем теле.")
		print("Очень может пригодиться в бою или после боя.")
		print("Не самое дешёвое мясо.")

	def show_dragonmeat_info(self):
		print("Мясо драконов - это то мясо, для добычи которого")
		print("стоит потрудиться.")
		print("Свежее мясцо дракона прибавить вам сил, залечит все ваши раны")
		print("и даже повысит ваши физические характеристики.")

	def show_yagodi_info(self):
		print("Клубника - обычная ягодка с огорода, в неплохом колличестве восстановит бодрость.")

		print("Малина - Почни ничем не отличающаяся от клубники ягода, сорванная с заброшенных садов.")
		print("Придаёт сил и бодрости.")
		print("Брусника - Всем известная ягода, повышает мышление и бодрость.")

		print("	")

		print("Рябина - Лайфхакер? Ягода для тебя. Довольно кислая, хорошо")
		print("Развивает и повышает мышление.")

		print("	")
		
		print("Харонт - Ягода со вкусом табака. Добывается на востоке. Но её используют")
		print("не для еды. Если её расплющить из неё пойдёт серый дым в течении 2-х минут. Правда не сильный.")
		
		print("	")

		print("Омперонт - Очень ядовитая ягода, одна капля сока может убить 8 человек. Очень похожа на Рябину.")
		print("Если подкинуть врагам, для них это будет неожиданный сюрприз.")
		
		print("	")

		print("Венайс - Ягода, сок которой крайне густой. Добывается на юге в Тропиках.")
		print("Её сок активно используется для производста моторного топлива.")
		
		print("	")

		print("Лотрак - Крайне редкая ягода, добываемая в пустынях юга.")
		print("Отличное средство для повышения восприятия. Не самая дешёвая...")

	def show_health_grass_info(self):
		print("Паста подорожника:	")
		print("Состав:")
		print("	Отчищеный молотый подорожник,")
		print("	Спирт,")
		print("	Вода.")
		print("Восстанавливает небольшую чать ран.")
		print("		")
		print("Настойка подорожника:	")
		print("Состав:")
		print("	Отчищеный подорожник,")
		print("	Отчищеный молотый одуванчик,")
		print("	Вода")
		print("	Спирт")
		print("Восстанавливает большую часть ран.")
		print("		")
		print("Факсуфор:	")
		print("Состав:")
		print("	Отчищеный Факсуфор")
		print("Восстанавливает почти все раны.")

	def show_bows_info(self):
		print("Лук маленький, предназначен исключительно для новичков и трениковок со стрельбой,")
		print("Он крайне удобен, но не сильно ранит.")
		print("	")
		print("Лук средний, для продвинутых стрелков. Лук боевой, есть возможность получить")
		print("смертельную рану. Дизайн выполнен идеальной гравировкой плавленым серебром")
		print("и золотом с идеально отполированным деревянным корпусом.")
		print("	")
		print("Лук большой, предназначен для обороняющихся. Крайне не удобен, но")
		print("в тот же момент, урон наносимый им - огромен! Наконечники выполнены из")
		print("очень крепкой, северянской стали. Дерево также идеально отполированно.")
		print("	")
		print("Лук Снайперский, для тех, кто очень точен в стрельбе и вообще во всём,")
		print("что связанно с этим. Не большой, очень удобный, тяжело натягиваемый Лук.")
		print("Без единой отдачи попадёт точно туда, куда вы целились. Строгий дизайн")
		print("из полированного дерева, меди и стали был придуман на Западе и очень")
		print("напоминает окрас богатого автомобиля Breach.")
		print("	")
		print("Лук Ассасинский, создан для ловкачей с повышенной скрытностью и меткостью.")
		print("Нереально точен, лёгок и прост в использовании, а самое главное почти")
		print("бесшумен. Дизайн из полированного дерева и серебра идеально подходит")
		print("для этого оружия.")
		print("	")

	def show_arrows_info(self):
		print("Стрелы обычные :")
		print("Самые обыкновенные, универсальные стрелы. ")
		print("С деревянным наконечником:")
		print("Урон при ударе не изменяется.")
		print("	")
		print("Со стальным наконечником:")
		print("Урон при ударе прибавляется в зависимости от меткости.")
		print("	")
		print("С наконечником из валерийской стали:")
		print("Урон при ударе +1 и прибавляется в зависимости от меткости.")
		print("	")
		print("Стрелы тонкие:")
		print("Предназначены для Ассасинского Лука.")
		print("	")
		print("С деревянным наконечником:")
		print("Урон при ударе не изменяется.")
		print("	")
		print("Со стальным наконечником:")
		print("Урон при ударе прибавляется в зависимости от меткости.")
		print("Но уже с меньшими критериями.")
		print("	")
		print("С наконечником из валерийской стали:")
		print("Урон при ударе +1 и прибавляется в зависимости от меткости.")
		print("Но уже с меньшими критериями.")
		print("	")
		print("Стрелы утолщённые:")
		print("Предназначены для Среднего и Большого Лука.")
		print("С деревянным наконечником:")
		print("Урон при ударе не изменяется.")
		print("	")
		print("Со стальным наконечником:")
		print("Урон при ударе +1 и прибавляется в зависимости от меткости.")
		print("	")
		print("С наконечником из валерийской стали:")
		print("Урон при ударе +1 и прибавляется в зависимости от меткости.")
		print("	")
		print("Стрелы удленённые:")
		print("Предназначены для Снайперского и большого лука.")
		print("	")
		print("С деревянным наконечником:")
		print("Урон при ударе не изменяется.")
		print("	")
		print("Со стальным наконечником:")
		print("Урон при ударе прибавляется в зависимости от меткости.")
		print("	")
		print("С наконечником из валерийской стали:")
		print("Урон +1 и прибавляется в зависимости от меткости.")
		print("	")
		print("Стрелы укороченные:")
		print("Предназначены для маленького Лука и Ассасинского.")
		print("	")
		print("С деревянным наконечником:")
		print("Урон при ударе -1.")
		print("	")
		print("Со стальным наконечником:")
		print("Урон при ударе не изменяется.")
		print("	")
		print("С наконечником из валерийской стали:")
		print("Урон изменяется в зависимости от меткости.")

	def show_pistols_info(self):

		print("Револьвер - самое выгодное и самое универсальное оружие на")
		print("рынке. Урон наносимый им не высок, но для перестрелки самое")
		print("то. Дизайн выполнен с помощью кисточек и красок с деревянным")
		print("трафаретом. Напоминает эскиз разлитых красок.")
		print("	")
		print("Револьвер R8 - более новый и удобный аналог предыдущего оружия.")
		print("Из модибикаций - точность сильно повысилась, оружие стало меньшего")
		print("размера, тем и удобнее, также увеличен наносимый урон.")
		print("Из минусов - очень тугой курок.")
		print("	")
		print("Glock 2 - идеально подходит для быстрой атаки противников не ")
		print("имеющих брони. Самый скорострельный пистолет в мире не самый ")
		print("дешёвый и есть не везде. Из плюслв - не слабый урон, точность,")
		print("скорострельность. Из минусов - цена на оружие и патроны.")
		print("	")
		print("Desert Eagle - недавно созданное оружие на востоке, превзошло")
		print("все ожидания производителей. С помощью него выигрывались многие")
		print("перестрелки и прочее, связанное с этим. Из плюсов - огромный урон,")
		print("стоимость боеприпасов. Из минусов: Высокая громкость, низкая точность.")
		print("	")

	def show_cold_weapon_info(self):
		print("Нож короткий - обычный универсальный нож для неожиданной атаки в близи.")
		print("Не очень эффективен, но очень не заметен.")
		print("	")
		print("Нож охотничий - Большой, достаточно длинный нож, подходит для персонажей")
		print("с повышенной ловкостью. Наносит большой урон, но достаточно заметен.")
		print("----- Фотография ножа находится в папке photo или Фото. -----")
		print("	")
		print("Нож бабочка - нож для ближней атаки, почти моментально разворачивается из")
		print("складного положения. Не обнаруживается ничем, но урон не большой.")
		print("----- Фотография ножа находится в папке photo или Фото. -----")
		print("	")
		print("Нож бабочка модификация 2.0 - всё тот же нож бабочка, но с увеличенным")
		print("уроном.")
		print("	")
		print("Клинок одиночный - Очень похож на обычный нож, но предназначен для")
		print("точного метания. Не требуется быть через чур метким для точных попаданий.")
		print("Достаточно заметное оружие. Урон в близи не большой, а при метании огромен.")
		print("	")
		print("Клинки боевые - два клинка идентичные Клинку одиночному. С теме же")
		print("характеристикиками, только они подготовлены для использования обеими")
		print("руками.")
		print("	")
		print("Стальной меч - самый обычный меч, популярный в средневековье,")
		print("подойдёт для начинающих бойцов. Обычно спасает от разбойников, у которых")
		print("хватает денег только на ближнее оружие.")
		print("	")
		print("Меч из Валерийской стали - Меч тех же габаритов, только изготовлен")
		print("из крепчайшого материала в мире.")
		print("	")
		print("Охотничий клинок - пиратский клинок с изогнутым наконечником для ближнего и среднего")
		print("боя. Урон приличный, скрытность не высокая.")
		print("	")
		print("Охотничий клинок из Валерийской стали - идентичный клинок с огромнейшим уроном")
		print("и такойже скрытностью.")
		print("	")

	def show_patrons_info(self):
		print("Описания для этих творений не требуется, просто боеприпасы.")
		print("	")

	#====================================================================================

	def show_head_clothes_info(self):
		print("Бандитская повязка на подбородок чёрного цвета. - повязка на половину")
		print("скрывающая ваше лицо. С помощью неё в толпе вас будет не узнать.")
		print("	")
		print("Бандитская повязка на подбородок белого цвета. - идентичная повязка,")
		print("для тех, кто предпочетает другую цветовую гамму.")
		print("	")
		print("Ковбойская шляпа. - шляпа, чтобы попонтоваться перед людьми,")
		print("перед народом.")
		print("	")
		print("Элитная Ковбойская шляпа. - такая же шляпа, только уже с раскраской, да в ")
		print("добавок если ты владеешь навыкамт колдовства, даёт тебе не плохое колличество опыта!")
		print("	")
		print("Повязка на лоб чёрного цвета. - что-то похожее на бандитскую повязку,")
		print("только уже на лоб. Чтобы солнце не пекло....")
		print("	")
		print("Шапка. - просто шапка.")
		print("	")

	def show_top_info(self):
		print("Чёрная кожаная куртка - куртка чёрного цвета.")
		print("	")
		print("Белая кожаная куртка - куртка белого цвета.")
		print("	")
		print("Синяя кожаная куртка - куртка сенего цвета.")
		print("	")
		print("Чёрный свитер - свитер чёрного цвета.")
		print("	")
		print("Серый свитер - свитер Серого цвета.")
		print("	")
		print("Белый свитер - свитер белого цвета.")
		print("	")
		print("Длинные Хитоны - Народные штаны распространённые в этом государстве.")
		print("	")

	def show_bottom_info(self):
		print("Длинные Хитоны - распространённые на юго-западе Народные штаны.")
		print("От холода защищают не сильно.")
		print("	")
		print("Штаны кожаные - Штаны для северян или для тех, кто находится в")
		print("постоянном холоде.")
		print("	")
		print("Брюки - пик моды на востоке и западе. От холода не защищают.")
		print("	")
		print("Шорты - дешёвый выбор одежды для южан.")
		print("	")
		print("Штаны меховые - похожи на кожаные штаны, только на много теплей")
		print("и удобней!")
		print("	")

	def show_shoes_info(self):
		print("Сапоги - обувь для путешествий по лесу, не опасно попасть в болото.")
		print("	")
		print("Сапоги укороченые - вариант сапогов для города или деревни.")
		print("	")
		print("Сандали - удобная дышащая обувь для южан.")
		print("	")
		print("Тапочки - самый дешёвый и практичный выбор среди обуви.")
		print("	")

	def show_gloves_info(self):
		print("Кожаные - Перчатки для работы, и для сохранения рук в тепле.")
		print("	")
		print("Меховые - для сохранения рук в тепле, при очень сильном холоде.")
		print("	")
		print("Боевые перчатки - Приносят пользу, при рукопашной борьбе, урон +1/+2.")
		print("	")
		print("Боевые перчатки усиленные - приносят пользу, при рукопашной борьбе, урон +3/+5.")
		print("	")

	def show_bronya_info(self):
		print("Кожаный доспех - доспех на грудь, защищающий не от многих")
		print("ударов. Дешёвый выбор.")
		print("	")
		print("Кираса - Железный доспех на грудь, защищающий от многих")
		print("ударов. Не самый дешёвый, но самый практичный выбор.")
		print("	")
		print("Мундир - Гусударственная одежда полководцев. Бессмысленный")
		print("выбор в качестве брони, но подойдёт, как показатель")
		print("служения государству.")
		print("	")

	def show_mechanic_bronya_info(self):
		print("Механический кулак - кулак, при специалном сжатии")
		print("которого из него резко выстреливаюш шипы. Специальное")
		print("сжатие также срабатывает при ударе кулаком по противнику,")
		print("тем самым можно нанести критическое ранение. Шипы остаются")
		print("в кулаке.")
		print("	")
		print("Механический доспех - нагрудник, с боков которых при ")
		print("нижатии кнопки вылетают ножи, их можно простым движением")
		print("вернуть обратно.")
		print("")
		print("Механические ботинки - ботинки, при пинке с готорых из них")
		print("вылетают ножи, лёгким движением можновернуть их обратно.")
		print("	")
		print("Механический штем, при ударе головой из него вылетает нож.")
		print("	")

	def show_konkistodor_info(self):
		print("Описания для данных продуктов не требуется,")
		print("так как это просто доспехи.")
		print("	")
#================================================================================
	
	def show_zelya_info(self):
		print("Зелье Исцеления - небольшой бутылёк с полупрозрачной фиолетовой")
		print("жидкостью, который при выпивании залечивает все ваши раны.")
		print("	")
		print("Зелье Ярости - красная жидкость в большом бутыльке. Понижает защиту, ")
		print("но повышает ловкость и силу на время боя.")
		print("	")
		print("Зелье Невидимости - зелёная жидкость, которая делает вас невидимым")
		print("на некоторое время, можно использовать во время боя или просто")
		print("взять из инвентаря.")
		print("	")

	def show_scopes_info(self):
		print("Калиматор - деревяный прицел с красной точкой по середине.")
		print("	")
		print("X2 - Прицел с небольшими линзами, увеличивающий не сильно")
		print("также с точкой по середине, только зелёной.")
		print("	")
		print("X3 - прицел для перестрелки на средней дистанции.")
		print("	")
		print("X4 - Самый универсальный прицел из всех, для просмотра")
		print("на большое расстояние.")
		print("	")
		print("X6 - Прицел для полуснайперких винтовок, помогает")
		print("разлядеть противника в далелке.")
		print("	")
		print("X8 - Устанавливается только на снайперские винтовки.")
		print("Предельная дальность просмотра = 300м.")
		print("	")
		print("X15 - Прицел, чем-то походяший на подзорную трубу, но ")
		print("внешность у него совсем другая. Предельная дальность")
		print("просмотра = 800м.")
		print("	")
		print("Красный прицел - Прицел, вобравший в себя все прицелы,")
		print("кроме колиматора. Дальность регулируется лёгким движением пальца.")
		print("")

	def show_dop_for_weapon_info(self):
		print("Приклад для винтовки - повышает удобность и уменьшает отдачу оружия.")
		print("	")
		print("Ручка для пистолета - используется для значительного уменьшения отдачи.")
		print("	")
		print("Ручка для винтовки - уменьшает отдачу и повышает точность выстрела")
		print("на дальнем расстоянии.")
		print("	")
		print("Увеличный магазин - магазин большого размера, вмезает в себя побольше")
		print("патронов, чем обычно.")
		print("	")
		print("Стойка для винтовки - крепится на пулемёты или снайперки, с ")
		print("помощью этой штуки их можно поставить на что-нибудь.")
		print("	")

	def show_off_noise_info(self):
		print("Укороченный глушитель - делает выстрелы оружия более тихими.")
		print("	")
		print("Удлинённый глушитель - делает выстрелы оружия почти бесшумными,")
		print("а также увеличивает слегка точность выстрела.")
		print("	")
		









	def show_drinks(self, gf):
		print("Вы зашли в отдел с напитками:")
		gf.enter()
		print("1 - Эликсиры")
		print("2 - Эль")
		print("3 - Крепкий Эль")
		print("4 - Белый дракон ")
		print("5 - Красный дракон ")
		print("6 - 'Змеиный яд' ")
		print("7 - Водка ")
		#print("8 - Настойка одичалых ")
		print("8 - Выход")
		ch = gf.player_ask_selection("", 1, 8)

		return ch

	def show_food(self, gf):
		print("Вы зашли в отдел с едой:")
		gf.enter()
		print("1 - Свинины")
		print("2 - Баранины")
		print("3 - Говядины")
		print("4 - Мясо драконов")
		#print("5 - Курятина")
		print("5 - Ягоды")
		print("6 - Травы целебные*")
		#print("8 - Настойка одичалых ")
		print("7 - Выход")
		ch = gf.player_ask_selection("", 1, 7)

		return ch

	def show_weapon(self, gf):
		print("Вы зашли в отдел с Оружием:")
		gf.enter()
		print("1 - Луки")
		print("2 - Стрелы")
		print("3 - Пистолеты")
		print("4 - Холодное оружие")
		print("5 - Патроны")
		#print("6 - Метательное")
		print("6 - Выход")
		ch = gf.player_ask_selection("", 1, 6)

		return ch

	def show_clothes(self, gf):
		print("Вы зашли в отдел с Одеждой:")
		gf.enter()
		print("1 - Головные уборы")
		print("2 - Верх")
		print("3 - Низ")
		print("4 - Обувь")
		print("5 - Перчатки")
		print("6 - Кожаные доспехи")
		print("7 - Механические доспехи")
		print("8 - Доспехи конкистодора.")
		print("9 - Выход")
		ch = gf.player_ask_selection("", 1, 9)

		return ch

	def show_special(self, gf):
		print("Вы зашли в отдел с Особыми товарами:")
		gf.enter()
		print("1 - Зелья")
		print("2 - Прицелы")
		print("3 - Примочки для оружия")
		print("4 - Глушитель")
		print("5 - Мехи")
		print("6 - Экзоскелет")
		print("7 - Модули на броню")
		print("8 - Выход")
		ch = gf.player_ask_selection("", 1, 8)

		return ch


	def show_trades(self, gf):
		print("Вы зашли в отдел с продажами")
		gf.enter()
		print("1 - Продать Рыбу")
		print('2 - Продать одежду')
		print('3 - Продать оружие')
		#print("2 - Снять предметы с продажи")
		#print("3 - Купить предметы бывшего употребления")
		print("4 - Выход")
		ch = gf.player_ask_selection("", 1, 2)

		return ch



	def show_talk(self, gf, l_char):
		print("Вы пдошли к торговцу")
		gf.enter()

		if l_char.find_work(5):
			print("1 - Вступить в диалог (Начать задание (Стражи порядка))")
		else:
			print("1 - Вступить в диалог")
		print("2 - Выйти")
	
		ch = gf.player_ask_selection("", 1, 2)

		return ch





	def trade(self, l_char, ch_item, gf):
		print("Укажите стоимость продаваемого товара:")

		ch_item.trade_price = gf.player_ask_selection("", 0, 1000000000000)

		l_char.in_trade.append(ch_item)

		print("Ваш товар находится на продаже, ожидайте уведомлений от клиентов.")



