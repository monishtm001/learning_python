bids = {}

while True:
    name = input("Enter bidder name: ")
    amount = int(input("Enter bid amount: ₹"))

    bids[name] = amount

    more = input("Are there more bidders? (yes/no): ").lower()
    if more == "no":
        break

# Find highest bidder
highest_bid = 0
winner = ""

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder

print(f"\nThe highest bidder is {winner} with a bid of ₹{highest_bid}")
