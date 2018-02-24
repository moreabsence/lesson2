names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

while True:
	x = names.pop()
	if x == 'Валера':
		print('Валера нашелся!')
		break
	else:
		print(x)
