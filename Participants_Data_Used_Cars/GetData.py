# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:31:03 2019

@author: Admin
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome import service
from time import sleep
from bs4 import BeautifulSoup
import requests


class Getdata:
    data=pd.DataFrame()
    NameList=[]
    def __init__(self,data,NameList):
        self.data=data
        self.NameList=NameList
        
    def make_dict(self,namelist,dataframe,key_column,value_column):
        temp={}
        for x in namelist:
            xx=dataframe[value_column][dataframe[key_column]==x]
            if len(xx.value_counts().index) > 0:
                temp[x]=xx.value_counts().index[0]
            else:
                temp[x]="nan"
        return temp
            
    def Getzigwheels(self,Source,userdict):
        driver = webdriver.Chrome("C:\\Users\\Admin\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
        url="https://www.zigwheels.com/newcars"
        driver.get(url)    
        driver.refresh()
        notfind=[]
        

        i=1

        for k,v in userdict.items():
            if k not in notfind:
                if v=="nan":
                    key_element=k.split(" ")
                    searchbox=driver.find_element_by_xpath("//*[@id='headerSearch']")
                    #searchbox.click()
                    searchbox.send_keys(key_element[0]+" "+key_element[1]+" "+key_element[2])
                    sleep(1)
                    searchbox.submit()
                   
                try:
                    onroad=driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div[2]/div/div[3]/span[4]/span")
                    onroad.click()
                    sleep(2)
                    price=driver.find_element_by_xpath("//*[@id='variant-top-carousal']/li[1]/table/tbody/tr[4]/td[2]")
                    userdict[k]=price.text
                    
                except Exception:
                    notfind.append(k)
                    pass
                if i <200:
                    i+=1
            else:
                break
        return userdict

    def Getnirol(Source,userdict):
        driver = webdriver.Chrome("C:\\Users\\Admin\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
        price_dict=userdict
        
        url="https://www.nriol.com/returntoindia/audicars-price.asp"
        driver.get(url)    
        driver.refresh()

        driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div/table/tbody/tr[2]/td[1]").click()

        #iframe=driver.switch_to.frame

        print(driver.find_elements_by_xpath("//*[@id='myModal']/div/div/div[2]/div/table/tbody/tr[2]/td[1]").text)

        source=requests.get(url).text

        soup=BeautifulSoup(source,'lxml')

        tables=soup.find_all('table')
        A=[]
        B=[]
        C=[]
        for t in tables:
            for row in t.find_all('tr'):
                cell=row.find_all('td')
                if len(cell)==3:
                    A.append(cell[0].text.strip())
                    B.append(cell[1].text.strip())
                    C.append(cell[2].text.strip())
                    
        for i in B:
            temp=i.split()
            if len(temp)==5:
                B[B.index(i)]=temp[3]+" "+temp[4]+" "+temp[0]+" "+temp[1]+" "+temp[2]
      
        
        for i in B:
            A[B.index(i)]= A[B.index(i)]+" "+i
            for i in A:
                temp=i.split()
                A[A.index(i)]=temp[0]


        temp_dict=dict(zip(A,C))

        for key in price_dict.keys():
            temp=key.split()
            if (temp[1]) in temp_dict.keys():
                price_dict[key]=temp_dict[temp[1]]
        
        return price_dict        

    def Getcarwale(Source,userdict):
        url="https://www.carwale.com/audi-cars/"
        price_dict=userdict
        source=requests.get(url).text

        soup=BeautifulSoup(source,'lxml')

        ModelName=[]
        ModelPrice=[]

        name=soup.find_all('strong',class_='text-unbold')
        for x in range(len(name)):
            ModelName.append(name[x].text)
            
        price=soup.find_all('div',class_='font20 margin-top15')

        for y in range(len(price)):
            ModelPrice.append(price[y].text)

        for z in ModelPrice:
            if len(z.split())>2:
                ModelPrice[ModelPrice.index(z)]=z.split()[1]+" "+z.split()[2]
    
        for i in ModelName:
            if len(i.split())<=2:
                ModelName[ModelName.index(i)]=i.split()[0]+" "+i.split()[1]
            else:
                ModelName[ModelName.index(i)]=i.split()[0]+" "+i.split()[1]
                
        temp_dict=dict(zip(ModelName,ModelPrice))
        
        for key in price_dict.keys():
            if price_dict[key]=="nan":
                temp=key.split()
            if len(temp) >2:
                if (temp[0]+" "+temp[1]) in temp_dict.keys():
                    price_dict[key]=temp_dict[temp[0]+" "+temp[1]]
                    print("y")
                else:
                    print("N")

    def GetDataFromSource(Source,userdict):
        if Source == "zigwheels":
            Getzigwheels(Source,userdict)
        elif Source == "nirol":
            Getnirol(Source,userdict)
        elif Source == "carwale":
            Getcarwale(Source,userdict)
    
