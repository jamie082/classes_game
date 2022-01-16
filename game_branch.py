#!/usr/bin/python3

import new_module
import sys

print("""Welcome to my Classes Python program! Do you want.
      to go through Door #1 or Door #2?""")

answer = input("> ")

class MainProgram ():

        if answer == "1":
            print("What do you want to do?")
            print("1. To you want to Won Game press (1)")
            print("2. Do you want to Lost Game, press (2)")

            answer_2 = input("> ")

            if answer_2 == "1":
                print("You pressed (1)") # You Lost, go to function

            elif answer_2 == "2":
              print("you pressed 2") # Won Game

            else:
                 print(f"Wrong selection, {answer_2}")
                 print("Error!")

            the_count = [5, 4, 3, 2, 1]

            for i in the_count:
                print(f"And you lose in...: {i}")

        elif answer == "2":
            print ("you pressed (2)")
            print ("You lose")
            print ("Enter function")

        else:
            print(f"Wrong selection, {answer}")
            print("Error!")

class Lost_Game(): # Lost class

    def print_function (name):
        print(f"You {name}")

        sys.exit()

class You_Won(): # Win class

    def identify (name):
        print(f"You {name}")

        sys.exit()

var_2 = Lost_Game.print_function('lost')
var = You_Won.identify('won')
