
"""
Data preparation, cleaning, pre-processing, cleansing, wrangling. 
Whatever term you choose, they refer to a roughly related set of 
pre-modeling data activities in the machine 
learning, data mining, and data science communities.
"""

import pandas as pd

# Importing the dataset
data = pd.read_csv("cricket_salary_data.csv")
data

features = data.iloc[:,:-1].values
labels = data.iloc[:,-1].values

print(features)
print(labels)


# Taking care of missing data axis = 0 for column wise and axis = 1 for rowwise
from sklearn.preprocessing import Imputer


# Create an imputer object that looks for 'NaN' values, 
# then replaces them with the mean value of the feature by columns (axis=0)
imputer = Imputer( 
                   missing_values = 'NaN', 
                   strategy = 'mean', axis = 0
                 )

# Train the imputer on the features dataset
imputer = imputer.fit(features[:, 1:2])

# Apply the imputer to the features dataset
features[:, 1:2] = imputer.transform(features[:, 1:2])

print(features)



"""
Imputation using the Pandas 

# mark zero values as missing or NaN
data.replace(0, numpy.NaN)


# count the number of NaN values in each column
print(data.isnull().sum())

# drop rows with missing values
data.dropna(inplace=True)

# fill missing values with mean column values
data.fillna(dataset.mean(), inplace=True)


"""


"""
Useless — useless for machine learning algorithms, that is — discrete
Nominal — groups without order — discrete
Binary — either/or — discrete
Ordinal — groups with order — discrete
Count — the number of occurrences — discrete
Time — cyclical numbers with a temporal component — continuous
Interval — positive and/or negative numbers without a temporal component — continuous

Ordinal — convert string labels to integer values 1 through k. Ordinal.
OneHot — one column for each value to compare vs. all other values. Nominal, ordinal.
Binary — convert each integer to binary digits. Each binary digit gets one column. Some info loss but fewer dimensions. Ordinal.
BaseN — Ordinal, Binary, or higher encoding. Nominal, ordinal. Doesn’t add much functionality. Probably avoid.
Hashing — Like OneHot but fewer dimensions, some info loss due to collisions. Nominal, ordinal.
"""


"""
Categorical Data can be converted into Numerical Data using 2 techniques

1. Label Encoding / Integer Encoding

2. One Hot Encoding

"""


"""
LabelEncoder can turn [dog,cat,dog,mouse,cat] into 
[1,2,1,3,2], but then the imposed ordinality means 
that the average of dog and mouse is cat. 
Still there are algorithms like decision trees and 
random forests that can work with categorical variables 
just fine and LabelEncoder can be used to store values 
using less disk space.

One-Hot-Encoding has a the advantage that the result 
is binary rather than ordinal and that everything sits 
in an orthogonal vector space. The disadvantage is that
for high cardinality, the feature space can really blow
up quickly and you start fighting with the curse of 
dimensionality. In these cases, I typically employ 
one-hot-encoding followed by PCA for dimensionality
reduction. I find that the judicious combination of
one-hot plus PCA can seldom be beat by other encoding
schemes. PCA finds the linear overlap, so will naturally
tend to group similar features into the same feature.

"""

# Show ML_Encoding.jpg Image 


# Encoding categorical data

# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

features[:,0] = labelencoder.fit_transform(features[:,0])

print(features)


# OneHotEncoding the labelled data
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[0])

features = onehotencoder.fit_transform(features).toarray()


# Encoding the Dependent Variable
labels = labelencoder.fit_transform(labels)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2)




"""
http://benalexkeen.com/mapping-categorical-data-in-pandas/
Label Encoding:
In fact in pandas.get_dummies there is a parameter i.e. drop_first allows you 
whether to keep or remove the reference 
(whether to keep k or k-1 dummies out of k categorical levels). 
Please note default = False meaning that the reference is not dropped and 
k dummies created out of k categorical levels! 
You set default = True, then it will drop the reference column after encoding.
"""
