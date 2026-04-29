'''
import re

def validatename(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern, name)

def validateemail(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validateph(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, phone)

def validatepass(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)

def main():
    name = input()
    email = input()
    phone = input()
    password = input()

    if not validatename(name):
        print("invalid name")
    elif not validateemail(email):
        print("invalid email")
    elif not validateph(phone):
        print("invalid phone number")
    elif not validatepass(password):
        print("invalid password")
    else:
        print("all inputs are valid! form submitted successfully")

if __name__ == "__main__":
    main()
'''
#Data Analysis
'''
why this needed ?
This is critical bcoz it converts raw data into actionable insights,enabling
information to decision making easy and 
improves operational efficiency ....
1.Decision-making
2.improved operational efficiency
3.customer understanding
4.market insight
5.risk management
6.data driven strategies


import matplotlib.pyplot as pit
x = [1,2,3,4]
y = [10,20,30,40]
pit.plot(x,y)
pit.show()
'''
#bar graph
import matplotlib.pyplot as pit
pit.bar(["A","B","C"],[1,2,3])
pit.show()

#pie graph
import matplotlib.pyplot as pit
pit.pie([30,40,30],labels = ["sandeep","deepak","sai"])
pit.show()

#histogram
import matplotlib.pyplot as pit
pit.hist([30,40,60,90])
pit.show()

#numpy
'''
-->Numpy (numerical python) is the functional open-source library for scientific
computing in python ,providing high performance ,N-dimensional array objects
(ndarray).
-->This enables efficient numerical computation linear algebra,and data
manipulation , serving as the basics for tools like tensorflow and scipy.
'''
import numpy as np
arr=np.array([1,2,3])
print(arr)

#pandas
'''
This  pandas is used for handling structured  data in table format
pip install pandas
'''
import pandas as pd
data = {"Name":["sandeep","sai","deepak"],"marks":[35,36,37]}
any = pd.DataFrame(data)
print(any)
