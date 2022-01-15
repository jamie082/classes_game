#!/usr/bin/python3

import new_module

print("Welcome to my Classes Python program!")
print("What do you want to do?")
print("1. Press (1) to win.")
print("2. Press (2) to die.")

action = input("> ")

if action == "1":
    print("You won")
elif action == "2":
    print("You died.")
elif action == "3":
    print("""You pressed '3"...""")
else:
    print (f"The name of the string is {answer}".format (action))

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

    the_count = [5, 4, 3, 2, 1]

    for i in the_count:
        print(f"And you die in...: {i}")

    quips = [
            "You died. You kinda suck at this.",
            "Your Mom would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this.",
            "You're worse than your Dad's jokes."
    ]

s = new_module.Death("new")
c = s.f1("Jamie", "Morrissey")
print(c) 
