import random

print("Welcome to my dice game!")

name = input("\nWhat is your name? - ")
play = input("\nDo you want to play? (y/n) - ").lower().strip()

if play != "y":
        print(f"FINE I DIDNT WANT YOU TO PLAY ANYWAYS, {name}")
        quit()

while 1:
    dice_roll = random.randint(1, 6)

    print(f"\nYou rolled a {dice_roll}")

    repeat = input("Do you want to roll the dice again? - (y/n)").lower().strip()

    if repeat != 'y':
        print(f"Thanks for playing {name}.")
        break
    
    