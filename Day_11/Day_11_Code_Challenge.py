
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests

websource="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

source=requests.get(websource).text

s=BeautifulSoup(source,'lxml')

table=s.find('table',class_='wikitable')

A=[]
B=[]

for row in table.findAll('tr'):
    cells=row.findAll('th')
    states=row.findAll('td')
    if len(states)==7:
        A.append(states[1].find(text=True))
        B.append(states[4].find(text=True))


#plt.rcdefaults()
VALUES=B[:6]
LABELS=A[:6]
explode=[.2,0,0,0,0,0]
plt.pie(VALUES,labels=LABELS,explode=explode,autopct='%.2f')
plt.show()


# Hands On 

# Find the mean, median, mode, and range for the following list of values:
# 13, 18, 13, 14, 13, 16, 14, 21, 13


#Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8


"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
import numpy as np

userdata=[int(x) for x in input("enter space separated values").split(" ")]

x=np.array(userdata)
x=x.reshape(3,3,)
print(x)





"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
import numpy as np


nparray=np.random.randint(5,15,40)
#nparray=np.linspace(5,15,40)

nparray=np.array(nparray,dtype='int64')

val,cnt=np.unique(nparray,return_inverse=True)

val[np.argmax(np.bincount(cnt))]


#with out np
from collections import Counter

a=dict(Counter(nparray))
value=list(a.values())
key=list(a.keys())

maximum=key[value.index(max(value))]

    


"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)
 
datamean=np.mean(incomes)
datamedian=np.median(incomes)

plt.hist(incomes,50)

#adding outlier

incomes=np.append(incomes,[10000000000])

datamean=np.mean(incomes)
datamedian=np.median(incomes)

plt.hist(incomes,50)



"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""

import numpy as np
import matplotlib.pyplot as plt
userdata = np.random.normal(150, 20, 1000)

plt.hist(userdata,100)

sd=np.std(userdata)

var=np.var(userdata)

"""
Code Challenge ( Bar Plot )
  Name: 
    Most Popular Programming Language out of 28 Languages
  Filename: 
    popular.py
  Problem Statement:
    Read the bardata.csv file
    It has a the survey of 87,570 people at the StackOverFlow Annual Developer Day
    The data has two parts
      1) ID of the Responser
      2) Semicolon seperated data of the languages known by them
    
    We need to now read the csv file using the csv reader and create a dictionary 
    This dictionary should store the Language as the key and value as the number 
    of times the responder has voted for it.
    
    Now display the data in the form of Horizontal Bar Chart to show the popularity of the 
    top 10 luangues and the votes from the developer 

  Hint:
      Use the concept of DictReader from csv 
      Also use the concept of Counter class from collections 
      and update it for each row of data
      Do not use pandas

"""

import csv
from collections import Counter
import matplotlib.pyplot as plt
import itertools

user=list()
with open("bardata.csv") as file:
    csvreader=csv.DictReader(file)
    for row in csvreader:
        user.extend(row['LanguagesWorkedWith'].split(";"))
        
userdict=dict(Counter(user))

userdict=dict(sorted(userdict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))

#top most rated language

plotdata=dict(itertools.islice(userdict.items(),0,10))
plotdata=dict(sorted(plotdata.items(), key = lambda kv:(kv[1], kv[0])))

#for ploting Horizontal bars

plt.barh(range(len(plotdata)), list(plotdata.values()))
plt.yticks(range(len(plotdata)), list(plotdata.keys()))
plt.show()

