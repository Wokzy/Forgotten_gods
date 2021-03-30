import random
from Enemy import *
from ElixirItem import *



class TeamMate():
	def __init__(self, name, hp, damage, ability=[], using_ability=True, type_='Человек'):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.type_ = type_
		self.ability = ability
		self.using_ability = using_ability
		self.ability_active = ''


	def check_die(self, l_char):
		if self.hp <= 0:
			for i in range(len(l_char.helpers)):
				g = l_char.helpers[i]
				if g.name == self.name:
					del l_char.helpers[i]
					break