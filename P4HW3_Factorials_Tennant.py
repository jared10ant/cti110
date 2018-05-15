#CTI-110
#Jared Tennant
#Factorials
#3/25/18

print('Enter a non-negative integer to calculate its factorial')
number = int(input('Enter your number: '))
factorial = 1
for count in range(1, number + 1):
     factorial = factorial * count
print('The factorial of', number, 'is', factorial)

