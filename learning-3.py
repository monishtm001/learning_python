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
    if age>=18:
        print("your bill will be $20")
    elif age<=12:
        print("Your bill will be $5")
    else:
        print("your bill will be $7")
else:
    print("Your not eligible for a ride")

# Creating PIZZA delivery final bill

print("Welcome to Moniss Pizza Delivery")
size = str(input("Enter which size pizza u want? S/M/L:"))
pproni = input("Do u want pproni in your pizza? Y for Yes and N for No")
xtra_cheese = input("Do u want extra cheese in your pizza? Y / N")
bill = 0
if size == "S":
    bill=5
elif size == "M":
    bill = 10
elif size == "L":
    bill = 20
if pproni == "Y":
    bill=bill+5
if xtra_cheese == "Y":
    bill=bill+7
    print("Your Bill is:" + str(bill))
else:
    print("Print Valid Value")
