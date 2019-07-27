# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:45:36 2019

@author: Admin
"""
# code for scrapping New_Price from different website

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome import service
from time import sleep
from bs4 import BeautifulSoup
import requests

data=pd.read_csv("new_data.csv")

#identifing unique car and their new price available in the list

y=data["Name"].value_counts()
y=list(y.index)
price_dict={}

def make_dict(namelist,dataframe,key_column,value_column):
    temp={}
    for x in namelist:
        xx=dataframe[value_column][dataframe[key_column]==x]
        if len(xx.value_counts().index) > 0:
            temp[x]=xx.value_counts().index[0]
        else:
            temp[x]="nan"
    return temp


price_dict=make_dict(y,data,"Name","New_Price")

#code for scraping new price and store in price dict
cnt=[]
notfind=[]
webdriver_service = service.Service("D:\\Data-Science\\operadriver_win64\\operadriver_win64\\operadriver.exe")
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

url="https://www.zigwheels.com/newcars"
driver.get(url)    
driver.refresh()

i=1

for k,v in price_dict.items():
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
                price_dict[k]=price.text
                cnt.append(price.text) 
            except Exception:
                notfind.append(k)
                pass
            if i <200:
                i+=1
            else:
                break
        

#scarping data from NRIOL.com

webdriver_service = service.Service("D:\\Data-Science\\operadriver_win64\\operadriver_win64\\operadriver.exe")
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

url="https://www.nriol.com/returntoindia/audicars-price.asp"
driver.get(url)    
driver.refresh()

driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div/table/tbody/tr[2]/td[1]").click()

iframe=driver.switch_to.frame

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
   #B[B.index(i)]=i.replace("("," ")
   #B[B.index(i)]=i.replace(")"," ")
   #B[B.index(i)]=i.replace("35","35 ")
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
        print("y")
    
#for Brand wise priceform carwale.com

url="https://www.carwale.com/audi-cars/"

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

ModelPrice.append(str("3.25 lakh"))
ModelName.append("Renault KWID")

ModelName[ModelName.index("Mercedes-Benz CLS")]="Mercedes-Benz CLS-Class"
ModelPrice[63]="84.4 Lakh"
ModelPrice=ModelPrice[0:-8]  
ModelName=ModelName[0:-8]  


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
    
        
#for assining new price from price dict to data frame
        
for i in range(len(data["Name"])):
    if str(data["New_Price"][i])=="nan":
        data["New_Price"][i]=price_dict[data["Name"][i]]
        
        
#data=data.iloc[:,3:]    
#for saving the updated data in dataframe

data.to_csv("new_data.csv")  

#for count NaN in dict
cntnan=0
for z in price_dict.values():
    if z == "nan":
        cntnan+=1
    




# finding NaN IN The Data set
import pandas as pd
import numpy as np
data=pd.read_csv("new_data.csv")       
        

data.isnull().any(axis=0)

#for converting crores in lakh

import re

regex=re.compile(r'\d+\.?\d*') 
regex1=re.compile(r'\D*$')

for i in range(len(data["New_Price"])):
    try:
        temp=regex1.search(data["New_Price"][i])
        if(temp[0]=="Crores" or temp[0]==" Crores" or temp[0]=="crore" or temp[0]==" Cr"):
            data["New_Price"][i]=str((float(regex.findall(data["New_Price"][i])[0]))* 100)
        else:
            data["New_Price"][i]=regex.findall(data["New_Price"][i])[0]
    except:
        print("No")
        
data["New_Price"]=pd.to_numeric(data["New_Price"])

#filling NaN with most occurance in seats
        
data["Seats"]=data["Seats"].fillna(data["Seats"].value_counts().index[0])

#data["Power"]=data["Power"].fillna(data.groupby("Name")["Power"].value_counts().index[0][1])

# extract actual numeric values

def numeric_convert(dataframe,target_column):
    for i in range(len(dataframe["Name"])):
        try:
            if len(regex.findall(dataframe[target_column][i])) > 0:
                dataframe[target_column][i] = regex.findall(dataframe[target_column][i])[0]
            else:
                dataframe[target_column][i]=0
        except:
            dataframe[target_column][i]=0
    dataframe[target_column]=pd.to_numeric(dataframe[target_column])
        
numeric_convert(data,"Power")
numeric_convert(data,"Engine")
numeric_convert(data,"Mileage")
      
power_dict=make_dict(y,data,"Name","Power")
engine_dict=make_dict(y,data,"Name","Engine")
mileage_dict=make_dict(y,data,"Name","Mileage")        

#for deleting zero

def delete_zero(data_dict):
    for i in data_dict.copy():
        if not data_dict[i]:
            data_dict.pop(i)
            
    for k in data_dict.copy():
        if len(k.split()) > 2:
            data_dict[k.split()[0]+" "+k.split()[1]]=data_dict.pop(k)

delete_zero(power_dict)
delete_zero(engine_dict)
delete_zero(mileage_dict)

#assign values to data frame

def fillzero(dataframe,targetcolumn,targetdict):
    for i in range(len(dataframe["Name"])):
        try:
            if dataframe[targetcolumn][i]==0:
                temp=dataframe["Name"][i].split()
                dataframe[targetcolumn][i]=targetdict[temp[0]+" "+temp[1]]
        except:
            pass
        
fillzero(data,"Power",power_dict)
fillzero(data,"Engine",engine_dict)
fillzero(data,"Mileage",mileage_dict)

data["Power"]=data["Power"].replace(0,np.nan)
data["Engine"]=data["Engine"].replace(0,np.nan)
data["Mileage"]=data["Mileage"].replace(0,np.nan)


#droping the rows with nan

data=data.dropna()

data.isnull().any(axis=0)


from sklearn.model_selection import train_test_split as TTS
from sklearn.preprocessing import LabelEncoder
import statsmodels.formula.api as SM
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


feature=data.iloc[:,:-1].values
label=data.iloc[:,-1].values
le=LabelEncoder()

feature[:,0]=le.fit_transform(feature[:,0])
feature[:,1]=le.fit_transform(feature[:,1])
feature[:,4]=le.fit_transform(feature[:,4])
feature[:,5]=le.fit_transform(feature[:,5])
feature[:,6]=le.fit_transform(feature[:,6])

feature=feature.astype(np.float64)


ss=StandardScaler()
feature=ss.fit_transform(feature)


lr=LinearRegression()

ftrain,ftest,ltrain,ltest=TTS(feature,label,test_size=0.2,random_state=0)

lr.fit(ftrain,ltrain)

predict=lr.predict(ftest)

socre=lr.score(ftest,ltest)
train_score=lr.score(ftrain,ltrain)
Model_score=[]
Model_Name=[]
Model_score.append(np.round((socre * 100),2))
Model_Name.append("Multi Linear")
# Visualization
def model_visual(train_score,test_score,model_name):
    s=[train_score,test_score]
    x_label=["Train","Test"]
    x_pos=np.arange(len(x_label))
    y_pos=np.arange(0,100,10)

    fig,ax=plt.subplots(figsize=(7,7))
    axx=ax.bar(x_pos,s, width=.5,color='r')
    plt.ylabel('Model Score')
    plt.xticks(x_pos,x_label)
    plt.yticks(y_pos)
    plt.title(model_name+" Regression")

    for r in axx:
        height=r.get_height()
        ax.text(r.get_x()+r.get_width()/2,1.02*height,str(height),ha='center', va='bottom')
        plt.savefig(model_name+".jpg")
    plt.show()

model_visual(np.round((train_score * 100),2),np.round((socre * 100),2),"MultiLinear")


#optimize model for the problem
feature=np.append(arr=np.ones((6003,1)).astype(int), values=feature,axis=1)

feature_opt=feature[:,[0,1,2,3,4,5,6,7,8,9,10,11,12]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=feature[:,[0,2,3,4,5,6,7,8,9,10,11,12]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=feature[:,[0,2,3,5,6,7,8,9,10,11,12]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=feature[:,[0,2,3,5,6,8,9,10,11,12]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

#as per the model summary feature name,year and kilometer has less participation in decision making

feature=data.iloc[:,[1,2,4,5,7,8,9,10,11]].values


feature[:,0]=le.fit_transform(feature[:,0])
feature[:,2]=le.fit_transform(feature[:,2])
feature[:,3]=le.fit_transform(feature[:,3])


feature=feature.astype(np.float64)


ss=StandardScaler()

feature=ss.fit_transform(feature)


lr=LinearRegression()

ftrain,ftest,ltrain,ltest=TTS(feature,label,test_size=0.2,random_state=0)

lr.fit(ftrain,ltrain)

predict=lr.predict(ftest)

socre=lr.score(ftest,ltest)

#for randomforest

from sklearn.ensemble import RandomForestRegressor


rfr=RandomForestRegressor(n_estimators=300,random_state=0)

rfr.fit(ftrain,ltrain)

rfpredict=rfr.predict(ftest)

rf_Train_score=rfr.score(ftrain,ltrain)

rf_Test_score=rfr.score(ftest,ltest)


model_visual(np.round(rf_Train_score*100,2),np.round(rf_Test_score*100,2),"RandomForest")
Model_score.append(np.round((rf_Test_score* 100),2))
Model_Name.append("Random Forest")


# applying k fold cross validation


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = rfr, X = ftrain, y = ltrain, cv = 10)

accuracies_test = cross_val_score(estimator = rfr, X = ftest, y = ltest, cv = 10)

print ("mean accuracy is",accuracies.mean())
print ("mean accuracy is",accuracies_test.mean())

#print (accuracies.std())


#applying ridge regression L2

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

ridge=Ridge()

parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]}

ridge_regressor = GridSearchCV(ridge, parameters,scoring='r2', cv=5)

ridge_regressor.fit(ftrain, ltrain)

ridgetrain_score=ridge_regressor.score(ftrain,ltrain)

ridgetest_score=ridge_regressor.score(ftest,ltest)

ridge_regressor.best_params_
ridge_regressor.best_score_

model_visual(np.round(ridgetrain_score*100,2),np.round(ridgetest_score*100,2),"Ridge (L2 Regularization)")
Model_score.append(np.round((ridgetest_score* 100),2))
Model_Name.append("Ridge Regression")

#applying lasso


from sklearn.linear_model import Lasso
from sklearn.pipeline import make_pipeline
lasso = Lasso()
"""
For ridge regression, we introduce GridSearchCV. 
This will allow us to automatically perform 5-fold cross-validation with a range of different regularization parameters in order to find the optimal value of alpha.
"""

parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]}

lasso_regressor = GridSearchCV(lasso, parameters, scoring='r2', cv = 5)

lasso_regressor.fit(ftrain,ltrain)

lassotrain_score=lasso_regressor.score(ftrain,ltrain)

lassotest_score=lasso_regressor.score(ftest,ltest)

lasso_regressor.best_params_
lasso_regressor.best_score_

model_visual(np.round(lassotrain_score*100,2),np.round(lassotest_score*100,2),"Lasso (L1 Regularization)")

Model_score.append(np.round((lassotest_score* 100),2))
Model_Name.append("Lasso Regression")

#applying elasticNet 

from sklearn.linear_model import ElasticNet

elastic_net=ElasticNet()

parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]}

elasticnet_regressor = GridSearchCV(elastic_net, parameters, scoring='r2', cv = 5)

elasticnet_regressor.fit(ftrain,ltrain)

elasticnettrain_score=elasticnet_regressor.score(ftrain,ltrain)

elasticnettest_score=elasticnet_regressor.score(ftest,ltest)

elasticnet_regressor.best_params_
elasticnet_regressor.best_score_

model_visual(np.round(elasticnettrain_score*100,2),np.round(elasticnettest_score*100,2),"ElasticNet")

Model_score.append(np.round((elasticnettest_score* 100),2))
Model_Name.append("ElasticNet Regression")
#xgboost

"""
XGBoost is an implementation of gradient boosted decision trees designed for 
speed and performance that is dominative competitive machine learning.
"""
from xgboost import XGBRegressor

xgb=XGBRegressor()

xgb.fit(ftrain,ltrain)

xgbtrain_score=xgb.score(ftrain,ltrain)

xgbtest_score=xgb.score(ftest,ltest)

model_visual(np.round(xgbtrain_score*100,2),np.round(xgbtest_score*100,2),"XGBoost")
Model_score.append(np.round((xgbtest_score* 100),2))
Model_Name.append("XGBoost")

#comparision visualization


x_pos=np.arange(len(Model_Name))
y_pos=np.arange(0,100,10)

fig,ax=plt.subplots(figsize=(7,7))
axx=ax.bar(x_pos,Model_score, width=.5,color='g')
plt.ylabel('Model Score')
plt.xticks(x_pos,Model_Name)
plt.setp(ax.get_xticklabels(), fontsize=8, rotation=30)
plt.yticks(y_pos)
plt.title("Comparision of All Model")
for r in axx:
    height=r.get_height()
    ax.text(r.get_x()+r.get_width()/2,1.02*height,str(height),ha='center', va='bottom')
    plt.savefig("Comparision.jpg")
plt.show()