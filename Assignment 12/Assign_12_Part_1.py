#Writing a function to determine if a word is a palindrome
def palindrome(word):
    length = len(word)

    for i in range(length):
        if word[i] != word[length-i-1]:
            return False
        if length-i-1 <= i:
            return True
#If an empty string is given, return True
    return True

#Using the function and showing that the function works correctly
w = palindrome("racecar")
if w != True:
    print("The function returned 'False' for",w, "which isn't correct.")
    exit()
else:
    w = palindrome("abba")
    if w != True:
        print("The function returned 'False' for",w, "which isn't correct.")
        exit()
    else:
        w = palindrome("hello")
        if w != False:
            print("The function returned 'True' for",w, "which isn't correct.")
            exit()
        else:
            w = palindrome("hi")
            if w != False:
                print("The function returned 'True' for",w, "which isn't correct.")
                exit()
            else:
                w = palindrome("")
                if w != True:
                    print("good morning")
                    print("The function returned 'False' for",w, "which isn't correct.")
                    exit()
                else:
                    print("This function works properly.")


#Output when I ran the program:
                    "This function works properly."
                    
                
