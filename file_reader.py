with open('referat.txt', 'r', encoding = 'utf-8') as file:
	content = f.read()
	words = content.split()
	print(len(words))