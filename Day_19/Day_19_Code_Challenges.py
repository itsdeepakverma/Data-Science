"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

Import the dataset Auto_mpg.txt
Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
Display the Car Name with highest miles per gallon value
Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)

"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as TTS
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv("Auto_mpg.txt",header=None,delim_whitespace=True)

df.columns=["mpg","cylinders","displacement","horsepower","weight","acceleration","model year","origin","car name"]

max_mpg_car=df["car name"][df["mpg"]==df.mpg.max()]

df.isnull().any(axis=0)

df["horsepower"]=df["horsepower"].replace("?",df["horsepower"].value_counts().index[0])

df['horsepower']=df['horsepower'].astype("float64")
df.dtypes


#decision tree

feature=df.iloc[:,1:-1].values
label=df.iloc[:,0].values

dtftrain,dtftest,dtltrain,dtltest=TTS(feature,label,test_size=0.2,random_state=0)

dtr=DecisionTreeRegressor()

dtr.fit(dtftrain,dtltrain)

dtpredict=dtr.predict(dtftest)

df_compareDT=pd.DataFrame({'Actual':dtltest, 'Predicted':dtpredict})  

model_score=dtr.score(dtftest,dtltest)



#randomforest

rfr=RandomForestRegressor(n_estimators=100,random_state=0)

rfr.fit(dtftrain,dtltrain)

rfpredict=rfr.predict(dtftest)

df_compareRF=pd.DataFrame({"Actual":dtltest,"Predicted":rfpredict})


model_scoreRF=rfr.score(dtftest,dtltest)


# prediction for [6,215,100,2630,22.2,80,3]

val=np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)

dt_val_Pre=dtr.predict(val)


rf_val_Pre=rfr.predict(val)

print("Value predicted by DT is {}".format(dt_val_Pre))


print("Value predicted by RF is {}".format(rf_val_Pre))


"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.

"""

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv("PastHires.csv")

mapdict={"Y":1,"N":0}

df["Employed?"]=df["Employed?"].map(mapdict)

df["Top-tier school"]=df["Top-tier school"].map(mapdict)

df["Interned"]=df["Interned"].map(mapdict)

df["Hired"]=df["Hired"].map(mapdict)

df["Level of Education"]=df["Level of Education"].map({"BS":0,"MS":1,"PhD":2})

feature=df.iloc[:,:-1].values
label=df.iloc[:,-1].values

#decision Tree

dtr=DecisionTreeRegressor()

dtr.fit(feature,label)

dt_predict=dtr.predict(feature)

#RandomForest 

rfr=RandomForestRegressor(n_estimators=10)

rfr.fit(feature,label)

rf_predict=rfr.predict(feature)

#prediction for [10, 1, 4, 0, 0, 0]

val_predictDT=dtr.predict([[10,0,4,0,0,0]])


val_predictRF=rfr.predict([[10,0,4,0,0,0]])



