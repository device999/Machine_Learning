
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



# 3. Write a Python program to find the number of divisors of a given integer is even or odd.
def divisor(n):
    for i in range(n):
        x = len( [i for i in range(1,n+1) if not n % i])
    return x

def divisor_even_or_odd(n):
    print(divisor(n))


# 4. Write a Python program to compute the summation of the absolute difference of all distinct pairs in an given array (non-decreasing order)
# past and copy :) 
def sum_distinct_pairs(arr):
    result = 0
    i = 0
    while i < len(arr):
        result+= i * arr[i] - (len(arr) - i - 1) * arr[i]
        i+=1
    return result

# 5. Write a Python program to find common divisors between two numbers in a given pair.
def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i
        i+=1
    return gcd

def num_comm_div(x, y):
  n = ngcd(x, y)
  result = 0
  z = int(n**0.5)
  i = 1
  while( i <= z ):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result



# 6. Write a Python program which solve the equation. (*)
# ax+by=c
# dx+ey=f
# Print the values of x, y where a, b, c, d, e and f are given.
# Input:
# a,b,c,d,e,f separated by a single space.
# (-1,000 = a,b,c,d,e,f = 1,000)
# Input the value of a, b, c, d, e, f:
# 5 8 6 7 9 4
# Values of x and y:
#-2.000 2.000
def is_diff_index_equal_zero(a,b,c,d):
  if((a - b) == 0):
    return True;
  if((c - d) == 0):
    return True;
  else: 
    return False; 


# ax + by = c
# dx + ey = f

def solution_(v,a,b,c,d,e,f):
  print("solution:")
  
  if(v == "x"):
    print("solution with x")
    # 0 = (c + f) - (b + e)
    # y = (c + f) / (b + e) 
    y = (c + f) / (b + e)
    x = (c - b) / a 
    print(" x = ", x, " y = ", y)

  if(v == "y"):
    # x = 
    x = (c + f) - (b + e) 
    y = (f - e) / d
    print(" x = ", x, " y = ", y)

  if(v == "NotFound"): 
    print("can not resolve")


def solve_equation(a,b,c,d,e,f):
  zeroValue = "NotFound"

  if(is_diff_index_equal_zero(a,d)):
    zeroValue = "x"
    solution_(zeroValue,a,b,c,d,e,f) 
  if(is_diff_index_equal_zero(b,e)):
    zeroValue = "y"
    solution_(zeroValue,a,b,c,d,e,f) 

def solve_equation_input():

  a = int(input("a"))
  b = int(input("b"))
  c = int(input("c"))
  d = int(input("d"))
  e = int(input("e"))
  f = int(input("f"))
  solve_equation(a,b,c,d,e,f)

# 7. Write a Python program to print the number of prime numbers which are less than or equal to an given integer.
# n (1 = n = 999,999)
# Input the number(n): test
# 35
# Number of prime numbers which are less than or equal to n.: 11
def primes(n):
  test = 0
  
  for i in range (2, n):
    if n <= 1: 
      print(n, "isn't a prime number.")

    for i in range (2, n):
      if n * 1.0 % i == 0:
        print (n * 1.0 / i)
        test = 1
      else:
        print(n * 1.0 / i) 
    if test == 1:  
      print("Digit ", n, " is not a prime digit") 
    else:
      print("Digit ", n, " is a prime")

# 8. Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. 
# The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters. 



# 9. Write a Python program to compute the sum of first n given prime numbers.



# 10. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.



# this is a main procedere for defined exersice  
def main():
#    OS_INFO()
#    input_numbers()    
#    divisor_even_or_odd(15)
#    divisor_even_or_odd(4)
#    divisor_even_or_odd(32)
#    divisor_even_or_odd(10)
    # error if n = 0
#    print("\4 Summe distinct pairs: ")
#    print("[1,2,3]", sum_distinct_pairs([1,2,3]))
#    print("[98,99,100]", sum_distinct_pairs([2,2,1]))

#    print("Number of common divisors: ",num_comm_div(2, 4))
#    print("Number of common divisors: ",num_comm_div(2, 8))
#    print("Number of common divisors: ",num_comm_div(12, 24))

#    solve_equation_input()
#    7 
     n = int(input("Number : "))
     print(primes(n))  

if __name__=="__main__":
    main()