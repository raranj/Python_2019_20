def printletters(input_name):
    print("inside the printletters function with input", input_name)
    print("the length is: ", len(input_name))
    for i in range(len(input_name)):
        print(input_name[len(input_name)-i-1])

#printletters(input("Enter a name: "))
name = input("Enter a name: ")
printletters(name)
