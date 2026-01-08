# String manipulation and Micro project

print(type(1.2))
print(type(458))
print(type(True))
print(type("Moniss"))

# When there are more than 1 type of mathematical operation in the code line-
# Rule is - PEMDAS - Parentheses,Exponents, Multiplication Division , Addition Substraction
# calculation takes place from Left to Right

# Tip Calculator
print("Welcome to Tip calculator!")
bill=float(input("what is the total bil amount?"))
tip=int(input("How much tip would you like to give? 10 | 20 | 30%?"))
tip=tip/100
bill=bill*tip+bill
print("Your total bill is ="+str(bill))
number_of_people= int(input("How many people are youn going to split the bill with?"))
Contro = round(bill/number_of_people,2)
print("Each person has to pay:$"+str(Contro))