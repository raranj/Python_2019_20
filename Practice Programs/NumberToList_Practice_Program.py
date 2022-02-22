def NumtoList(num):
    list = []

    if num == 0:
        list.insert(0,0)
        
    while num != 0:
        dig = num % 10
        list.insert(0, dig)
        num = num // 10

    return list

num = int(input("Enter a positive integer: "))

if num < 0:
    print("You entered a negative number.")
    exit()

ret = NumtoList(num)
print(ret)

