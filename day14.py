'''Break---> this is used to exit from the loop, when we found the required value...
these are all control statements.'''

for j in range(1,10):
    print(j)
    if j == 5:
        break

list_ = [1,2,3,4]
for n in list_:
    print(n)
    if n == 1:
        break

#Continue--->this is used to skip that particular loop.
    
for j in range(1,10):
    if j == 5:
        continue
    print(j)

list_ = [34,67,56,98]
for n in list_:
    if n == 67:
        continue
    print(n)

'''pass--->this is called as space holder when this is used incase any statement like
(if,for,else,elif...) this should complete, if not we will get indentation error to avoid
this we are using pass'''

for i in range(1,100):
    pass

'''else -- for
------------
it will fall back to else block, when all loops are completed.'''

for m in range(1,10):
    print(m)
else:
    print("else block")

'''while---> this is a combination of for and if statements, if we did not end the loop
in proper way it will run upto the memory space.'''
num = 1
while num<5:
    print(num)
    num += 1

user_in = int(input("Enter  the limit:"))
num_1 = 0
num_2 = 1
print(num_1,num_2,end=" ")

for i in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")










