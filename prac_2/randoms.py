import random
print(random.randint(5, 20))  # line 1
# the smallest number is 5 and the largest is 20
print(random.randrange(3, 10, 2))  # line 2 / the (2) in is the step value
# In line 2 the number 4 will not appear in the results since it is skipped as it fall withing the step value.
# The smallest value is 5 and the largest is 9
print(random.uniform(2.5, 5.5))  # line 3
# The smallest number that I could see is 2.532 and the biggest is 5.4

# The number 1 and 100 is inclusive.
print(random.randint(1, 100))
