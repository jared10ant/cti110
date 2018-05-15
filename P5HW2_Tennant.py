#CTI-110
#Jared Tennant
#Guessing Game
#4/22/18

import random 

def main():
     print("Lets play a game")
     print("I'll make up a number (1-100) and you take 3 chances to guess it correctly")
     print("Let's begin\n********************")
     game() #call the game function in order to play
     retry() #call the retry function to ask user to play again

def retry():
     again = input("Would you like to play again? Type 'y' for yes, 'n' for no: ")
     if again == "y":
          game() #calls the game function to play again if the user desires
          retry() #call retry function to ask user to play again
     else:
          print("Thanks for playing\n********************") #end of game
     
def game():
     secret_num = random.randint(1,100) #sets up variable with random integer between 1 and 100
     max_guess = 0   #sets accumulator variable to zero
     while max_guess < 3:  #control structure for the amount of guesses
          guess = int(input("What is your guess? "))
          max_guess = max_guess + 1  #adds a turn to the accumulator
          if guess != secret_num:    #decision structure for the guess being wrong
               if guess > secret_num:
                    print("Too high")
               else:
                    print("Too low")
          else:
               print("Perfect guess! Good job!") #result if the guess is correct
          if max_guess == 3:  #decision for when user has reached max guesses
               print("AHAHAHAAHAHAH WHAT A DUMBASS!!!!!")

main() #call the main function
 
