pick_num=int(input("Enter a number!"))
if pick_num>0:
    print("num is +ve")
elif pick_num<0:
    print("num id -ve")
else:
    print("num is zero")

pick_num=int(input("Enter a number!"))
if pick_num % 2==0:
    print("entered num is even")
elif pick_num % 2!=0:
    print("entered number is odd ")

my_list=[]
no_of_items=int(input("enter how many numbers u wnat to check"))
for n in range(no_of_items):
    cust_entered_num=int(input("Enter Number:"))
    my_list.append(cust_entered_num)

no=0 
for num in my_list:
    if num>no:
        no=num
print(f"{no} is the greatest number")

# learn .split
my_list = map(str,input("Enter items: ").split())
print(list(my_list))
        
