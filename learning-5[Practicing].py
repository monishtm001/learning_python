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
