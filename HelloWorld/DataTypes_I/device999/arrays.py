# Arrays



if __name__ == '__main__':
# Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
# Write a Python program to get the number of occurrences of a specified element in an array. (Done in lists)
    sizeArray = int(input("Input the size of arrays = "))
    my_array = []
    for i in range(sizeArray):
        my_array.append(int(input("Input the "+str(i+1)+" element = ")))
    print("Second element of the array is = "+str(my_array[1]))
# Write a Python program to reverse the order of the items in the array.
    print(my_array)
    my_array.reverse()
    print(my_array)
# Write a Python program to remove a specified item using the index from an array.
    my_array.remove(12)
    print(my_array)
# Write a Python program to insert a new item before the second element in an existing array.
    my_array.insert(1, 12)
    print(my_array)