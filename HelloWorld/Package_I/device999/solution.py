import datetime
from datetime import date

# task 1
# Write a Python program to display the current date and time.
def task1():
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

# task 2
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
def task2():
    print('What is your name? ')
    name = input()
    print('What is your surname? ')
    surname = input()
    print ('Nice to meet you, '+surname+' '+name);

# task 3
# Write a Python program to accept a filename from the user and print the extension of that.
def task3():
    print('What is the file you want to upload? ')
    filename = input()
    parts = filename.split(".")
    print ("You are uploading <"+parts[1]+"> file")

# task 4
# Write a Python program to display the first and last element from the following list.
def task4():
    color_list = ["Red","Green","White" ,"Black"]
    list_size = len(color_list)
    print ("The first element = "+ color_list[0])
    print ("The last element = "+ color_list[list_size-1])

# task 5
# Write a Python program to calculate number of days between two dates.
def task5():
    date1 = date(2019,5,12)
    date2 = date(2019,6,7)
    print ((date2-date1).days)

# task 6
# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def task6():
    var1 = float(input())
    var2 = float(input())
    var3 = float(input())
    if(var1==var2 and var2==var3 ):
        print(3*(var1+var2+var3))
    else:
        print(var1+var2+var3)

# task 7
# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
def task7():
    var1 = float(input())
    if(var1 % 2==0): print ("Number is even")
    else: print ("Number is odd")

# task 8
# Write a Python program to check whether a specified value is contained in a group of values.
def task8():
    elements = [1,2,7,6,4]
    number = 5
    for index in range(len(elements)):
        if(number == elements[index]):
            print("Number found in position = "+str(index))
            return
    print ("Number is missing")

# task 9
# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
def task9():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print (color_list_1-color_list_2)

# task 10

# task 11
# Write a Python program to check if a string is numeric.
def task11():
    str = "a";
    if(str.isdigit()): print("It is number")
    else: print("It is string")


# task 12
# Write a Python program to check if a number is positive, negative or zero.
def task12():
    var1 = float(input())
    if(var1>0): print("Number is positive")
    elif(var1<0): print("Number is negative")
    else: print("Number equals to 0")

# task 13
# Write a Python program to check if lowercase letters exist in a string.
def task13():
    sampleStr = "HELLO WORLD"
    for elem in sampleStr:
        if(elem.islower()): 
            print("Lower case was found")
            return
    print ("No lower case was found")

# task 14
# Write a Python program to test if a variable is a list or tuple or a set.
def task14():
    my_list = [1, 2, 3]
    my_set = {1, 2, 3}
    my_tuple = (1, 2, 3)
    if type(my_set) is list:
        print('list')
    elif type(my_set) is set:
        print('set')
    elif type(my_set) is tuple:
        print('tuple')    
    else:
        print('Neither a list or a set or a tuple.')

# task 15
# Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
def task15():
    print("Input the number")
    var1 = float(input())
    print("Input the number")
    var2 =  float(input())
    if(var1 % var2==0): print ("Division was sucessful")
    else: print ("Division failed")




if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
#   Task 10 isnot complete.
    task11()
    task12()
    task13()
    task14()
    task15()