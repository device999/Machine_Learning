import array as arr 

# 1. Write a Python program to find smallest and largest word in a given string
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

# 2. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
def count_U_L_Sch_Num_Values(s):
    a = s.split()
    count_Uppercase = 0
    count_Lowercase = 0
    count_s_char = 0
    count_numerics = 0
    count_special_char = 0

    for element in a:
        if element.isupper():
            count_Uppercase = count_Uppercase + 1
        if element.islower():
            count_Lowercase = count_Lowercase + 1
        if element.isdigit():
            count_numerics = count_numerics + 1
        else:
            count_special_char = count_special_char + 1

    print("Uppercase: ", count_Uppercase)
    print("Lowercase: ", count_Lowercase)
    print("Chars", count_s_char)
    print("Numerics",count_numerics)
    print("Fehler in Special char: ", count_special_char)

# 3 Write a Python program to move all spaces to the front of a given string in single traversal.
def move_all_spaces_to_the_front(s):
    #return(s.strip())
    #b = ('20%' if ord(char) == ord(token) else char for char in s)
    b = s.replace(" ","")
    return b

# 4 Write a Python program to remove duplicate characters of a given string.
def remove_duplicate_chars(s):
    b = "".join(set(s)) 
    return b

#5 Write a Python program to capitalize first and last letters of each word of a given string.
def capitalize(s):
#    b = s.capitalize()
    a = s.split()
    b = ""
    for element in a:
        b = b + element.capitalize() + " "
        # ToDo last letter         
    return b

# 6 Write a Python program to find the first repeated word in a given string.
def find_repeated_word(s):
    b = ""
    return b


# this is a main procedere for defined exersice  
def main():
    # Strings 
    s = "Write a Python program to find smallest and largest word in a given string"
    print("smallest word: ", get_smallest_string(s))
    print("largest word: ", get_largest_string(s))
    count_U_L_Sch_Num_Values("Unbekannte finden nichtS Numerisches : 123I")  
    print(move_all_spaces_to_the_front(s))
    print(remove_duplicate_chars(s))
    print(capitalize(s))








if __name__=="__main__":
    main()