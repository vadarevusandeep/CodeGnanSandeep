#multilevel inheritance
'''This occurs when a class inherits from  a child class,creating a
grandparent-->parent-->child in this strucure.
'''
class grandparent:
    def show_Gp(self):
        print("Im grand parent")

class parent(grandparent):
    def show_P(self):
        print("Im parent")

class child(parent):
    def show_C(self):
        print("Im child")

c = child()
c.show_Gp()
c.show_P()
c.show_C()

#hierarchical inheritance:
'''This occurs when mutiple child classes inherit from a single parent class
this process is called hierarchical inheritance.
'''
class parent:
    def parent_(self):
        print("I am parent")
class child1(parent):
    def child_1(self):
        print("Im 1st child")
class child2(parent):
    def child_2(self):
        print("Im 2nd child")

c2 = child2()
c1 = child1()
c1.child_1()
c2.child_2()
c1.parent_()

#hybrid inheritance
'''This is combination of two or more types of inheritance such as
single,multiple,multilevel,hierarchical all this in a single class...
'''
class parent:
    def parent_(self):
        print("I am parent")
class child1(parent):
    def child_1(self):
        print("Im 1st child")
class child2(parent):
    def child_2(self):
        print("Im 2nd child")
class child3(child1,child2):
    def child_3(self):
        print("Im 3rd child")
c3 = child3()
c3.parent_()
c3.child_1()
c3.child_2()
c3.child_3()
#we use both hierarchical and multiple combindly above in single class.

