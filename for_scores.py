all_scores = [
	{'school_class': '4a', 'scores': [3,4,4,5,2,3,4,4,5,2,3,4,4,5,2]}, 
	{'school_class': '4б', 'scores': [3,4,4,5,2,3,2,4,5,2,5,4,2,4,4,5,2,3,4,4,5,2]}, 
	{'school_class': '5а', 'scores': [3,4,4,5,2,2,5,2,5,4,2,3,4,4,5,2,3,4,4,5,2]}, 
	{'school_class': '5б', 'scores': [3,4,4,5,2,3,4,4,2,4,5,2,5,4,2,5,4,2,5,4,5,2,3,4,4,5,2]}, 
	{'school_class': '6a', 'scores': [3,4,4,5,2,3,4,4,2,4,5,2,5,4,2,5,2,5,2,3,4,4,5,2]}, 
	{'school_class': '6б', 'scores': [5,4,4,5,5,5,4,2,5,5,5,5,5,2,5,4,2,4,5,2,5,4,4,5,2]}, 
]

class_rates = []

for classes in all_scores:
	class_summary = sum(classes.get('scores'))
	students = len(classes.get('scores'))
	class_rate = (class_summary / students)
	class_rates.append(class_rate)
	print('Средний бал {} класса: {}'.format(classes.get('school_class'), round(class_rate,1)))

school_rate = sum(class_rates) / len(all_scores)
print('Средний бал школы: {}'.format(round(school_rate,1)))