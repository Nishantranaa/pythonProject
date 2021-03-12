"""
CP1404/CP5632 - Practical
Broken program to determine score status
The intention is that the score must be between 0 and 100
inclusive; 90 or more is excellent; 50 or more is a pass;
below 50 is bad.
Be very careful of your boundary conditions... and test!
"""
from random import seed
from random import randint

def main():
    score = float(input("Enter score: >>>"))
    checking_value(score)
    print("\nA list of random numbers: \n")
    calculating_random_score()


def checking_value(score):
    if score < 0 or score > 100:
        print("Invalid Score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def calculating_random_score():
    # generate random integer values
    # seed random number generator
    seed(1)
    # generate some integers
    for _ in range(100):
        value = randint(0, 100)
        print(value)

main()