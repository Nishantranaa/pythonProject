# # TODO THIS CODE ASKS A USER TO ENTER A PET NAME AND THEN
# # TODO CHECKS WHETHER THE NAME EXISTS IN THE LIST.



myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
