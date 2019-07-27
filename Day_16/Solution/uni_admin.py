
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
import numpy as np

dataset = pd.read_csv("University_data.csv")

features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1:].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

features = features[:, 1:]

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

Pred = regressor.predict(features_test)

x = [0,0,1,0,300,5,5.5,9.6,1]
x = np.array(x)
regressor.predict(x.reshape(1, -1))

# University(Beaver,Albany,Cabrini,Maryland,Alaska Methodist University)

le = labelencoder.transform(['Cabrini'])
ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
x = [ohe[0][1],ohe[0][2],ohe[0][3],ohe[0][4],300,5,5.5,9.6,1]
x = np.array(x)
regressor.predict(x.reshape(1, -1))

regressor.score(features_train,labels_train)
regressor.score(features_test,labels_test)
