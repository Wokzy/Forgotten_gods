import random


def hangman():
	with open('words.txt', 'r') as f: words = f.read().split('\n')
	word = random.choice(words)

	print('Слово состоит из ' + str(len(word)) + ' букв(ы)')
	string = list('-'*len(word))
	itr = 15
	while ''.join(string) != word and itr > 0:
		print('Результат: ', ''.join(string))
		mode = False
		print('Попыток осталось: ', itr)
		while True:
			k = input('Введите желаемую букву: ')
			if len(k) == 1 and k.isalpha() : break
			else: print('То, что вы ввели не корректно, повторите ввод.') 

		for i in range(len(word)):
			g = word[i]
			if k == g:
				del string[i]
				string.insert(i, k)
				mode = True
		if mode == False: itr -= 1

	if itr == 0: print('Вы проиграли! Слово: ', word)
	print('Вы выиграли! Слово: ', ''.join(string))




hangman()
input()