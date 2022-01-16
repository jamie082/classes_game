#!/usr/bin/python3

import new_module
import sys

print("Welcome to my Classes Python program! Do you want",
            "to go through Door #1 or Door #2?")

answer = input("> ")

class MainProgram ():

    def identify (name):
        print(f"You won,  {name}")

    if answer == "1":
        print("What do you want to do?")
        print("1. Press (1) to Win.")
        print("2. Press (2) to Die.")

        answer_2 = input("> ")

        if answer_2 == "1":
            print("You pressed (1)") # You Win, go to function

        elif answer_2 == "2":
           print("you pressed 2") # You Die

        else:  
            print(f"Wrong selection, {answer_2}")
            print("Error!")

        the_count = [5, 4, 3, 2, 1]

        for i in the_count:
            print(f"And you die in...: {i}")

class End_Game():

    def print_function(self):

        i = 0
        while count < 5:  # output bzzzzd'd 5 times
            print ("BZZZZZZD! EOF!!")
            i += count

class You_Won():

    def win (self):
        var.identify()

var = MainProgram.identify('jamie')
