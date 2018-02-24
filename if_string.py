def comprasion(string_1, string_2):
	if string_1 == string_2:
		return 1
	elif string_1 != string_2 and len(string_1) > len(string_2) and string_2 != 'learn':
		return 2 
	elif string_1 != string_2 and string_2 == 'learn':
		return 3

string_1 = input('Введите первую строку: ')
string_2 = input('Введите вторую строку: ')
result = comprasion(string_1, string_2)
print(result)