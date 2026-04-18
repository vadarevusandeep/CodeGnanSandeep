#constructor - A constructor is a special method used to intialize object data.
#__init__()
#example
'''class STUDENT:
    def __init__(self,name,Id):
        self.n=name
        self.i=Id

    def display(self):
        print(self.n,self.i)
st1=STUDENT("SANDEEP",754)
st1.display()'''

#ACCESS SPECIFIERS
#public
'''syntax - name
we can use it anywhere in the program.'''
#protected
'''syntax - _name
only for internal use.'''
#private
'''syntax - __name
this one is restricted '''
#self
'''this keyword is instance variable and unique for each object'''

#example
class some:
    def __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private = "private"
any = some()
print(any.public)
#print(any._protected) this gives error because of calling protected variable
#print(any.__private) same as above we use private variable i.e using __name












