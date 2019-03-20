import datetime

#1
def date_time():
    now = datetime.datetime.now()
    print ("Current date - time: ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

#2
def accept_user_name():
    first_name = input("Your first name: ")
    last_name = input("Your last name: ")
    print(last_name + " " + first_name)

#3 
def accept_inputed_filename():
    file_name = input("Input the file name with extention: ")
    splitting_array = file_name.split(".",1)
    print("File extention: ",  splitting_array[1])

#4

# this is a main procedere for defined exersice  
def main():
#    date_time()
#    accept_user_name()
    accept_inputed_filename()

if __name__=="__main__":
    main()


