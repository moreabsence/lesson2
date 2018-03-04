import csv

answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}


with open('export.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    for key, value in answers.items():
        writer.writerow([key] + [value])

