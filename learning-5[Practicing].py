# Learning through Solving
# Sum of numbers from 1 to input value

find_sum=int(input("Enter until what number you would want to find the sum of number from 1:"))

sum = 0
for num in range (1,find_sum+1):
    sum+=num

print(sum)


# printing multiplication table of the input number

multiply_num=int(input("enter which multiplication table would u like to see?"))

for num in range(1,11):
    print(f"{multiply_num}*{num}={multiply_num*num}")

#
multiply_num=int(input("enter which multiplication table would u like to see?"))

for num in range(1,11):
    print(f"{multiply_num}*{num}={multiply_num*num}")




multiply_num=int(input("enter which multiplication table would u like to see?"))

for num in range(1,11):
    print(f"{multiply_num}*{num}={multiply_num*num}")




multiply_num=int(input("enter which multiplication table would u like to see?"))

for num in range(1,11):
    print(f"{multiply_num}*{num}={multiply_num*num}")


import random

letters = [
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J",
    "K","L","M","N","O","P","Q","R","S","T",
    "U","V","W","X","Y","Z"
]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "[", "]"]

print("🔐 Welcome to Password Generator")

num_letters = int(input("How many letters do you want? "))
num_numbers = int(input("How many numbers do you want? "))
num_symbols = int(input("How many symbols do you want? "))

password_list = []

# Add random letters
for _ in range(num_letters):
    password_list.append(random.choice(letters))

# Add random numbers
for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

# Add random symbols
for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

# Shuffle password
random.shuffle(password_list)

# Convert list to string
password = ""
for char in password_list:
    password += char

print("\nYour generated password is:")
print(password)
