
"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'db_university.db' )

c=conn.cursor()

c.execute("create table students (student_name text,Student_age integer,Student_Roll integer,Student_Branch)")


c.execute("insert into students values ('Deepak', 25,01,'CSE')")
c.execute("insert into students values ('Vijay', 26,02,'CSE')")


c.execute("select * from Students")

print(c.fetchall())

df=DataFrame(c.fetchall())
df.columns=['Name','Age','Roll_No','Branch']


"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""
import pymongo

client=pymongo.MongoClient("mongodb://demopython:demo%40123@democluster-shard-00-00-qorkd.gcp.mongodb.net:27017,democluster-shard-00-01-qorkd.gcp.mongodb.net:27017,democluster-shard-00-02-qorkd.gcp.mongodb.net:27017/test?ssl=true&replicaSet=DemoCluster-shard-0&authSource=admin&retryWrites=true&w=majority")

mydb= client.db_university

mydb.Student.insert_one(
                {
                "name" : "Deepak",
                "Age" : 28,
                "Id" : 1,
                "Branch" : "CSE"
                })
        
mydb.Student.insert_one(
                {
                "name" : "Raj",
                "Age" : 29,
                "Id" : 2,
                "Branch" : "IT"
                })

mydb.Student.insert_one(
                {
                "name" : "Rajesh",
                "Age" : 20,
                "Id" : 3,
                "Branch" : "ECE"
                })

std=mydb.Student.find()
for x in std:
    print(x)


"""

Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database on cloud 

"""
from selenium import webdriver
from selenium.webdriver.chrome import service
from time import sleep
url = "https://bidplus.gem.gov.in/bidlists"

webdriver_service = service.Service("C:\\Users\\Admin\\Downloads\\operadriver_win64\\operadriver_win64\\operadriver.exe")
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

driver.get(url)
driver.refresh()

bid_no=[]
Item=[]
Quantity=[]
Department_name=[]
S_date=[]
E_date=[]


for i in range(1,6):
    x=1
    while(x<=10):
        bid_no.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[1]/p[1]/a')).text)
        Item.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[2]/p[1]/span')).text)
        Quantity.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[2]/p[2]/span')).text)
        Department_name.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[3]/p[2]')).text)
        S_date.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[4]/p[1]/span')).text)
        E_date.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[4]/p[2]/span')).text)
    
        x+=1

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    nextpage=driver.find_element_by_xpath('//*[@id="pagination"]/ul/li/ul/li['+str(i+2)+']/a')
    nextpage.click()                
    sleep(5)
    
Sdate=[]
Stime=[]
Edate=[]
Etime=[]                                    
for x in S_date:
    Sdate.append(x[:x.index(" ")])
    Stime.append(x[x.index(" ")+1:])
        
for x in E_date:
    Edate.append(x[:x.index(" ")])
    Etime.append(x[x.index(" ")+1:])
import pandas as pd

df=pd.DataFrame()

df['bid_no']=bid_no
df['Item']=Item
df['Quantity']=Quantity
df['Department_name']=Department_name
df['Start_date']=Sdate
df['Strat_time']=Stime
df['End_date']=Edate
df['End_time']=Etime                                
                                    
df.to_csv("bid_dat.csv")

import mysql.connector 
from pandas import DataFrame

conn = mysql.connector.connect(user='demopython', password='demo@123',
                              host='db4free.net',database='mydemodb')
c = conn.cursor()
c.execute ("""CREATE TABLE biddata1(
          bid_id TEXT,
          Item  TEXT,
          Qty INTEGER,
          DEPT_NAME TEXT,
          S_DATE TEXT,
          S_TIME TEXT,
          E_DATE TEXT,
          E_TIEM TEXT
          )""")

for i in range(len(bid_no)):
    c.execute("insert into biddata1 values('{}','{}','{}','{}','{}','{}','{}','{}')".format(bid_no[i],Item[i],int(Quantity[i]),Department_name[i],Sdate[i],Stime[i],Edate[i],Etime[i]))
    conn.commit()
c.execute("drop table biddata")



"""

Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi

"""


from bs4 import BeautifulSoup
import requests


source=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').text
print(source)
soup=BeautifulSoup(source,'lxml')
print(soup.prettify)

table=soup.find('table',class_='table')

print(table.prettify)

rank=[]
nation=[]
weighted_matches=[]
score=[]
rating=[]
for row in table.findAll('tr'):
    cell=row.findAll('td')
    if len(cell)==5:
        rank.append(cell[0].text.strip())
        nation.append(cell[1].text.strip())
        weighted_matches.append(cell[2].text.strip())
        score.append(cell[3].text.strip())
        rating.append(cell[4].text.strip())


import pymongo

client=pymongo.MongoClient("mongodb://demopython:demo%40123@democluster-shard-00-00-qorkd.gcp.mongodb.net:27017,democluster-shard-00-01-qorkd.gcp.mongodb.net:27017,democluster-shard-00-02-qorkd.gcp.mongodb.net:27017/test?ssl=true&replicaSet=DemoCluster-shard-0&authSource=admin&retryWrites=true&w=majority")
        
mydb=client.ICC

for x in range(len(rank)):
    userdict={"Rank":rank[x],
              "Nation":nation[x],
              "Weighted_Matches":weighted_matches[x],
              "Score":score[x],
              "Rating":rating[x]}
    mydb.ICCDB.insert_one(userdict)
    
team=mydb.ICCDB.find()
for x in team:
    print(x)


