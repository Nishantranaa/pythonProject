try:

    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # while numerator or denominator != 0:
    fraction = numerator / denominator
    print(fraction)
        # break


except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Please re-enter a non zero integer")
    print("Please re-enter a non zero integer")
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")

# TODO Answer the following questions:
# 1. When will a ValueError occur?
#
# When the user enters a non int value on either numerator or denominator. This will be
# caught by the except value error statement.
#
# 2. When will a ZeroDivisionError occur?
#
# This will occur during the logical process when the numerator or the
# denominator is divided by an 0 and will throw a Zero division error.
#
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?

# Yes we can use a while loop which will trigger when the integer 0 is entered and it will notify the user that he must
# enter a another number without ending the program plus mitigating the chance of an error likely to affect other
# portions of the code.
