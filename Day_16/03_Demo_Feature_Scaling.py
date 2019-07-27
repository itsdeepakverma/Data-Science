
"""
Why Scaling ?

Most of the times, your dataset will contain features highly varying in magnitudes, 
units and range. But since, most of the machine learning algorithms use 
Eucledian distance between two data points in their computations, this is a problem.

If left alone, these algorithms only take in the magnitude of features neglecting the units. 
The results would vary greatly between different units, 5kg and 5000gms. 
The features with high magnitudes will weigh in a lot more in the distance 
calculations than features with low magnitudes.

To supress this effect, we need to bring all features to the same level of magnitudes. 
This can be acheived by scaling.


How to Scale Features ?

There are four common methods to perform Feature Scaling.

1. Standardisation ( Z Score ): 
    Standardisation replaces the values by their Z scores.
        z=(x−μ/σ)
        where μ is the mean (average)
        σ is the standard deviation from the mean
    
    The result of standardization (or Z-score ) is that the features 
    will be rescaled so that they’ll have the properties of a standard normal 
    distribution with μ=0 and σ=1    
    Standardizing the features means that they are centered around 0 
    with a standard deviation of +1 and -1


2. Mean Normalisation:
   x(dash) = x - mean(x) / max(x) - min(x) 
   
   This distribution will have values between -1 and 1 with μ=0.

     
3. Min-Max Scaling(Normalisation):
    
    x(norm) = x − min(x) / max(x) − min(x)

    This scaling brings the value between 0 and 1.
    http://sebastianraschka.com/Articles/2014_about_feature_scaling.html#about-min-max-scaling
    
4. Unit Vector:
    x(dash) = x / ||x||
    Unit Vector techniques produces values of range [0,1]

Ref:
    
https://medium.com/greyatom/why-how-and-when-to-scale-your-features-4b30ab09db5e


When to Scale ?

Some examples of algorithms where feature scaling matters are:

    k-nearest neighbors with an Euclidean distance measure is sensitive to 
    magnitudes and hence should be scaled for all features to weigh in equally.
    
    Scaling is critical, while performing Principal Component Analysis(PCA). 
    PCA tries to get the features with maximum variance and the variance is high 
    for high magnitude features. This skews the PCA towards high magnitude features.
    
    We can speed up gradient descent by scaling. 
    This is because θ will descend quickly on small ranges and slowly on large ranges, 
    and so will oscillate inefficiently down to the optimum when the variables are very uneven.
    
    Tree based models are not distance based models and can handle varying ranges of features. 
    Hence, Scaling is not required while modelling trees.
    
    Algorithms like Linear Discriminant Analysis(LDA), Naive Bayes are by design 
    equipped to handle this and gives weights to the features accordingly. 
    Performing a features scaling in these algorithms may not have much effect.


"""

# Using Vanilla Python

x = [1,4,5,6,6,2,3]
mean = sum(x)/len(x)
std_dev = (1/len(x) * sum([ (x_i - mean)**2 for x_i in x]))**0.5

# Standardization or z score normalisation
z_scores = [(x_i - mean)/std_dev for x_i in x]

# Min-Max scaling
minmax = [(x_i - min(x)) / (max(x) - min(x)) for x_i in x]



# Using NumPy
import numpy as np


# Standardization or z score normalisation
x_np = np.asarray(x)
z_scores_np = (x_np - x_np.mean()) / x_np.std()

# Min-Max scaling
np_minmax = (x_np - x_np.min()) / (x_np.max() - x_np.min())



# Using scikit learn 

from sklearn.preprocessing import MinMaxScaler

#scaler = MinMaxScaler()
#scaler.fit(X_train)

#X_train = scaler.transform(X_train)
#X_test = scaler.transform(X_test)



from sklearn.preprocessing import StandardScaler

#scaler = StandardScaler()
#scaler.fit(X_train)

#X_train = scaler.transform(X_train)
#X_test = scaler.transform(X_test)





