#generator
'''This is a special type of function that return an iterator whichat a time.
'''
'''def my_generator1():
    yield 1
    yield 2
    yield 3
an=my_generator1()
print(next(an))
print(next(an))
print(next(an))
'''
#yield
'''It will take a pause and again resume ,this is not a normal keyword cannot
be use in normal functions
This is used to produce a value and pause execution.
'''
#next()
'''This is used to get next value from a generator
when the value is finished ,it will stop the iterator
'''

# generator another example
def square_gen(n):
    for i in range(n):
        yield i*i
for j in square_gen(5):
    print(j)

'''it gives output as from o to usernumber at each iteration  it gives
each number i.e 0,1,2,....upto usernumber
here we use yield so, yield everytime  holds value at each iteration it display
different values from 0 to userinput number.
'''
#function
def square_gen1(n):
    for i in range(n):
        pass
    return i*i
n1 = int(input())
for j in range(n1):
    print(square_gen1(n1))
''' it gives only the last return value i.e 16 it gives usernumber times
and print 16 that many times '''


