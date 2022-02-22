import math

num = float(input("Enter a positive integer: "))

while num < 0:
    print("You did not enter a positive number.")
    num = float(input("Enter a positive intetger: "))

#Checking if it's an integer
hi = num//1
dec = num - hi
if dec != 0:
    print("You did not enter an integer.")
    exit()

#Printing the answer
ans = num**(1/2)
print("The square root of this number is", ans)
