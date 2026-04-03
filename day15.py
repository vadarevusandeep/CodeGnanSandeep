#number patterns

print("number pattern output\n")
num = int(input("enter the limit"))
for i in range(num):
    for j in  range(i):
          print(j,end= "")
    print()
print()


#star pattern
    
print("number pattern output\n")
for i in range(num):
    for j in  range(i):
          print("*",end= "")
    print()
print()


#square pattern
    
print("square pattern output\n") 
for i in range(num):
    for j in  range(num):
        print("*",end = "")
    print()
print()


#reverse  number pattern
    
print("reverse pattern output\n")
for i in range(num):
    for j in  range(num-i):
          print("*",end= "")
    print()
print()


#pyramid pattern

print("pyramid pattern output\n")
for j in  range(num):
          print(" "*(num-j),end = " ")
          for i in range(j+1):
              print("*",end = " ")
          print()
print()


#general atm

SBI_sandeep_AC_details ={
                        "name" : "sandeep",
                        "pin_no" : 1234,
                        "balance":10000
                        }
print("Welcome to SBI ATM")
print("pls insert your card")
SBI_Pin = int(input("Enter your 4 digit pin : "))
if len(str(SBI_Pin)) == 4 :
    if SBI_Pin == SBI_sandeep_AC_details['pin_no']:
        print("pin is correct")
        user_choice = int(input("Enter \n1.withdrawl :\n2.deposit :\n3.ministatement\n4.balance enquiry "))
        if user_choice ==1:
            money_with = int(input("enter amount to withdraw :"))
            if money_with <= SBI_sandeep_AC_details['balance']:
                SBI_sandeep_AC_details['balance'] -=  money_with
                print("balance",SBI_sandeep_AC_details['balance'])
            else:
                print("insufficeint")
    else:
        print("invalid pin\nenter correct pin")
else:
    print(" enter 4 digit pin ")
              
      
          
