
from os import system

clear = lambda: system('cls')
clear()


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def find_highest_bidder(all_bids):
    max = 0
    for bidder in all_bids:
        if max < all_bids[bidder]:
            max = all_bids[bidder]
            winner = bidder
    return winner,max

print("\nWelcome to the secret auction program.")

more_bidders = True

all_bids = {}

while more_bidders:
    bidder = input("What is your name?: ")
    bid = input("What is your bid?: ")

    bid = bid.lstrip("$")
    all_bids[bidder] = int(bid)

    choice = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    if choice != 'yes':
        more_bidders = False
    
    clear()

winner,winning_bid = find_highest_bidder(all_bids)

print(f"The winner is {winner} with bid of ${winning_bid}.")