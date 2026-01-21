# def full_name():
#     """Hello There, this function returns full name using input of first andf last name."""
#     f_name=input("Enter your First Name:").title()
#     l_name=input("Enter Your Last name:").title()
#     return f"your full name is {f_name} {l_name}"
# print(full_name())


## Creating a calculator


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

operations={}

operations["+"]=add
operations["-"]=subtract
operations["*"]=multiply
operations["/"]=divide
always=True
num_a=float(input("Enter First Num:"))
while always==True:

    for keyss in operations:
        print(keyss)
    opss=input("Pick any operation:")
    num_b=float(input("Enter second Num:"))
    answer=operations[opss](a=num_a,b=num_b)
    print(f"{num_a} {opss} {num_b} = {answer}")        

    choice=print(input("Enter Y to continue with the op else type N to continue with new calculation:"))

    if choice=="Y":
        num_a=answer
    else:
        always=False

        
        
        