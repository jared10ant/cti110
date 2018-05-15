#CTI-110
#Jared Tennant
#Running Total
#3/25/18

print('Enter your numbers at the prompt. Enter a negative number to exit.')
total = 0
number = int(input('Enter a number: '))
while number >= 0:
     total += number
     number = int(input('Enter a number: '))
print('Total: ', total)
