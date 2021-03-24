# # def main():
# #     print('Type in a temperature or "done" to finish')
# #     temps = []  # list to store days' temperatures
# #     sum = 0
# #     done = input("Day 1's high temp: ")
# #     day = 1
# #     while (done != "done"):  # Eead each day's temperature
# #         done = int(done)
# #         sum = sum + done
# #         temps.append(done)
# #         done = input(("Day " + str(day + 1) + "'s high temp: "))
# #         day = day + 1
# #     average = sum / day
# #     count = 0  # See if each day is above average
# #     for i in range(0, day - 1):
# #         if (temps[i] > average):
# #             count = count + 1
# #     print("Average temp = " + str(average))
# #     print(str(count) + " days above average")
# #
# #
# # main()
#
#
# # Reads from the user, gives average
# # and number of days above average.
# def main():
#     days = int(input("How many days? "))
#     temps = [0] * days  # List to store temps.
#     sum = 0
#     for i in range(0, days): # Read each number.
#        temps[i] = int(input(("Day "+(i+1)+"'s temp: ")))
#        sum = sum + temps[i]
#     average = sum / days
#
#     count = 0 # See if each day is above average.
#     for i in range(0, days):
#         if (temps[i] > average):
#             count = count + 1
#     # Report the results.
#     print("Average temp = " + str(average))
#     print(str(count) + " days above average")
#
#
# main()


# letters = list("Things")  # assigns the string things to a list as 'T' 'h' 'i' 'n' 'g' 's' to the variable letters
# print(letters)
# print(list)
#
# things = [1, 'a', True]
# print(things)
# print(type(things))
#
# # A list of lists: each item is a short list of 2 items.
#
# all_months = [['january', 31], ['february', 28], ['march', 31],
#                    ['april', 30], ['may', 31], ['june', 30],
#                    ['july', 31], ['august', 31], ['september', 30],
#                    ['october', 31], ['november', 30], ['december', 31]]
#
# # Print the number of days in each month of all_months:
#
# # for j in range(0, len(all_months)):
# #     print(all_months[j][1])


# List of lists

# things = ['a', [1, 2, 3], 'z']
# things.remove('z')
# print(things.pop())

# things = ['dress', 'pink', 'flower', 'bee', 'Krishna']
# # things.remove('bee')
# # print(things.pop())
# print(" / ".join(things))

# print(things[1][0])
# print(things[1][1]) # the second element of index 1
# print(things[2][0]) # prints z
#
# for thing in things:
#     print(thing, end=" ")
#


# before = [1, 4, 0, -1]
# print(before.sort())
# print(before)
#
# before = ['n', "j", 'k']
# print(before.sort())
# print(before)
#
# things = list("Nishant")
# print(things)
# things.pop()
# print(things)

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort()
print(data)
# Gives [['Aaron', 9], ['Bob', 6], ['Carrie', 8], ['Derek', 7]]


from operator import itemgetter

 data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
 data.sort(key=itemgetter(1))
 print(data)
# Gives [['Bob', 6], ['Derek', 7], ['Carrie', 8], ['Aaron', 9]]


from operator import itemgetter

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort(key=itemgetter(1, 0))
print(data)
# Gives [['Bob', 6], ['Derek', 7], ['Carrie', 8], ['Aaron', 9]]
