states = {'Oregon': 'OR','Florida' : 'FL','California' : 'CA','New York' : 'NY','Michigan' : 'MI'}
cities = {
		'CA' : 'San Francisco',
		'MI' : 'Detroit',	
		'FL' : 'Jacksonville',
	
	}
	
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
	
print '-' * 10
print "NY State has :" , cities['NY']
print "OR state has: " , cities['OR']
		
print '-' * 10
print "Michigans Abbreviation is" , states['Michigan']
print "Florida has: ", cities[states['Florida']]
	
print '-' * 10
for state, abbrev in states.items():
		print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])
		
	