#file handling
#handling errors
'''
try block
---->the try block will test a block of code for errors.
example:
try:
    print(b)
    
except block
----> This block will take care of any errors.
example:
except:
    print("This block can handle error")
    
else block
---->else keyword is define a block of code to be executed.

finally block
---->this block will execute either try block having any error or not.
'''


#full example of having all blocks 
try:
    a = 9
    b = 10
    print(a+b)#no error in try then else block executes.
except NameError:
    print("error in code")
else:
    print("no error")
finally:            #executes everytime if having errors in try or not having.
    print("entered finally block")#default block or used as conclusion


#another example with error
try:
    a = 10
    print(c)
except:
    print("error occured in try block")
else:
    print("no error in try block")
finally:
    print("reached finally block")


#example taking input from user and finding any type of error
try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    result = num1/num2
    #print(some)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")
except NameError:
    print("we are getting name error")
except TypeError:
    print("type not matched")
else:
    print(f"result: {result}")
finally:
    print("program completed")
