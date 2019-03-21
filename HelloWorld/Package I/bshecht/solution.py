import datetime

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



# this is a main procedere for defined exersice  
def main():
#    date_time()
#    accept_user_name()
#    accept_inputed_filename()
#    display_elements_from_list()
#    calc_diff_date()
    calc_three_numbers(1,1,3)
    calc_three_numbers(2,2,2)




if __name__=="__main__":
    main()


