import math

MENU = str(
    "Menu \n (E)VEN NUMBERS BETWEEN X AND Y \n (O)DD NUMBERS BETWEEN X AND Y \n (S)QUARES BETWEEN X AND Y \n (Q)QUIT")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(MENU)
choice = str(input("SELECT OPTION: ")).upper()
while choice != "Q":
    if choice == "E":
        for num in range(x, y + 1):
            if num % 2 == 0:
                print(num, end=" ")
                choice = "Q"
    elif choice == "O":
        for num in range(x, y, + 1):
            if num % 2 > 0:
                print(num, end=" ")
                choice = "Q"
    elif choice == "S":
        print('Square root of the first number is:', math.sqrt(x), "and the second number is:", math.sqrt(y))
        choice = "Q"

    else:
        print("Invalid Input try again")
        print(MENU)
        choice = (input("SELECT OPTION:")).upper()

print("The End")
