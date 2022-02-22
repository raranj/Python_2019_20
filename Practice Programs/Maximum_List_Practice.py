def findMax(list):
    biggest =list[0]
    
    for num in list:
        if biggest < num:
            biggest = num
    return biggest

list = [23, 478, 43, -65]
list1 = [-7654, -7.654, -1]
adios = findMax(list1)
print("The biggest number in this list is", adios,".") 
