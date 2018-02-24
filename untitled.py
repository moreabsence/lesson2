from ephem import *

planet_name = input('Планета') 

planets = {'Mars': Mars}

if planet_name in planets:
    m = planets.get(planet_name) 
    print(constellation(m('2017')))

