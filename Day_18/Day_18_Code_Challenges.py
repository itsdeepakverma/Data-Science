"""


Q1. (Create a program that fulfills the following specification.)
affairs.csv


Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

    Now, perform Classification using logistic regression and check your model accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as categorical variables. Careful from dummy variable trap for both!!

    What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood of having an affair.)

    Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.

Optional

    Build an optimum model, observe all the coefficients.


--------------------------
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import confusion_matrix
data=pd.read_csv("affairs.csv")

feature=data.iloc[:,:-1].values
label=data.iloc[:,-1].values

wocc_OHE=OneHotEncoder(categorical_features=[6])

feature=wocc_OHE.fit_transform(feature).toarray()

feature=feature[:,1:]

hocc_OHE=OneHotEncoder(categorical_features=[11])

feature=hocc_OHE.fit_transform(feature).toarray()

feature=feature[:,1:]

ftrain,ftest,ltrain,ltest=tts(feature,label,test_size=0.2,random_state=0)

lr=LogisticRegression(random_state=0)

lr.fit(ftrain,ltrain)

predictlabel=lr.predict(ftest)

cm=confusion_matrix(ltest,predictlabel)

model_score=lr.score(ftest,ltest)


#prediction for data in the table

val=np.array([3,25,3,1,4,16,4,2]).reshape(1,-1)

val=wocc_OHE.transform(val).toarray()
val=val[:,1:]

val=hocc_OHE.transform(val).toarray()

val=val[:,1:]

val_predict=lr.predict(val)


#optional


import statsmodels.formula.api as sm

feature = np.append(arr = np.ones((feature.shape[0], 1)).astype(int), 
                     values = feature, axis = 1)

f_opt=feature[:,[0,1,2,3,4,5,6,7,8]]
regressor_OLS=sm.OLS(label,f_opt).fit()
regressor_OLS.summary()

f_opt=feature[:,[0,1,2,3,5,6,7,8]]
regressor_OLS=sm.OLS(label,f_opt).fit()
regressor_OLS.summary()

f_opt=feature[:,[0,1,2,3,5,6,7]]
regressor_OLS=sm.OLS(label,f_opt).fit()
regressor_OLS.summary()




"""
Q2. (Create a program that fulfills the following specification.)
mushrooms.csv

Import mushrooms.csv file

This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one.

 

Attribute Information:

classes: edible=e, poisonous=p (outcome)

cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s

cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s

cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y

 

bruises: bruises=t, no=f

 

odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s

 

gill-attachment: attached=a,descending=d,free=f,notched=n

 

gill-spacing: close=c,crowded=w,distant=d

 

gill-size: broad=b,narrow=n\

 

gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,

green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y

 

stalk-shape: enlarging=e,tapering=t

 

stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?

 

stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s

 

stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s

 

stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

 

stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

 

veil-type: partial=p,universal=u

 

veil-color: brown=n,orange=o,white=w,yellow=y

ring-number: none=n,one=o,two=t

 

ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z

 

spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y

 

population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y

 

habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d

    Perform Classification on the given dataset to predict if the mushroom is edible or poisonous w.r.t. it’s different attributes.

(you can perform on habitat, population and odor as the predictors)

    Check accuracy of the model.



"""


import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


data=pd.read_csv("mushrooms.csv")

feature=data.iloc[:,list(data.columns).index('odor'):list(data.columns).index('odor')+1]

feature[data.columns[list(data.columns).index('habitat')]]=data.iloc[:,list(data.columns).index('habitat'):list(data.columns).index('habitat')+1]

feature[data.columns[list(data.columns).index('population')]]=data.iloc[:,list(data.columns).index('population'):list(data.columns).index('population')+1]

feature=feature.values

label=data.iloc[:,list(data.columns).index('class')].values


odor=LabelEncoder()
habitat=LabelEncoder()
population=LabelEncoder()


feature[:,0]=odor.fit_transform(feature[:,0])

feature[:,1]=habitat.fit_transform(feature[:,1])

feature[:,2]=population.fit_transform(feature[:,2])


odorOHE=OneHotEncoder(categorical_features=[0])

feature=odorOHE.fit_transform(feature).toarray()

habitatOHE=OneHotEncoder(categorical_features=[9])

feature=habitatOHE.fit_transform(feature).toarray()

populationOHE=OneHotEncoder(categorical_features=[16])

feature=populationOHE.fit_transform(feature).toarray()

from sklearn.model_selection import train_test_split as TTS


ftrain,ftest,ltrain,ltest=TTS(feature,label,test_size=0.2,random_state=0)


from sklearn.neighbors import KNeighborsClassifier

classifier=KNeighborsClassifier(n_neighbors=5,p=2)

classifier.fit(ftrain,ltrain)


pred=classifier.predict(ftest)

from sklearn.metrics import confusion_matrix

cm=confusion_matrix(ltest,pred)

model_score=classifier.score(ftest,ltest)



"""
*****
Classification Code Challenge
*****

