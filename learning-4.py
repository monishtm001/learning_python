import random
one_zero = random.randint(2,5)
print(one_zero)
rezero = random.random()*9
print(rezero)
ikrep = random.uniform(5,125)
print(ikrep)


friends=["Moniss","Bully","Vade","putta","Bobby"]
choose = random.choice(friends)
print(choose)


# Loops
scores = [78, 85, 92, 88, 76, 95, 89]
for score in scores:
    print(score)
    print(score + 20)

scoresidk_ok = [23,12,5,75,48,16945,25]
max = 0
for high in scoresidk_ok:
    if high>=max:
        max = high
        
print(max)

scoresidk_ok = [23,12,5,75,48,16945,25]
sum = 0
for xy in scoresidk_ok:
   sum = sum+xy
print(sum)
        
zoro = 0
for luffy in range(1, 101):
    zoro = zoro + luffy

print(zoro)


for num in range(1,100):
    if num%3 == 0:
        print("Fizz")
    elif num%5== 0:
        print ("Buzz")
    elif num%3 and num%5 == 0:
        print("Fizz Buzz")
    else :
        print (num)

# Password generator
letters = [
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J",
    "K","L","M","N","O","P","Q","R","S","T",
    "U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", ":", ";", "<", ">", "?", "/"]

print("Welcome to Moniss password Generator")
alpha= int(input("How many letters would u like to include in your password:"))
beta=int(input("How many numbers would u like to include in your password"))
gama=int(input("How many number of symbols would u like to include in your password:"))

pass_list=[]
for nami in range(0,alpha):
    pass_list.append(random.choice(letters))

for nami in range(0,beta):
    pass_list.append(random.choice(numbers))

for nami in range(0,gama):
    pass_list.append(random.choice(symbols))

print(pass_list)
random.shuffle(pass_list)
print(pass_list)

char=""
for robin in pass_list:
    char +=robin

print(char)

