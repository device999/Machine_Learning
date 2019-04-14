import operator

if __name__ == '__main__':
# Write a Python script to sort (ascending and descending) a dictionary by value.
# Write a Python script to sort (ascending and descending) a dictionary by key.
# Write a Python program to sort a list alphabetically in a dictionary.
    taskDictionary = {
        "first_name": "Lyndsey",
        "last_name": "Houdhury",
        "email": "lhoudhury0@globo.com",
        "gender": "Female",
        "eye_color": "Red",
        "language": "Italian",
    }
    for i in sorted (taskDictionary) : 
        print ((i, taskDictionary[i]), end =" ")
    print()
    print()
    for i1 in sorted (taskDictionary, reverse=True) : 
        print ((i1, taskDictionary[i1]), end =" ")
    print()
    print()
    print(sorted(taskDictionary.items(), key=operator.itemgetter(0)))
    print()
    print(sorted(taskDictionary.items(), key=operator.itemgetter(0),reverse=True))
# Write a Python script to concatenate following dictionaries to create a new one.
    print("Write a Python script to concatenate following dictionaries to create a new one.")
    dictionary2 = {
        "password":"123435",
        "position":"Developer",
        "profession":"Developer",
        "password":"12343775"
    }
    taskDictionary.update(dictionary2)
    print(taskDictionary)
    print()
# Write a Python program to check multiple keys exists in a dictionary. 
    print("Write a Python program to check multiple keys exists in a dictionary.")
    duplicatedFields = {
        "password":"123123123",
        "password":"444",
    }
    print(duplicatedFields)
    for i in duplicatedFields:
        multiple = False
        for j in duplicatedFields:
            if duplicatedFields[i]!=duplicatedFields[j] and i==j:
                multiple=True
                break
        if multiple:
            print(i)

# Write a Python program to print all unique values in a dictionary.   
    print("Write a Python program to print all unique values in a dictionary.") 
    for i in taskDictionary:
        unique = True
        value = taskDictionary[i]
        for j in taskDictionary:
            if taskDictionary[j]==value and i!=j:
                unique=False
                break
        if unique:
            print(i)