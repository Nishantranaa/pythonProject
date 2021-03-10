s = ord("N") #  used to find the unicode dec value of a single character and not a string value.
print(s)

s = chr(78) # this function is used to find the char value using a unicode dec value.
print(s)

s = "My God name is HariKrishna and I believe in Him entirely"
t = s[:]
print(t)

s = "I believe in Hari Krishna"
reversed=s[::-1]
print(reversed)

for char in "Test":
    print(char, type(char))

# the operator is overloaded means that an operator does diffent task based off the datatype.
print("Nishant" + "HariKrishna")

word = "Transport"
t = "r" in word
print(t)

t = "z" in word
print(t)

compare = "Transport"
if word == compare:
    print('Yes')

print(compare[1])

compare = 'CARS'
print(compare)

# updating a character in a word

word = 'Nishant'
updated_word = word[:2] + 'z' + word[3:] + " pronounced by Shila kaki"
print(updated_word)

"""This is a docstring. It describes the how the function works."""

# A function algorithm is encapsulated within it, we only need to know the name of the function to call it and operate it .
# A method is applied on a object using a dot notation invocation. Invocation means the action of invoking someone or something.


for num in range(00, 13, 3):
    print(num, end=' ')





