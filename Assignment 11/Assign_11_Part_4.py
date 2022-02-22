n = int(input("Enter a number: "))

if n < 0:
    print("You can't find the Fibonacci of this number.")
    exit()
elif n == 0:
    fib = 0
elif n == 1:
    fib = 1
else:
    
    p2 = 0
    p1 = 1
    for i in range (2, n+1):
        fib = p1 + p2
        p2 = p1
        p1 = fib

print(fib)
