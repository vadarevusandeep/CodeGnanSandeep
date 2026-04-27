#regular expressions
'''
---> This regular expression or RegEx is a sequence of characters that forms
a searching pattern.
---> To use this we have to import re, which will unlock the package

Functions:
1.findall
---> by using this function, it will find all sequence in the string
syntax --> re.findall("metachar",variable_name)

2.search
---> by using this function ,it will only find the first sequence in the string
syntax --> re.search("metachar",variable_name)

Metacharacters:
---> Meta characters are used to form searching pattern
'''

#1.square brackets []:
'''
---> In this metacharacter we can search for [a-zA-Z0-9] we can also
use it individually.
'''
import re
any = "Iam sandeep trainee23 in 777 codegnan"
so = re.findall("[0-9A-Z]",any)#searching pattern
se = re.search("[n-z]",any)
print(so)
print(se)#in search in span it gives (4,5) means based on our string the first
#occurence of the character in the string in the given range i.e [n-z]etc. 


#2. dot . :
'''
--->This metacharacter will form a searching pattern As it will take
any single character to dot.
'''
import re
we = "hello."
the = re.findall(".",we)
print(the)

import re
we = "hello."
thing = re.search(".",we)
print(thing)

import re
text = "cat bat rat"
print(re.findall(".at", text))

import re
we = "hello."
print(re.findall(r"\.", we))

#3.^ cap :
'''
---> This is used to find the string is starting with the sequence or not 
syntax --> re.findall("metachar",variable_name)
'''
import re
how = "This is used to find the string is starting with the sequence"
who = re.findall("^This is",how)
then = re.search("^This",how)
print(who)
print(then)


#4.dollar $ :
'''
---> This is used to find the string is ending with the sequence or not
syntax --> re.findall("$",variable_name)
'''
import re
how = "This is used to find the string is starting with the sequence"
who = re.findall("sequence$",how)
then = re.search("sequence$",how)
print(who)
print(then)


#5. astric *:
'''
---> This meta character will form a searching pattern as it wil take any for *
from zero or more characters.
syntax --> re.findall(".*",variable_name)
'''
import re
how = "This is used to find the string is starting with the sequence"
who = re.findall("T.*s",how)
then = re.search("i.*",how)
print(who)
print(then)


#6.plus +:
'''
---> This metacharacter will form a searching pattern as it will take atleast
one character between the given pattern for .+
syntax --> re.findall(".*",variable_name)
'''
import re
how = "This is used to find the string is starting with the sequence"
who = re.findall("wi.+h",how)
then = re.search("i.+",how)
print(who)
print(then)
