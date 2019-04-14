# Lists



if __name__ == '__main__':
    my_list = [1, 7, 21, 6, 7, 8, 21, 15]
    other_list = [ 1, 7, 21]
# Write a Python program to sum all the items in a list
# Write a Python program to get the largest number from a list.
# Write a Python program to get the smallest number from a list.
# Write a Python program to find all the values in a list are greater than a specified number.
    sum = 0
    smallest = 100000000000000000
    largest = 0
    specifiedNumber = 21
    for val in my_list:
        sum = sum +val
        if val > largest:
            largest = val
        if val < smallest:
            smallest = val
        if val == specifiedNumber:
            print(str(val)+" equals to the given number")
    print("Largest number = "+str(largest))
    print("Smallest number  = "+str(smallest))
    print("Sum is = "+str(sum))
# Write a Python program to remove duplicates from a list.
# Write a Python program to get the difference between the two lists.
    print("Before sorting")
    print(my_list)
    my_list = list(dict.fromkeys(my_list))
    print("After sorting")
    print(my_list)
    print(list(set(my_list) - set(other_list)))
