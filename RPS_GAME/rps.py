import random
import time
import tkinter as tk
from enum import Enum
import pygame
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Initialize pygame
pygame.init()

# Load sound files (adjust file paths as needed)
win_sound = pygame.mixer.Sound(
    "C:/Users/yohan/Desktop/Code/Python/RPS_GAME/win_sound.wav"
)
lose_sound = pygame.mixer.Sound(
    "C:/Users/yohan/Desktop/Code/Python/RPS_GAME/lose_sound.wav"
)
tie_sound = pygame.mixer.Sound(
    "C:/Users/yohan/Desktop/Code/Python/RPS_GAME/tie_sound.wav"
)
start_sound = pygame.mixer.Sound(
    "C:/Users/yohan/Desktop/Code/Python/RPS_GAME/begin_sound.wav"
)

# Set volume for all sound effects
win_sound.set_volume(1.0)
lose_sound.set_volume(1.0)
tie_sound.set_volume(1.0)
start_sound.set_volume(1.0)

# Create a dictionary to map choices to their names
choice_names = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def toggle_rules():
    if result_label.cget("text") == "":
        show_rules()
        rules_button.config(text="Hide Rules", relief=tk.SUNKEN)
    else:
        result_label.config(text="")
        rules_button.config(text="Show Rules", relief=tk.RAISED)


def show_rules():
    rules = "Game Rules:\n1. Rock beats Scissors.\n2. Paper beats Rock.\n3. Scissors beat Paper.\nYou and Python will make your choices. Let's see who wins."
    result_label.config(
        text=rules,
        font=("Helvetica", 12),
        bg="lightblue",
        padx=10,
        pady=10,
        relief=tk.RIDGE,
    )


def play_rps():
    player_choice = player_choice_var.get()
    # Adjust the computer's choice to favor the player (e.g., make it choose randomly from 1 or 2)
    computer_choice = random.choice([1, 3])

    result_label.config(
        text=f"You chose {choice_names[player_choice]}\nPython chose {choice_names[computer_choice]}",
        font=("Helvetica", 12),
        bg="lightblue",
        padx=10,
        pady=10,
    )

    if player_choice == computer_choice:
        result_label.config(
            text=result_label.cget("text") + "\nIt's a Tie!", bg="orange"
        )
        tie_sound.play()

    elif (
        (player_choice == 1 and computer_choice == 3)
        or (player_choice == 2 and computer_choice == 1)
        or (player_choice == 3 and computer_choice == 2)
    ):
        result_label.config(
            text=result_label.cget("text") + "\nYou Win!", bg="lightgreen"
        )
        win_sound.play()
    else:
        result_label.config(
            text=result_label.cget("text") + "\nPython Wins!", bg="lightcoral"
        )
        lose_sound.play()


# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game by Yohan Shyam Sundar")

# Set the window size
root.geometry("400x400")

# Create a label to display the result
result_label = tk.Label(
    root, text="", font=("Helvetica", 16), padx=10, pady=10, relief=tk.RIDGE
)
result_label.pack(pady=20)

# Create a label for instructions
instruction_label = tk.Label(root, text="Choose Rock or Paper:", font=("Helvetica", 14))
instruction_label.pack()

# Create a variable to hold the player's choice
player_choice_var = tk.IntVar()

# Create radio buttons for choices
for choice in choice_names:
    choice_radio = tk.Radiobutton(
        root,
        text=choice_names[choice],
        variable=player_choice_var,
        value=choice,
        font=("Helvetica", 12),
    )
    choice_radio.pack()

# Create a button to play
play_button = tk.Button(
    root,
    text="Play",
    command=play_rps,
    font=("Helvetica", 14),
    relief=tk.RAISED,
    bg="lightgreen",
)
play_button.pack(pady=10)

# Create a button to show or hide rules
rules_button = tk.Button(
    root,
    text="Show Rules",
    command=toggle_rules,
    font=("Helvetica", 14),
    relief=tk.RAISED,
    bg="lightblue",
)
rules_button.pack()

# Run the Tkinter main loop
root.mainloop()


# import random
# import time
# import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# from enum import Enum
# import pygame

# # Initialize pygame
# pygame.init()

# # Load sound files (adjust file paths as needed)
# win_sound = pygame.mixer.Sound("C:/Users/yohan/Desktop/Code/Python/RPS_GAME/win_sound.wav")
# lose_sound = pygame.mixer.Sound("C:/Users/yohan/Desktop/Code/Python/RPS_GAME/lose_sound.wav")
# tie_sound = pygame.mixer.Sound("C:/Users/yohan/Desktop/Code/Python/RPS_GAME/tie_sound.wav")
# start_sound = pygame.mixer.Sound("C:/Users/yohan/Desktop/Code/Python/RPS_GAME/begin_sound.wav")

# # Set volume for all sound effects
# win_sound.set_volume(1.0)
# lose_sound.set_volume(1.0)
# tie_sound.set_volume(1.0)
# start_sound.set_volume(1.0)

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSORS = 3

# show_rules = lambda: print("Game Rules:\n1. Rock beats Scissors.\n2. Paper beats Rock.\n3. Scissors beat Paper.\nYou and Python will make your choices. Let's see who wins!\n")

# print("Welcome to Rock, Paper, Scissors!\n")
# print("1 for Rock, 2 for Paper, or 3 for Scissors\n")

# play_again = "y"  # Initialize play_again variable


# # Ask the user whether they want to read the rules
# read_rules = input("Do you want to read the rules? (y/n): ").strip().lower()

# while play_again == "y":
#     try:
#         if read_rules == "y":
#             start_sound.play()
#             show_rules()

#         playerchoice = int(input("Enter your choice: "))

#         if playerchoice < 1 or playerchoice > 3:
#             print("Invalid choice. You must enter 1, 2, or 3.")
#         else:
#             computerchoice = random.randint(1, 3)

#             print("\nYou chose", str(RPS(playerchoice)).replace("RPS.", "").lower().title())
#             print("Python chose", str(RPS(computerchoice)).replace("RPS.", "").lower().title())

#             if playerchoice == computerchoice:
#                 print("Tie Game!😲")
#                 tie_sound.play()
#                 time.sleep(2.5)
#             elif (playerchoice == 1 and computerchoice == 3) or (playerchoice == 2 and computerchoice == 1) or (playerchoice == 3 and computerchoice == 2):
#                 print("You win!🍾🥳🎇🎈🎆")
#                 win_sound.play()
#                 time.sleep(2.5)
#             else:
#                 print("Python Wins!🐍")
#                 lose_sound.play()
#                 time.sleep(2.5)

#         play_again = input("Play again? (y/n): ").strip().lower()

#         if play_again == "y":
#             read_rules = "n"  # Reset the read_rules variable
#             start_sound.set_volume(0)
#             print("1 for Rock, 2 for Paper, or 3 for Scissors\n")

#     except ValueError:
#         print("Invalid input. Please enter a number.")
#         for i in range(5, 0, -1):
#             print(i, "...")
#             time.sleep(0.5)
#         quit()
#     except:
#         print("An error occurred.")
#         quit()
