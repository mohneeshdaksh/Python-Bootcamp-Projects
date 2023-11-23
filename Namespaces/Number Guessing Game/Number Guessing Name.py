import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")
CHOSEN_NUMBER = random.randint(1,100)

def guess_again(attempts):
    if attempts != 0:
        print("Guess again.")

def game(attempts):
    correct_guess = False
    while not correct_guess:
        if attempts == 0:
            print("You've exhausted all of your attempts, you lose!")
            correct_guess = True
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == CHOSEN_NUMBER:
                print(f"You got it! The answer was {CHOSEN_NUMBER}")
                correct_guess = True
            elif guess < CHOSEN_NUMBER:
                attempts -= 1
                print("Too low!")
                guess_again(attempts)
            else:
                attempts -= 1
                print("Too high!")
                guess_again(attempts)

        

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts_present = 10
    game(attempts=attempts_present)
elif difficulty == "hard":
    attempts_available = 5
    game(attempts=attempts_available)
else:
    print("Invalid entry!")