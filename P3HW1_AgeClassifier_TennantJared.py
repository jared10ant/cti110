#CTI-110
#Age Classifier
#Jared Tennant
#02/23/18

def main ():
     age = int(input("What is your age?"))
     if age <= 1:
          print("You are an infant")
     elif age > 1 and age < 13:
          print("You are a child")
     elif age >= 13 and age < 20:
          print("You are a teenager")
     else:
          print("You are an adult")
main()
