#CTI-110
#Software Sales
#Jared Tennant
#02/23/18

def main():
     print("You can receive a discount based on the amount of units you purchase today")
     units = int(input("How many units do you plan on purchasing? "))
     if units >= 10 and units <= 19:
          print("You will receive a 10% discount on your purchase")
          discount1 = .10 #Sets the discount to a variable for future use
          savings1 = units * discount1 #Gets the savings by multiplying units by the discount %
          total1 = units * 99 - savings1 #Total multiplies the units by the retail price and subtracts the discount
          print("The total for your purchase is $", total1)
     elif units >= 20 and units <= 49:
          print("You will receive a 20% discount on your purchase")
          discount2 = .20
          savings2 = units * discount2
          total2 = units * 99 - savings2
          print("The total for your purchase is $", total2)
     elif units >= 50 and units <= 99:
          print("You will receive a 30% discount on your purchase")
          discount3 = .30
          savings3 = units * discount3
          total3 = units * 99 - savings3
          print("The total for your purchase is $", total3)
     elif units >= 100:
          print("You will receive a 40% discount on your purchase")
          discount4 = .40
          savings4 = units * discount4
          total4 = units * 99 - savings4
          print("The total for your purchase is $", total4)
     else:
          print("Unfortunately, that is not enough units to earn a discount")
          total5 = units * 99
          print("The total for your purchase is $", total5)

main()
