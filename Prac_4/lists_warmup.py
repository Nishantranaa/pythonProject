numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]
# numbers[-1]
# numbers[3]
# numbers[:-1]
# numbers[3:4]
# 5 in numbers
# 7 in numbers
# "3" in numbers
# numbers + [6, 5, 3]

print(numbers[0:])
print(numbers[3:5])
print(numbers + [6, 5, 3])
# change the first element of numbers to "ten"
numbers[0] = str("ten")
print(numbers[0])
# change the last element of numbers to 1
numbers[-1] = str(1)
print(numbers[1])
# Get all the elements from numbers except the first two (slice)
print(numbers[2:])
# Check if 9 is an element of numbers
test = numbers[-2] > 0 # boolean statement
print("It is a numeric value")
print(type(test))
