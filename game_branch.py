#!/usr/bin/python3

import new_module

print("Welcome to my Classes Python program! Do you want", 
    "to go through Door #1 or Door #2?")

answer = input("> ")

if answer == "1":
    print("What do you want to do?")
    print("1. Press (1) to Win.")
    print("2. Press (2) to Die.")

    answer_2 = input("> ")

    if answer_2 == "1":
        print("You pressed (1)")
    elif answer_2 == "2":
        print("You pressed (2)")
    else:
        print(f"Well, doing {answer_2}")
    
    the_count = [5, 4, 3, 2, 1]
    
    for i in the_count:
        print(f"And you die in...: {i}")

elif answer == "2":
    print("you pressed 2")

class Finished ():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards (self):
        print("You won! Good job.")

class Redundent ():
    def print_function(self, output):
        self.output = output
