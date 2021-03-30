import pickle
from GameFunctions import *
import random
from ElixirItem import *
from Home import *


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

class Character():
	"""simple for Character"""
	def __init__(self, name, s, m, mg, u, l, vs):
		#super(Character, self).__init__()
		self.name = name
		self.s = s
		self.m = m
		self.mg = mg
		self.u = u
		self.l = l
		self.vs = vs
		self.mon = 0
		self.exp = 0
		self.upgr = 0
		self.weap = [Weapon("Кулаки", self.s, self.mg, 0, 0, 0)]
		self.awards = []
		self.loc = 0
		self.dialog = 0
		self.work = []
		self.work_end = 0
		self.invent = []
		self.heal = 0
		self.sleep = 0
		self.loc_town = 0
		self.hits = 0
		self.take_weap = 0
		self.work_finish = [0]
		self.dop_work_finish = []
		self.rod = 0 #Откуда персонаж родом
		self.kills = 0
		self.dies = 0
		self.trades = 0
		self.monster_kills = 0

		self.ability = []  #Боевые способности
		self.using_ability = True
		self.ability_active = ''
		
		self.dragon_kills = 0
		self.animals = [] #Владение животными
		self.machines = [] #Владение транспортом или боевыми машинами.
		self.competitions = [] #Выиграные соревнования по бегу
		self.helpers = [] #Союзники
		self.in_trade = [] #Товары находящиеся в процессе продажи

		self.buildings = [Home(0, 990000, 0)] #Приобретённые строения. Код для домов - 0.
		self.buildings_invents = []

		self.dialogs = []

		self.skills = []

		self.status = ''

		self.mining_list = {}

		#self.weap.append(Weapon("Камень", 200, 3, 1, 200001, 0))




	def load_state(self, filename):
		print("Выберите сохранение:")
		print("1 - Последнее")

		for i in range(10):
			print(str(i+2) + " - " + str(i+1) + "-я ячейка.")

		ch = int(input())

		while ch < 1 or ch > 11:
			print("Выбор некорректный, пожалуйста повторите.")
			ch = int(input())			
		
		if ch == 1:
			with open('saves/autosave.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 2:
			with open('saves/save_01.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 3:
			with open('saves/save_02.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 4:
			with open('saves/save_03.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 5:
			with open('saves/save_04.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 6:
			with open('saves/save_05.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 7:
			with open('saves/save_06.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 8:
			with open('saves/save_07.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 9:
			with open('saves/save_08.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 10:
			with open('saves/save_09.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()
		if ch == 11:
			with open('saves/save_10.bin', 'rb') as f:
				g = pickle.load(f)
				f.close()

		self.name = g['name']
		self.s = g['s']
		self.m = g['m']
		self.mg = g['mg']
		self.u = g['u']
		self.l = g['l']
		self.vs = g['vs']
		self.mon = g['mon']
		self.exp = g['exp']
		self.upgr = g['upgr']
		self.weap = g['weap']
		self.awards = g['awards']
		self.loc = g['loc']
		self.dialog = g['dialog']
		self.work = g['work']
		self.work_end = g['work_end']
		self.invent = g['invent']
		self.heal = g['heal']
		self.sleep = g['sleep']
		self.loc_town = g['loc_town']
		self.hits = g['hits']
		self.work_finish = g['work_finish']
		self.dop_work_finish = g['dop_work_finish']
		self.rod = g['rod']
		self.kills = g['kills']
		self.dies = g['dies']
		self.trades = g['trades']
		self.monster_kills = g['monster_kills']
		self.ability = g['sp']
		self.dragon_kills = g['dragon_kills']
		self.animals = g['animals']
		self.machines = g['machines']
		self.competitions = g['competitions']
		self.helpers = g['helpers']
		self.in_trade = g['in_trade']

		self.buildings = g['buildings']
		self.buildings_invents = g['buildings_invents']

		self.dialogs = g['dialogs']

		for i in range(len(self.buildings_invents)):
			g = self.buildings_invents[i]

			self.buildings[i].invent = g

		try:
			self.skills = g['skills']
			self.status = g['status']
			self.mining_list = g['mining_list']
		except:
			self.skills = []
			self.status = ''
			self.mining_list = {}


	def save_state(self, filename):
		save_data = {'name' : self.name, 's' : self.s, 'm' : self.m, 'mg' : self.mg, 'u' : self.u, 
			'l' : self.l, 'vs' : self.vs, 'mon' : self.mon, 'exp' : self.exp, 
			'upgr' : self.upgr, 'weap' : self.weap,
			'awards' : self.awards, 'loc' : self.loc, 'dialog' : self.dialog,
			'work' : self.work, 'work_end' : self.work_end, 'invent' : self.invent,
			'heal' : self.heal, 'sleep' : self.sleep, 'loc_town' : self.loc_town,
			'hits' : self.hits, 'work_finish' : self.work_finish, 
			'dop_work_finish' : self.dop_work_finish, 'rod' : self.rod, 
			'kills' : self.kills, 'dies' : self.dies, 'trades' : self.trades,
			'monster_kills' : self.monster_kills, 'sp' : self.ability,
			'dragon_kills' : self.dragon_kills, 'animals' : self.animals,
			'machines' : self.machines, 'competitions' : self.competitions,
			'helpers' : self.helpers, 'in_trade' : self.in_trade,
			'buildings' : self.buildings, 'buildings_invents' : self.buildings_invents,
			'dialogs' : self.dialogs, 'skills' : self.skills, 'status' : self.status,
			'mining_list' : self.mining_list

		}

		with open(filename, 'wb') as f:
			pickle.dump(save_data, f)
			f.close()
		#print(save_data)

	def add_money(self, some_money):
		self.mon += some_money

	def decrease_money(self, price):
		self.mon -= price

	def can_afford(self, price):
		if self.mon > price:
			return True
		else:
			print("Вам не хватает денег на прокупку данного товара.")
			return False

	def buy_item(self, item, code=0):
		self.invent.append(item)
		print("Товар " + item.name + " находится в вашем инвентаре!")
		self.decrease_money(item.price)


	def check_clothes(self, item, code, a, b):
		self.invent.append(item)

	def buy_clothes(self, item, code):
		self.check_clothes(item, code, 86, 92)
		self.decrease_money(item.price)
		if code == 115 or code == 116:
			self.buy_weapon(item, code)


	def buy_weapon(self, item, code):
		self.weap.append(item)
		print("Оружие " + item.name + " находится в вашем инвентаре!")
		self.decrease_money(item.price)

	def buy_patron(self, item, code):
		for i in range(len(self.weap)):
			g = self.weap[i]

			if g.code == code:
				g.patrons += 10
				print("Боезапас пополнен.")
			else: 
				self.weap.append(item)
				print("Боеприпасы " + item.name + " находится в вашем инвентаре!")
				self.decrease_money(item.price)



	def die(self):
		gf = GameFunctions("")
		sp_hp = 0
		for kk in self.invent:
			if kk.__class__.__name__ == 'Clothes'and 'Одето' in kk.name:
				try:
					if kk.code >= 117 and kk.code <= 123:
						sp_hp += kk.hp
				except: continue
		if self.hits >= (20 + sp_hp):
			print("Вы умерли!")
			gf.enter()
			return 1
		else:
			return 0

	def search_weapon(self):
		print("У вас есть: ")
		for i in range(len(self.weap)):
			g = self.weap[i]

			
			print(g.name)


	def choose_weap(self, gf):
		if len(self.weap) > 0:
			print("Выбирайте:")
			for i in range(len(self.weap)):
				g = self.weap[i]
				print(str(i+1) + " - " + g.name)
			ch = gf.player_ask_selection("", 1, len(self.weap))
			self.take_weap = self.weap[ch-1]
			del self.weap[ch-1]
		else:
			print("В вашем инвентаре нет оружия.")

	def return_weap(self):
		if self.take_weap != 0:
			self.weap.append(self.take_weap)
			self.take_weap = 0

	def miss(self):
		miss_say = ["Вы нереально сильно замахнулись, но всё же не попали.", 
					"Оружие - " + self.take_weap.name + " Отказывается функционировать",
					"Вы меткий игрок, но сегодня это вам не помогло.",
					"Соберись, нужно действовать, а не промахиваться.",
					"Вы сосредаточенно собрались нанести удар, но под конец сбились с цели!"]

		return miss_say[random.randrange(4)]



	def check_full(self):
		if self.s == 20 and self.m == 20 and self.mg == 20 and self.u == 20 and self.l == 20 and self.vs == 20:
			return 1


	def find_work(self, work_code):
		for i in self.work_finish:
			if work_code == i:
				return False

		return True

	def find_dialog(self, code):
		for i in range(len(self.dialogs)):
			g = self.dialogs[i]

			if g == code:
				return False

		return True

	def find_item(self, name):
		for i in self.invent:
			if i.name == name: return True
		return False




'''
self.name = name
		self.s = s
		self.m = m
		self.mg = mg
		self.u = u
		self.l = l
		self.vs = vs
		self.mon = 0
		self.exp = 0
		self.upgr = 0
		self.weap = [Weapon("Кулаки", self.s, self.mg, 0, 0, 0)]
		self.awards = []
		self.loc = 0
		self.dialog = 0
		self.work = 0
		self.work_end = 0
		self.invent = []
		self.heal = 0
		self.sleep = 0
		self.loc_town = 0
		self.hits = 0
		self.take_weap = 0
		self.work_finish = []
		self.dop_work_finish = []
		self.rod = 0
		self.kills = 0
		self.dies = 0
		self.trades = 0
		self.monster_kills = 0
		self.sp = []  #Боевые способности
		self.animals = [] #Владение животными
		self.machines = [] #Владение транспортом или боевыми машинами.
		self.competitions = [] #Выиграные соревнования по бегу
		self.helpers = [] #Союзники

'''