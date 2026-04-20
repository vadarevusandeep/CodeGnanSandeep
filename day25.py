#encapsulation
'''
-->The princple OF binding data(attributes) and methods that operate on that
data into a simple unit ,which is a class
'''
class BankAc:
    def __init__(self,balance,amount):
        self.__balance=balance
        self.amount = amount
    def deposit(self):
        self.__balance += self.amount
    def get_balance(self):
        return self.__balance
    def withdrawl(self):
        print(f"ur amount {self.amount}")
        print(f"{self.__balance - self.amount}")
acc = BankAc(15000,7000)
acc.deposit()
print(acc.get_balance())
acc.withdrawl()

#inheritance
'''
-->this allows a child class(subclass) to acquire the attributes and methods
of a parent class (base class) this is called inherintance
1.single Inheritance
2.MUltiple

super()
-->this is used to call methods of the parent class from the child class.
'''

class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is child class")
obj = parent()
obj.display()
objc = child()
objc.display()


#multiple inheritance
class father:
    def skill_1(self):
        print("father : hardworking")
class mother:
    def skill_2(self):
        print("mother : cooking")
class child(father,mother):
    def all_skills(self):
        super().skill_1()
        super().skill_2()
        print("child : coding")
c = child()
c.all_skills()



    
        

