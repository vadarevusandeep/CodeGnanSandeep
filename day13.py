#printing table of user choice

table_num = int(input("enter required table number : "))
for i in range(1,11):
    print(f"{table_num} * {i} = {table_num*i}")

'''
string methods
count(),join(),strip(),replace(),split(),capitalize(),casefold(),isalnum(),
isdigit(),isdecimal(),islower(),isupper()..
'''

#finding no of capital letters and smaller letters  in given string

given_str = input("enter any string")
capital_count = 0
small_count = 0
space_count = 0
for i in given_str:
    if i.islower():
        small_count+=1
    elif i.isupper():
        capital_count+=1
    else:
        space_count+=1
print(f"small letters = {small_count}\ncapital count = {capital_count}\nspace count ={space_count} ")

#now print the each lettercase in given string seperately

lower_list = []
capital_list = []
for i in given_str:
    if i.islower():
        lower_list.append(i)
    elif i.isupper():
        capital_list.append(i)
print(f"lower letters = {lower_list}\n capital_letters = {capital_list}")

#general atm

SBI_sandeep_AC_details ={
                        "name" : "sandeep",
                        "pin_no" : 1234
                        }
print("Welcome to SBI ATM")
print("pls insert your card")
SBI_Pin = int(input("Enter your 4 digit pin : "))
if len(str(SBI_Pin)) == 4 :
    if SBI_Pin == SBI_sandeep_AC_details['pin_no']:
        print("pin is correct")
    else:
        print("invalid pin\nenter correct pin")
else:
    print(" enter 4 digit pin ")

#perfect number check
    
per_num = int(input("enter a number: "))
fact_all = 0
for i in range(1,per_num):
    if per_num % i == 0:
        fact_all+=i
if fact_all == per_num:
    print(f"{per_num} is perfect number ")
else:
    print(f"{per_num} is not a perfect number")































