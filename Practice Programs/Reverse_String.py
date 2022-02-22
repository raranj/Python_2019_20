def isconsonant(l):
    if l != "a" and l != "e" and l != "i" and l != "o" and l != "u":
        return True
    else:
        return False
    
def revstr(string):
    endstr = ""
    nvowels=0
    for l in string:
        if isconsonant(l):
            endstr = l + endstr
        else:
            nvowels = nvowels + 1
            

    return endstr

string = input("Enter a string: ")
mystring = revstr(string)
print(mystring)
