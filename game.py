#!/usr/bin/python3

import mod_1

class StartProgram:
    def __init__ (self, name):
        self.name = name

    def print_function(self):
        print("Welcome to my Python Program!", self.name)
        print("What do you want to do?", self.name)
        print("1. Press (1) to win.", self.name)
        print("2. Press (2) to die.", self.name)

        answer = input("> ")

        if answer == "1":
           print("You won!")
        elif answer == "2":
           print("You died.")
        else:
            print (f"The name of the string is {answer}".format (answer))

class Death:

    quips = [   # dictionary
            "You died. You kinda suck at this.",
            "Your Mom would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this.",
            "You're worse than your Dad's jokes."
    ]

    print(quips)

class Finished:

    def enter(self):
        print("You won! Good job.")
        return 'finished'


print(mod_1.tangerine)

p = StartProgram('Nikhil')
p.print_function()

d = Death("print")
# execute Death function after
