#!/usr/bin/python3

import new_module
import sys

print("""Welcome to my Classes Python program! Do you want,
        to (C)ontinue game or (Q)uit game? Press "1" or "2""")

answer = input("> ")

class MainProgram ():

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

class Lost_Game():
    def print_function (name):
        print(f"You {name}")

        sys.exit()

class Win_Game():

    def win_function (name):
        print(f"You {name}")

        sys.exit()

class End_Function:
    
    def __init__ (self, first, last):
        self.first = first
        self.last = last

    def details (self):
        print("First :", self.first)
        print("Last  :", self.last)

# create object

struct = End_Function('Jamie', 'Morrissey')
struct.details()
var_2 = Lost_Game.print_function('lost')
var = You_Won.identify('won')
