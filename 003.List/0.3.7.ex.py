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