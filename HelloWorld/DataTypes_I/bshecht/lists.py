import array as arr 

# List 
# 1  Write a Python program to sum all the items in a list
def sum_all_elements(a):
    sum = 0
    for el in a:
        sum = sum + el
    return sum

#2. Write a Python program to get the largest number from a list.
def count_elements(a):
    return(len(a))

#3. Write a Python program to get the smallest number from a list.
def get_smallest_element_from_list(a):
    a.sort()
    el = a[0]
    return el

# 4. Write a Python program to remove duplicates from a list.
def remove_duplicates(a):
    dup_items = set()
    uniq_items = []
    for x in a:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    return dup_items

# 6. Write a Python program to get the difference between the two lists.


# this is a main procedere for defined exersice  
def main():
    print("Lists")
    ar = [9, 1, 2, 3, 9, 4, 2]
    print("summe: ",sum_all_elements(ar))
    print("Anzahl Elementen: ", count_elements(ar))
    print("smallest element: ",get_smallest_element_from_list(ar))
    print("unic elements: ", remove_duplicates(ar))


if __name__=="__main__":
    main()