tree_addhealth.csv

Q1. (Create a program that fulfills the following specification.)

For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set, an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the University of North Carolina’s Carolina Population Center, http://www.cpc.unc.edu/projects/addhealth/data.

Import tree_addhealth.csv

 

The attributes are:

 

BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)

Explanatory Variables:

Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale

 

Build a classification tree model evaluating if an adolescent would smoke regularly or not
based on: gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, 
alcohol use, alcohol problems, marijuana use, cocaine use, inhalant use, availability of 
cigarettes in the home, depression, and self-esteem.

Build a classification tree model evaluation if an adolescent gets expelled or not from school based on their Gender and violent behavior.
Use random forest in relation to regular smokers as a target and explanatory variable specifically with Hispanic, White, Black, Native American and Asian.

(Please make confusion matrix and also check accuracy score for each and every section)
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split as TTS
from sklearn.metrics import confusion_matrix, accuracy_score


df=pd.read_csv("tree_addhealth.csv")



#for missing valuse


df.isnull().any(axis=0)

df=df.fillna(df.mean())

df=df.iloc[:-1,:]

label=df["TREG1"].values
feature=df[["BIO_SEX","age","HISPANIC","WHITE","BLACK","NAMERICAN","ASIAN","ALCEVR1",\
            "ALCPROBS1","marever1","cocever1","inhever1","cigavail","DEP1","ESTEEM1"]].values


FTRAIN,FTEST,LTRAIN,LTEST=TTS(feature,label,test_size=0.2,random_state=0)

classifier=DecisionTreeClassifier(criterion="entropy",random_state=0)
classifier.fit(FTRAIN,LTRAIN)
predict=classifier.predict(FTEST)

model_acc=accuracy_score(LTEST,predict)



#Build a classification tree model evaluation if an adolescent gets expelled or not
# from school based on their Gender and violent behavior.


feature1 = df[["BIO_SEX","VIOL1"]].values
label1 = df["EXPEL1"].values

# Splitting the Data into Test and Train
ftrain1,ftest1,ltrain1,ltest1 = TTS(feature1,label1,test_size=.2,random_state=0)

# Applying DecisionTreeClassifier
classifier.fit(ftrain1,ltrain1)
predict1 = classifier.predict(ftest1)

# Building Confusion Matrix
cm = confusion_matrix(ltest1,predict1)

# Getting Accuracy Score of the Mode

model_acc1 = accuracy_score(ltest1,predict1)

print ("Accuracy Score of the Model : "+str(round(model_acc1*100,2))+"%")


#Use random forest in relation to regular smokers as a target and explanatory 
#variable specifically with Hispanic, White, Black, Native American and Asian.


feature2 = df[['WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN']].values
label2 = df["TREG1"].values

ftrain2,ftest2,ltrain2,ltest2 = TTS(feature2,label2,test_size=.2,random_state=0)

classifier1 = RandomForestClassifier(n_estimators=10,criterion="entropy", 
                                random_state=0)
classifier1.fit(ftrain2,ltrain2)
predict2 = classifier1.predict(ftest2)


cm2 = confusion_matrix(predict2,ltest2)

model_acc2 = accuracy_score(ltest2,predict2)

print ("Accuracy Score of the Model : "+str(round(model_acc2*100,2))+"%")


