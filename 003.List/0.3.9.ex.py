#0.3.4.ex
print('#0.3.4.ex')
invitation_list = ['Tarek', 'Ferdous', 'Madara']
message1 = ' will be invited.'
message0 = 'Total person, '
print(invitation_list[0] + message1)
print(invitation_list[1] + message1)
print(invitation_list[2] + message1)
print(message0 + str(len(invitation_list)) + '\n')

#0.3.5.ex
print('#0.3.5.ex')
invitation_list = ['Tarek', 'Ferdous', 'Madara']
message1 = ' will be invited'
temp = invitation_list.pop(0)
print(temp + ' cannot make it to dinner.')
invitation_list.insert(0, 'Itachi')
print(invitation_list[0] + message1)
print(invitation_list[1] + message1)
print(invitation_list[2] + message1)
print(message0 + str(len(invitation_list)) + '\n')

#0.3.6.ex
print('#0.3.6.ex')
invitation_list = ['Tarek', 'Ferdous', 'Madara']
message = ' will be invited.'
invitation_list.insert(0, 'Itachi')
invitation_list.insert(3, 'Sasuke')
invitation_list.append('Kakashi')
print(invitation_list[0] + message)
print(invitation_list[1] + message)
print(invitation_list[2] + message)
print(invitation_list[3] + message)
print(invitation_list[4] + message)
print(invitation_list[5] + message)
print(message0 + str(len(invitation_list)) + '\n')

#0.3.7.ex
print('#0.3.7.ex')
invitation_list = ['Itachi', 'Tarek', 'Ferdous', 'Sasuke', 'Madara', 'Kakashi']
message = ' will be invited.'
message2 = 'I cannot invite you to my dinner.'
#task01
print('I can invite only two people for dinner')
#task02
temp = invitation_list.pop()
print('Sorry, ' + temp + message2)
temp = invitation_list.pop()
print('Sorry, ' + temp + message2)
temp = invitation_list.pop()
print('Sorry, ' + temp + message2)
temp = invitation_list.pop()
print('Sorry, ' + temp + message2)
#task03
print(invitation_list[0] + message)
print(invitation_list[1] + message)
#task04
del invitation_list[0]
del invitation_list[0]
print(str(invitation_list))
print(message0 + str(len(invitation_list)))