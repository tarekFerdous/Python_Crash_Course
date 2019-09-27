cities = ['Dhaka', 'Rajshahi', 'Barisal', 'Chattogram', 'Sylhet']
#append
cities.append('Khulna')
#insert
cities.insert(3, 'Rangpur')
#del
del cities[3]
#pop
cities.pop()
cities.pop(4)
#remove
cities.remove('Chattogram')
#sorted()
print('Sorted() ascending: ' + str(sorted(cities)))
print('Sorted() descending: ' + str(sorted(cities, reverse=True)))
#sort()
cities.sort()
print('Sort() ascending: ' + str(cities))
cities.sort(reverse=True)
print('Sort() descending: ' + str(cities))
#reverse()
cities.reverse()
print('Reversed() : ' + str(cities))