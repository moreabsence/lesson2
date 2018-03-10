import csv
import datetime

file_list = []

with open('data-397-2018-03-02.csv', 'r', encoding = 'utf-8') as file:
	fields = [
	'ID',
	'Name',
	'Longitude_WGS84',
	'Latitude_WGS84',
	'NameOfStation',
	'Line',
	'ModeOnEvenDays',
	'ModeOnOddDays',
	'FullFeaturedBPAAmount',
	'LittleFunctionalBPAAmount',
	'BPAAmount',
	'RepairOfEscalators',
	'global_id',
	'geoData']
	reader = csv.DictReader(file, fields, delimiter = ';')
	for row in reader:
		file_list.append(row)

top_street = []

repairs = {}

for line in file_list:
	if line['RepairOfEscalators'] == '':
		continue
	else:
		repairs[line['Name']] = line['RepairOfEscalators']


print(repairs)
