#dictionaries

stuff = dict()
stuff['kite'] = 'sting'
stuff[1] = 20
stuff[-5] = 66

print(stuff)

del stuff[-5]

print(stuff)

#create a mapping of states to their abbreviations

states = {'Oregon': 'OR', 'Florida':'FL', 'California':'CA', 'New York': 'NY', 'Michigan': 'MI'}

#create basic dict of states and some cities in them

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'NY': 'Buffalo', 'FL':'Miami'}

#add some cities
cities['OR'] = 'Portland'
cities['NY'] = 'New York'

#print some cities
print('-'*10)
print("NY State has ", cities['NY'])
print("OR state has ", cities['OR'])

#print some states
print('-'*10)
print("Micigan's abbreviation is: ", states['Michigan'])
print("Oregon's abbreviation is: ", states['Oregon'])

#do it by using states and then cities
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("New York has: ", cities[states['New York']])

#print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

#print every city in state
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at at time
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
#safely get an abbreviation by state that may not be there

state = states.get('Texas')

if not state:
    print('Sorry, no Texas')

#get a city with default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")