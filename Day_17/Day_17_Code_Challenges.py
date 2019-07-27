"""

Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

"""
import pandas as pd
import numpy as np

df=pd.read_csv("Female_Stats.csv")

features=df.iloc[:,1:]
labels=df.iloc[:,0]

import statsmodels.formula.api as sm
features=np.append(arr=np.ones((214,1)).astype(int),values=features,axis=1)

features_opt=features[:,[0,1,2]]
regressor_OLS=sm.OLS(labels,features_opt).fit()
regressor_OLS.summary()

print(regressor_OLS.params)

#Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not

#as per observation of summary p values for both independent variable are less than .05 so both significant for dependent variable

#When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
#When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

#Answer are the cofe values in model summary that can be get by params

"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv("bluegills.csv")

features=dataset.iloc[:,0:1].values
labels=dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split as tts

ftrain,ftest,ltrain,ltest=tts(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression 
lr=LinearRegression()

lr.fit(ftrain,ltrain)

predictvalues=lr.predict(ftest)
print("length of 5 year old fish {}".format(lr.predict((np.array([5])).reshape(1,-1))))


#ploting

plt.scatter(ftest,ltest)
plt.plot(ftest,lr.predict(ftest),color="red")


#polynomial


from sklearn.preprocessing import PolynomialFeatures

poly=PolynomialFeatures(degree=4)
poly_features=poly.fit_transform(features)

pftrain,pftest,pltrain,pltest=tts(poly_features,labels,test_size=0.2,random_state=0)

lr1=LinearRegression()
lr1.fit(pftrain,pltrain)

polypredict=lr1.predict(pftest)

#plotting

plt.scatter(ftrain,ltrain)
plt.plot(ftrain,lr1.predict(poly.fit_transform(ftrain)),color='red')


print("length of 5 year old fish {}".format(lr1.predict(poly.fit_transform((np.array([5])).reshape(1,-1)))))




"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as SST
from sklearn.linear_model import LinearRegression as LR

df=pd.read_csv("iq_size.csv")

feature=df.iloc[:,1:].values
label=df.iloc[:,0].values

f_train,f_test,l_train,l_test=SST(feature,label,test_size=0.2,random_state=0)

lr=LR()
lr.fit(f_train,l_train)

predictlabel=lr.predict(f_test)

x=[90,70,150]
a=np.array(x)
a=a.reshape(1,-1)


print("IQ lavel for given attribute is {}".format(lr.predict(a)))

#optimize model for the problem

import statsmodels.formula.api as SM

features=np.append(arr=np.ones((38,1)).astype(int), values=feature,axis=1)

feature_opt=features[:,[0,1,2,3]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[0,1,2]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[1,2]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[1]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

#brain more important as compare with other independent variables for predicting IQ
#as per OLS Model Summary



