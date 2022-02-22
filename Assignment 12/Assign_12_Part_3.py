#Writing a function that adds up the digits of a number
def digitSum(num):
    dig_sum = 0
    
#If the number is negative, the absolute value of the number will be taken
    num = abs(num)
    
    while num != 0:
        digit = num % 10
        dig_sum = dig_sum + digit
        num = num//10
    return dig_sum

#Using the function and showing that the function works properly
d = digitSum(546)
if d != 15:
    print("This function returned",d, "instead of 15.")
    exit()
else:
    d = digitSum(0)
    if d != 0:
        print("This function returned",d, "instead of 0.")
        exit()
    else:
        d = digitSum(-34)
        if d != 7:
            print("This function returned",d, "instead of 7.")
            exit()
        else:
            print("This function added up the digits accurately.")
    
#Output when I ran the program:
            "This function added up the digits accurately."

