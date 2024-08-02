from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

enough_bids = False
bids = {}

def find_highest_bidder(bidding_record):
  winner = ''
  highest_bid = 0
  for name in bids:
    if bids[name] > highest_bid:
      highest_bid = bids[name]
      winner = name
  print(f"The winner is {winner} with a bid of ${high_bid}")
      
while not enough_bids:
  name = input("What is your name? ")
  your_bid = int(input("What is your bid? $"))
  bids[name] = your_bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  
  if more_bidders == "no":
    enough_bids = True
    find_highest_bidder(bids) 
  elif more_bidders == "yes":
      clear()

