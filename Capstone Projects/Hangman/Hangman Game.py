# This code/game contains topics like Lists (Modification), Randomization, F-String, If-Else Conditions, 
# For Loop which is inside If-Else Condition which is also inside a While Loop, importing and creating modules and many more!
import random
import os
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Creating an empty List called display. For each letter in the chosen_word, adding a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display.append("_")

# Creating a variable called 'lives' to keep track of the number of lives left. 
lives = 6

guessed_letters = ""

# Asking the user to guess a letter and assign their answer to a variable called guess and making it lowercase.
# Using a while loop to let the user guess again until the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('clear')

    # If the user has entered a letter they've already guessed, the below will print the letter and let them know.
    if guess in guessed_letters:
         print(f"You have already guessed '{guess}'! Please guess a new letter.")
    else:
        # Checking if the letter the user guessed (guess) is one of the letters in the chosen_word.
        # Looping through each position in the chosen_word;
        # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        # Example: If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
        if guess not in chosen_word:
                print(f"You guessed '{guess}', that's not in the word. You lose a life!")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print("You lose. Try again!")
        else:
            for position in range(0, word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = guess
        # If guess is not a letter in the chosen_word, then reducing 'lives' by 1. 
        # If lives goes down to 0 then the game should stop and it should print "You lose."

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.

        if "_" not in display:
            end_of_game = True
            print("You win, Congratulations!!!")

        guessed_letters += guess

    # Time to print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(f"{stages[lives]} \nLives left: {lives}\n")