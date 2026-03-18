'''
variables ----> are named storage location that is used to hold the data in the memory ,
                to make it simple it is the label which points out to a value.
                ----> storsge placeholders.

Rules for defining variables:
    use A-Z,a-z,0-9,
    start with uppercase,lowercase letters even with a underscore _
    but u cant start with symbols (@,#,$,...),even numbers also.

better prefarable way is to go with general purpose --> you want to store
                    your details name ,email,account_number....

'''
'''
a = 1
b = 5
a = 25
#python is dynamically typed ,you need not to define the datatypes and also
#only the recent value to the variable with same name is pinted 
print(a)
print(b)

#1a23 = 25 --->syntax error

#@werf = 4.5 ---> syntax error

#$dsf = 12 --->invalid syntax

#store ur personal details
name = "codegnan"
location = "visakhapatnam"
age = 7
email_id = "cmo@codegnan.com"
#here in the email we use snake case(putting _ in betweeen email and id) to understand better to user.
print(name,location,age,email_id)

#how to assign multiple values to a variable
akash,praneeth,ajay = 21,20,23
print(akash)
print(praneeth)
print(ajay)

#assign same value to multiple variables
x=y=z=21
print(x,y,z)

#keywords are reserved words which will have specific usage/meaning.
#there are 35 keywords  in python
#never use keywords as identifiers.

# python is case senstive
false=25
"(here we can assign 25 to false but not to False)"
#identifiers are names given to variables functions,classes, objects..
#literals are fixed values to a identifier
name = 25
name = 'sandeep'
print(name)
"name is identifier and 25 is literal"
'''
'''
#single line comments ---> #
#multi line comments ---> start and end with  quotes.

#builtin datatypes ---> numeric,boolean,collections

#numeric datatypes ---> int,float,complex
#int ---> count,values,quantities
#float ---> temperature, percentage,price
#complex ---> specific conversions(real and imaginary)

count = 40
print(count)
print(type(count))

price= 175.25
print(price)
print(type(price))

value=2+3j  #we cant put j3 its differt because it take j3 as another variable ,not a complex number.
print(value)
print(type(value))
#small example for above
j3= 25
value=2+j3
print(value)
print(type(value))#here its giving float instead of complex



#typecasting ---> conveting one type to another
#float,complex ---> int
a= 2.35
print(type(a))
b = int(a)
print(b)
print(type(b))
#complex to int
c=3+3j
print(c)
print(type(c))
d=int(c)
print(type(d))
print(d)
#here above scenario complex to int, float not possible to typecast.


#boolean datatype --> validation True/False
a= True
print(a)
print(type(a))

#type conversion of bool
b= int(a)
print(b)
c=float(a)
print(c)
d= complex(float(int(False)))
print(d)
print(type(d))


#input ----> input()/output -->print()
a = 5
print(a)

a=input("enter a value")#takes by default string value until u put any datatype 
print(a)
print(type(a))

#int data taking by input()
b= int(input("enter a integer value"))
print(b)
print(type(b))

#for taking only float data
c=float(input("enter float data"))
print(c)
print(type(c))
'''
#now lets work on a simple case study using above --> fee calculator
#details of the student
name=input("enter the student name :")
print("------------")
admission_fee=int(input("enter the admission fee:"))
tuition_fee=float(input("enter the tuition fee:"))
hostel_fee=float(input("enter the hostel fee:"))
#calculating total fee
total_fee=admission_fee+tuition_fee+hostel_fee
print("___________________")
print("student name  :",name)
print("Admission fee :",admission_fee)
print("tuition fee   :",tuition_fee)
print("hostel fee    :",hostel_fee)
print("total fee     :",total_fee)
                 




































