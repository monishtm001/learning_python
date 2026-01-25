# Password Generator
import random
# letters = [
#     "a","b","c","d","e","f","g","h","i","j",
#     "k","l","m","n","o","p","q","r","s","t",
#     "u","v","w","x","y","z"
# ]
# numbers = ["0","1","2","3","4","5","6","7","8","9"]
# symbols = [
#     "!", "@", "#", "$", "%", "^", "&", "*",
#     "(", ")", "_", "+", "-", "=", "{", "}",
#     "[", "]", ":", ";", "<", ">", "?", "/"
# ]

# num_numbers=int(input("Enter number of numbers u want to include in your password:"))
# num_letters=int(input("Enter number of letters u want to include in your password:"))
# num_symbols=int(input("Enter number of symbols u want to include in your password:"))

# pass_in_list=[]

# for i in range(num_letters):
#     pass_in_list.append(random.choice(letters))

# for n  in range(num_numbers):
#     pass_in_list.append(random.choice(numbers))

# for s  in range(num_symbols):
#     pass_in_list.append(random.choice(symbols))

# random.shuffle(pass_in_list)

# char=""
# for word in pass_in_list:
#     char+=word
# print(char)

## Hang Man Game

words = [
    "python", "coding", "developer", "programming", "computer",
    "keyboard", "internet", "software", "hardware", "network",
    "hangman", "password", "security", "encryption", "hacker",
    "treasure", "island", "pirate", "adventure", "mystery",
    "machine", "learning", "artificial", "intelligence", "robot",
    "science", "engineer", "technology", "future", "innovation",
    "school", "college", "student", "teacher", "education",
    "football", "cricket", "basketball", "tennis", "chess",
    "music", "guitar", "piano", "drums", "concert",
    "mountain", "river", "forest", "desert", "ocean",
    "travel", "journey", "explore", "discovery", "freedom",
    "friendship", "family", "happiness", "success", "dream",
    "camera", "mobile", "laptop", "tablet", "device",
    "history", "culture", "language", "literature", "art"
]

ran_word=random.choice(words)
len_word=len(ran_word)
print(f"Your pick of the day word has {ran_word} letters")
Display_let_in_list=["_"]*len_word
str_of_list=" ".join(Display_let_in_list)
print(str_of_list)
LIFES=6


while "_" in Display_let_in_list:
    ask_let=input("Enter a Random Letter").lower()
    for i in range(len_word):
        if ran_word[i]==ask_let:
            Display_let_in_list[i]=ask_let
            str_of_list=" ".join(Display_let_in_list)
            print(str_of_list)
        else:
            print(str_of_list)


            







        