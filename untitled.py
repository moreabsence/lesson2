from ephem import *

planet_name = input('Планета') 

planets = {'Mars': Mars}

if planet_name in planets:
    m = planets.get(planet_name) 
    print(constellation(m('2017')))

words = {
        'ноль' : 0,
        'один' : 1,
        'два' : 2,
        'три': 3,
        'четыре' : 4,
        'пять' : 5,
        'шесть' : 6,
        'семь' : 7,
        'восемь' : 8,
        'девять' : 9}

        for station, geo_station in repairs.items():
	try:
		for stop, geo_stop in geo_stations.items():
			if geopy.distance.vincenty(geo_station, geo_stop).m < 500:
				if not station in stops_for_station:
					stops_for_station[station] = 1
				elif station in stops_for_station:
					stops_for_station[station] += 1
	except ValueError:
		continue


		
				elif station in stops_for_station:

					stops_for_station[station] += 1

for geo_stop in geo_stations:

	try:

		for station in repairs:
			print(station)

			if geopy.distance.vincenty(geo_stop, repairs.get(station)).m < 500:

				if not station in stops_for_station:

					stops_for_station[station] = 1

	except ValueError:

		continue



for station, stops in stops_for_station.items():
	if not top_station:
		top_station = (station, stops)	
	elif int(stops) > int(top_station[1]):
		top_station = (station, stops)	

print(stops_for_station)
print(top_station)