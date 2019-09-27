invitation_list = ['Tarek', 'Ferdous', 'Madara']
message = ' will be invited'
temp = invitation_list.pop(0)
print(temp + ' cannot make it to dinner.')
invitation_list.insert(0, 'Itachi')
print(invitation_list[0] + message)
print(invitation_list[1] + message)
print(invitation_list[2] + message)
