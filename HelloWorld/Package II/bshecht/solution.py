
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


# this is a main procedere for defined exersice  
def main():
    OS_INFO()



if __name__=="__main__":
    main()