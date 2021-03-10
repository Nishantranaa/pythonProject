# Solution 1

print ("Electricity bill estimator of washing per year")
cost = float(input("Enter cost per kWh:  "))
usage = float(input("Enter number of hours per wash: "))
billed_days = int(input("Enter number of days per week you do washing: "))

print(cost)
print(usage)
print(billed_days)
estimated_bill = (usage * cost) * billed_days
print("You consume $", estimated_bill, "of electricity per week")

# Solution 2
# print("Electricity bill estimator per wash using a washing machine")
# TARRIF_11 = 0.244618
# TARRIF_31 = 0.136928
# usage = float(input("Enter number of hours of washing per day: "))
# billed_days = int(input("Enter number of days you wash your cloths: "))
# tarrif = int(input("Enter tariff 11 or 31: "))
#
# if tarrif == 11:
#     estimated_bill = (usage * TARRIF_11) / billed_days
#     print("Every", billed_days, "days you pay $", estimated_bill)
# elif tarrif == 31:
#     estimated_bill = (usage * TARRIF_31) / billed_days
#     print("Every", billed_days, "days you pay $", estimated_bill)

