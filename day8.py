'''Vowel_con = input("enter a letter:")
if Vowel_con in "AEIOUaeiou":
    print("entered letter - {Vowel_con} is vowel")
else:
    print("entered letter - {Vowel_con} is consonant")
'''
'''
time_aday = input("enter 24hrs time: ")
parts = time_aday.split(":")
hours = int(parts[0])
minutes = int(parts[1])
if hours >= 13 and minutes < 60:
    if hours == 24 :
        print(f"{time_aday} is converted into {hours - 12}:{minutes}am")
    else:
        print(f"{time_aday} is converted into {hours - 12}:{minutes}pm")
else:
    print(f"you have entered nrml or min incorrect")

'''

#list  ---> different types of data inside the [],which are seperated by  ,
#eg ---> [1,"sandy", 4 ,3]
#list indexing
list_1 = [1,2,3,"python",[1,2,["python","java"],"language"]]
print(list_1[4][2][0][3])
print(list_1[4])


#list methods
'''mutable -- can modify or change directly the varible.
   immutable - cant modify a variable data directly.(we can by using another variable)
   append()-- adds new items at the end of list.
    syntax - variable_name.append(item)
    
   extend()-- this method is used to add items in the last indices as individual characters at each index.
    syntax - variable_name.extend(item)
    
   remove()-- delete the item directly from the list.
    syntax - variable_name.remove(item_to_remove)
    
   pop()   -- this method will delete the item in the list using indices.
    syntax - variable_name.pop(item_index)
    includes negative indexing.
'''
#append
list_2 = [1,3,4,5,6]
print(list_2)
list_2.append(8)
print(list_2)
list_2.append(9)
print(list_2)
list_2.append([143,144])
print(list_2)

#extend
list3 = [1,4,3]
list3.extend("sandy")
print(list3)
list3.extend(["sandy"])
print(list3)

#remove
list4 = [1,234,45,"sandy"]
list4.remove(234)
print(list4)
list4.remove("sandy")
print(list4)

#pop
list5 = [4,2,45,86,565,98]
list5.pop(-1)
print(list5)
list5.pop(4)
print(list5)














