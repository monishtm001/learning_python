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