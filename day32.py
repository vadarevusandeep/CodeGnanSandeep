#7.question mark ?
'''
This meta character will form a searching pattern as it will take any zero or
one character for (?)
syntax --> re.findall(".?",variable)
           re.search(".?",variable)
'''
import re
any = "this metachar"
an = re.findall("th.?",any)
se = re.search("th.?",any)
print(an)
print(se)


#8. curly braces {}
'''This meta character will form a searching pattern as we can mention the size
in the {}.
syntax --> re.search(".{size}",variable)
'''
import re
any = "this metachar"
an = re.findall(".{10}r",any)
se = re.search(".{10}r",any)
print(an)
print(se)


#9. pipe |
'''
THis metachar will form a searching pattern as it consider  right or left any
string is present or not for (|)
'''
import re
any = "this metachar will form"
an = re.findall("that|will",any)
se = re.search("that|will",any)
print(an)
print(se)


#10.special sequence \A
'''
A special sequence is a \ followed by one of the characters in the list below,
and has a special  meaning.
\A
returns a match if the specified characters are at the beginning of the string
eg : "\AThe"
'''
import re
txt = "The rain in spain"
#check if the string starts with "The":
x = re.findall(r"\AThe",txt)
print(x)
if x:
    print("yes, There is a match!")
else:
    print("No match!")


#11.\b
'''
returns a match if the specified characters are at the beginning or at the
end of a word
eg : r"\bain"
'''
import re
txt = "The rain in spain"
#check if the string starts with "The":
x = re.findall(r"\bThe ",txt)
print(x)
if x:
    print("yes, There is atleast one match!")
else:
    print("No match!")


#12.\d
'''
returns a match where the string contains digits(0-9)
'''
import re
txt = "The rain in 56 spain"
#check if the string contains any digits ():
x = re.findall(r"\d",txt)
print(x)
if x:
    print("yes, There is atleast one match!")
else:
    print("No match!")


#13. \D
'''
returns a match where the string DOES NOT contain digits
eg: "\D"
'''
import re
txt = "The rain in 56 spain"
#return a match at every no-digit character:
x = re.findall(r"\D",txt)
print(x)
if x:
    print("yes, There is atleast one match!")
else:
    print("No match!")


#14.\s
'''
returns a match where the string contain a white space character
eg : "\s"
'''
import re
txt = "The rain in 56 spain"
#return a match at every white space character:
x = re.findall(r"\s",txt)
print(x)
if x:
    print("yes, There is atleast one match!")
else:
    print("No match!")


#15.\S
'''
returns a match where the string  does not contain a white space character
eg : "\S"
'''
import re
txt = "The rain in 56 spain"
#return a match at every NON white space character:
x = re.findall(r"\S",txt)
print(x)
if x:
    print("yes, There is atleast one match!")
else:
    print("No match!")


#Time and Date
'''
%d --> day
%m --> month
%Y --> Year
%H --> Hour
%M --> Minutes
%S --> Seconds
%p --> AM/PM
%A --> Day name
%B --> Month name
'''
import datetime
now = datetime.datetime.now()
print()
print(now)
today = datetime.date.today()
print(today.strftime("%d-%m-%y"))
print(today.strftime("%A"))
print(today.strftime("%B"))
print(today.strftime("%H"))
print(today.strftime("%M"))
