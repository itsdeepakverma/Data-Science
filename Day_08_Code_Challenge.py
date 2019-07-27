

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
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
    
import pandas as pd

df=pd.DataFrame()

df['Rank']=rank
df['Nation']=nation
df['Weighted Mathces']=weighted_matches
df['Score']=score
df['Rating']=rating

df.to_csv('ICCRANK.csv')

"""
Code Challenge:  
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
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
                                   #//*[@id="pagi_content"]/div[2]/div[1]/p[1]/a
                                   #//*[@id="pagi_content"]/div[10]/div[1]/p[1]/a
        Item.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[2]/p[1]/span')).text)
                                    #//*[@id="pagi_content"]/div[2]/div[2]/p[1]/span
        Quantity.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[2]/p[2]/span')).text)
        Department_name.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[3]/p[2]')).text)
        S_date.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[4]/p[1]/span')).text)
        E_date.append((driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(x)+']/div[4]/p[2]/span')).text)
    
        x+=1

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    nextpage=driver.find_element_by_xpath('//*[@id="pagination"]/ul/li/ul/li['+str(i+2)+']/a')
    nextpage.click()                #//*[@id="pagination"]/ul/li/ul/li[5]/a  //*[@id="pagination"]/ul/li/ul/li[7]/a  
                                    #//*[@id="pagination"]/ul/li/ul/li[4]/a
    sleep(5)                               #//*[@id="pagination"]/ul/li/ul/li[6]/a
                                    #//*[@id="pagination"]/ul/li/ul/li[6]/a
                                    #//*[@id="pagination"]/ul/li/ul/li[7]/a
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
"""
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image

"""
from selenium import webdriver
from selenium.webdriver.chrome import service
from time import sleep
import urllib
url = "http://forsk.in/images/"


webdriver_service = service.Service("C:\\Users\\Admin\\Downloads\\operadriver_win64\\operadriver_win64\\operadriver.exe")
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

driver.get(url)
driver.refresh()


nextimage=driver.find_element_by_xpath('/html/body/table/tbody/tr[4]/td[2]/a')
nextimage.click()
sleep(5)

image=driver.find_element_by_xpath('/html/body/img')
driver.save_screenshot('example.png')



#/html/body/table/tbody/tr[4]/td[2]/a
#/html/body/table/tbody/tr[5]/td[2]/a
#/html/body/table/tbody/tr[6]/td[2]/a

