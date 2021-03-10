# out_file = open('name.txt', 'w')
#
# name = str(input("What is your name: "))
# print("My name is {}".format(name), file=out_file)
# out_file.close()

# TODO: Prac - This code reads the files and then prints the name.

# in_file = open('name.txt', 'r')
# print(in_file.read())
# in_file.close

# It is very important to close a file so as to not loose any data, its its saves it from buffer to file.

# TODO: Prac - This code will read the first two lines then add them together and prints the result.


out_file = open('numbers.txt', 'r')
line1 = out_file.readline()
line2 = out_file.readline() # the second line would be read as the first current file position is saved and will read
# from there onwards.
number = int(line1) + int(line2)

print(number)

out_file.close()


# out_file = open('numbers.txt', 'r')
# print(out_file.read(1)) # read each characters one by one.
# out_file.close()

# TODO: Prac - This last block of code would literate through the entire list and then add all the lines.
# Need to convert the incoming string to an integer.


in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number

in_file.close()
print(total)
