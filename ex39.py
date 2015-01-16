#Exercise 39: Dictionaries, Oh Lovely Dictionaries

print  "====== Start of Exercise 39: Dictionaries, Oh Lovely Dictionaries ====="
# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Maryland': 'MD'
        }
#print states

#Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'MD': ' Lutherville'
}
#print cities

#print "Before adding more ", cities
# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['MD'] = 'Baltimore'
cities['NY'] = 'Bufallo'
#print "After adding more ", cities

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 10
print "Michagan's Abbervation is: ", states['Michigan']
print "Florida's Abbervation is: ", states['Florida']

# do it by using the state and cities dict
print '-' * 10
print "Michagan's Abbervation is: ", cities[states['Michigan']]
print "Michagan's Abbervation is: ", cities[states['Florida']]

print '\n'
#print states.items()
#print cities.items()

# print every states abbreviation
print '-' * 10
for state , abbrev in states.items():
        print "%s is abbreviated %s" % (state, abbrev)

# print every city in the states
print '-' * 10
for abbrev, city in cities.items():
        print "%s is abbreviated %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
        print "%s state is abbreviated %s and has city %s " % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by states that might now be there
state =  states.get('Texas')
#print state

if not state:
        print "Sorry, no Texas."

# get a city with a default value
city = cities.get("TX","does not Exist" )
print "The city for the state 'TX' is: %s" % city


print "====== End of Exercise 39: Dictionaries, Oh Lovely Dictionaries   ====="
