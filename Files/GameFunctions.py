import random
from data_3 import *
import data_4
from ElixirItem import *
import os
from playsound import playsound
import Researching_city as rc
import Quests as quests

from cities import nircing
from cities import kirt_arrosh

lcwd = os.getcwd()
os.chdir('scripts')

from scripts import randoms
from scripts import colors
from scripts import Runner

os.chdir(lcwd)




class GameFunctions():
	""" useful game function """
	def __init__(self, name):
		#super(Character, self).__init__()
		self.name = name
		self.dialogs = GameDialogs("Dialogs")
		self.locations = GameLocations("Локации")
		self.save_turn = 0


		self.server_units_default = [ \
	'Контрабандист', 'Повозка с напитками для бара', 'Повозка с едой в таверну', 'Торговец хлебом', \
	'Маленький отряд, охраняющий небольшую, на вид дорогую, повозку', 'Торговец из Локрии', \
	'Стражники с повозкой, похоже что, в банк', '3 человека в чёрном плаще, капюшоне и маске', \
	'Повозка с оружием и 2-мя стражниками', 'Стражники возле ворот'\
	\
	]


		self.server_units = list(server_units_default)


	def player_ask_selection(self, ask_str, _min, _max):

		ch = -10
		print(ask_str)

		while True:
			user_str = input();

			if user_str.isdigit():
				ch = int(user_str)

				if ch >= _min and ch <= _max:
					break

			print("Выбор некорректный, пожалуйста повторите.")

		return ch

	def player_ask_selection_iq(self, ask_str, _min, _max):

		ch = -10
		print(ask_str)

		while True:
			user_str = input();

			if (user_str == 'i'):
				ch = -1
				break

			if (user_str == 'q'):
				ch = -10
				break

			if user_str.isdigit():
				ch = int(user_str)

				if ch >= _min and ch <= _max:
					break

			print("Выбор некорректный, пожалуйста повторите.")

		return ch

	def enter(self):
		print("Нажмите Enter для продолжения")
		input()

	def cls(self):
		try: os.system('cls')
		except:
			try: os.system('clear')
			except: print('\n')

	def is_exit_code(self, ch):
		return (ch == -10)

	def show_game_info(self, name):

		print(name, "- Сюжетная RPG кампания, с большим миром и огромными возможностями,\n"
			"Во время вашего путешесвия по игровому миру, вы будете сталкиваться с разными\n"
			"проработанными NPC, с почти каждым из которых вы можете завести диалог.\n"
			"Также вы будете получать задания и просьбы от выших командиров, друзей, союзников.\n"
			"В самом начале вы - простой служитель в государсте Анторпы.\n"
			"Но вас ждут самые захватывающие приключения.\n"
			"Карту вы можете посмотреть в папке - map/карта\n\n"
			"Внимание!!! Игра имеет функцию автосохранения, не выключайте приложение, пока происходит процесс\n"
			"Удачной игры исследователь.\n")


	def show_start_menu(self):

		ch = self.player_ask_selection(
			"Выберите и введите:\n"
			"1 - Новая игра\n"
			"2 - Загрузить сохранение\n"
			"3 - Об игре\n"
			'4 - Что нового \n',
			1, 4);

		return ch

	def find_some_money(self, some_money):
		if (some_money <= 7):
			return some_money
		else:
			return random.randrange(some_money-7, some_money+7)

	def fill_shop_loc2(self, shop_loc2):
		self.fill_shop_loc2_elixir_items(shop_loc2)
		self.fill_shop_loc2_el_items(shop_loc2)
		self.fill_shop_loc2_hardel_items(shop_loc2)
		self.fill_shop_loc2_whitedragon_items(shop_loc2)
		self.fill_shop_loc2_reddragon_items(shop_loc2)
		self.fill_shop_loc2_Vodka_items(shop_loc2)
		self.fill_shop_loc2_Pig_items(shop_loc2)
		#self.fill_shop_loc2_Pig_items(shop_loc2)
		self.fill_shop_loc2_Mutton_items(shop_loc2)
		self.fill_shop_loc2_Beef_items(shop_loc2)
		self.fill_shop_loc2_DragonMeat_items(shop_loc2)
		self.fill_shop_loc2_Yagodi_items(shop_loc2)
		self.fill_shop_loc2_HealthGrass_items(shop_loc2)
		self.fill_shop_loc2_Bow_items(shop_loc2)
		self.fill_shop_loc2_arrow_items(shop_loc2)
		self.fill_shop_loc2_Pistols_items(shop_loc2)
		self.fill_shop_loc2_Cold_Weapon_items(shop_loc2)
		self.fill_shop_loc2_Patrons_items(shop_loc2)
		self.fill_shop_loc2_Head_clothes_items(shop_loc2)
		self.fill_shop_loc2_Top_items(shop_loc2)
		self.fill_shop_loc2_Bottom_items(shop_loc2)
		self.fill_shop_loc2_Shoes_items(shop_loc2)
		self.fill_shop_loc2_Gloves_items(shop_loc2)
		self.fill_shop_loc2_Bronya_items(shop_loc2)
		self.fill_shop_loc2_Konkistodor_items(shop_loc2)
		self.fill_shop_loc2_zelya_items(shop_loc2)
		self.fill_shop_loc2_scopes_items(shop_loc2)
		self.fill_shop_loc2_dop_for_weapon_items(shop_loc2)


	def fill_shop_loc2_elixir_items(self, shop_loc2):
		'''
		print("1 - Эликсир 0.2. 10 медяков")
		print("2 - Эликсир 0.5. 18 медяков")
		print("3 - Эликсир 1 л. 24 медяка")
		print("4 - Эликсир 5 л. 32 медяка")
		print("5 - Информация о продукте")
		print("6 - Выход")
		'''

		'''
		item = ShopItem("Эликсир 0.2", "drink", 10)
		shop_loc2.add_elixir_item(item);

		item = ShopItem("Булка", "food", 2)
		shop_loc2.add_food_item(item);

		item = ShopItem("Палка", "weapon", 2)
		shop_loc2.add_weapon_item(item);
		'''




		item = ElixirItem("Эликсир 0.2", 43, 1)
		shop_loc2.add_elixir_item(item)

		item = ElixirItem("Эликсир 0.5", 90, 2)
		shop_loc2.add_elixir_item(item)

		item = ElixirItem("Эликсир 1", 150, 3)
		shop_loc2.add_elixir_item(item)

		item = ElixirItem("Эликсир 5", 600, 4)
		shop_loc2.add_elixir_item(item)

	def fill_shop_loc2_el_items(self, shop_loc2):

		item = ElItem("Эль 0.2", 3, 5)
		shop_loc2.add_el_item(item)

		item = ElItem("Эль 0.5", 7, 6)
		shop_loc2.add_el_item(item)

		item = ElItem("Эль 1", 14, 7)
		shop_loc2.add_el_item(item)

		item = ElItem("Эль 5", 26, 8)
		shop_loc2.add_el_item(item)

	def fill_shop_loc2_hardel_items(self, shop_loc2):

		item = HardElItem("Крепкий Эль 0.2", 3, 9)
		shop_loc2.add_hardel_item(item);

		item = HardElItem("Крепкий Эль 0.5", 7, 10)
		shop_loc2.add_hardel_item(item)

		item = HardElItem("Крепкий Эль 1", 14, 11)
		shop_loc2.add_hardel_item(item)

		item = HardElItem("Крепкий Эль 5", 26, 12)
		shop_loc2.add_hardel_item(item)


	def fill_shop_loc2_whitedragon_items(self, shop_loc2):

		item = WhiteDragonItem("Белый дракон 0.5", 32, 13)
		shop_loc2.add_whitedragon_item(item);

		item = WhiteDragonItem("Белый дракон 1", 50, 14)
		shop_loc2.add_whitedragon_item(item)

		item = WhiteDragonItem("Белый дракон 3", 120, 15)
		shop_loc2.add_whitedragon_item(item)

		item = WhiteDragonItem("Белый дракон 5", 200, 16)
		shop_loc2.add_whitedragon_item(item)

		item = WhiteDragonItem("Белый дракон 10", 340, 17)
		shop_loc2.add_whitedragon_item(item)

	def fill_shop_loc2_reddragon_items(self, shop_loc2):

		item = RedDragonItem("Красный дракон 0.5", 64, 18)
		shop_loc2.add_reddragon_item(item)

		item = RedDragonItem("Красный дракон 1", 100, 19)
		shop_loc2.add_reddragon_item(item)

		item = RedDragonItem("Красный дракон 3", 280, 20)
		shop_loc2.add_reddragon_item(item)

		item = RedDragonItem("Красный дракон 5", 400, 21)
		shop_loc2.add_reddragon_item(item)

		item = RedDragonItem("Красный дракон 10", 760, 22)
		shop_loc2.add_reddragon_item(item)

	def fill_shop_loc2_snake_items(self, shop_loc2):

		item = SnakeItem("'Змеиный яд' 0.1", 93, 23)
		shop_loc2.add_snake_item(item);

		item = SnakeItem("'Змеиный яд' 0.3", 250, 24)
		shop_loc2.add_snake_item(item)

		item = SnakeItem("'Змеиный яд' 0.5", 400, 25)
		shop_loc2.add_snake_item(item)

		item = SnakeItem("'Змеиный яд' 1", 780, 26)
		shop_loc2.add_snake_item(item)

		item = SnakeItem("'Змеиный яд' 2", 1250, 27)
		shop_loc2.add_snake_item(item)

	def fill_shop_loc2_Vodka_items(self, shop_loc2):

		item = VodkaItem("Водка 0.5", 52, 28)
		shop_loc2.add_vodka_item(item);

		item = VodkaItem("Водка 1", 67, 29)
		shop_loc2.add_vodka_item(item)

		item = VodkaItem("Водка 2", 106, 30)
		shop_loc2.add_vodka_item(item)

		item = VodkaItem("Водка 5", 299, 31)
		shop_loc2.add_vodka_item(item)

		item = VodkaItem("Водка 10", 600, 32)
		shop_loc2.add_vodka_item(item)

	#===================================================================================================================

	def fill_shop_loc2_Pig_items(self, shop_loc2):

		item = PigItem("Свинина 1 кг", 180, 33)
		shop_loc2.add_pig_item(item)

	def fill_shop_loc2_Mutton_items(self, shop_loc2):

		item = MuttonItem("Баранина 1 кг", 150, 34)
		shop_loc2.add_mutton_item(item)

	def fill_shop_loc2_Beef_items(self, shop_loc2):

		item = BeefItem("Говядина 1 кг", 200, 35)
		shop_loc2.add_beef_item(item)

	def fill_shop_loc2_DragonMeat_items(self, shop_loc2):

		item = DragonMeatItem("Мясо драконов 1 кг", 1200, 36)
		shop_loc2.add_dragonmeat_item(item)

	def fill_shop_loc2_Yagodi_items(self, shop_loc2):

		item = YagodiItem("Клубника - 100г", 20, 37)
		shop_loc2.add_yagodi_item(item)

		item = YagodiItem("Малина - 100г", 35, 38)
		shop_loc2.add_yagodi_item(item)

		item = YagodiItem("Брусника - 100г", 45, 39)
		shop_loc2.add_yagodi_item(item)

		item = YagodiItem("Рябина - 100г", 45, 40)
		shop_loc2.add_yagodi_item(item)

		item = YagodiItem("Харонт - 100г", 230, 41)
		shop_loc2.add_yagodi_item(item)

		item = YagodiItem("Омперонт - 100г", 200, 42)
		shop_loc2.add_yagodi_item(item)

		item = YagodiItem("Венайс - 100г", 640, 43)
		shop_loc2.add_yagodi_item(item)

		item = YagodiItem("Лотрак - 15г", 750, 44)
		shop_loc2.add_yagodi_item(item)

	def fill_shop_loc2_HealthGrass_items(self, shop_loc2):

		item = HealthGrassItem("Паста подорожника 100 г.", 40, 45)
		shop_loc2.add_health_grass_item(item)

		item = HealthGrassItem("Настойка подорожника 100 г.", 80, 46)
		shop_loc2.add_health_grass_item(item)

		item = HealthGrassItem("Факсуфор 100 г.", 140, 47)
		shop_loc2.add_health_grass_item(item)


	def fill_shop_loc2_Bow_items(self, shop_loc2):

		item = Weapon("Лук маленький", 3, 0, 140, 48, 1)
		shop_loc2.add_bows_item(item)

		item = Weapon("Лук средний", 6, 0, 210, 49, 1)
		shop_loc2.add_bows_item(item)

		item = Weapon("Лук большой", 9, 0, 320, 50, 1)
		shop_loc2.add_bows_item(item)

		item = Weapon("Лук Снайперский", 15, 0, 500, 51, 1)
		shop_loc2.add_bows_item(item)

		item = Weapon("Лук Ассасинский", 7, 0, 750, 52, 1)
		shop_loc2.add_bows_item(item)

	def fill_shop_loc2_arrow_items(self, shop_loc2):

		item = Patron("Стрелы обычные с деревянным наконечником", 0, 10, 53)
		shop_loc2.add_arrows_item(item)

		item = Patron("Стрелы обычные со стальным наконечником", 0, 22, 54)
		shop_loc2.add_arrows_item(item)

		item = Patron("Стрелы обычные с наконечником из валерийской стали", 1, 60, 55)
		shop_loc2.add_arrows_item(item)

		item = Patron("Стрелы тонкие с деревянным наконечником", 0, 12, 56)
		shop_loc2.add_arrows_item(item)

		item = Patron("Стрелы тонкие со стальным наконечником", 0, 25, 57)
		shop_loc2.add_arrows_item(item)

		item = Patron("Стрелы тонкие с наконечником из валерийской стали", 1, 75, 58)
		shop_loc2.add_arrows_item(item)

		item = Patron("Стрелы утолщённые с деревянным наконечником", 0, 15, 59)
		shop_loc2.add_arrows_item(item)
		
		item = Patron("Стрелы утолщённые со стальным наконечником", 1, 30, 60)
		shop_loc2.add_arrows_item(item)
		
		item = Patron("Стрелы утолщённые с наконечником из валерийской стали", 1, 90, 61)
		shop_loc2.add_arrows_item(item)

		item = Patron("Стрелы удленённые с деревянным наконечником", 0, 15, 62)
		shop_loc2.add_arrows_item(item)
		
		item = Patron("Стрелы удленённые со стальным наконечником", 0, 38, 63)
		shop_loc2.add_arrows_item(item)
		
		item = Patron("Стрелы удленённые с наконечником из валерийской стали", 1, 100, 64)
		shop_loc2.add_arrows_item(item)

		item = Patron("Стрелы укороченные с деревянным наконечником", -1, 8, 65)
		shop_loc2.add_arrows_item(item)
		
		item = Patron("Стрелы укороченные со стальным наконечником", 0, 18, 66)
		shop_loc2.add_arrows_item(item)
		
		item = Patron("Стрелы укороченные с наконечником из валерийской стали", 0, 50, 67)
		shop_loc2.add_arrows_item(item)

	def fill_shop_loc2_Pistols_items(self, shop_loc2):

		item = Weapon("Револьвер обычный", 10, 1, 190, 68, 9)
		shop_loc2.add_psitols_item(item)

		item = Weapon("Револьвер R8", 24, 1, 360, 69, 8)
		shop_loc2.add_psitols_item(item)

		item = Weapon("Glock 2", 14, 1, 280, 70, 20)
		shop_loc2.add_psitols_item(item)

		item = Weapon("Desert Eagle", 56, 1, 675, 71, 7)
		shop_loc2.add_psitols_item(item)

	def fill_shop_loc2_Cold_Weapon_items(self, shop_loc2):

		item = Weapon("Нож короткий", 4, 2, 35, 72, 0)
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Нож охотничий", 6, 1, 60, 73, 0)
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Нож бабочка", 4, 2, 70, 74, 0)
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Нож бабочка модификация 2.0", 7, 2, 120, 75, 0)
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Клинок одиночный", 3, 9, 65, 76, 0)
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Клинки боевые", 7, 9, 145, 77, 0)
		item.count += 1
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Стальной меч", 6, 0, 100, 78, 0)
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Меч из Валерийской стали", 20, 1, 400, 79, 0)
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Охотничий клинок", 7, 4, 90, 80, 0)
		shop_loc2.add_cold_weapon_item(item)

		item = Weapon("Охотничий клинок из Валерийской стали", 18, 8, 290, 81, 0)
		shop_loc2.add_cold_weapon_item(item)

	def fill_shop_loc2_Patrons_items(self, shop_loc2):

		item = Patron("Патроны для Револьвер обычный", 0, 20, 82)
		shop_loc2.add_patrons_item(item)

		item = Patron("Патроны для Револьвер R8", 0, 50, 83)
		shop_loc2.add_patrons_item(item)

		item = Patron("Патроны для Glock 2", 0, 40, 84)
		shop_loc2.add_patrons_item(item)

		item = Patron("Патроны для Desert Eagle", 0, 80, 85)
		shop_loc2.add_patrons_item(item)

	#===================================================================================--------------------------------

	def fill_shop_loc2_Head_clothes_items(self, shop_loc2):

		item = Item_standart("Бандитская повязка на подбородок чёрного цвета.", 40, 86)
		shop_loc2.add_head_clothes(item)

		item = Item_standart("Бандитская повязка на подбородок белого цвета.", 40, 87)
		shop_loc2.add_head_clothes(item)

		item = Item_standart("Ковбойская шляпа.", 57, 88)
		shop_loc2.add_head_clothes(item)

		item = Item_standart("Элитная Ковбойская шляпа.", 40, 87)
		shop_loc2.add_head_clothes(item)

		item = Item_standart("Повязка на лоб чёрного цвета.", 40, 90)
		shop_loc2.add_head_clothes(item)

		item = Item_standart("Шапка.", 25, 91)
		shop_loc2.add_head_clothes(item)

	def fill_shop_loc2_Top_items(self, shop_loc2):

		item = Clothes("Чёрная кожаная куртка", 70, 93, 25)
		shop_loc2.add_top(item)

		item = Clothes("Белая кожаная куртка", 90, 94, 25)
		shop_loc2.add_top(item)

		item = Clothes("Синяя кожаная куртка", 80, 95, 25)
		shop_loc2.add_top(item)

		item = Clothes("Чёрный свитер", 60, 96, 10)
		shop_loc2.add_top(item)

		item = Clothes("Серый свитер", 60, 97, 10)
		shop_loc2.add_top(item)

		item = Clothes("Белый свитер", 60, 98, 10)
		shop_loc2.add_top(item)

		item = Clothes("Лёгкая рубаха белого цвета", 60, 99, 5)
		shop_loc2.add_top(item)

	def fill_shop_loc2_Bottom_items(self, shop_loc2):

		item = Clothes("Длинные Хитоны", 70, 101, 10)
		shop_loc2.add_bottom(item)

		item = Clothes("Штаны кожаные", 90, 102, 20)
		shop_loc2.add_bottom(item)

		item = Clothes("Брюки синие", 140, 103, 15)
		shop_loc2.add_bottom(item)

		item = Clothes("Брюки поношеные", 50, 104, 10)
		shop_loc2.add_bottom(item)

		item = Clothes("Брюки красные", 160, 105, 15)
		shop_loc2.add_bottom(item)

		item = Clothes("Брюки чёрные", 140, 106, 15)
		shop_loc2.add_bottom(item)

		item = Clothes("Шорты", 40, 107, 0)
		shop_loc2.add_bottom(item)

		item = Clothes("Штаны меховые", 170, 108, 50)
		shop_loc2.add_bottom(item)

	def fill_shop_loc2_Shoes_items(self, shop_loc2):

		item = Clothes("Сапоги", 70, 109, 12)
		shop_loc2.add_shoes(item)

		item = Clothes("Сапоги укороченые", 40, 110, 6)
		shop_loc2.add_shoes(item)

		item = Clothes("Сандали", 40, 111, 0)
		shop_loc2.add_shoes(item)

		item = Clothes("Тапочки", 30, 112, 0)
		shop_loc2.add_shoes(item)

	def fill_shop_loc2_Gloves_items(self, shop_loc2):

		item = Clothes("Кожаные перчатки", 70, 113, 15)
		shop_loc2.add_gloves(item)

		item = Clothes("Меховые перчатки", 90, 114, 15)
		shop_loc2.add_gloves(item)

		item = Weapon("Боевые перчатки", random.randrange(1, 2), 1, 50, 115, 0)
		shop_loc2.add_gloves(item)

		item = Weapon("Боевые перчатки усиленные", random.randrange(3, 5), 1, 150, 116, 0)
		shop_loc2.add_gloves(item)

	def fill_shop_loc2_Bronya_items(self, shop_loc2):

		item = Clothes("Кожаный доспех", 80, 117, 10)
		shop_loc2.add_bronya(item)

		item = Clothes("Кираса", 140, 118, 15)
		shop_loc2.add_bronya(item)

		item = Clothes("Мундир", 100, 119, 20)
		shop_loc2.add_bronya(item)

	def fill_shop_loc2_Mechanic_Bronya_items(self, shop_loc2):

		item = Clothes("Механический кулак", 4000, 120, 2)
		shop_loc2.add_mechanic_bronya(item)

		item = Clothes("Механический доспех", 10000, 121, 25)
		shop_loc2.add_mechanic_bronya(item)

		item = Clothes("Механические ботинки", 2000, 122, 3)
		shop_loc2.add_mechanic_bronya(item)

		item = Clothes("Механический шлем", 1500, 123, 8)
		shop_loc2.add_mechanic_bronya(item)

	def fill_shop_loc2_Konkistodor_items(self, shop_loc2):

		item = Clothes("Перчатки - доспех", 1000, 124, 10)
		shop_loc2.add_konkistodor(item)

		item = Clothes("Перчатки - доспех", 3000, 125, 15)
		shop_loc2.add_konkistodor(item)

		item = Clothes("Перчатки - доспех", 500, 126, 5)
		shop_loc2.add_konkistodor(item)

		item = Clothes("Перчатки - доспех", 1000, 127, 10)
		shop_loc2.add_konkistodor(item)

	#============================================================================

	def fill_shop_loc2_zelya_items(self, shop_loc2):

		item = Item_standart("Зелье Исцеления", 300, 128)
		shop_loc2.add_zelya(item)

		item = Item_standart("Зелье Ярости", 600, 129)
		shop_loc2.add_zelya(item)

		item = Item_standart("Зелье Исцеления", 200, 130)
		shop_loc2.add_zelya(item)

	def fill_shop_loc2_scopes_items(self, shop_loc2):

		item = Scope("Колиматор", 250, 131, 25)
		shop_loc2.add_scopes(item)

		item = Scope("X2", 300, 132, 40)
		shop_loc2.add_scopes(item)

		item = Scope("X3", 390, 133, 80)
		shop_loc2.add_scopes(item)

		item = Scope("X4", 450, 134, 120)
		shop_loc2.add_scopes(item)

		item = Scope("X6", 700, 135, 200)
		shop_loc2.add_scopes(item)

		item = Scope("X8", 900, 136, 300)
		shop_loc2.add_scopes(item)

		item = Scope("X15", 1800, 137, 800)
		shop_loc2.add_scopes(item)

		item = Scope("Красный прицел", 2200, 138, 800)
		shop_loc2.add_scopes(item)

	def fill_shop_loc2_dop_for_weapon_items(self, shop_loc2):

		item = Item_standart("Приклад для винтовки", 250, 139)
		shop_loc2.add_dop_for_weapon(item)

		item = Item_standart("Ручка для пистолета", 100, 140)
		shop_loc2.add_dop_for_weapon(item)

		item = Item_standart("Ручка для винтовки", 150, 141)
		shop_loc2.add_dop_for_weapon(item)

		item = Item_standart("Увеличеный магазин для пистолета", 200, 142)
		shop_loc2.add_dop_for_weapon(item)

		item = Item_standart("Увеличеный магазин для винтовки", 300, 143)
		shop_loc2.add_dop_for_weapon(item)

		item = Item_standart("Стойка для винтовки", 250, 144)
		shop_loc2.add_dop_for_weapon(item)




	def set_awards(self):
		all_awards = []


		award_ = Award("Начинающий игрок - заработать 50 ед. игрового опыта.", 1, 0) 
		all_awards.append(award_)


		#======================================================
		#Начинающий игрок I-V
		#======================================================


		award_ = Award("Начинающий игрок I - заработать 100 ед. игрового опыта", 2, 0) 
		all_awards.append(award_)

		award_ = Award("Начинающий игрок II - заработать 300 ед. игрового опыта", 3, 0) 
		all_awards.append(award_)

		award_ = Award("Начинающий игрок III - заработать 500 ед. игрового опыта", 4, 0) 
		all_awards.append(award_)

		award_ = Award("Начинающий игрок IV - заработать 800 ед. игрового опыта", 5, 0) 
		all_awards.append(award_)

		award_ = Award("Начинающий игрок V - заработать 1000 ед. игрового опыта", 6, 0) 
		all_awards.append(award_)


		#======================================================
		#Опытный игрок I-V
		#======================================================


		award_ = Award("Опытный игрок I - заработать 1300 ед. игрового опыта", 7, 0) 
		all_awards.append(award_)

		award_ = Award("Опытный игрок II - заработать 1600 ед. игрового опыта", 8, 0) 
		all_awards.append(award_)

		award_ = Award("Опытный игрок III - заработать 2000 ед. игрового опыта", 9, 0) 
		all_awards.append(award_)

		award_ = Award("Опытный игрок IV - заработать 2300 ед. игрового опыта", 10, 0) 
		all_awards.append(award_)

		award_ = Award("Опытный игрок V - заработать 2500 ед. игрового опыта", 11, 0) 
		all_awards.append(award_)


		#======================================================
		#Продвинутый игрок I-V
		#======================================================


		award_ = Award("Продвинутый игрок I - заработать 2800 ед. игрового опыта", 12, 0) 
		all_awards.append(award_)

		award_ = Award("Продвинутый игрок II - заработать 3200 ед. игрового опыта", 13, 0) 
		all_awards.append(award_)

		award_ = Award("Продвинутый игрок III - заработать 3600 ед. игрового опыта", 
			14, 0) 
		all_awards.append(award_)

		award_ = Award("Продвинутый игрок IV - заработать 4000 ед. игрового опыта", 15, 0) 
		all_awards.append(award_)

		award_ = Award("Продвинутый игрок V - заработать 4400 ед. игрового опыта", 16, 0) 
		all_awards.append(award_)


		#======================================================
		#Проффесионал I-V
		#======================================================


		award_ = Award("Проффесионал I - заработать 5000 ед. игрового опыта", 17, 0) 
		all_awards.append(award_)

		award_ = Award("Проффесионал II - заработать 5500 ед. игрового опыта", 18, 0) 
		all_awards.append(award_)

		award_ = Award("Проффесионал III - заработать 6000 ед. игрового опыта", 20, 0) 
		all_awards.append(award_)

		award_ = Award("Проффесионал IV - заработать 6200 ед. игрового опыта", 21, 0) 
		all_awards.append(award_)

		award_ = Award("Проффесионал V - заработать 6500 ед. игрового опыта", 22, 0) 
		all_awards.append(award_)


		#======================================================
		#Эксперт I-X
		#======================================================


		award_ = Award("Експерт I - заработать 7000 ед. игрового опыта", 23, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт II - заработать 8000 ед. игрового опыта", 24, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт III - заработать 9000 ед. игрового опыта", 25, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт IV - заработать 10000 ед. игрового опыта", 26, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт V - заработать 10500 ед. игрового опыта", 27, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт VI - заработать 11500 ед. игрового опыта", 28, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт VII - заработать 13000 ед. игрового опыта", 29, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт VIII - заработать 15000 ед. игрового опыта", 30, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт IX - заработать 17000 ед. игрового опыта", 31, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт X - заработать 20000 ед. игрового опыта", 32, 0) 
		all_awards.append(award_)




		#======================================================
		#Эксперт I-V
		#======================================================

		award_ = Award("Експерт I - заработать 25000 ед. игрового опыта", 33, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт II - заработать 30000 ед. игрового опыта", 34, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт III - заработать 35000 ед. игрового опыта", 35, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт IV - заработать 40000 ед. игрового опыта", 36, 0) 
		all_awards.append(award_)

		award_ = Award("Експерт V - заработать 50000 ед. игрового опыта", 37, 0) 
		all_awards.append(award_)



		#======================================================
		#Остальные игровые очивки и достижения
		#======================================================

		award_ = Award("Убийца - совершить 10 убийств", 38, 10) 
		all_awards.append(award_)

		award_ = Award("Немного разнообразия - получить огнестрельное оружие", 39, 15) 
		all_awards.append(award_)

		#award_ = Award("Санитар - совершить 50 убийств", 40, 20)
		#all_awards.append(award_)

		award_ = Award("\"Ужас монстров\" - убить 60 монстров", 41, 20) 
		all_awards.append(award_)

		award_ = Award("Колдун-чародей - обучиться магии.", 42, 10) 
		all_awards.append(award_)

		award_ = Award("Ниндзя - прокачать Ловкость до 8-ми единиц", 43, 30) 
		all_awards.append(award_)

		#award_ = Award("\"Киллер из Африки\" - совершить 120 убийств", 44, 50) 
		#all_awards.append(award_)

		award_ = Award("Маг - прокачать магию до 10-ти единиц.", 45, 30) 
		all_awards.append(award_)

		award_ = Award("Великий маг - прокачать магию до 20-ти единиц", 46, 60) 
		all_awards.append(award_)

		award_ = Award("Целитель - прокачать способность исцеления до 1 ед.", 47, 5) 
		all_awards.append(award_)

		award_ = Award("Хилл - прокачать способность исцеления до 3-х единиц", 48, 10) 
		all_awards.append(award_)

		award_ = Award("Простой смертный - умереть 1 раз.", 49, 10) 
		all_awards.append(award_)

		award_ = Award("Путник - выполнить 5 сюжетных заданий.", 50, 30) 
		all_awards.append(award_)

		award_ = Award("Путешественник - выполнить 12 сюжетных заданий", 51, 50) 
		all_awards.append(award_)

		award_ = Award("Продавец - продать что-нибудь", 52, 20) 
		all_awards.append(award_)

		award_ = Award("КОНЕЦ? - открыть портал из книг", 53, 1000) 
		all_awards.append(award_)

		award_ = Award("Боец - научиться 3-м боевым навыкам", 54, 20) 
		all_awards.append(award_)

		award_ = Award("Обновка для оружия - нацепить что-нибудь на оружие", 55, 10) 
		all_awards.append(award_)

		award_ = Award("Силач - прокачать силу до 8-ми единиц", 56, 10) 
		all_awards.append(award_)

		award_ = Award("Супер силач - прокачать силу до 20-ти единиц", 57, 50) 
		all_awards.append(award_)

		#award_ = Award("Самурай - совершить 250 убийств", 58, 140) 
		#all_awards.append(award_)

		award_ = Award("Маристр хранитель - прокачать все пассивные навыки до 20-ти", 59, 1000) 
		all_awards.append(award_)

		#award_ = Award("Скорострел - совершить 400 убийств", 60, 250) 
		#all_awards.append(award_)

		award_ = Award("\"Армор спасает раунды\" - Полная экипировка брони", 61, 80) 
		all_awards.append(award_)

		award_ = Award("Искатель - найти гиппер посох", 62, 150) 
		all_awards.append(award_)

		award_ = Award("Победа! Победа! Вместо обеда! - закончить все сюжетные задания", 63, 3000) 
		all_awards.append(award_)

		award_ = Award("Сталкер - убить дракона", 64, 10) 
		all_awards.append(award_)

		award_ = Award("Продвинутый Сталкер - оседлать дракона", 65, 50) 
		all_awards.append(award_)

		award_ = Award("Медаль за служибу - побороть бандитов во всей варнии", 66, 100) 
		all_awards.append(award_)

		award_ = Award("Пловец - купить корабль", 67, 40) 
		all_awards.append(award_)

		award_ = Award("Любитель выпить", 68, 50) 
		all_awards.append(award_)

		award_ = Award("Атлет - выиграть 5 соревнований по бегу", 69, 40) 
		all_awards.append(award_)

		award_ = Award("Медаль лучшего атлета страны - выиграть все соревнования по бегу в стране", 70, 110) 
		all_awards.append(award_)

		award_ = Award("Медаль лучшего атлета мира - выиграть все соревнования по бегу в мире", 71, 1110) 
		all_awards.append(award_)

		award_ = Award("\"Тренировка - есть тренировка\"", 72, 10) 
		all_awards.append(award_)

		award_ = Award("Богач - баланс 500 медяков", 73, 50) 
		all_awards.append(award_)

		award_ = Award("\"Миллионер\"", 74, 100) 
		all_awards.append(award_)

		award_ = Award("\"Друг в беде поможет\" - найти союзника", 75, 15) 
		all_awards.append(award_)




		return all_awards



	def add_award(self, l_char, c, all_awards):
		#=================================================================
		#Обработка рангов по достижению определённого опыта
		#=================================================================

		if c == 1:
			if l_char.exp >= 50:
				l_char.awards.append(all_awards[c-2])
		elif c == 2:
			if l_char.exp >= 100:
				l_char.awards.append(all_awards[c-2])
		elif c == 3:
			if l_char.exp >= 300:
				l_char.awards.append(all_awards[c-2])
		elif c == 4:
			if l_char.exp >= 500:
				l_char.awards.append(all_awards[c-2])
		elif c == 5:
			if l_char.exp >= 800:
				l_char.awards.append(all_awards[c-2])
		elif c == 6:
			if l_char.exp >= 1000:
				l_char.awards.append(all_awards[c-2])
		elif c == 7:
			if l_char.exp >= 1300:
				l_char.awards.append(all_awards[c-2])
		elif c == 8:
			if l_char.exp >= 1600:
				l_char.awards.append(all_awards[c-2])
		elif c == 9:
			if l_char.exp >= 2000:
				l_char.awards.append(all_awards[c-2])
		elif c == 10:
			if l_char.exp >= 2300:
				l_char.awards.append(all_awards[c-2])
		elif c == 11:
			if l_char.exp >= 2500:
				l_char.awards.append(all_awards[c-2])
		elif c == 12:
			if l_char.exp >= 2800:
				l_char.awards.append(all_awards[c-2])
		elif c == 13:
			if l_char.exp >= 3200:
				l_char.awards.append(all_awards[c-2])
		elif c == 14:
			if l_char.exp >= 3600:
				l_char.awards.append(all_awards[c-2])
		elif c == 15:
			if l_char.exp >= 4000:
				l_char.awards.append(all_awards[c-2])
		elif c == 16:
			if l_char.exp >= 4400:
				l_char.awards.append(all_awards[c-2])
		elif c == 17:
			if l_char.exp >= 5000:
				l_char.awards.append(all_awards[c-2])
		elif c == 18:
			if l_char.exp >= 5500:
				l_char.awards.append(all_awards[c-2])
		elif c == 19:
			if l_char.exp >= 6000:
				l_char.awards.append(all_awards[c-2])
		elif c == 20:
			if l_char.exp >= 6200:
				l_char.awards.append(all_awards[c-2])
		elif c == 22:
			self.exp_awards(l_char, all_awards, c, 6500)
		elif c == 23:
			self.exp_awards(l_char, all_awards, c, 7000)
		elif c == 24:
			self.exp_awards(l_char, all_awards, c, 8000)
		elif c == 25:
			self.exp_awards(l_char, all_awards, c, 9000)
		elif c == 26:
			self.exp_awards(l_char, all_awards, c, 10000)
		elif c == 27:
			self.exp_awards(l_char, all_awards, c, 10500)
		elif c == 28:
			self.exp_awards(l_char, all_awards, c, 11500)
		elif c == 29:
			self.exp_awards(l_char, all_awards, c, 13000)
		elif c == 30:
			self.exp_awards(l_char, all_awards, c, 15000)
		elif c == 31:
			self.exp_awards(l_char, all_awards, c, 17000)
		elif c == 32:
			self.exp_awards(l_char, all_awards, c, 20000)
		elif c == 33:
			self.exp_awards(l_char, all_awards, c, 25000)
		elif c == 34:
			self.exp_awards(l_char, all_awards, c, 30000)
		elif c == 35:
			self.exp_awards(l_char, all_awards, c, 35000)
		elif c == 36:
			self.exp_awards(l_char, all_awards, c, 40000)
		elif c == 37:
			self.exp_awards(l_char, all_awards, c, 50000)



		#=================================================================
		# Обработка остальных достижений
		#=================================================================

		#elif c == 38:
			#self.kill_awards(l_char, all_awards, c, 10, 10)
		elif c == 39:
			for i in range(len(l_char.weap)):
				g = l_char.weap[i]

				if g.code >= 68 and g.code <= 71:
					self.get_award(l_char, 15, all_awards, c)
		#elif c == 40:
			#self.kill_awards(l_char, all_awards, c, 20, 50)
		elif c == 41:
			self.monster_kill_awards(l_char, all_awards, c, 60, 20)
		elif c == 42:
			self.magic_award_01(l_char, all_awards, c, 10)
		elif c == 43:
			self.nindzya_award(l_char, all_awards, c, 30)
		#elif c == 44:
			#self.kill_awards(l_char, all_awards, c, 50, 120)
		elif c == 45:
			self.mag_award(l_char, all_awards, c, 30)
		elif c == 46:
			self.super_mag_award(l_char, all_awards, c, 60)
		elif c == 47:
			self.hill_award(l_char, all_awards, c, 5)
		elif c == 48:
			self.heal_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 49:
			self.just_died(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 50:
			self.putnic_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 51:
			self.puteshestvennic(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 52:
			self.trader_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 53:
			self.END(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 54:
			self.boech(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 55:
			self.obnovka_for_weap(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 56:
			self.silach(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 57:
			self.super_silach(l_char, all_awards, c, all_awards[c-2].exp)
		#elif c == 58:
			#self.samurai(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 59:
			self.magistr(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 60:
			self.killer_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 61:
			self.armor_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 62:
			self.founder_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 63:
			self.winner_chicken_dinner_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 64:
			self.stalker_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 65:
			self.pro_stalker_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 66:
			self.slushba_medal_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 67:
			self.plovech_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 68:
			self.love_drink_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 69:
			self.atlet_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 70:
			self.best_country_atlet_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 71:
			self.best_world_atlet_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 72:
			self.training_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 73:
			self.bogach_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 74:
			self.millioner_award(l_char, all_awards, c, all_awards[c-2].exp)
		elif c == 75:
			self.friend_award(l_char, all_awards, c, all_awards[c-2].exp)


	def get_award(self, l_char, experience, all_awards, code):
		l_char.awards.append(all_awards[code-1])
		l_char.exp += experience
		print("Получено достижение " + str(all_awards[code-1].name))
		print("Получено " + str(experience) + "Единиц опыта")
		self.enter()


	def END(self, l_char, all_awards, c, experience):
		#Дописать позже!!!! Когда будет известно!!!
		#Дописать позже!!!! Когда будет известно!!!
		#Дописать позже!!!! Когда будет известно!!!
		#Дописать позже!!!! Когда будет известно!!!
		#Дописать позже!!!! Когда будет известно!!!
		pass


	def trader_award(self, l_char, all_awards, c, experience):
		if l_char.trades >= 1:
			self.get_award(l_char, experience, all_awards, c)


	def obnovka_for_weap(self, l_char, all_awards, c, experience):
		if len(l_char.weap) >= 1:
			for i in range(len(l_char.weap)):
				g = l_char.weap[i]

				if len(g.invent) >= 1:
					self.get_award(l_char, experience, all_awards, c)
					break




	def puteshestvennic(self, l_char, all_awards, c, experience):
		if len(l_char.work_finish) >= 12:
			self.get_award(l_char, experience, all_awards, c)


	def armor_award(self, l_char, all_awards, c, experience):
		fill_armor = []
		for i in range(len(l_char.weap)):
			g = l_char.weap[i]

			if g.code >= 117 and g.code <= 127:
				fill_armor.append(g)

		if len(fill_armor) >= 4:
			self.get_award(l_char, experience, all_awards, c)



	def bogach_award(self, l_char, all_awards, c, experience):
		if l_char.mon >= 500:
			self.get_award(l_char, experience, all_awards, c)


	def killer_award(self, l_char, all_awards, c, experience):
		if l_char.kills >= 400:
			self.get_award(l_char, experience, all_awards, c)



	def friend_award(self, l_char, all_awards, c, experience):
		if len(l_char.helpers) >= 1:
			self.get_award(l_char, experience, all_awards, c)


	def super_silach(self, l_char, all_awards, c, experience):
		if l_char.s >= 20:
			self.get_award(l_char, experience, all_awards, c)


	def love_drink_award(self, l_char, all_awards, c, experience):
		for i in range(len(l_char.invent)):
			g = l_char.invent[i]

			if g.code >= 18 and g.code <= 20:
				self.get_award(l_char, experience, all_awards, c)


	def training_award(self, l_char, all_awards, c, experience):
		# ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!!
		# ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!!
		# ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!!
		# ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!!
		# ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!!
		pass


	def boech(self, l_char, all_awards, c, experience):
		if len(l_char.sp) >= 3:
			self.get_award(l_char, experience, all_awards, c)



	def best_country_atlet_award(self, l_char, all_awards, c, experience):
		if len(l_char.competitions) >= 40:
			self.get_award(l_char, experience, all_awards, c)


	def best_world_atlet_award(self, l_char, all_awards, c, experience):
		if len(l_char.competitions) >= 70:
			self.get_award(l_char, experience, all_awards, c)


	def pro_stalker_award(self, l_char, all_awards, c, experience):
		for i in range(len(l_char.animals)):
			g = l_char.animals[i]

			if g.code == 1:
				self.get_award(l_char, experience, all_awards, c)


	def samurai(self, l_char, all_awards, c, experience):
		if l_char.kills >= 250:
			self.get_award(l_char, experience, all_awards, c)


	def silach(self, l_char, all_awards, c, experience):
		if l_char.s >= 8:
			self.get_award(l_char, experience, all_awards, c)


	def plovech_award(self, l_char, all_awards, c, experience):
		#ПОЗЖЕ ДОПИСАТЬ!!!!

		for i in range(len(l_char.machines)):
			g = l_char.machines[i]

			if g.code >= 1 and g.code <= 3:
				self.get_award(l_char, experience, all_awards, c)



	def millioner_award(self, l_char, all_awards, c, experience):
		if l_char.mon >= 5000:
			self.get_award(l_char, experience, all_awards, c)



	def atlet_award(self, l_char, all_awards, c, experience):
		if len(l_char.competitions) >= 5:
			self.get_award(l_char, experience, all_awards, c)



	def heal_award(self, l_char, all_awards, c, experience):
		if l_char.heal >= 3:
			self.get_award(l_char, experience, all_awards, c)


	def slushba_medal_award(self, l_char, all_awards, c, experience):
		pass
		# ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!


	def putnic_award(self, l_char, all_awards, c, experience):
		if len(l_char.work_finish) >= 5:
			self.get_award(l_char, experience, all_awards, c)


	def stalker_award(self, l_char, all_awards, c, experience):
		if l_char.dragon_kills >= 1:
			self.get_award(l_char, experience, all_awards, c)


	def just_died(self, l_char, all_awards, c, experience):
		if l_char.dies >= 1:
			self.get_award(l_char, experience, all_awards, c)


	def magic_award_01(self, l_char, all_awards, c, experience):
		if l_char.mg >= 1:
			self.get_award(l_char, experience, all_awards, c)


	def winner_chicken_dinner_award(self, l_char, all_awards, c, experience):
		pass
		#ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!
		#ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!
		#ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!
		#ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!
		#ДОПИСАТЬ ПО ВОЗМОЖНОСТИ!!!!


	def magistr(self, l_char, all_awards, c, experience):
		if l_char.check_full() == 1:
			self.get_award(l_char, experience, all_awards, c)
			

	def hill_award(self, l_char, all_awards, c, experience):
		if l_char.heal >= 1:
			self.get_award(l_char, experience, all_awards, c)			


	def mag_award(self, l_char, all_awards, c, experience):
		if l_char.mg >= 10:
			self.get_award(l_char, experience, all_awards, c)

	def super_mag_award(self, l_char, all_awards, c, experience):
		if l_char.mg >= 20:
			self.get_award(l_char, experience, all_awards, c)



	def nindzya_award(self, l_char, all_awards, c, experience):
		if l_char.l >= 8:
			self.get_award(l_char, experience, all_awards, c)



	def monster_kill_awards(self, l_char, all_awards, code, monster_kills, experience):
		if l_char.monster_kills >= monster_kills:
			self.get_award(l_char, experience, all_awards, code)



	def founder_award(self, l_char, all_awards, c, experience):
		for i in range(len(l_char.invent)):
			g = l_char.invent[i]

			if g.code == 811456:
				self.get_award(l_char, experience, all_awards, code)
				break





	def kill_awards(self, l_char, all_awards, code, experience, kills):
		if l_char.kills >= kills:
			self.get_award(l_char, experience, all_awards, code)
			


	def exp_awards(self, l_char, all_awards, c, experience):
		if l_char.exp >= experience:
			l_char.awards.append(all_awards[c-1])




	def awards(self, l_char):
		all_awards = self.set_awards()

		for i in range(len(all_awards)):
			g = all_awards[i]

			have = 0
			g_code = g.code


			for f in range(len(l_char.awards)):
				k = l_char.awards[f]

				if k.code == g.code:
					have = 1
					break

			if have == 0:
				self.add_award(l_char, g_code, all_awards)











	def autosave(self, l_char):
		#print("Идёт автосохранение")
		l_char.save_state('saves/autosave.bin')
		#enter = input()
		#print("Готово!")
		#print('')


	def check_patrons(self, l_char):
		for i in range(len(l_char.invent)):
			g = l_char.invent[i]

			if g.code >= 82 and g.code <= 85:
				if g.patrons <= 0:
					del l_char.invent[i]
					return False
				else:
					return True


	def update(self, l_char):
		l_char.mon = int(l_char.mon)

		if l_char.die():
			l_char.load_state(l_char)
			while True:
				if l_char.loc == 'Nircing':
					nircing.Nircing().play_menu(l_char, self)
				else: self.play_menu(l_char, self, 1)

		#if l_char.take_weap != 0:
		#	self.reload(l_char.take_weap, l_char)
		#	print("Оружие " + l_char.take_weap.name + " максимально перезаряжено.")

		#self.check_patrons(l_char)
		if len(l_char.helpers) > 0:
			for i in l_char.helpers:
				i.check_die(l_char)
		#self.awards(l_char)
		self.autosave(l_char)





	def save_st(self, my_char):
		print("Выберите сохранение:")
		print("1 - 1-я ячейка")
		print("2 - 2-я ячейка")
		print("3 - 3-я ячейка")
		print("4 - 4-я ячейка")
		print("5 - 5-я ячейка")
		print("6 - 6-я ячейка")
		print("7 - 7-я ячейка")
		print("8 - 8-я ячейка")
		print("9 - 9-я ячейка")
		print("10 - 10-я ячейка")
		ch = int(input())

		while ch > 10 or ch < 1:
			print("Ответ не корректный, пожалуйста повторите")
			ch = int(input)


		print("Идёт сохранение игры, не выключайте игру и компьютер!")


		if ch == 1:
			my_char.save_state('saves/save_01.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 2:
			my_char.save_state('saves/save_02.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 3:
			my_char.save_state('saves/save_03.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 4:
			my_char.save_state('saves/save_04.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 5:
			my_char.save_state('saves/save_05.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 6:
			my_char.save_state('saves/save_06.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 7:
			my_char.save_state('saves/save_07.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 8:
			my_char.save_state('saves/save_08.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 9:
			my_char.save_state('saves/save_09.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()
		elif ch == 10:
			my_char.save_state('saves/save_10.bin')
			print("Сохранение успешно, Нажмите enter для продолжения")
			enter = input()



	def get_player_info(self, l_char):
		print(str(l_char.name))
		print("Сила - " + str(l_char.s))
		print("Меткость - " + str(l_char.m))
		print("Магия - " + str(l_char.mg))
		print("Удача - " + str(l_char.u))
		print("Ловкость - " + str(l_char.l))
		print("Восприятие - " + str(l_char.vs))
		print("Деньги - " + str(l_char.mon))
		print("Игровой опыт - " + str(l_char.exp))
		print("Очки для прокачки навыков - " + str(l_char.upgr))
		print("Локация - " + str(l_char.loc))
		print("")
		print("Оружие:")
		
		for i in range(len(l_char.weap)):
			g = l_char.weap[i]
			print(g.name)
		print("")
		print("Инвентарь:")
		for i in range(len(l_char.invent)):
			g = l_char.invent[i]
			print(g.name)
		print("")
		print("Достижения: ")

		for i in range(len(l_char.awards)):
			print(l_char.awards[i].name)
		print("")

		print("Нажмите Enter для продолжения")
		enter = input()


	def check_work(self, l_char, wk):
		for i in range(len(l_char.work_finish)):
			g = l_char.work_finish[i]
			if g == wk:
				start_work = wk
				return wk
		return 0


	def minus_item(self, l_char, c):
		for i in range(len(l_char.invent)):
			g = l_char.invent[i]

			if g.code == c:
				del l_char.invent[i]
				break



	def drink_elixir(self, l_char, ch_item):
		d = ch_item.code

		if d == 1:
			l_char.sleep -= 20
			self.minus_item(l_char, d)
		elif d == 2:
			l_char.sleep -= 40
			self.minus_item(l_char, d)
		elif d == 3:
			l_char.sleep -= 70
			self.minus_item(l_char, d)
		elif d == 4:
			l_char.sleep -= 100
			self.minus_item(l_char, d)


	def drink(self, name, ch_item, l_char):
		if name in ch_item.name.lower():
			print("1 - Выпить")
			print("2 - Выкинуть")
			print("3 - Выйти")

			ch = self.player_ask_selection("", 1, 3)

			if ch == 1:
				print("Вы употребили напиток - " + ch_item.name)
			elif ch == 2:
				self.minus_item(l_char, ch_item.code)



	def reload(self, ch_weapon, l_char):
		for i in range(len(l_char.invent)):
			g = l_char.invent[i]

			if ch_weapon.code == 68:
				if g.code == 82:
					while ch_weapon.patrons != ch_weapon.max_patrons or g.patrons != 0:
						ch_weapon.patrons += 1
						g.patrons -= 1
						self.update(l_char)
					break

			elif ch_weapon.code == 69:
				if g.code == 83:
					while ch_weapon.patrons != ch_weapon.max_patrons or g.patrons != 0:
						ch_weapon.patrons += 1
						g.patrons -= 1
						self.update(l_char)
					break

			elif ch_weapon.code == 70:
				if g.code == 84:
					while ch_weapon.patrons != ch_weapon.max_patrons or g.patrons != 0:
						ch_weapon.patrons += 1
						g.patrons -= 1
						self.update(l_char)
					break

			elif ch_weapon.code == 71:
				if g.code == 85:
					while ch_weapon.patrons != ch_weapon.max_patrons or g.patrons != 0:
						ch_weapon.patrons += 1
						g.patrons -= 1
						self.update(l_char)
					break



	def weapon_(self, ch_item, l_char):
		print("1 - Вооружить")
		print("2 - Выкинуть")
		print("3 - Перезарядить")
		print("4 - Выйти")

		ch = self.player_ask_selection("", 1, 4)

		if ch == 1:
			l_char.take_weap = ch_item

			for i in range(len(l_char.invent)):
				g = l_char.invent[i]
				if g.code == ch_item.code:
					del l_char.invent[i]

				break
		elif ch == 2:
			
			for i in range(len(l_char.invent)):
				g = l_char.invent[i]
				if g.code == ch_item.code:
					del l_char.invent[i]
		elif ch == 3:
			self.reload(ch_item, l_char)




	def eat(self, name:str, ch_item, l_char, heal, exp:int=0):
		if name in l_char.name.lower():
			print("1 - Съесть")
			print("2 - Выкинуть")
			print("3 - Выйти")

			ch = self.player_ask_selection("", 1, 3)

			if ch == 1:
				print("Вы съели продукт " + ch_item.name)
				l_char.hits -= heal
				l_char.exp += exp
			elif ch == 2:
				self.minus_item(l_char, ch_item.code)



	def choose_invent_item(self, l_char):
		for i in range(len(l_char.invent)):
			g = l_char.invent[i]

			print(str(i+1) + " - " + str(g.name))

		ch = self.player_ask_selection("", 1, len(l_char.invent))

		return ch



	def choose_weapon_item(self, l_char):
		for i in range(len(l_char.weap)):
			g = l_char.weap[i]

			print(str(i+1) + " - " + str(g.name))

		ch = self.player_ask_selection("", 1, len(l_char.weap))

		return ch



	def is_fire_weapon_selected(self, l_char, gf):
		f = l_char.take_weap.code

		if f >= 68 and f <= 71 or f >= 48 and f <= 52:
			return True
		else:
			return False

	def is_bow_selected(self, l_char, gf):
		f = l_char.take_weap.code

		if f >= 48 and f <= 52:
			return True
		else:
			return False

	def is_cold_selected(self, l_char, gf):
		f = l_char.take_weap.code

		if f >= 72 and f <= 81:
			return True
		else:
			return False


	def clothes_inventorys(self, f, ch_item, l_char):
		if ch_item.code in f:
			print("1 - Выкинуть")
			print("2 - Выйти")
			if 'Одето' in ch_item.name:
				print('3 - снять')
			else: print('3 - одеть')

			ch = self.player_ask_selection("", 1, 3)

			if ch == 1: self.minus_item(l_char, ch_item.code)
			elif ch == 3:
				for i in l_char.invent:
					if i == ch_item and 'Одето' in ch_item.name:
						i.name = i.name[::-1][8:][::-1]
						break
					elif i == ch_item:
						i.name += ' - Одето'



	def work_inventory(self, l_char, gf):
		print("Выберите предмет из инвентаря:")

		for i in range(len(l_char.invent)):
			g = l_char.invent[i]
			print(str(i+1) + " - " + g.name)

		ch = gf.player_ask_selection_iq("", 1, len(l_char.invent))

		ch_item = l_char.invent[ch-1]

		if ch_item.code >= 1 and ch_item.code <= 4:
			print("1 - Выпить")
			print("2 - Выкинуть")
			print("3 - Выйти")

			ch = self.player_ask_selection("", 1, 3)

			if ch == 1:
				self.drink_elixir(l_char, ch_item)
				print("Вы употребили напиток")
				for i in range(len(l_char.invent)):
					g = l_char.invent[i]

					if g.code == ch_item.code:
						del l_char.invent[i]
						break
			elif ch == 2:
				for i in range(len(l_char.invent)):
					g = l_char.invent[i]

					if g.code == ch_item.code:
						del l_char.invent[i]
						break

		self.drink('эль', ch_item, l_char)
		self.drink("дракон", ch_item, l_char)
		self.drink("змеиный яд", ch_item, l_char)
		self.drink("водка", ch_item, l_char)
		self.drink("виски", ch_item, l_char)
		self.drink("морковный сок", ch_item, l_char)
		self.drink("лимночелло", ch_item, l_char)
		self.drink("жигулёвское", ch_item, l_char)
		self.drink("дикая", ch_item, l_char)

		self.eat('Свинина'.lower(), ch_item, l_char, 3, 0)
		self.eat('Баранина '.lower(), ch_item, l_char, 3, 0)
		self.eat('Говядина '.lower(), ch_item, l_char, 4, 0)
		self.eat('Мясо драконов'.lower(), ch_item, l_char, 6, 6)
		self.eat('Клубника '.lower(), ch_item, l_char, 1, 1)
		self.eat('Малина '.lower(), ch_item, l_char, 1, 1)
		self.eat('Брусника '.lower(), ch_item, l_char, 2, 3)
		self.eat('Рябина '.lower(), ch_item, l_char, 2, 5)
		self.eat('Харонт '.lower(), ch_item, l_char, -3, 0)
		self.eat('Омперонт '.lower(), ch_item, l_char, -20, 0)
		self.eat('Венайс '.lower(), ch_item, l_char, -2, 0)
		self.eat('Лотрак '.lower(), ch_item, l_char, 0, 25)

		self.eat('Паста подорожника'.lower(), ch_item, l_char, 2, 0)
		self.eat('Настойка подорожника'.lower(), ch_item, l_char, 5, 0)
		self.eat('Факсуфор '.lower(), ch_item, l_char, 8, 0)

		ii = [i+0 for i in range(85, 127)]
		self.clothes_inventorys(ii, ch_item, l_char)
		self.update(l_char)




	def work_weapon(self, l_char, gf):
		print("Выберите Оружие из инвентаря:")

		for i in range(len(l_char.weap)):
			g = l_char.weap[i]
			print(str(i+1) + " - " + g.name)

		ch = gf.player_ask_selection_iq("", 1, len(l_char.weap))

		ch_item = l_char.weap[ch-1]


		self.weapon_(ch_item, l_char)

		self.update(l_char)




	def play_menu(self, l_char, gf, die=0):
		while True:
			if die == 1:
				l_char.dies += 1
				die = 0

			die = 0

			self.dialogs.ch_dialog(l_char, gf)

			l_char.loc_town = 0

			if l_char.work == 'Свет в конце тоннеля':
				quests.AdditionalQuests().light_in_the_end_of_tonnel(l_char, l_char, gf)
				continue
			elif l_char.work == 'Свет в конце тоннеля: Цель 1.1 - Посетить местного торговца в трущобах.':
				rc.Kastomaki().ghetto(l_char, gf)

			print("Вы находитесь в игровом меню:")
			print("1 - Выбрать локацию")
			print("2 - Посмотреть текущие миссии")
			print("3 - Сохранение")
			print("4 - Информация по персонажу")
			print("5 - Взаимодействовать с предметами из инвентаря.")
			print("6 - Выход из игры")

			ch = self.player_ask_selection("", 1, 9)

			if ch == 1:
				self.locations.choose_loc(l_char, gf)
				self.enter()
			elif ch == 2:
				print("Ваши текущие миссии - ", ''.join(l_char.work))

				continue
			elif ch == 3:
				self.save_st(l_char)
				continue
			elif ch == 4:
				self.get_player_info(l_char)
				self.enter()
				continue
			elif ch == 5:
				self.work_inventory(l_char, gf)
			elif ch == 6:
				self.autosave(l_char)
				exit()
			elif ch == 7:
				l_char.weap.append(Weapon("Лук средний", 6, 0, 210, 49, 1))
			elif ch == 8:
				l_char.work = 'Свет в конце тоннеля'
				gf.update(l_char)
				quests.AdditionalQuests.light_in_the_end_of_tonnel(l_char, l_char, gf)
			elif ch == 9:
				l_char.invent = []
				gf.update(l_char)







	def shoot(self, gf, l_char):
		if self.check_patrons(l_char):
			l_char.take_weap.max_patrons -= 1
			return True
		else:
			print("В вашем оружии нет патронов.")
			self.enter()
			return False


	def choose_ability(self, l_char, gf):
		o = 1
		for i in l_char.ability:
			print(o, " - ", i)
			o += 1

		ch = gf.player_ask_selection('', 1, len(l_char.ability))
		return l_char.ability[ch-1]


	def use_ability(self, l_char, gf, ability, person):
		global weap_hit_old
		weap_hit_old = l_char.take_weap.hit

		if ability == 'Ярость':
			person.ability_active = 'Ярость'
			person.damage *= 2
			person.using_ability = False
		elif ability == 'Быстрая стрельба':
			if l_char.take_weap.code > 45 and l_char.take_weap.code < 53:
				l_char.ability_active = 'Быстрая стрельба'
				l_char.take_weap.hit += l_char.take_weap.hit // 4
				l_char.m = l_char.m // 2
				l_char.using_ability = False
			else: print('Эту способность можно использовать только с луком в руках.')
		elif ability == 'Боевое безумие':
			l_char.ability_active = 'Боевое безумие'
			print('Выберите, сколько урона вы хотите получить:')
			print('1 - 25%')
			print('2 - 50%')
			print('3 - 75%')

			ch = gf.player_ask_selection('', 1, 3)
			if ch == 1:
				l_char.hits += 5
				l_char.take_weap.hit += l_char.take_weap.hit // 4
			elif ch == 2:
				l_char.hits += 10
				l_char.take_weap.hit += (l_char.take_weap.hit // 4) * 2
			elif ch == 3:
				l_char.hits += 15
				l_char.take_weap.hit += (l_char.take_weap.hit // 4) * 3
			l_char.using_ability = False
		elif ability == 'Дымовая завеса':
			global enemy_enable
			enemy_enable = 2
			l_char.using_ability = False
		elif ability == 'Древнее знание':
			global lost_char
			lost_char = None
			if random.randint(1, 2) == 1:
				print('Ваши характеристики увеличились на 1-ну единицу')
				lost_char = False
				l_char.s += 1
				l_char.m += 1
				l_char.mg += 1
				l_char.u += 1
				l_char.l += 1
				l_char.vs += 1
			else:
				print('Ваши характеристики уменьшились на 1-ну единицу')
				l_char.s -= 1
				l_char.m -= 1
				l_char.mg -= 1
				l_char.u -= 1
				l_char.l -= 1
				l_char.vs -= 1
				lost_char = True
			l_char.using_ability = False
		else: return

	def stop_ability(self, l_char, gf, person):
		if person.ability_active == 'Ярость':
			person.ability_active = ''
			person.damage = person.damage // 2
			person.using_ability = True
		elif l_char.ability_active == 'Быстрая стрельба':
			l_char.ability_active = ''
			l_char.m *= 2
			l_char.take_weap.hit = weap_hit_old
		elif l_char.ability_active == 'Боевое безумие':
			l_char.ability_active = ''
			l_char.take_weap.hit = weap_hit_old
			l_char.using_ability = True
		elif l_char.ability_active == 'Дымовая завеса':
			pass
		elif l_char.ability_active == 'Древнее знание':
			global lost_char
			if lost_char == True:
				lost_char = None
				l_char.s += 1
				l_char.m += 1
				l_char.mg += 1
				l_char.u += 1
				l_char.l += 1
				l_char.vs += 1
			else:
				l_char.s -= 1
				l_char.m -= 1
				l_char.mg -= 1
				l_char.u -= 1
				l_char.l -= 1
				l_char.vs -= 1
				lost_char = None
			l_char.using_ability = False
		else: return

	def update_ability(self, l_char, gf, ability):
		if l_char.ability_active == 'Быстрая стрельба':
			gf.save_turn = 2
			gf.stop_ability(l_char, gf, l_char)
		elif l_char.ability_active == 'Дымовая завеса':
			gf.save_turn = 3
		if gf.save_turn != 0:
			gf.save_turn -= 1
		elif gf.save_turn == 0:
			l_char.using_ability = True
		else: return

	def use_ability_enemy(self, l_char, gf, ability):
		return

	def update_ability_enemy(self, l_char, gf):
		global enemy_ability
		ability = enemy_ability
		if ability == None: return
		if ability.name.lower() == 'подавляющий удар':
			if ability.cdn == 2: return
			elif ability.name == 'подавляющий удар': enemy_ability = None
		return



	def battle(self, gf, l_char, enemyes, teammates=[]):
		l_char.choose_weap(gf)
		global enemy_enable
		enemy_enable = 0
		team_damage = 0
		turn = 0
		ability_chosen = None
		global enemy_ability
		enemy_ability = None

		while len(enemyes) != 0:
			team_damage = 0
			counter = 0

			print('1 - Сменить оружие')
			print('2 - Продолжить')
			#print(l_char.using_ability)
			if l_char.using_ability == True:
				print("3 - Использовать способность")
				ch = gf.player_ask_selection("", 1, 3)
			else: ch = gf.player_ask_selection("", 1, 2)

			if ch == 1:
				l_char.return_weap()
				l_char.choose_weap(gf)
			elif ch == 3:
				ability_chosen = gf.choose_ability(l_char, gf)
				self.use_ability(l_char, gf, ability_chosen, l_char)


			print("Выберите противника для атаки:")

			for i in range(len(enemyes)):
				print(str(i+1) + ' ' + enemyes[i].name)

			ch = gf.player_ask_selection("", 1, len(enemyes)+1)

			ch_e = enemyes[ch-1]
			ch_n = ch-1

			if len(l_char.helpers) > 0:
				for i in l_char.helpers:
					if i.using_ability == True and len(i.ability) > 0:
						ability = i.ability[random.randrange(0, len(i.ability))]
						print(i.name, ' Использовал(а) способность ', ability)
						gf.use_ability(l_char, gf, ability, i)

				if len(l_char.helpers) != 0:
					for i in l_char.helpers:
						team_damage += i.damage

				print('Ваши союзники нанесли урон - ' + str(team_damage))
				ch_e.hp -= team_damage
				print('У противника осталось ', ch_e.hp, ' ед. здоровья.')
				gf.enter()

			if enemy_ability == 'подавляющий удар':
				dmg = l_char.take_weap.hit // 2
			else: dmg = l_char.take_weap.hit

			if gf.is_fire_weapon_selected(l_char, gf):
				print("1 - Выстрелить по противнику")
				print("2 - Подготовиться контратаковать")

				ch = gf.player_ask_selection("", 1, 2)

				if ch == 1:
					if l_char.m >= 1 and True:
						print("Вы попали по противнику " + str(ch_e.name))
						
						print("Вы нанесли " + str(dmg) + " единиц урона")
						ch_e.hp -= dmg
						print("У противника " + str(ch_e.name) + " " + str(ch_e.hp) + " единиц здоровья.")
					else:
						print("Урона вы не нанесли")
				elif ch == 2:
					counter = 1
			elif gf.is_cold_selected(l_char, gf):
				print("1 - Подбежать и сделать ранение в шею")
				print("2 - Подбежать и сделать ранение в живот")
				print("3 - Подбежать и сделать ранение в руку")
				print("4 - Кувыркнуться и пронзить противника.")
				print("5 - Заблокировать удар")

				ch = gf.player_ask_selection("", 1, 5)

				if ch == 1:
					if l_char.l >= 3:
						print("Вы подбегаете и наносите " + str(dmg + 2) + " единиц урона противнику " + str(ch_e.name))
						ch_e.hp -= dmg + 2
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print(l_char.miss())
				elif ch == 2:
					if l_char.l > 1 and l_char.m >= 1:
						print("Вы подбегаете и наносите " + str(dmg) + " единиц урона противнику " + str(ch_e.name))
						ch_e.hp -= dmg
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print(l_char.miss())
				elif ch == 3:
					if l_char.l > 2 and l_char.m >= 1:
						print("Вы подбегаете и наносите " + str(dmg + 1) + " единиц урона противнику " + str(ch_e.name))
						ch_e.hp -= dmg + 1
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print(l_char.miss())
				elif ch == 4:
					if l_char.l >= 3 and l_char.m >= 2:
						print("Вы кувыркаетесь с " + str(dmg + 4) + " единицами урона противнику " + str(ch_e.name))
						ch_e.hp -= dmg + 4
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print("К сожалению ваших навыков для кувырка не хватило.")
				elif ch == 5:
					print("Вы приготовились к блокировке удара.")
					counter = 2


			else:
				print("1 - Нанести удар в голову")
				print("2 - Нанести удар в плечо")
				print("3 - Нанести удар по ноге ногой")
				print("4 - Сделать пару ударов в живот")
				print("5 - Заблокировать удар")

				ch = gf.player_ask_selection("", 1, 5)

				if ch == 1:
					if l_char.m >= 1 and l_char.l >= 2:
						print("Удар прошёл по противнику " + str(ch_e.name) + " с " + str(dmg + 1) + "Единицами урона")
						ch_e.hp -= dmg + 1
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print(l_char.miss())
				elif ch == 2:
					if l_char.m >= 1:
						print("Удар прошёл по противнику " + str(ch_e.name) + " с " + str(dmg + 1) + "Единицами урона")
						ch_e.hp -= dmg + 1
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print(l_char.miss())
				elif ch == 3:
					if l_char.l >= 2:
						print("Удар прошёл по противнику " + str(ch_e.name) + " с " + str(dmg) + "Единицами урона")
						ch_e.hp -= dmg
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print(l_char.miss())
				elif ch == 4:
					if l_char.s >= 2:
						print("Удар прошёл по противнику " + str(ch_e.name) + " с " + str(dmg) + "Единицами урона")
						ch_e.hp -= dmg
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print(l_char.miss())
				else:
					counter = 3

			if enemy_enable > 0:
				enemy_enable -= 1
				continue

			if ch_e.die_enemy(gf, l_char) == 1:
				del enemyes[ch_n]
			else:
				ch_e_r = enemyes[random.randrange(0, len(enemyes))]

				if ch_e.abilities != []:
					for j in range(len(ch_e.abilities)):
						if ch_e.abilities[j].cdn == 0:
							self.use_ability_enemy(l_char, gf, ch_e.abilities[j])
							ch_e.abilities[j].cdn = ch_e.abilities[j].cooldown
							print('Противник использовал способность - ', ch_e.abilities[j].name)
							enemy_ability = ch_e.abilities[j]
							break

				if enemy_ability != None and enemy_ability.name.lower() == 'подавляющий удар': hp_ = ch_e.damage - (ch_e.damage // 100) * 30
				else: hp_ = ch_e.damage

				if counter == 0:
					print("Вас атакует противник " + str(ch_e.name))
					l_char.hits += hp_
					if hp_ < 2: print('По вам попали, но не значительною.')
					else: print('Вы получили критический урон!')
				elif counter == 1:
					print("На вас проявил агрессию противник " + str(ch_e.name))
					if True:
						print("Но вы подготовились и произвели выстел, нанеся урон " + str(dmg))
						ch_e_r.hp -= dmg
						print("У противника осталось " + str(ch_e.hp) + " единиц здоровья")
					else:
						print("К сожалению выстрел произвести не получилось.")
				elif counter == 2 or counter == 3:
					print("На вас проявил агрессию противник " + str(ch_e.name))

					if dmg >= hp_:
						print("Вы успешно заблокировали удар")
					else:
						print("Вы получили урон " + str(dmg - hp_))
						l_char.hits += dmg - hp_
				if ch_e.die_enemy(gf, l_char) == 1:
					del enemyes[ch_n]

			gf.update_ability_enemy(l_char, gf)
			gf.update_ability(l_char, gf, ability_chosen)
			gf.update(l_char)

		for i in l_char.helpers:
			if i.ability_active != '':
				gf.stop_ability(l_char, gf, i)
		gf.update(l_char)





	# durak functions:

	def lower_card(self, cards):
		lower = 0
		for i in cards:
			if i.scale < lower:
				lower = i.scale
		return lower

	def who_first(self, lower_player, lower_bot):
		if lower_player < lower_bot:
			print('Вы ходите первыми, ибо у ваша меньшая карта меньше, чем у противника.')
			return 'player'
		elif lower_player == lower_bot:
			if random.randrange(1, 2) == 1:
				print('Вы ходите первыми, ибо так решил рандом.')
				return 'player'
			else:
				print('Противник ходит первым, ибо так решил рандом.')
				return 'bot'
		else:
			print('Противник ходит первым, ибо у него меньшая карта меньше, чем у вас.')
			return 'bot'


	def start_playing_durak(self, l_char, gf, first, player_cards, bot_cards):
		if first == 'bot':
			lower = bot_cards[0]
			for i in bot_cards:
				if i.scale < lower.scale and i :
					lower = bot_cards[i]


	def cubes_start(self, l_char, gf):
		numbers = input('Введите колличество кубиков(Standart 2): ')
		iterations = input('Введите колличество подбрасываний(Standart 10): ')

		if not numbers.isdigit() or int(numbers) < 2: numbers = 2
		else: numbers = int(numbers)
		if iterations.isdigit() or int(iterations) < 1: iterations = 10
		else: iterations = int(iterations)

		#if l_char.mon < 100*numbers:
		#	print('У вас нет денег для такой ставки!')
		#	return

		if randoms.cubes_fall(numbers, iterations):
			win = 100 * numbers
			if iterations >= 10: win = win / (iterations // 5)
			print('Вы победили! и получили: ', int(win), ' медяков')
			l_char.mon += win
		else:
			win = 100 * numbers
			print('Вы проиграли и потеряли', int(win), ' медяков')
			l_char.mon -= win

		gf.update(l_char)


	def start_colors(self, l_char, gf):
		while True:
			stv = input('Введите ставку: ')
			if stv.isdigit() and int(l_char.mon) >= int(stv):
				stv = int(stv)
				l_char.mon -= stv
				break
			else: print('То, что вы ввели не корректно или вам не хватает денег.')

		print('1 - Поставить на красное')
		print('2 - Поставить на чёрное')
		print('3 - Поставить на первую половину (0-30)')
		print('4 - Поставить на вторую половину (31 - 00)')
		print('5 - Поставить на конкретное число')

		ch = gf.player_ask_selection('', 1, 5)

		win = 2

		if ch == 1: stav = 62
		elif ch == 2: stav = 63
		elif ch == 3: stav = 64
		elif ch == 4: stav = 65
		else:
			while True:
				stav = input('Введите число, на которое вы хотите поставить: ')

				if stav == '00': break
				elif stav.isdigit() and 0<=int(stav)<60: break
				else: print('Введённое вами число не корректно, поваторите ввод.')
			win = 60

		if colors.colors(stav):
			l_char.mon += stv * win
			print('Вы выиграли, ваш выигрыш состовляет: ', stv * win, ' медяков.')
		else:
			print('Вы проиграли!')
			l_char.mon -= stv

		gf.update(l_char)


	def start_runner(self, l_char, gf):
		while True:
			stv = input('Введите ставку в медяках: ')
			if stv.isdigit() and l_char.mon >= int(stv):
				stv = int(stv)
				l_char.mon -= stv
				break
			else: print('То, что вы введи либо не корректно, либо у вас не хватает денег на ставку.')

		while True:
			stav = input('Ведите коэффицент от 1.00 до 9.00: ')
			try:
				stav = float(stav)
				break
			except ValueError: print('Не корректный ввод, повторите.')

		if Runner.runner(stav):
			win = int(stav*stv)
			print('Вы победили и получили ', win, ' медяков')
			l_char.mon += win
		else: print('Вы проиграли!')

		gf.update(l_char)


	def teammate_exception(self, l_char, gf, exc:str='Ag4234sgnfte'):
		old_help = list(l_char.helpers)
		for i in l_char.helpers:
			if exc not in i.name: l_char.helpers.remove(i)
		gf.update(l_char)
		return old_help

	def return_teammates(self, l_char, gf, old_help):
		l_char.helpers = list(old_help)
		gf.update(l_char)

	def weapon_exception(self, l_char, gf, exc:str='51h89f5h9834ch'):
		old_weap = list(l_char.weap)
		for i in l_char.weap:
			if exc not in i.name: l_char.weap.remove(i)
		gf.update(l_char)
		return old_weap

	def return_weapon(self, l_char, gf, old_weap):
		l_char.weap = list(old_weap)
		gf.update(l_char)

	def buy_tree_pick(self, l_char, gf):
		print('')
		print('1 - Деревянная_кирка (145 медяков)')
		print('2 - Деревянная_кирка+ (180 медяков)')
		print('3 - Деревянная_кирка++ (220 медяков)')
		print('4 - Деревянная_кирка_spp (с возможностью усиления с помощью модулей) (260 медяков)')
		print('5 - Информация')
		print('6 - Выход')

		ch = gf.player_ask_selection('', 1, 6)

		if ch == 1:
			item = Pick('Деревянная_кирка', {'pwr' : 1, 'stone' : 0.9}, 145)
			l_char.buy_item(item)
		elif ch == 2:
			item = Pick('Деревянная_кирка+', {'pwr' : 2, 'stone' : 1.1}, 180)
			l_char.buy_item(item)
		elif ch == 3:
			item = Pick('Деревянная_кирка++', {'pwr' : 3, 'stone' : 1.4}, 220)
			l_char.buy_item(item)
		elif ch == 4:
			item = Pick('Деревянная_кирка_spp', {'pwr' : 1, 'stone' : 0.9}, 260, 'Moduled')
			l_char.buy_item(item)
		elif ch == 5:
			print('Деревянная кирка самая слабая из всех.', \
				'Деревянная_кирка: камень - 0.9'\
				'Деревянная_кирка+: камень - 1.1'\
				'Деревянная_кирка++: камень - 1.4'\
				'Деревянная_кирка_spp: камень - 0.9')
		return

	def buy_rock_pick(self, l_char, gf):
		print('')
		print('1 - Каменная_кирка (300 медяков)')
		print('2 - Каменная_кирка+ (340 медяков)')
		print('3 - Каменная_кирка++ (390 медяков)')
		print('4 - Каменная_кирка_spp (с возможностью усиления с помощью модулей) (410 медяков)')
		print('5 - Информация')
		print('6 - Выход')

		ch = gf.player_ask_selection('', 1, 6)

		if ch == 1:
			item = Pick('Каменная_кирка', {'pwr' : 5, 'stone' : 1.6}, 300)
			l_char.buy_item(item)
		elif ch == 2:
			item = Pick('Каменная_кирка+', {'pwr' : 6, 'stone' : 1.9}, 340)
			l_char.buy_item(item)
		elif ch == 3:
			item = Pick('Каменная_кирка++', {'pwr' : 7, 'iron' : 1.0, 'stone' : 2.2}, 390)
			l_char.buy_item(item)
		elif ch == 4:
			item = Pick('Каменная_кирка_spp', {'pwr' : 5, 'iron' : 0.8, 'stone' : 1.7}, 410, 'Moduled')
			l_char.buy_item(item)
		elif ch == 5:
			print(\
				'Каменная_кирка: камень - 1.6'\
				'Каменная_кирка+: камень - 1.9'\
				'Каменная_кирка++: камень - 2.2 железо - 1.0'\
				'Каменная_кирка_spp: камень - 1.7 железо - 0.8')
		return

	def buy_iron_pick(self, l_char, gf):
		print('')
		print('1 - Железная_кирка (480 медяков)')
		print('2 - Железная_кирка+ (550 медяков)')
		print('3 - Железная_кирка++ (590 медяков)')
		print('4 - Железная_кирка_spp (с возможностью усиления с помощью модулей) (600 медяков)')
		print('5 - Информация')
		print('6 - Выход')

		ch = gf.player_ask_selection('', 1, 6)

		if ch == 1:
			item = Pick('Железная_кирка', {'pwr' : 9, 'iron' : 1.2, 'stone' : 2.6}, 480)
			l_char.buy_item(item)
		elif ch == 2:
			item = Pick('Железная_кирка+', {'pwr' : 10, 'iron' : 1.5, 'stone' : 3.0}, 550)
			l_char.buy_item(item)
		elif ch == 3:
			item = Pick('Железная_кирка++', {'pwr' : 11, 'iron' : 1.7, 'stone' : 3.7, 'redstone' : 0.1}, 590)
			l_char.buy_item(item)
		elif ch == 4:
			item = Pick('Железная_кирка_spp', {'pwr' : 9, 'iron' : 1.2, 'stone' : 2.7}, 600, 'Moduled')
			l_char.buy_item(item)
		elif ch == 5:
			print(\
				'Железная_кирка: камень - 2.6 железо - 1.2'\
				'Железная_кирка+: камень - 3.0 железо - 1.5'\
				'Железная_кирка++: камень - 3.7 железо - 1.7 редстоун - 0.1'\
				'Железная_кирка_spp: камень - 2.7 железо - 1.2')
		
		return