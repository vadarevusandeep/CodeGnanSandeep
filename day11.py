#for loop and conditional statements
any="python is a programming language"
vowel_count=0
space_count=0
consonant_count=0
for j in any:
    if j in "AEIOUaeiou":
        vowel_count+=1
    elif j==" ":
        space_count+=1
    else:
        consonant_count+=1
print("vowel count :",vowel_count)
print("space count :",space_count)
print("consonant count :",consonant_count)
print(f"count of consonants is {len(any)-(vowel_count+space_count)}")



#Range
a=9
for j in range(a-10,a+4):   #j is a initial variable and it does not represent a undefined variable. hence there is no error
    print(j)
'''
#range( )--->is used to generate numbers
#syntax--->range(start,end,step)
'''
#small work using range()
print("even numbers")
for j in range(0,11,2):       #prints even numbers upto 10
    print(j)



#conversions
print("conversions output")
any='abc'
print(list(any))   #string to list
print(tuple(any))  #string to tuple
anyy='123'
print(int(anyy))   #string to int
print(float(anyy)) #string to float



#negative indexing using range()
name="madam"                #reverse the string      name[::-1]
empty_str=""
for j in name:
    empty_str=empty_str+j  #empty_str=empty_str+j--->(gives the name in correct order) but this reverses the string
if empty_str == name:
    print("palindrome")
else:
    print("not a palindrome")



#another example
for num in range(1,101):
    if num%2==0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")

