
import numpy as np

# Simultaneous Assignment


print (type(X))
print (type(y))

print (X)
print (y)


# train_test_split splits arrays or matrices into random train and test subsets. 
# That means that everytime you run it without specifying random_state, 
# you will get a different result, this is expected behavior. 



#from sklearn.cross_validation import train_test_split
#Deprecated since version 0.18: This module will be removed in 0.20. 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

print (X_train)
print (X_test)

print (y_train)
print (y_test)



# If you use random_state=some_number, 
# then you can guarantee that your split will be always the same. 
# This is useful if you want reproducible results, 
# I would say, set the random_state to some fixed number while you test stuff, 
# but then remove it in production if you need a random (and not a fixed) split.



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print (X_train)
print (X_test)

print (y_train)
print (y_test)


# This result would be different from last one, but if you run it again and again it will be same

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100)

print (X_train)
print (X_test)

print (y_train)
print (y_test)





"""
Steps in Data Preprocessing

Step 1 : Import the libraries
Step 2 : Import the data-set
Step 3 : Check out the missing values - imputation using sklearn, pandas
Step 4 : Label encoding - categorical data using LabelEncoder, cat.code (category)
Step 5 : order issue - onehotencoding (dummy encoding) - OneHotEncoder, get_dummies
Step 6 : Splitting the data-set into Training and Test Set
Step 7 : Feature Scaling

"""
