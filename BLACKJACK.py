Blackjack="""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗      ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗     ██║██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""
import random
print(Blackjack)
print("WELCOME TO THE GAME")
PLAYER_NAME=input("PEASE PROVIDE YOUR GAME NAME:")
print(f"WELCOME {PLAYER_NAME} LETS START THE GAME")
Shuffle=input("WOULD U LIKE TO SHUFFLE THE CARDS BEFORE STARTING: TYPE YES/NO").lower()

if Shuffle=="yes":
    print(f"""
          
             ┌─────┐   ┌─────┐   ┌─────┐
             │░░░░░│   │░░░░░│   │░░░░░│
             └─────┘   └─────┘   └─────┘
                 ↘     ↓     ↙
             ┌─────┐   ┌─────┐   ┌─────┐
             │░░░░░│   │░░░░░│   │░░░░░│
             └─────┘   └─────┘   └─────┘
              {"Shuffle Complete"}
""")
else:
    print("Lets Continue")

import random

def create_card(rank, suit):
    rank_str = rank.ljust(2) if rank != "10" else rank
    return [
        "┌─────────┐",
        f"│ {rank_str}      │",
        "│         │",
        f"│    {suit}    │",
        "│         │",
        f"│      {rank_str} │",
        "└─────────┘"
    ]

def card_value(rank):
    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11  # Ace default = 11
    else:
        return int(rank)

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♥", "♦", "♣"]

deck = []

for suit in suits:
    for rank in ranks:
        deck.append({
            "rank": rank,
            "suit": suit,
            "value": card_value(rank),
            "ascii": create_card(rank, suit)
        })



Player = random.sample(deck, 2)
sum=0
print("\nPLAYER CARDS:")
for card in Player:
    print()
    for line in card["ascii"]:
        print(line)
    sum+=card["value"]
print(f"player total={sum}")
        


Dealer = random.sample(deck, 2)
total=0
print("\nDEALER CARDS:")
for card in Dealer:
    print()
    for line in card["ascii"]:
        print(line)
    total+=card["value"]
print(f"player total={total}")


choice=input("Choose your Hand : HIT/STAND:").lower()
print(choice)

if choice=="stand":
    if sum>total and sum<21:
        print(f"{PLAYER_NAME} Has Won the Game")
    elif total>sum and total<21:
        print("Dealer has Won the Game")
elif choice=="hit":
    Player.append(random.choice(deck))
    print("\nPLAYER CARDS:")
    sum=0
    for card in Player:
        print()
        for line in card["ascii"]:
            print(line)
        sum+=card["value"]
    print(f"player total={sum}")
    Dealer.append(random.choice(deck))
    print("\nPLAYER CARDS:")
    total=0
    for card in Dealer:
            print()
            for line in card["ascii"]:
                print(line)
            total+=card["value"]
    print(f"player total={total}")











