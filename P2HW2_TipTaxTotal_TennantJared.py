#CTI-110
#P2HW21 - Tip Tax Total
#Jared Tennant
#02/12/18

cost = int(input("How much did your meal cost? $"))
tip = cost * .18
tax = cost * .07
total = cost + tax
print("Based on the cost, you should leave $", tip, "as a tip.")
print("The total cost of your meal including sales tax is $", total)
