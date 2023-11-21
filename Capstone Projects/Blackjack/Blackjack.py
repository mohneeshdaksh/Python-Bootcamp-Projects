# BlackJack
import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack_check(your_sum, computer_sum):
    if your_sum == 21:
        return "Win"
    elif computer_sum == 21:
        return "Lose"
    else:
        return "Resume"



def result(player_total, dealer_total):
    if player_total < 22 and dealer_total < 22:
            if player_total > dealer_total:
                print("You win 😃")
            elif player_total == dealer_total:
                print("Draw 🙃")
            else:
                print("You lose 😤")
        elif player_total > 21:
            print("You went over. You lose 😤")
        elif dealer_total > 21:
            print("Opponent went over. You win 😁")


def ace_check(player_set, player_sum, dealer_set, dealer_sum):
    if player_sum > 21 and 11 in player_set:
        for value in player_set:
            if player_sum > 21 and player_set[value] == 11:
                player_set[value] = 1
    
    if dealer_sum > 21 and 11 in dealer_set:
        for num in dealer_set:
            if dealer_sum > 21 and dealer_set[num] == 11:
                dealer_set[num] = 1





def blackjack():
    os.system('clear')
    print(logo)
    your_cards = []
    computer_cards = []
    for card in range(0,2):
        your_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    
    your_cards_sum = 0
    for number in your_cards:
        your_cards_sum += number
    
    
    computer_cards_sum = 0
    for num in computer_cards:
        computer_cards_sum += num
    
    print(f"    Your cards: {your_cards}, current score: {your_cards_sum}")
    print(f"    Computer's first card: {computer_cards[0]}")

    # Checking if it is a blackjack or not!
    check = blackjack_check(your_sum=your_cards_sum, computer_sum=computer_cards_sum)

    if check == "Win":
        print("You win 😃")
    elif check == "Lose":
        print("You lose 😤")
    elif check == "Resume":
        pick_next_card = True
        while pick_next_card:
            another_card = input("Type 'y' to get another card or type 'n' to pass: ")
            if another_card == 'y':
                your_next_card = random.choice(cards)
                your_cards.append(your_next_card)
                your_cards_sum += your_next_card
                print(f"    Your cards: {your_cards}, current score: {your_cards_sum}")
                print(f"    Computer's first card: {computer_cards[0]}")
                if your_cards_sum > 21:
                    pick_next_card = False
            else:
                pick_next_card = False

        pick_more = True
        while pick_more:
            if computer_cards_sum < 16:
                computer_next_card = random.choice(cards)
                computer_cards.append(computer_next_card)
                computer_cards_sum += computer_next_card
            else:
                pick_more = False

        print(f"    Your cards: {your_cards}, final score: {your_cards_sum}")
        print(f"    Computer cards: {computer_cards}, final score: {computer_cards_sum}")
        
        result(player_total=your_cards_sum, dealer_total=computer_cards_sum)
        


# def blackjack_resume():

play_blackjack = True
while play_blackjack:
    os.system('clear')
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "y":
        blackjack()
    else:
        play_blackjack = False
        os.system('clear')
        print("Goodbye!")