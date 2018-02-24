birth_year = input('Введите возраст: ')
birth_year = float(birth_year)
if birth_year < 7:
	print('Вам пора в детский сад')
elif birth_year >= 7 and birth_year < 18:
	print('Вам пора в школу:')
elif birth_year >= 18 and birth_year < 22:
	print('Вам пора в институт')
elif birth_year >= 22:
	print('Вам пора на работу')