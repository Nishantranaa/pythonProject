
for i in range(1, 20, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(1, 21, 1):
    print(i, end=' ')
print()

number_of_stars = int(input("Number of stars: >>>>"))
for i in range(number_of_stars):
    print('*', end='')
print()



for i in range(1, 10, 3):
 print(i)

number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print('*' * i)


names = ["Barry", "Tux", "Ada", "Maggie"]
for i, name in enumerate(names):
    print(i, " - ", name)


age = int(input("Age: "))
while age < 0:
    print("Invalid age!")
    age = int(input("Age: "))
print("You are {} years old".format(age))

is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)