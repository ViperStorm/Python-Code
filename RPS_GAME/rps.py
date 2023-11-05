import random
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from enum import Enum
import pygame

# Initialize pygame
pygame.init()

# Load sound files (adjust file paths as needed)
win_sound = pygame.mixer.Sound("C:/Users/yohan/Desktop/Code/Python/RPS_GAME/win_sound.wav")
lose_sound = pygame.mixer.Sound("C:/Users/yohan/Desktop/Code/Python/RPS_GAME/lose_sound.wav")
tie_sound = pygame.mixer.Sound("C:/Users/yohan/Desktop/Code/Python/RPS_GAME/tie_sound.wav")
start_sound = pygame.mixer.Sound("C:/Users/yohan/Desktop/Code/Python/RPS_GAME/begin_sound.wav")

# Set volume for all sound effects
win_sound.set_volume(1.0)
lose_sound.set_volume(1.0)
tie_sound.set_volume(1.0)
start_sound.set_volume(1.0)

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

show_rules = lambda: print("Game Rules:\n1. Rock beats Scissors.\n2. Paper beats Rock.\n3. Scissors beat Paper.\nYou and Python will make your choices. Let's see who wins!\n")

print("Welcome to Rock, Paper, Scissors!\n")
print("1 for Rock, 2 for Paper, or 3 for Scissors\n")

play_again = "y"  # Initialize play_again variable



# Ask the user whether they want to read the rules
read_rules = input("Do you want to read the rules? (y/n): ").strip().lower()

while play_again == "y":
    try:
        if read_rules == "y":
            start_sound.play()
            show_rules()

        playerchoice = int(input("Enter your choice: "))

        if playerchoice < 1 or playerchoice > 3:
            print("Invalid choice. You must enter 1, 2, or 3.")
        else:
            computerchoice = random.randint(1, 3)

            print("\nYou chose", str(RPS(playerchoice)).replace("RPS.", "").lower().title())
            print("Python chose", str(RPS(computerchoice)).replace("RPS.", "").lower().title())

            if playerchoice == computerchoice:
                print("Tie Game!😲")
                tie_sound.play()
                time.sleep(2.5)
            elif (playerchoice == 1 and computerchoice == 3) or (playerchoice == 2 and computerchoice == 1) or (playerchoice == 3 and computerchoice == 2):
                print("You win!🍾🥳🎇🎈🎆")
                win_sound.play()
                time.sleep(2.5)
            else:
                print("Python Wins!🐍")
                lose_sound.play()
                time.sleep(2.5)

        play_again = input("Play again? (y/n): ").strip().lower()

        if play_again == "y":
            read_rules = "n"  # Reset the read_rules variable
            start_sound.set_volume(0)
            print("1 for Rock, 2 for Paper, or 3 for Scissors\n")

    except ValueError:
        print("Invalid input. Please enter a number.")
        for i in range(5, 0, -1):
            print(i, "...")
            time.sleep(0.5)
        quit()
    except:
        print("An error occurred.")
        quit()
