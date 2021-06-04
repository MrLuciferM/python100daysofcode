import random

logo = """
    ________                                __  .__                                 ___.                 
   /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   _____________
  /   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __  /
  \    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
   \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
          \/            \/     \/     \/             \/     \/       \/            \/    \/     \/       
"""

print(logo)

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.")

difficulty_level = input(
    "Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = random.randint(1, 100)

if difficulty_level == 'easy':
    number_of_attempts = 10
elif difficulty_level == 'hard':
    number_of_attempts = 5

guessed_number = 0

while number_of_attempts > 0 and guessed_number != number:
    print(
        f"You have {number_of_attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))

    if guessed_number > number:
        print("Too high.\nGuess again.")
    elif guessed_number < number:
        print("Too low.\nGuess again.")
    else:
        print(f"You Got it! The answer was {number}.")

if guessed_number != number and number_of_attempts == 0:
    print("You've run out of guesses, You lose.")
