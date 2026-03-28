#dictionaries
#A dictionary is used to store data in key : value pairs.
#syntax:
'''dict_name = {
    key:value,
    key:value
            }'''

#example
student = {
    "name": "Sandeep",
    "age": 22,
    "course": "BTech"
}


#Characteristics (Rules)
#Keys must be unique
#Keys must be immutable (string, int, tuple)
#Values can be any datatype
#Dictionary is mutable (can change)

#dictionary methods
#1. keys() Method

#Returns all keys from the dictionary.
''' syntax: dict_name.keys()

example:'''

student = {
    "name": "Sandeep",
    "age": 22,
    "course": "BTech"
}

print(student.keys())

#2. values() Method
'''Returns all values from the dictionary.
syntax: dict_name.values()'''

#example:

student = {
    "name": "Sandeep",
    "age": 22,
    "course": "BTech"
}

print(student.values()) 

#3. clear() Method 

'''Removes all items from the dictionary.
syntax: dict_name.clear()'''

#example '''

student = {
    "name": "Sandeep",
    "age": 22,
    "course": "BTech"
}

student.clear()

print(student)

#4. get() (VERY IMPORTANT)

#Safe way to access value

print(student.get("name"))     # None
print(student.get("marks"))    # None
print(student.get("marks", 0)) # 0




#4th data type
'''Sets in Python {}
What is a Set?

A set is a collection of unique elements(that are of same data type).
s = {1, 2, 3, 4}

No duplicates allowed
No order (unordered)
Mutable (can change)'''
#Uses {}

s = {1, 2, 2, 3, 4}
print(s)   #duplicates removed

#Set Operations (VERY IMPORTANT)

#Union (|)
a = {1, 2}
b = {2, 3}

print(a | b)

'''union -> this is used to add or get two different sets without duplicates
intersection -> this method is used to find out common items from both the sets
difference -> this method is used to find the different once from the second set'''
any={1,2,3,4}
so={4,5,6}
print(any.union(so))
print(any.intersection(so))
print(any.difference(so))
any.pop()
print(any) #output={2,3,4}
#pop() method in sets will remove first element in set and in list will remove last element in list

correct_pin = {"1234"}   # set
user_pin = input("Enter PIN: ")
if user_pin in correct_pin:
    print("Correct PIN ✅")
else:
    print("Wrong PIN ❌")

