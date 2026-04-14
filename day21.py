#modules
'''
A Module  in a python is simply a file that contain python code
(functions,variables,classes)
To use the modules in our program we can use keyword called import
as import module_name

                Types of Modules
1.user defined
2.built in or Inbuilt  
'''

#user defined module example
'''This is developed by the user or programmer inside a file of python
code and used by calling import  this filename in another python file.
when needed this file in the new file.
syntax - import existing_filename
using of the functionality of the existing file is as follows
---> existing_filename.functionality
here functionality means i.e function call.
and existing_filename means i.e imported module.
'''

import mymodule
print(mymodule.add(2,3))
print(mymodule.namereverse("sandy"))
mymodule.welcome("sandy")

#built in module example
'''These are comes with installation of python and we can use it by importing
a certain module and can access their functionality as same like in userbuilt
modules
built in modules are developed by  python developers.
syntax  -----  modulename.function()
for importing ---- import module
example
import math
math.add()
'''

#example
import math
print(math.sqrt(4))
print(math.pow(4,2))
print(math.factorial(4))
print(math.floor(4.9))#gives leftside value if we 4.9 also it gives 4
print(math.ceil(4.2)) #gives rightside value if we give 4.2 it gives 5


#number guessing game using random

import random
randomnum = random.randint(1, 10)
attempts = 3
while attempts>=0:
    userguess = int(input())
    if userguess == randomnum:
        print("you win")
        break
    else:
        attempts-=1
        print(f"you have remaining {attempts} attempts")
    if attempts == 0:
        print("you lose")
