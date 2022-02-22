n = int(input("Enter a number: "))

if n <= 0:
    print("Please enter a positive number.")
    exit()
else:

    p = 1
    sum = 0
    for i in range(1, n+1):
        sum = p + sum
        p = p + 2

print("The sum of the first", n, "odd numbers is", sum) 
