# learning if else and operators

check_OE = int(input("Enter a valid number to check odd or even:"))
print(check_OE)

if check_OE%2==0:
    print("Entered number is EVEN number.")
else:
    print("Entered number is ODD number.")
    
# Creating the Total bill of a roller coaster ride as the prices of tickets depend on age.

print("Welcome to Lyffy's roller coaster ride. Have a wonderful experience")
height=int(input("please enter your height in cm:"))
if height>=120:
    print("you are eligible for a ride.")
    age=int(input("enter your age:"))
    elif age>=18:
        print("your bill will be $20")
    elif age<=12:
        print("Your bill will be $5")
    else:
        print("your bill will be $7")
else:
    print("Your not eligible for a ride")