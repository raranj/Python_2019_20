fruits=['apple','orange','mango','lemon','banana']
x = len(fruits)
print(x)

def listLength(list):
    length = 0

    for x in list:
        length += 1
    return(length)

fruits=['apple','orange','mango','lemon','banana']
print(listLength(fruits))
