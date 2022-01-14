#!/usr/bin/python3

import module

class StartProgram():
    def display1(self):
        print("This is superclass")

    def function(self):
        print("Hello")

class CentralCorridor (): # main body
    def swim (self):
        print("""You have selected a very important part of the game""")

    def print_function(self):
        print("Welcome to my Classes Python Program!")
        print("What do you want to do?")
        print("1. Press (1) to win.")
        print("2. Press (2) to die.")

        action = input("> ")

        if action == "1":
            print("You won!")
            return 'finished'
        elif action == "2":
            print ("You died.")
            return 'death'
        elif action == "3":
            print ("You pressed '3'...")
            return 'death'
        else:
            print (f"The name of the string is {answer}".format (answer))

class Finished ():

    def __init__(self, first_name, last_name ="Fish"):
        self.first_name = first_name
        self.last_name = last_name

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards (self):
        print("You won! Good job.")

class Death ():

    elements = []

    the_count = [5, 4, 3, 2, 1]

    for i in elements:
        print(f"And you die in...: {i}")

    def swim(self):
        print(Death.quips[randint(0, len(self.quips) -1)])

    quips = [   # dictionary
            "You died. You kinda suck at this.",
            "Your Mom would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this.",
            "You're worse than your Dad's jokes."
    ]

print(module.tangerine)

g = CentralCorridor()
g.print_function()

