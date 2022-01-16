#!/usr/bin/python3

class Death:
    def __init__ (self, name):
        self.name = name

    def __str__(self):
         myString = "Name: {} , ".format(self.name)
         return 'You Died. You kinda suck at this...'
