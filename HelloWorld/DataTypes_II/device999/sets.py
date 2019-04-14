# Write a Python program to create a set.
# Write a Python program to find the length of a set.
# Write a Python program to find maximum and the minimum value in a set.
# Write a Python program to remove an item from a set if it is present in the set.
#  Write a Python program to create a union of sets.


if __name__ == '__main__':
    my_set = set([1,2,3,62])
    print(len(my_set))
    min_val = 25
    max_val = 0
    for i in my_set:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    print(max_val)
    print(min_val)