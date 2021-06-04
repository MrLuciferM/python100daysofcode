import random

print("Welcome to Rock Paper Scissors Game. Let's thow hands!")

choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

compChoice = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

if choice < 0 or choice > 2:
    print("Invalid number dumbass!")
else:
    print(f"You chose: \n{choices[choice]}\n")
    print(f"Computer chose: \n{choices[compChoice]}\n")
    if choice == compChoice:
        print("It's a draw!!")
    elif choice == 0 and compChoice == 1:
        print("You lose!")
    elif choice == 1 and compChoice == 2:
        print("You lose!")
    elif choice == 2 and compChoice == 0:
        print("You lose!")
    else:
        print("You won!")
