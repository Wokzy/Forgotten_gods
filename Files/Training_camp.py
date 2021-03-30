import random
import keyboard
import os
from ElixirItem import *
from Enemy import *



class Training_camp():
	def __init__(self):
		self.a = 1
		self.enemyes_names = ['Гильем', 'Ричард', 'Иоханн', 'Роберт', 'Гугон', 'Рогир', 
								'Вальтер', 'Томас', 'Ральф', 'Гальфрид', 'Генрих', 
								'Адам', 'Николас', 'Алан', 'Гилберт', 'Стефан', 
								'Режинальд', 'Александр(Саня - бессметрный сосед)', 
								'Осберт', 'Арнольд ', 'Годфрид', 'Герберт', 
								'Филипп', 'Эдвард',]


	def start_training(self, l_char, gf):
		while True:
			print('')
			print('Добро пожаловать в тренировочный лагерь!')
			print('Выберите тип тренировок:')
			print('')
			print('1 - Силовой')
			print('2 - На ловкость')
			print('3 - Пойти наколдовать удачи')
			print('4 - Пойти тренировать магию')
			print('5 - Отточить восприятие')
			print('6 - Потренировать стрельбу')
			print('7 - Устроить дуэль')
			print('8 - Выход')

			ch = gf.player_ask_selection('', 1, 8)

			if ch == 1: self.power_training(l_char, gf)
			elif ch == 2: self.dexterity_training(l_char, gf)
			elif ch == 3: self.lucky_training(l_char, gf)
			elif ch == 4: self.magic_training(l_char, gf)
			elif ch == 5: self.perception_training(l_char, gf)
			elif ch == 6: self.shoot_training(l_char, gf)
			elif ch == 7: self.duel(l_char, gf)
			else:
				gf.update(l_char)
				break

			gf.update(l_char)




	def power_training(self, l_char, gf):
		if l_char.s >= 4 and len(l_char.work_finish) < 6:
			print('Вам нужно пройти больше миссий, чтобы снова тренироваться здесь.')
		else:
			if l_char.u < 2 and random.randrange(0, 3) == 1: 
				print('Вы попытались что-то исполнить, но у вас не получилось')
			else:
				print('Вы подкачали свои мышцы и теперь ваша сила возросла на 1-ну единицу')
				l_char.s += 1
				l_char.exp += 10
				gf.enter()

	def dexterity_training(self, l_char, gf):
		if l_char.l >= 3 and len(l_char.work_finish) < 6:
			print('Вам нужно пройти больше миссий, чтобы снова тренироваться здесь.')
		else:
			if l_char.s < 3 and random.randrange(0, 3) == 1: 
				print('Вы попытались что-то исполнить, но у вас не получилось')
			else:
				print('Вы улучшили свой навык ловкости, теперь ловкость возросла на 1-ну единицу')
				l_char.l += 1
				l_char.exp += 15
				gf.enter()

	def lucky_training(self, l_char, gf):
		if len(l_char.work_finish) < 8:
			print('Вам нужно пройти больше миссий, чтобы снова тренироваться здесь.')
		else:
			print('Вы пришли к колдунье и собираетесь наколдовать себе удачу')
			print('Всё получилось успешно')
			l_char.u += random.randrange(0, 2)
			l_char.exp += 15
			gf.enter()

	def magic_training(self, l_char, gf):
		if l_char.m == 0 or len(l_char.work_finish) < 10:
			print('Вы пока что не можете тренировать навыки магии.')
		else:
			print('Вы успешно улучшили новые приёмы магии.')
			l_char.mg += random.randrange(0, 2)
			l_char.exp += 30
			gf.enter()

	def perception_training(self, l_char, gf):
		if l_char.vs >= 3 and len(l_char.work_finish) < 5:
			print('Вам нужно пройти больше миссий, чтобы снова тренироваться здесь.')
		else:
			print('Вы зашли в лес и начали тренировку восприятия')
			print('Вы повысили своё восприятие на 1-ну единицу')
			l_char.vs += 1
			l_char.exp += 20
			gf.enter()

	def shoot_training(self, l_char, gf):
		if l_char.m >= 3 and len(l_char.work_finish) < 7:
			print('Вам нужно пройти больше миссий, чтобы снова тренироваться здесь.')
		else:
			print('Вы взяли огнестрел (Револьвер) и начали стрельбу по мишеням.')
			if random.randrange(0, 4) == 1: print('Вы вдоволи настрелялись но навыки не улучшили =(')
			else:
				print('Вы повысили свою меткость на 1-ну единицу')
				l_char.m += 1
				l_char.exp += 30
			gf.enter()

	def duel(self, l_char, gf):
		l_char.heal = 0
		l_char.weap.append(Weapon("Револьвер тренировочный", 10, 1, 190, 68, 9))

		enemy_name = self.enemyes_names[(random.randrange(0, len(self.enemyes_names)))]
		enemy = Enemy(enemy_name, random.randrange(10, 60), 1)
		print('Ваш соперник в текущей дуэли - ' + enemy_name + '. Желаем удачи.')
		gf.enter()
		gf.battle(gf, l_char, [enemy])
		
		for i in range(len(l_char.weap)):
			g = l_char.weap[i]
			if g .name == "Револьвер тренировочный":
				del l_char.weap[i]
		gf.update(l_char)

		exp = random.randrange(20, 70)
		money = random.randrange(15, 40)
		print('')
		print('Вы успешно сразили соперника - ' + enemy_name + ". И получили " + str(exp) + 'ед. опыта\
, А также ' + str(money) + ' монет(у)(ы)')
		l_char.exp += exp
		l_char.mon += money
		gf.update(l_char)