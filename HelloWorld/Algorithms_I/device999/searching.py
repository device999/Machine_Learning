# Binary Search
from sorting import gnomeSort

def binarySearch(sort_list,val):
  found = False
  totalSize = len(sort_list)
  while found==False:
    middle = int(len(sort_list)/2)
    print(sort_list)
    if sort_list[middle] == val:
      return "Given element exists"
      found=True
    elif sort_list[middle] < val:
      sort_list = sort_list[middle:]
    else:
      sort_list = sort_list[:middle]


if __name__=="__main__":
  unsorted_list = [24,12,43,56,7,15,-4,25,11,22,44,33,77,112,655,4,2,10]
  sorted_list = gnomeSort(unsorted_list)
  required_number = 56
  print(binarySearch(sorted_list,required_number))
  #print(sorted_list)