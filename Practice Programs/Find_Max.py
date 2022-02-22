#Assuming the list not empty

def findMax(list):
    max = list[0]
    for num in list:

        if num > max:
            max = num
    return max

mylist = [1,-7,5,2]
mymax = findMax(mylist)
print(mymax)
