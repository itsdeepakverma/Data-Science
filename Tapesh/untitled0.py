# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:16:27 2019

@author: Admin
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome import service
from time import sleep
import requests
from bs4 import BeautifulSoup


driver = webdriver.Chrome("C:\\Users\\Admin\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")

url="http://diamondexch9.com/login"
driver.get(url)    
driver.refresh()
sleep(1)
username=driver.find_element_by_xpath("//*[@id='frm_lgn']/div[1]/input")
username.send_keys("Tapesh99")
password=driver.find_element_by_xpath("//*[@id='inputPassword']")
password.send_keys("Rahul@123**")
login=driver.find_element_by_xpath("//*[@id='frm_lgn']/div[4]/button")
login.click()
sleep(2)
driver.find_element_by_xpath("//*[@id='game^4']/a/span").click()
sleep(1)
driver.find_element_by_xpath("//*[@id='league^11365612^Test Matches^']/a/span").click()
sleep(1)
driver.find_element_by_xpath("//*[@id='date^11365612^2019/07/24^']/a/span").click()
sleep(1)
driver.find_element_by_xpath("//*[@id='team^29125905^England v Ireland^']/a/span").click()
sleep(1)
driver.find_element_by_xpath("//*[@id='odds^1.160127177^MATCH_ODDS^29125905']/a/span").click()

url=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div[2]").text
url_list=url.split("\n")

while(True):
    print("Back= {}".format(url_list[7]))
    print("Lay= {}".format(url_list[9]))
    sleep(5)
    
source=requests.get(url).text
soup=BeautifulSoup(source,'lxml')
tables=soup.find_all('table',class_='table coupon-table table table-striped table-bordered m-t-10')

