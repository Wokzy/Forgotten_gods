import random


def cubes_fall(numbers, iteration):
	global check
	check = False

	lst = []
	it = 0

	numb = numbers

	for i in range(numb): lst.append(0)
	lst.append('')


	while check != True:
		for i in range(len(lst)-1):
			lst[i] = random.randint(1, 7)

		for i in range(len(lst)-1):
			check = True
			g = lst[i]
			if not g == lst[i+1] and lst[i+1] != '':
				check = False
				break
		if it > iteration:
			return False
		it += 1

	lst.pop()
	return True