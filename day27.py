#polymorphism
'''This allows a object of different classes to be treated as instance of the
same base class,with methods behaving differently baesd on the actual object
type.
eg print(len("python"))
print(len([1,3,4]))
'''

#method overloading
'''This defines multiple methods with the same name but different parameters
(number,type,or order) in the same class.
'''
class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
clc = calculator()
print(clc.add(5))
print(clc.add(4,6))
print(clc.add(4,6,9))

#example 2
class calculator:
    def sub(self,a,b,c=0):
        return a-b-c
clc = calculator()
print(clc.sub(5,2))
print(clc.sub(4,6))
print(clc.sub(4,6,9))

#overriding
'''This occurs in the child class ,redefining a parent class method with the
same signature for runtime.
'''
class animal:
    def speak(self):
        return "sound"
class dog(animal):
    def speak(self):
        return "woof"
dg = dog()
print(dg.speak())

#example 2
class parent:
    def speak(self):
        return "sound"
class mother(parent):
    def speak(self):
        return "scold for not eating food "
class father(parent):
    def speak(self):
        return "scold for not getting marks"
fr = father()
mt = mother()
print(fr.speak())
print(mt.speak())

#operater overloading
'''This is customizes operator like +,- for user-defined classes by implementing
special methods.
eg  __add__,__sub__
'''
class someone:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return someone(self.a+other.a,self.b+other.b)
    def __str__(self):
        return f"({self.a},{self.b})"
any = someone(2,3)
so = someone(5,9)
print(any+so)

#abstraction
'''This hides complex implementation details, exposing only essential features
via abstract class or interface.
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(circle.area())
