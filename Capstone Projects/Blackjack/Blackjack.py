'''BlackJack Game'''

import random
import os
from art import logo


def deal_card():
    '''Returns a random card from the deck.'''
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card


def result(player_total, dealer_total):
    '''Print the final game result.'''
    if player_total < 22 and dealer_total < 22:
        if player_total == dealer_total:
            print("Draw 🙃")
        elif player_total == 21:
            print("You win with a blackjack 😃")
        elif dealer_total == 21:
            print("Lose, opponent got blackjack 😱")
        elif player_total > dealer_total:
            print("You win 😃")
        else:
            print("You lose 😤")
    elif player_total > 21:
        print("You went over. You lose 😤")
    elif dealer_total > 21:
        print("Opponent went over. You win 😁")


def blackjack():
    '''Compute the main algorithm of the Blacjack game. No input is required for this function.'''
    os.system('clear')
    print(logo)

    player_cards = []
    computer_cards = []

    # Drawing two random cards from a deck for both
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    go_on = True
    while go_on:
        player_sum = sum(player_cards)
        computer_sum = sum(computer_cards)

        print(f"    Your cards: {player_cards}, current score: {player_sum}")
        print(f"    Computer's first card: {computer_cards[0]}")


        if player_sum == 21:
            go_on = False
        elif computer_sum == 21:
            go_on = False
        elif player_sum == 21 and computer_sum == 21:
            go_on = False
        else:
            if player_sum > 21:
                if 11 in player_cards:
                    player_cards.remove(11)
                    player_cards.append(1)
                    player_sum = sum(player_cards)
                else:
                    go_on = False
            else:
                another_card = input("Type 'y' to get another card or type 'n' to pass: ")
                if another_card == 'y':
                    player_cards.append(deal_card())
                else:
                    go_on = False

    computer_turn = True
    while computer_turn:
        if computer_sum < 17:
            computer_cards.append(deal_card())
            computer_sum = sum(computer_cards)
        elif 11 in computer_cards and computer_sum > 21:
            computer_cards.remove(11)
            computer_cards.append(1)
            computer_sum = sum(computer_cards)
        else:
            computer_turn = False

    print(f"    Your cards: {player_cards}, final score: {player_sum}")
    print(f"    Computer cards: {computer_cards}, final score: {computer_sum}")
    result(player_total=player_sum, dealer_total=computer_sum)


play_blackjack = True
while play_blackjack:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "y":
        blackjack()
    else:
        play_blackjack = False
        os.system('clear')
        print("Goodbye!")
