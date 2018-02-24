answers = {"Сколько время?": "Пора спать!", "Как дела?": "Лучше всех", "Что дальше?": "Увидишь"}


def get_answers(question, answers):
    return answers.get(question)


def ask_user(answers):
	try:
		while True:
			user_say = input('Что ты хочешь узнать? ')
			print(get_answers(user_say, answers))
			if user_say == 'Пока!':
				break
	except KeyboardInterrupt:
		print(' Прошу вас, постойте!')

if __name__ == '__main__':
	ask_user(answers)

