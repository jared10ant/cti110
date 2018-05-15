#CTI-110
#Jared Tennant
#3/24/18
#Bug Collector

total = 0
print("Enter the number of bugs you collect each day, for 7 days")
for day in range (1, 8):
     number = int(input("How many bugs were collected today?"))
     total = total + number
print("The total number of all bugs collected this week is", total)
