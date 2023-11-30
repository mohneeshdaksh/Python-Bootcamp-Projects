'''Secret Auction'''
import os
from art import logo

print(logo)
print("Welcome to the Secret Auction Program!")

secret_action_database = {}

def bidder_data(person_name, bid_amount):
    '''Creates a dictionary with person name as key and bid amount as value.'''
    secret_action_database[person_name] = bid_amount

other_bidder = True
while other_bidder:
    person = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidder_data(person_name=person, bid_amount=bid)
    restart = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if restart == "no":
        other_bidder = False
    else:
        os.system('clear')

highest_bid = 0
for key in secret_action_database:
    bid_value = secret_action_database[key]
    if bid_value > highest_bid:
        highest_bid = bid_value
        winner = key

print(f"\nThe winner is {winner} with a bid of ${highest_bid}!")
print(f"\nBidders ('Name', Bid Amount):\n{secret_action_database.items()}\n")
