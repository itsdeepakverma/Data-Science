# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:07:35 2019

@author: User
"""

"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

import pandas as pd

df = pd.read_csv("kc_house_data.csv")
df["date"] = df["date"].apply(lambda x: x[:4])

if any(df.isnull().any()):
    df = df.fillna(method="bfill")

for i in df:
    if df[i].dtype == object:
        df[i] = df[i].astype(int)

features = df.drop(["id","price"],axis=1).values
labels = df["price"].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)


from sklearn.model_selection import train_test_split as TTS
f_train,f_test, l_train, l_test = TTS(features, labels, test_size=0.3, random_state=0)

model_scores = {}

from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators=50, random_state=0)
reg.fit(f_train, l_train)

s1 = reg.score(f_train, l_train)
s2 = reg.score(f_test, l_test)

model_scores["RandomForest(Train,Test)"] = [s1, s2]

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(f_train, l_train)

s1 = reg.score(f_train, l_train)
s2 = reg.score(f_test, l_test)

model_scores["LinearRegression(Train,Test)"] = [s1, s2]


from sklearn.linear_model import Ridge
lm_ridge = Ridge()
lm_ridge.fit(f_train,l_train)
pred = lm_ridge.predict(f_test)

s1 = lm_ridge.score(f_train, l_train)
s2 = lm_ridge.score(f_test, l_test)

model_scores["Ridge(Train,Test)"] = [s1, s2]


from sklearn.linear_model import Lasso
lm_lasso = Lasso() 
lm_lasso.fit(f_train, l_train)

s1 = lm_lasso.score(f_train, l_train)
s2 = lm_lasso.score(f_test, l_test)

model_scores["Lasso(Train,Test)"] = [s1, s2]
