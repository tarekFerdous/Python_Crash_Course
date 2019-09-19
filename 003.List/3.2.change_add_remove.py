motorcycles = ['honda', 'yamaha', 'suzuki']
print('Original List : ' + str(motorcycles))


#changing element 0
motorcycles[0] = 'ducati'
print('Changed element 0 : ' + str(motorcycles))

motorcycles[0] = 'honda'


#adding elements to list with append()
motorcycles.append('ducati')
print('After appending : ' + str(motorcycles))


#adding elements to empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print('Empty list filled : ' + str(motorcycles))


#inserting elements using insert()
motorcycles.insert(0, 'ducati')
print('Inserting element at index 0 : ' + str(motorcycles))



#removing elements using del
del motorcycles[0]
print('Deleting element 0 : ' + str(motorcycles))


#removing element with pop()
temp=motorcycles.pop()
print('After popping : ' + str(motorcycles))
print('Popped element : ' + temp)


#removing element with pop(int index)
temp=motorcycles.pop(1)
print('After popping : ' + str(motorcycles))
print('Popped element : ' + temp)

motorcycles = ['honda', 'yamaha', 'suzuki', 'honda']


#removing an element by value with remove(value)
motorcycles.remove('honda')
print('After removing honda : ' + str(motorcycles))