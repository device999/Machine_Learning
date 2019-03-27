
import os
import platform  



# 1. Write a Python program to display some information about the Operating System where the script is running
def OS_INFO():
    print("OS INFO: ")
    print(platform.platform())
    print(platform.system())
    print(platform.machine())    
    print(platform.processor())

# 2. Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.    
def summe(number):
    x = 0
    print(number)

    
    return(x)

def input_numbers(): 
    x = 0 
    x = input("enter positive number:")
    sum = 0
    sum = summe(x)
    print("Summe all digits in the number: ", sum)
#    while x != -1: 
#        x = int(input("Input a digit or '-1' for ENDE "))
#        if x != -1:
#            sum = summe(x)
#    print("summe: ", sum)

# this is a main procedere for defined exersice  
def main():
#    OS_INFO()
    input_numbers()




if __name__=="__main__":
    main()