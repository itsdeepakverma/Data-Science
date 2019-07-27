

"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd
import numpy as np

df=pd.read_csv("Foodtruck.csv")

# checking missing values

df.isnull().any(axis=0)

#no missing valuse in the dataset

feature=df.iloc[:,:-1].values
label=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LinearRegression as LR
import matplotlib.pyplot as plt


f_train,f_test,l_train,l_test=TTS(feature,label,test_size=0.2,random_state=0)

lr=LR()
lr.fit(f_train,l_train)

labelpredict=lr.predict(f_test)

#model score

Test_score=lr.score(f_test,l_test)
Train_score=lr.score(f_train,l_train)


#training set graph

plt.scatter(f_train,l_train,color='red')
plt.plot(f_train,lr.predict(f_train), color='blue')

plt.title('training set')
plt.xlabel('profit')
plt.ylabel('population')


# for test set

plt.scatter(f_test,l_test,color='red')
plt.plot(f_test,lr.predict(f_test), color='blue')

plt.title('test set')
plt.xlabel('profit')
plt.ylabel('population')


#prediction for Jaipue outlet

jaipur=[5.073]
jaipur=np.array(jaipur)
jaipur=jaipur.reshape(1,-1)

result=lr.predict(jaipur)

print("prediction for jaipur outlet is {}".format(result))


from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(l_test, labelpredict))  
print('Mean Squared Error:', metrics.mean_squared_error(l_test, labelpredict))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(l_test, labelpredict))) 


print (np.mean(df.values[:,1]))


"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
#First Approch

import pandas as pd

from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LinearRegression as LR
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_csv("Bahubali2_vs_Dangal.csv")

#checking for Nan values
df.isnull().any(axis=0)

feature=df.iloc[:,0:1].values
B_label=df.iloc[:,1].values
D_label=df.iloc[:,2].values

#model for Bahubali2

bf_train,bf_test,bl_train,bl_test=TTS(feature,B_label,test_size=0.2,random_state=0)

lr=LR()

lr.fit(bf_train,bl_train)

predictB=lr.predict(bf_test)

Bday=[10]
Bday=np.array(Bday)
Bday=Bday.reshape(1,-1)
B10days=lr.predict(Bday)

#plotting training set

plt.scatter(bf_train,bl_train,color='red')
plt.plot(bf_train,lr.predict(bf_train), color='blue')

plt.title('training set')
plt.xlabel('Days')
plt.ylabel('Collection')

#plotting testing set

plt.scatter(bf_test,bl_test,color='red')
plt.plot(bf_test,lr.predict(bf_test), color='blue')

plt.title('testing set')
plt.xlabel('Days')
plt.ylabel('Collection')


#model for Dangal

df_train,df_test,dl_train,dl_test=TTS(feature,D_label,test_size=0.2,random_state=0)

lr1=LR()
lr1.fit(df_train,df_train)

predictD=lr1.predict(df_test)

Dday=[10]
Dday=np.array(Dday)
Dday=Dday.reshape(1,-1)

D10days=lr1.predict(Dday)

if(B10days>D10days):
    print("Bahubali will collect more and collection is {}".format(B10days))
else:
    print("Dangal will collect more and collection is {}".format(D10days))

#plotting training set

plt.scatter(df_train,dl_train,color='red')
plt.plot(df_train,lr.predict(df_train), color='blue')

plt.title('training set')
plt.xlabel('Days')
plt.ylabel('Collection')

#plotting testing set

plt.scatter(df_test,dl_test,color='red')
plt.plot(df_test,lr.predict(df_test), color='blue')

plt.title('testing set')
plt.xlabel('Days')
plt.ylabel('Collection')



#second approch
    
S_feature=df.iloc[:,0:1].values
S_label=df.iloc[:,1:].values

S_feature_train,S_feature_test,S_label_train,S_label_test=TTS(S_feature,S_label,test_size=0.2,random_state=0)

Slr=LR()

Slr.fit(S_feature_train,S_label_train)

Spredict=Slr.predict(S_feature_test)
    
#10 day collection

DB10day=Slr.predict(Dday)

if DB10day[0][0]>DB10day[0][1]:
    print("Bahubali will have more collection {}".format(DB10day[0][0]))
else:
    print("Dangal will have more collection {}".format(DB10day[0][1]))

    
"""

Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.preprocessing import StandardScaler
import numpy as np

df=pd.read_csv("University_data.csv")

#check for missing value

df.isnull().any(axis=0)

features=df.iloc[:,:-1].values

label=df.iloc[:,-1].values

uni_name=LabelEncoder()

features[:,0]=uni_name.fit_transform(features[:,0])

uni_nameOHE=OneHotEncoder(categorical_features=[0])

features=uni_nameOHE.fit_transform(features).toarray()

#droping first column

features=features[:,1:]

#scalling


ss=StandardScaler()

features=ss.fit_transform(features)

#spliting

f_train,f_test,l_train,l_test=TTS(features,label,test_size=0.2,random_state=0)

lr=LR()

lr.fit(f_train,l_train)

Label_predict=lr.predict(f_test)

result_Compare=pd.DataFrame({"Actual":l_test,"Predicted":Label_predict})

#precition for [cabrini,300,4,3.5,8.0,1]

l=uni_name.transform(["Cabrini"])
lcode=uni_nameOHE.transform(l.reshape(1,1)).toarray()

lcode=lcode[:,1:]

x=[lcode[0][0],lcode[0][1],lcode[0][2],lcode[0][3],350,4,3.5,9.0,1]
x=np.array(x)
x=x.reshape(1,-1)
x=ss.transform(x)

xpredict=lr.predict(x)








