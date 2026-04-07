'''Ways to pass arguments in calling function:
required arguments:
-------------------
-->it should match same number variables in calling with def
'''

num_1 = 11
num_2 = 10
def add(num_1, num_2):
    print(num_1+num_2)
add(num_1, num_2)


#Default Arguments:
#-----------------
#-->it will take the default values from tthe arguments.

My_name = "akash"
def sum_num(name):
  print(name)
sum_num(name="sai")
sum_num(name="harshith")



a = int(input("enter a num: "))
def even(a):
  if a % 2 == 0:
      print(f"{a} is even")
  else:
      print(f"{a} is not a even")
even(a)



def prime_num(num,count):
    for j in range(1,num+1):
        if num % j == 0:
            count+= 1
    if count == 2:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not a prime")
prime_num(num=9,count=0)
prime_num(num=47,count=0)


'''Keyword arguments:
------------------
-->above num=47 is called keyword arguments.
syntax: key = value
-->making the function call more readable and order-independent.
-->This is particularly useful when dealing with functions that have multiple optional
parameters.
'''

def any(num_1, num_3, num_2):
    print(f"num_1 = {num_1}, num_2= {num_2}, num_3= {num_3}")
any(num_2=7, num_1=0, num_3 = 90)



'''Variable length arguments:
--------------------------
adding a star(*) before the parameters name in the function, recieve a tuple of arguments
and can access items with indexes.
'''

def name(*Candidate_):
    print(Candidate_)
name("teja","sony","akash")

