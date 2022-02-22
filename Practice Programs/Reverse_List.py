def revlist(list):
    newlist = []
    for num in list:
        newlist.insert(0,num)
    return newlist

mylist = [1,2,3,4]
ret = revlist(mylist)
print(ret)
