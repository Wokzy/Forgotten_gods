import random

def colors(stav):
	if stav == '00': stv = 61
	else: stv = int(stav)
	res = random.randint(1, 61)

	print('Выпадает ', res)

	k = 0

	if res%2 == 0 and stv == 62: return True
	elif res%2 != 0 and stv == 63: return True
	elif res <= 30 and stv == 64: return True
	elif res >= 31 and stv == 65: return True
	elif res == stv: return True
	else: return False

'''
while True:
	print(colors(input()))
'''