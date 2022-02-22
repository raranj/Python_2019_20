import math

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x < 0 and y < 0:
    sign = 1
elif x > 0 and y > 0:
    sign = 1
else:
    sign = -1

x = abs(x)
y = abs(y)
prod = 0
if (x > y):
    for i in range(y):
        prod = prod + x
else:
    for i in range(x):
        prod = prod + y

print("The product is ", prod * sign)
