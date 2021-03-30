import random

def runner(stav):
	stv = str(float(stav))
	a = random.randint(1, 9)
	b = random.randint(0, 99)

	print('Текущее число - ', str(a)+'.'+str(b))

	if len(stv) < 4: stv += '0'

	a_ = int(stv[0])
	b_ = int(stv[2] + stv[3])

	x = a_*100 + b_
	y = a*100 + b

	if x <= y: return True
	else: return False

'''
while True:
	print(runner(input()))
	input()
'''
'''
	while True:
		try:
			stv = float(input('Введите вашу ставку: '))
			break
		except: print('Ставка не корректная, пожалуйста повторите.')
'''