import operator

# 1 Write a Python script to sort (ascending and descending) a dictionary by value.
def sort_by_key():

    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print('Original dictionary : ',d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(0))
    print('Dictionary in ascending order by value : ',sorted_d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
    print('Dictionary in descending order by value : ',sorted_d)

# 2. Write a Python script to sort (ascending and descending) a dictionary by key.
def sort_by_value():

    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print('Original dictionary : ',d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(0))
    print('Dictionary in ascending order by value : ',sorted_d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
    print('Dictionary in descending order by value : ',sorted_d)

# 3. Write a Python script to concatenate following dictionaries to create a new one.
def concat_dictionary(dic1,dic2): 
  dicd = {} 
  for d in (dic1, dic2): 
      dicd.update(d)
  return dicd

# 4. Write a Python program to check multiple keys exists in a dictionary.
# can not implemented becouse multiple keys will be deleted
#def check_multiple_keys_in_dictionary(d):
#  multiple_key = {}
#  for key in d.:
#      print key
#  return multiple_key

## Typle
# 1. Write a Python program to find the length of a tuple.

# 2. Write a Python program to create a tuple with different data types.

# 3. Write a Python program to remove an empty tuple(s) from a list of tuples.

# 4. Write a Python program to reverse a tuple.

def main():
    print(" Data Types II ")
    # 1 
    sort_by_value()
    # 2
    sort_by_key()
    d1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    d2 = {3:0, 9:1}
    print(d1)
    print(d2)
    d3 = concat_dictionary(d1,d2)
    print(d3)
    d1.update(d2)
    print(d1)
#    mKey = check_multiple_keys_in_dictionary(d1)
#    print(mKey)
    ## Typle  
    # 1 
    tuple1 = ("apple", "banana", "cherry")
    print("length from tuple1 is ", len(tuple1))
    #print("length from tuple1 is ", tuple1.__len__)
    # 2
    tuple_diff_data = ("apple", 3.14, 3)
    print(tuple_diff_data)
    # 3 
    L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    print(L)
    L = [t for t in L if t]
    print(L)
    # 4 
    x = ("w3resource")
    y = reversed(x)
    print(tuple(y))
    x = (5,10,15,20)
    print(tuple(x))
    y = reversed(x)
    print(tuple(y))

    ### Set 
    # 1. Write a Python program to create a set.
    x = set()
    print("Empty Set: ", x)
    n = set([0,1,2,3,4])
    print(n)
    # 2. Write a Python program to find the length of a set.
    print("len x ", len(x), " len n", len(n))
    print("min : ", min(n), " max : ", max(n))
    n.discard(4)
    print(n)
    # 5 Write a Python program to create a union of sets.
    #Union
    setx = set(["green", "blue"])
    sety = set(["blue", "yellow"])
    seta = setx | sety
    print(seta)
    


      

    






if __name__=="__main__":
    main()
