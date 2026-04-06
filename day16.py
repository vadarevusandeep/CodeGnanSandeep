'''functions()
-----------
this is a block of code which is reusable.
these are 2 types:1. built-in or In-built
                  2. user defined
1. built-in or In-built

they comes with program and those are already defined...
eg: print(),sum(),map().....



2. user defined

this is created by a person who is developing or using for development.

Note
->its starts with def keyword followed by func name
->And it has calling func...

syntax: def func_name(a,b):
        _______________
        _______________
        fun_name()
        
a,b are parameters, (a,b)are arguments.
'''


n=int(input("enter a  num: "))
def even(n):
    if n%2 == 0:
      print(f"{n} is even.")
    else:
      print(f"{n} is not even.")
even(n=2)


prime_num = 7
count = 0
def prime_check(Num, k):
    for i in range(1,Num+1):
        if Num % i == 0:
            k += 1
    if k == 2:
        print("prime")
    else:
        print("not prime")
prime_check(prime_num,count)



we=(input("enter a  string: "))
empty = ""
def palindrome(we,empty):
    for i in we:
        empty=i+empty
    if empty == we:
        print(f"{we} is a palindrome")
    else:
        print(f"{we} is not a palindrome")
palindrome(we,empty)



number=int(input("enter a  num: "))
num1=0
num2=1
def fib(number,num1,num2):
    print(num1,num2,end="")
    for i in range(number):
       num3=num1+num2
       num1=num2
       num2=num3
       print(num3,end="")
fib(number,num1,num2)

    
    
