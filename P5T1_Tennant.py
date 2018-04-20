#CTI-110
#Jared Tennant
#Kilometer Converter
#04/19/18

def main():
     print('This program will convert kilometers into miles')
     show_miles()

def show_miles():
     kilo = int(input('Enter the kilometers you wish to convert: '))
     results = kilo * 0.62137
     print('Here are your kilometers converted into miles:', results)

main()
