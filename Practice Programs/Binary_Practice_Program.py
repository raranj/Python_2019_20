def ListToStr(binary):

    string = ""
    length = len(binary)
    for i in range(length):
        elem = (length - i - 1)
        if binary[elem] == 1:
            string = string + "1"
        else:
            string = string + "0"
            
    return string
        
def FindBin(num):
    binary = []
    
    if num < 0:
        print("You entered a negative number.")
        exit()
        
    while num != 0:
        rem = num % 2
        num = num // 2
        binary.append(rem)

    return binary

base_10 = int(input("Enter a positive number: "))
ret = FindBin(base_10)

dec = ListToStr(ret)
print("Your number in binary is", dec)

            


        
        
