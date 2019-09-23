
#Gnome sort algorithm

def gnomeSort(unsorted_list):
  i = 0
  j = 1
  while i<len(unsorted_list)-1 or j < len(unsorted_list)-1:
    temporal = 0
    temporal1 = unsorted_list[j] 
    tmeporal2 = unsorted_list[i]
    if(unsorted_list[j] < unsorted_list[i]):
      temporal = unsorted_list[j]
      unsorted_list[j] = unsorted_list[i]
      unsorted_list[i] = temporal
      if i==0:
        i = 0
        j = 1
      else:
        i = i - 1
        j = j - 1      
      #print(unsorted_list)
    else:
      i = i+1
      j = j+1
  return unsorted_list
    


if __name__=="__main__":
  unsorted_list = [24,12,43,56,7,15,-4]
  unsorted_list = gnomeSort(unsorted_list)
  print(unsorted_list)
