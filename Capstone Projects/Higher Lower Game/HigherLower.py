# Higher Lower Game

from random import choice
from GameData import data
from art import logo, vs
import os


def score_count(score):
    if score != 0:
        print(f"You're right! Current score: {score}.")


def comparison(follower_count_1, follower_count_2):
    if follower_count_1 > follower_count_2:
        return "A"
    else:
        return "B"


score = 0
first_choice = choice(data)
winning = True

while winning:
    os.system('clear')
    print(logo)
    score_count(score)

    follower_count_1 = int(first_choice['follower_count'])

    second_choice = choice(data)
    
    while second_choice == first_choice:
        second_choice = choice(data)
    
    follower_count_2 = int(second_choice['follower_count'])

    comparison(follower_count_1, follower_count_2)

    # To test, un-comment the below line.
    # print(first_choice)
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")

    print(vs)

    # To test, un-comment the below line.
    # print(second_choice)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")

    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if player_choice == comparison(follower_count_1, follower_count_2):
        score += 1
        first_choice = second_choice
    else:
        os.system('clear')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        winning = False