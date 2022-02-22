#Writing a function that reverses the digits of a number
def reverse(num):
    ret = 0
#Checking whether the number is positive or negative, and dealing with it later
    if num < 0:
        sign = -1
        num = abs(num)
    else:
        sign = 1

    while num != 0:
        rem = num % 10
        ret = ret*10 + rem
        num = num//10
    return (ret*sign)

#Using the function and showing that the function works properly
r = reverse(1234)
if r != 4321:
    print("This function doesn't work.")
    exit()
else:
    r = reverse(0)
    if r != 0:
        print("This function doesn't work.")
        exit()
    else:
        r = reverse(-54)
        if r != -45:
            print("This function doesn't work.")
            exit()
        else:
            print("This function works correctly.")



#Output when I ran the program:
            "This function works correctly."

     
        
