
"""
Ridge Regression and Lasso
This notebook explores ridge regression and lasso. These alternative linear fitting techniques can improve a model's performance and interpretability.
"""
"""
Part 2 Discussions
"""


#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Data Analysis
ddata = pd.read_csv("Advertising.csv")
ddata.head()

#Drop the first column

ddata.drop(['Unnamed: 0'], axis=1, inplace=True)

print (ddata.head())

print (ddata.columns)

#lets plot few visuals
def scatter_plot(feature, target):
    plt.scatter(ddata[feature], ddata[target], c='black')
    plt.xlabel("Money spent on {} ads ($)".format(feature))
    plt.ylabel("Sales ($k)")
    plt.show()

scatter_plot('TV', 'sales')
scatter_plot('radio', 'sales')
scatter_plot('newspaper', 'sales')

#Lets build the models now
#Multiple Linear Regression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

dfeatures = ddata.drop(['sales'], axis=1) #drop the target to get the features
dlabels = ddata['sales'].values.reshape(-1,1) #choose the target

lin_reg = LinearRegression()

MSEs = cross_val_score(lin_reg, dfeatures, dlabels, scoring='neg_mean_squared_error', cv=5)

mean_MSE = np.mean(MSEs)

print(mean_MSE)


#Ridge Regression
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

#alpha = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]

ridge = Ridge()

parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]}

ridge_regressor = GridSearchCV(ridge, parameters,scoring='neg_mean_squared_error', cv=5)

ridge_regressor.fit(dfeatures, dlabels)

r=ridge_regressor.predict(dfeatures)
ridge_regressor.score(dfeatures,dlabels)
ridge_regressor.best_params_
ridge_regressor.best_score_


#Lasso
from sklearn.linear_model import Lasso
from sklearn.pipeline import make_pipeline
lasso = Lasso()
"""
For ridge regression, we introduce GridSearchCV. 
This will allow us to automatically perform 5-fold cross-validation with a range of different regularization parameters in order to find the optimal value of alpha.
"""

parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]}

lasso_regressor = GridSearchCV(lasso, parameters, scoring='neg_mean_squared_error', cv = 5)

lasso_regressor.fit(dfeatures, dlabels)

lasso_regressor.best_params_
lasso_regressor.best_score_

model2=make_pipeline(dfeatures,Ridge(alpha=0.1))

model2.fit(dfeatures,dlabels)

#Version 2

# Standardize x_train
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(dfeatures)
dfeatures = scaler.transform(dfeatures)

from sklearn.linear_model import Ridge, Lasso

# Fit x_train and y_train
ridge = Ridge().fit(dfeatures, dlabels)
lasso = Lasso().fit(dfeatures, dlabels)


# Print results for both Ridge and Lasso
print('Ridge: ', ridge.coef_)
print('Lasso:', lasso.coef_)

print('Ridge: ', ridge.coef_)
print('Lasso:', lasso.coef_)



