'''
Introduction to oop's
classes
objects
attributes
methods

oop's
----
---->object oriented programming
it is a style of programming where we model real-world things that contain
both data and functions() i.e also behaviour.
----> reusability of code
----> and also scalable

class
-----
---->it is a blueprint or template that defines what kind of data and behaviour
a certain type of object will have.

object
------
----->Instance of a class or an object is a real instance created from a class.
it is the actual thing that exists in memory while the program runs.

attributes
----------
----->these are variables that store data related to a class or object.

'''
class car:
    pass
car1=car()#object of class car
car2=car()#same as above

#example class
class dog:
    def __init__(self,breed,color):
        self.brd = breed
        self.clr = color
dog1 = dog("germanshepard","brown")
dog2 = dog("lab","white")
print(dog1.brd)
print(dog2.clr)
print(dog1.brd,dog1.clr)

#another example
class foods:
    def __init__(self,starter,maincourse):
        self.str = starter
        self.mc  = maincourse
    def info(self):
        return f"you ordered {self.str} and {self.mc}"
veg = foods("paneer","mushroo Biryani")
nonveg = foods("chicken wings","dum biryani")
print(veg.info())
print(nonveg.info())




