import random


'''
class ShopItem():
	""" useful game function """
	def __init__(self, name, item_type_, price):
		#super(Character, self).__init__()
		self.name = name
		self.type_ = item_type_
		self.price = price
'''



class ElixirItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class ElItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class HardElItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class WhiteDragonItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class RedDragonItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class SnakeItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class VodkaItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class PigItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class MuttonItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class BeefItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class DragonMeatItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class YagodiItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None

class HealthGrassItem():
	""" useful game function """
	def __init__(self, name, price, code):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = None





class Clothes():
	""" useful game function """
	def __init__(self, name, price, code=10100101, hp=0):
		#super(Character, self).__init__()
		self.name = name
		self.price = price
		self.hp = hp
		self.code = code
		self.invent = []
		self.trade_price = 0
		self.type_ = 'Clothes'






class Item_standart():
	"""docstring for Item"""
	def __init__(self, name, price, code):
		self.name = name
		self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = 'Standart'


class Scope():
	"""docstring for Item"""
	def __init__(self, name, price, code, leight):
		self.name = name
		self.price = price
		self.code = code
		self.leight = leight
		self.trade_price = 0
		self.type_ = None


class Item_special():
	"""docstring for Item"""
	def __init__(self, name, code:str='101010101'):
		self.name = name
		#self.price = price
		self.code = code
		self.trade_price = 0
		self.type_ = 'Special'


class Weapon():
	"""docstring for Item"""
	def __init__(self, name, hit, air_hit, price:int=0, code=10101011, max_patrons=100):
		self.name = name
		self.hit = hit
		self.code = code
		self.price = price
		self.air_hit = air_hit
		self.count = 1
		self.invent = []
		self.max_patrons = max_patrons
		self.patrons = max_patrons
		self.trade_price = 0
		self.type_ = 'Weapon'


class Patron():
	"""docstring for Item"""
	def __init__(self, name, damage, price, code):
		self.name = name
		self.code = code
		self.damage = damage
		self.patrons = 60
		self.price = price
		self.trade_price = 0
		self.type_ = None

class Award():
	"""docstring for Item"""
	def __init__(self, name, code, exp):
		self.name = name
		self.code = code
		self.exp = exp
		self.type_ = None




class Card():
	def __init__(self, scale, lear):
		self.scale = scale
		self.lear = lear
		self.type_ = None


class Udochka:
	def __init__(self, name, chance, price=None, work=100, code='x'):
		self.name = name
		self.price = price
		self.code = code
		self.type_ = 'Удочка'
		self.chance = chance
		self.work = work

class Fish:
	def __init__(self, name, price):
		self.name = name
		self.price = price
		self.type_ = 'Рыба'


class Ability:
	def __init__(self, name, cooldown):
		self.name = name
		self.cooldown = cooldown
		self.cdn = 0


class Pick:
	def __init__(self, name, speed:dict, price, mine_type:str='Standart'):
		self.name = name
		self.speed = speed
		self.mine_type = mine_type
		self.price = price