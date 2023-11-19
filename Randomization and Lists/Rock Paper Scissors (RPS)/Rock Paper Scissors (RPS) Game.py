# Rock Paper Scissors Game!
import random
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
game_images = [rock, paper, scissors]

print("\nWelcome to Rock Paper Scissors Game!")

user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if user_choice > 3 or user_choice < 0:
    print("Invalid Entry.")
else:
    print(game_images[user_choice])

print("Computer Chose:")
computer_choice = random.randint(0,2)
print(game_images[computer_choice])

if (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
    print("You win!!! \n")
elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 2 and user_choice == 1) or (computer_choice == 1 and user_choice == 0):
    print("You lose! \n")
elif user_choice == computer_choice:
    print("It's a draw! \n")
else:
    print("Invalid Entry. You lose!")