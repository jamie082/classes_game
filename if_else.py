#!/usr/bin/python3

print("Welcome to my Python 3 game")

answer = input("> ")

if answer == "1":
    print("What do you want to do?")
    print("Press (1) to Win")
    print("Press (2) to Die")
    
    answer_2 = input("> ")

    if answer_2 == "1":
        print("You pressed (1)")
    elif answer_2 == "2":
        print("You pressed (2)")
    else:
        print(f"Well, doing {answer_2}")

