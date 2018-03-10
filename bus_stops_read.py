import csv

list = []

with open('data-398-2018-02-13.csv', 'r', encoding = 'utf-8') as file:
	fields = [
	'id',
	'Остановка',
	'Долгота',
	'Широта',
	'Улица',
	'AdmArea',
	"District",
	"RouteNumbers",
	"StationName",
	"Direction",
	"Pavilion",
	"OperatingOrgName",
	"EntryState",
	"global_id",
	"geoData"]
	reader = csv.DictReader(file, fields, delimiter = ';')
	for row in reader:
		list.append(row)
		print(row)

top_street = []

stops_for_street = {}

for line in list:
	if not line['Улица'] in stops_for_street:
		stops_for_street[line['Улица']] = 1
	if line['Улица'] in stops_for_street:
		stops_for_street[line['Улица']] += 1

for street, stops in stops_for_street.items():
	if not top_street:
		top_street = (street, stops)	
	elif int(stops) > int(top_street[1]):
		top_street = (street, stops)	

print(top_street)