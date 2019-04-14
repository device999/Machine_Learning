# Strings



if __name__ == '__main__':
# Write a Python program to find smallest and largest word in a given string
    text = str(input("Input the string = "))
    words = text.replace("."," ").split()
    smallestWord = ""
    smallestWordLength = 500
    largestWord = ""
    largestWordLength = 0

    for word in words:
        if len(word) > largestWordLength:
            largestWordLength = len(word)
            largestWord = word
        if len(word) < smallestWordLength:
            smallestWordLength = len(word)
            smallestWord = word
    print ("Smallest word = "+smallestWord+" with the length of = "+str(smallestWordLength))
    print ("Largest word = "+largestWord+" with the length of = "+str(largestWordLength))
# Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
    lowerCaseAmount = 0
    upperCaseAmount = 0
    numericalAmount = 0
    specialAmount = 0
    for letter in text.replace(" ",""):
        if letter.isupper():
            upperCaseAmount = upperCaseAmount + 1
        elif letter.islower():
            lowerCaseAmount = lowerCaseAmount + 1
        elif letter.isdigit():
            numericalAmount = numericalAmount + 1
        else:
            specialAmount = specialAmount + 1
    print ("Number of lowercase = "+str(lowerCaseAmount))
    print ("Number of uppercase = "+str(upperCaseAmount))
    print ("Number of numerical = "+str(numericalAmount))
    print ("Number of special = "+str(specialAmount))
# Write a Python program to find the first repeated word in a given string.
# Write a Python program to count repeated characters in a string.
# Write a Python program to find the first non-repeating character in given string.
    firstRepeated = True
    firstNonRepeated= True
    for word in words:
        if text.count(word)>1:
            if firstRepeated:
                print(word+" is the first word, which repeated "+str(text.count(word))+" times")
                firstRepeated = False
            else:
                print(word+" is repeated "+str(text.count(word))+" times")
        else:
            if firstNonRepeated:
                print(word+" is the first non repeated word ")
                firstNonRepeated = False



        
        