import platform
import os

# Write a Python program to display some information about the Operating System where the script is running

def task1():
    print(os.name)
    print(platform.system())
    print(platform.release())
    print(platform.machine())
    print(platform.processor())
    print(platform.python_build())


# Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.

def task2():
    posNumber = input("enter positive number:")
    counter = 0
    while(int(posNumber)>0):
        print("Step = "+str(counter))
        print("Number = "+str(posNumber))
        sum = 0
        for temp in str(posNumber):
            sum = sum +int(temp)
        posNumber = int(posNumber) - sum
        counter= counter + 1        
    print("done")

# Write a Python program to find the number of divisors of a given integer is even or odd.

def task3():
    posNumber = int(input("enter number:"))
    counter = 0
    for i in range(1, posNumber):
        if posNumber%i==0:
            counter=counter+1
    if(counter%2==0):
        print("Number of divisors are even")
    else:
        print("Number of divisors are odd")


# Write a Python program to find common divisors between two numbers in a given pair.

def task5():
    number1 = int(input("enter number 1:"))
    number2 = int(input("enter number 2:"))
    for i in range(1, number1):
        if number1%i==0 and number2%i==0:
            print("Common divisor = "+str(i))
    if number2%number1==0:
        print("Common divisor = "+str(number1))

#  Write a Python program to print the number of prime numbers which are less than or equal to an given integer.

def prime(number):
    for i in range(1,number):
        if number%i==0 and i!=1:
            print(str(number)+" is divided by"+str(i))
            return False
    return True


def task7():
    posNumber = int(input("enter number:"))
    iterator = 2
    counter = 0
    while(iterator<posNumber):
        if prime(iterator):
            counter= counter + 1
        iterator = iterator+1
    print(counter)

# Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. 
# The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters. 

def task8():
    text = input("Input big text ")
    words = text.replace("."," ").split()
    firstWord = ""
    firstWordAmount = 0
    secondWord = ""
    secondWordSize = 0
    
    for word in words:
        if text.count(word)>firstWordAmount:
            firstWordAmount = text.count(word)
            firstWord = word
        if len(word) > secondWordSize:
            secondWordSize = len(word)
            secondWord = word
    print (firstWord)
    print (firstWordAmount)
    print (secondWord)
    print (secondWordSize)


# Write a Python program to compute the sum of first n given prime numbers.

def task9():
    posNumber = int(input("enter number:"))
    iterator = 2
    sum = 0
    while(iterator<posNumber):
        if prime(iterator):
            sum= sum + iterator
        iterator = iterator+1
    print(sum)
    



# Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.

def task10():
    text = input("Input big text ")
    words = text.replace("."," ").split()    
    for word in words:
        print(word+" is repeated "+str(text.count(word))+" times")





if __name__ == '__main__':
    task1()
    #task2()
    #task3()
    #task5()
    #task7()
    #task8()
    #task9()
    task10()