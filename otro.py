#Se creo el diccionario
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

#ou can determine the number of items by using len, and iterate through it by using for loops. In the dictionary you created, the planet names are keys and the number of moons are the values.
#Start by retrieving a list with the number of moons, and store this in a variable named moons. Then obtain the total number of planets and store that value in a variable named total_planets.
moons = planet_moons.values()
total_planets = len(planet_moons.keys())

#Start by creating a variable named total_moons; this will be your counter for the total number of moons.
total_moons = 0
#add a for loop to loop through the list of moons
for moon in moons:
    #adding each value to total_moons
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet average {average} moon')