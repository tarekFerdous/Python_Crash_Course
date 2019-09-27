cars = ['bmw', 'audi', 'toyota', 'subaru']
#original list
print('Original List : ' + str(cars))

#sorted list
cars.sort()
print('Sorted List : ' + str(cars))

#sorted list in reverse
cars.sort(reverse = True)
print('Sorted List in reverse : ' + str(cars))

#temporary sort with sorted(list)
print('Sorted List with sorted(list): ' + str(sorted(cars)))

#temporary reversed sort with sorted(list)
print('Sorted List with sorted(list, reverse): ' + str(sorted(cars, reverse=True)) + '\n')


cars = ['bmw', 'audi', 'toyota', 'subaru']
#reversed list
cars.reverse()
print('Reversed List : ' + str(cars))

#length of a list
print('Length of the list : ' + str(len(cars)))