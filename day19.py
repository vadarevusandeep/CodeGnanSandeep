#lambda function is also anonymous function
'''which have lambda function can taken n number of arguments
        but having only one expression.
        
       syntax:
           lambda arguments : expression
       '''
any = lambda so : so+10
print(any(16))  #output  26
print("addition",any(10))  #can pass only single argument at a time.

some = lambda an,how : how-an
print("difference",some(10,20))  #we can pass many arguments at a time like this.
                    #by increasing n:of arguments after lambda keyword and
                    #pass that no of arguments while calling.
area=lambda pi,r : pi*(r**2)
print("circle area : ",area(3.14,5))
division = lambda a,b:a/b
print("division",division(4,2))

#list comprehension
'''This  offers the shorter syntax when you want to create a new list
    from the existing list.
    syntax :
        variable_name = [expression loop  condition(if having)]
    '''
old_list = [1,2,3,4,5]
new_list = [j for j in old_list]
print("new list",new_list)
print("old list",old_list)

even_list = [j for j in old_list if j%2 == 0]
print("even list",even_list)










































