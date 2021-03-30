import pickle


test = {'hello' : 155}

with open('saves/Test.bin', 'wb') as f:
	pickle.dump(test, f)


with open('saves/Test.bin', 'rb') as f:
	g = pickle.load(f)
	print(g)

input()