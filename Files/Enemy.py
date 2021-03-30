import random


class Enemy():
	"""docstring for Enemy"""
	def __init__(self, name, hp, type_, damage=1, abilities=[]):
		
		self.name = name
		self.hp = hp
		self.type_ = type_
		self.damage = damage
		self.abilities = abilities

	def die_enemy(self, gf, l_char):
		if self.hp <= 0:
			print("Враг " + self.name + " повержен!")
			if self.type_ == 1:

				l_char.kills += 1
			else:
				l_char.monster_kills += 1
			gf.enter()
			return 1
		else:
			return 0
		