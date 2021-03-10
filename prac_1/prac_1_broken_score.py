"""
CP1404/CP5632 - Practical
Broken program to determine score status
The intention is that the score must be between 0 and 100
inclusive; 90 or more is excellent; 50 or more is a pass;
below 50 is bad.
Be very careful of your boundary conditions... and test!
"""

score = float(input("Enter score: >>>"))
if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

