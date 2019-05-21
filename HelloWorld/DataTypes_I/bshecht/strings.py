#1. Write a Python program to find smallest and largest word in a given string
def get_smallest_string(s):
    a = s.split()
    smallest = a[0]

    for element in a:
        if len(smallest) > len(element):
            smallest = element    
    return smallest

def get_largest_string(s):
    a = s.split()
    largest = a[0]
    for element in a:
        if len(largest) < len(element):
            largest = element    
    return largest 


def str_smallest_largest_word(one_string):
    print("smallest string: ", get_smallest_string(one_string))
    print("largest string: ", get_largest_string(one_string)) 


#2. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.

#3. Write a Python program to move all spaces to the front of a given string in single traversal.

#4. Write a Python program to remove duplicate characters of a given string.

#5. Write a Python program to capitalize first and last letters of each word of a given string.

#6. Write a Python program to find the first repeated word in a given string.

#7. Write a Python program to find the first non-repeating character in given string.

#8. Write a Python program to count repeated characters in a string.

# this is a main procedere for defined exersice
def main():
    print("Strings")
    str_smallest_largest_word("Hello, it's a function who can find smallest and largest word in an given string.")


if __name__=="__main__":
    main()

