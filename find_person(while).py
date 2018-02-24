def find_person(name, mylist):
	while True:
		x = mylist.pop()
		if x == name:
			print('{} нашелся!'.format(name))
			break
		else:
			print(x)

find_person('Валера', ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"])