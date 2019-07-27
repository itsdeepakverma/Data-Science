"""
Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

Import the dataset Auto_mpg.txt

Give the column names as "mpg", "cylinders", "displacement","horsepower",
"weight","acceleration", "model year", "origin", "car name" respectively

Display the Car Name with highest miles per gallon value

Build the Decision Tree and Random Forest models and find out which of the 
two is more accurate in predicting the MPG value

Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs 
with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 
horsepower engine giving it a displacement of about 215. 

(Give the prediction from both the models)

file name "auto_mpg.py"

"""

# city-cycle fuel consumption in miles per gallon (Label)

import pandas as pd

# column names
cols = ["mpg","cylinders","displacement","horsepower","weight","acceleration",
        "model year","origin","car name"]

# Reading data from text file
data = pd.read_csv("Auto_mpg.txt",header=None,delim_whitespace=True,names=cols)

# Fill the missing values given by '?'
data["horsepower"][data["horsepower"]=='?'] = data["horsepower"].mode()[0]

# Convert from object to float64
data["horsepower"] = data["horsepower"].astype('float64')  

# Car name with highest MPG
car = data["car name"][data["mpg"]==data.mpg.max()]

# Dependent and Independent variables
features = data.iloc[:,1:-1].values
labels = data.iloc[:,0].values

# Splitting dataset to test and train
from sklearn.cross_validation import train_test_split as TTS
ftrain, ftest, ltrain, ltest = TTS(features,labels,test_size=0.2,random_state=0)

# Scaling all the features
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
ftrain =sc.fit_transform(ftrain)
ftest = sc.transform(ftest)

# Decision Tree Model
from sklearn.tree import DecisionTreeRegressor

D_reg = DecisionTreeRegressor(random_state=0)
D_reg.fit(ftrain,ltrain)
D_Pred = D_reg.predict(ftest)
D_Score = D_reg.score(ftest,ltest)

# Random Forest Model
from sklearn.ensemble import RandomForestRegressor

RF_reg = RandomForestRegressor(n_estimators=10,random_state=0)
RF_reg.fit(ftrain,ltrain)
RF_Pred = RF_reg.predict(ftest)
RF_Score = RF_reg.score(ftest,ltest)

# individual prediction using  both (6,215,100,2630,22.2,80,3)
import numpy as np
val = np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)
val = sc.transform(val)

D_car_pred = D_reg.predict(val)
RF_car_pred = RF_reg.predict(val)

print ("\n")
print ("Prediction from Decision Tree : "+str(D_car_pred[0]))
print ("Prediction from Random Forest : "+str(round(RF_car_pred[0],2)))
print ("\n")