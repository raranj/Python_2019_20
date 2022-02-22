def unique_list(list):
    newlist = []
    for x in list:
        if x not in newlist:
            newlist.append(x)
        print('x:', x)
        print('newlist:', newlist)

    return(newlist)


list = [4,5,3,8,6,7,7,7]
print(unique_list(list))
