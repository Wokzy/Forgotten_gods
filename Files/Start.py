import math
import random

from character import *
from GameFunctions import *
from data_1 import *
from Quests import *
from data_4 import *
from data_5 import *
from data_6 import *

import Researching_city as rc

from cities import nircing
from cities import kirt_arrosh


# В качестве защиты от пиратства можно использовать ключи, как в ssh.

# - \n\t\

VERSION = '0.5.1:48'
GAME_NAME = 'Forgotten Gods'
UPDATE_LOG = \
'__0.5.0__\n\t\
- Добавлен новый побочный квест (Свет в конце тоннеля)\n\t\
- Добавлена возможность рыбачить (В Нирсинге)\n\t\
- Теперь у соперников есть способности и они могут их применять\n\t\
- Обновлена система обилок и способностей как главного героя, так и его союзников\n\t\
- В Нирсинге добавлен залив, добавлена локация тракт и ещё 3 локации...\n\t\
- Исправлены ошибки с приминением брони и её покупкой.\n\t\
\n\
__0.4.0__ \n\t\
- Добавлен новый побочный квест\n\t\
- Обновлён отдел продажи, продавать можно большинство вещей из инвентаря.\n\t\
- Одежду теперь можно одевать.\n\t\
- Обновлены трущобы, теперь у торговца можно покупать больше предметов.\n\t\
\n\
 __0.3.18__ \n\t\
- Исправлены ошибки хранилищ в домах\n\t \
- Добавлен новый побочный квест \n\t \
- Оптимизирована система автосохранений\n\t \
'




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




ch = 0







def menu(l_char_):
	while True:
		gf = GameFunctions('init')

		ch = gf.show_start_menu()

		if ch == 1:
			l_char = new_game(l_char_, gf)
			print(l_char.m)
			gf.update(l_char)
			while True:
				gf.play_menu(l_char, gf, 0)
		elif ch == 2:
			l_char_.load_state(l_char_)
			while True:
				if l_char_.loc == 'Nircing':
					nircing.Nircing().play_menu(l_char_, gf)
				elif l_char_.loc == "Кирт'Аррош":
					kirt_arrosh.KirtArrosh().play_menu(l_char_, gf)
				else: gf.play_menu(l_char_, gf, 0)
		elif ch == 3:
			gf.show_game_info(GAME_NAME)
			#menu(l_char_)
		elif ch == 4:
			print(UPDATE_LOG)



print("Добро пожаловать в квест-игру ", GAME_NAME)
print("Версия - ", VERSION)
print("Нажмите Enter для продолжения")

g_char0 = Character('Player',0,0,0,0,0,0)
g_char1 = Character('Player1',0,0,0,0,0,0)

enter = input()

menu(g_char0)
#while True:
'''
def game_menu(l_char, gf):

	ask_str = """Вы находитесь в игровом меню, выберите и введите:\n
1 - Играть
2 - Подробная информация по персонажу
3 - Сохранение
4 - Выход из игры\n"""

	ch = gf.player_ask_selection(ask_str, 1, 4)

	print("Вы выбрали: " + str(ch))

	if ch == 1:
		gf.dialogs.ch_dialog(l_char, gf)
		gf.update(l_char)
		#game_menu(l_char, gf)
	elif ch == 2:
		#l_char.show_info();
		gf.get_player_info(l_char)
		game_menu(l_char, gf)
	elif ch == 3:
		gf.save_st(l_char)
		print("Нажмите Enter для продолжения:")
		enter = input()
		game_menu(l_char, gf)
'''
'''
shop_loc1 = Shop("The shop (loc 1)");
gf.fill_shop_loc1(shop_loc1)

shop_loc2 = Shop("The shop (loc 2)");
gf.fill_shop_loc2(shop_loc2)

shop_loc3 = Shop("The shop (loc 3)");
gf.fill_shop_loc3(shop_loc3)

shop_loc4 = Shop("The shop (loc 4)");
gf.fill_shop_loc4(shop_loc4)
'''
#my_char.load('save.bin')
