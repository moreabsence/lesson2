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