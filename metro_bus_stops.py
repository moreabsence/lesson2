import csv
import datetime
import geopy.distance

metro_list = []

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
		metro_list.append(row)

repairs = {}
 	
for line in metro_list:
	if not line['RepairOfEscalators'] == '':
		repairs[line['NameOfStation']] = (line['Longitude_WGS84'],line['Latitude_WGS84'])


bus_list = []

with open('data-398-2018-02-13.csv', 'r', encoding = 'utf-8') as file:
	fields = [
	'id',
	'Остановка',
	'Longitude_WGS84',
	'Latitude_WGS84',
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
		bus_list.append(row)

geo_stations = []

for line in bus_list:
	geo_stations.append((line['Longitude_WGS84'], line['Latitude_WGS84']))

top_station = []

stops_for_station = {}

for geo_stop in geo_stations:
	try:
		for station in repairs:
			if geopy.distance.vincenty(repairs.get(station), geo_stop).m < 500:
				if not station in stops_for_station:
					stops_for_station[station] = 1
				elif station in stops_for_station:
					stops_for_station[station] += 1
	except ValueError:
		continue

for station, stops in stops_for_station.items():
	if not top_station:
		top_station = (station, stops)	
	elif int(stops) > int(top_station[1]):
		top_station = (station, stops)	

print(stops_for_station)
print(top_station)