import datetime
import sys 

#1 Write a Python program to display the current date and time.
def date_time():
    now = datetime.datetime.now()
    print ("Current date - time: ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

#2  Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
def accept_user_name():
    first_name = input("Your first name: ")
    last_name = input("Your last name: ")
    print(last_name + " " + first_name)

#3 Write a Python program to accept a filename from the user and print the extension of that.
def accept_inputed_filename():
    file_name = input("Input the file name with extention: ")
    splitting_array = file_name.split(".",1)
    print("File extention: ",  splitting_array[1])

#4 Write a Python program to display the first and last element from the following list.
def display_elements_from_list():
    color_list = ["Red","Green","White","Black"]
    for element in color_list:
        print(element)

#5 Write a Python program to calculate number of days between two dates.
def calc_diff_date():
    from datetime import date
    today = date.today()
    print(today)
    date_1 = date(2019,3,20)
    date_2 = date(2019,3,18)
    diff = date_1 - date_2
    print(diff.days)

    
#6 Function to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def calc_three_numbers(d1,d2,d3):
    if d1==d2==d3:
        sum = d1 * 3
    else: 
        sum = d1 + d2 + d3
    print("Summe: ", sum)

#7 Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.         
def out_user_infos(message, dig, info):
    print(message, dig, info)

def deside_even_or_odd_number(number):
    if (number % 2) != 0:
        print("even")
    else:
        print("odd")


def input_numbers():
    print("Ende mit '-1'")
    x = 0 
    while x != -1: 
        x = int(input("Input a digit or '-1' for ENDE "))
        if x != -1:
            deside_even_or_odd_number(x)
        

#8 to check whether a specified value is contained in a group of values.
def is_value_contained_in_group():
    a = [1,5,8,3] 
    x = int(input("Input your search digit: "))
    for i in a:
        if x == i:
            print("List containt :", x)
        else:
            print("this element was not foundet in the list")

#9. to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
# Test Data : 
# color_list_1 = set(["White", "Black", "Red"]) 
# color_list_2 = set(["Red", "Green"])
# Expected Output : 
# {'Black', 'White'}
def search_for_key(): 
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    color_list_3 = set([])

    for i in color_list_1:
        color_list_3.add(i)        
        for j in color_list_2: 
            print(i,j)
            if i == j: 
                color_list_3.remove(i)
    print("{")            
    for k in color_list_3:
            print(k)
    print("}")
        


# this is a main procedere for defined exersice  
def main():
#    date_time()
#    accept_user_name()
#    accept_inputed_filename()
#    display_elements_from_list()
#    calc_diff_date()
#    calc_three_numbers(1,1,3)
#    calc_three_numbers(2,2,2)
#    input_numbers()
#    is_value_contained_in_group()
    search_for_key()


if __name__=="__main__":
    main()


