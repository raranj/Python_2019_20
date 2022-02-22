def addtonum(num):
    sum = 0
    if num < 0:
        print("You entered a negative number.")
        exit()
    for i in range(1, num +1):
        sum = sum + i
    return sum

num = int(input("Enter a positive integer: "))
ret = addtonum(num)
print(ret)
