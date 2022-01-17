#!/usr/bin/python3

import sys

# Creat out class
class Game:
    def __init__ (self):
        # Set some class variables
        self.win = 0
        self.lost = 0

        def score (self):
            return f'Games Won: {self.win} / Lost: {self.lost}'

print("""Welcome to my Classes Python program! Do you want,
        to (C)ontinue game or (Q)uit game? Press "1" or "2""")

answer = input("> ")

#class MainProgram ():
def main():
    # Initialize the Game class
    game = Game()

    if answer == "1":
         print("What do you want to do?")
         print("1. Do you want to Win the game, press (1)")
         print("2. Do you want to Lose the game, press (2)")

         answer_2 = input("> ")

         if answer_2 == "1":
             print("You pressed (1)") # You Lost, go to function
             print("You win")

         elif answer_2 == "2":
             print("you pressed 2") # Won Game
             print("You lost")

         else:
             print(f"Wrong selection, {answer_2}")
             print("Error!")

    elif answer == "2":
            print ("you pressed (2)")
            print ("You lose")

    else:
            print(f"Wrong selection, {answer}")
            print("Error!")
main()
