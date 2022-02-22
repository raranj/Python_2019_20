def digsum(num):
    list = []
    if num == 0:
        list.append(0)
    while num != 0:
        rem = num%10
        list.insert(0, rem)
        num = num//10
    return list

mylist = digsum(1234)
print(mylist)
