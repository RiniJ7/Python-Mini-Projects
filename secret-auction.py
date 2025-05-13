bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? :")
    price = int(input("What is your bid? : $"))
    bids[name] = price
    should_continue = input("Are there any bidders? Type 'yes' for more or 'no'. \n").lower()
    if should_continue == 'no':
        continue_bidding = False  # End the bidding loop

def find_highest_bidder(bidding_dictionary):  # Added missing colon
    highest_bid = 0
    winner = ""  # Initialize winner variable
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")  # Updated to print winner, not bidder

# Call the function after bidding is complete
find_highest_bidder(bids)