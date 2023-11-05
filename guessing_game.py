import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Initialize attempts and max_attempts
attempts = 0
max_attempts = 5

# Define the lose function
def lose():
    print("\nYou have run out of attempts. The number was", random_number)

while attempts < max_attempts:
    try:
        guess = int(input("Guess the number (between 1 and 10): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    attempts += 1

    if guess < random_number:
        print(f"\nToo low! Try again. You have {max_attempts - attempts} attempts left")
    elif guess > random_number:
        print(f"\nToo high! Try again. You have {max_attempts - attempts} attempts left")
    else:
        print(f"Congratulations! You guessed the number ({random_number}) in {attempts} attempts with {max_attempts - attempts} attempts left!")
        break

if attempts == max_attempts:
    lose()