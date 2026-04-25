#file Handling
'''
File handler is an object of file to maintain several functions of file
such as creating,reading, writing and update also deleting the file

#How to open a file
1. open()
---> This open ()function takes 2 parameters and in this we have to close
the file by calling close() function after program..
1file name
2mode 

2.with open():
----> can be 
modes:
----->("r","w","a","x","t")

1."r"-- read:
----------->  to read the file we will use this mode and if the file doesnt
exist it will throw the error.

any = open("demofile.txt","r")
print(any.read())
any.close()

2."w" -- write:
-------------> to write the text into file we will use this mode and it will
create the file if it doesn't exist.
override the text in existing file with new text.

3."a" -- append:
-------------->  to add the text at last into the file this is used and it will
create the file if it doesn't exist.
it will write the text at the end.

4."x" -- create:
---------------> this is used to create a file.but if the file is already exists
it throws an error like file alrady exists.


#To tead a file:
----------------
1.read():
-------- This method can read entire file chunk by chunk ,we can also specify
size.(like we put 10 in parenthesis we get first 10 places with including space)

2.readline():
----------- This will only read the one line at a time in a file.

3.readlines():
----------- This method can read the entire file and return into list with each
line as one index in list.
'''
import os
any = open("demofile.txt","a")
print(any.write("This line is appended using a mode"))
any.close()
os.remove("demofile.txt")

#withn open()
with open("demofile.txt","w") as var:
    print(var.write("This is using write method"))

with open("demofile.txt","r") as var:
    print(var.read())



    
