#CTI-110
#Jared Tennant
#Feet to Inches
#4/19/18

inch_per_foot = 12

def main():
     print('This program converts feet to inches')
     feet_to_inches()

def feet_to_inches():
     feet = int(input('Enter the number of feet: '))
     results = feet * inch_per_foot
     print('There are', results, 'inches in', feet, 'feet.')

main()
     
