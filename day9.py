
#list indexing 
lista = [3,4,"sandy",["sai","deepak"]]
listb = ["meghana","satya",[1,4,3,[1,3,4,]]]
listc = ["apple","banana",['a','b','c']]
listd = [1,2,3,[11,34,44],["apple","banana",['a','b','c']]]

#output
print(lista[3][1][2])
print(listb[2][3][1])
print(listc[2][2])
print(listd[4][2][1])


#tuples 
print(9+8)
print("python"+"language")
print([1,2] + [3,4])


#concatenation
'''this is nothing but , a (+) behaviour..
case 1
integers --> this will act as addition for int
'''

#case 2
#note --> if we try to do concatenation on different datatypes we cant and get a type error.
'''like
print("sandy"+[1,4,3])
for other datatypes (we have to use both same datatypes for concatenation)
'''


#tuple()--> is a collection of different datatypes and   this is represented by parathesis ()
#and seperated by comma ,

thing = (1,"sandy",[1,4,3],(3,4,"sandy"))
print(thing)
thing1 = (12,89,"python",(22,"sandy",[67,"python is a language",(7,8)],[8,("python",[34,9])]))
print(thing1[3][2][1][9])

num1 = 9
num2 = 90
print(f"before swapping - {num1},{num2}")
num1,num2 = num2,num1
print(f"after swapping - {num1},{num2}")
a = 10
b = 20
a,b = b,a
print(a,b)


#leap year code

leapyear = int(input("Enter year: "))
if (leapyear % 4 == 0 and leapyear % 100 != 0)or leapyear % 400 == 0:
    print(f"{leapyear} is leap year")
else:
    print(f"{leapyear} is not a leap year")
    































