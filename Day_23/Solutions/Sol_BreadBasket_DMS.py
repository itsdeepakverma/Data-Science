# -*- coding: utf-8 -*-
"""Associations2.ipynb
"""

from apyori import apriori

import pandas as pd
dataset=pd.read_csv('BreadBasket_DMS.csv')

dataset.shape

dataset.head(20)

print("List of Items sold at the Bakery:")
print("Total Items: ",len(dataset.Item.unique()))
print("-"*15)
for i in dataset.Item.unique():
    print(i)

"""**TOP 15 SELLING PRODUCTS **"""

import matplotlib.pyplot as plt
plt.figure(1, figsize=(10,10))
dataset['Item'].value_counts().head(15).plot.pie(autopct="%1.1f%%")
plt.show()

x=set(list(dataset['Transaction']))
list1=[]
for i in x:
  y=list(dataset.loc[dataset['Transaction'] ==i , 'Item'])
  list1.append(y)

print list1




#use apriori class and convert it into list 
rules= apriori(list1,min_support=0.0025, min_confidence=0.2, min_length=2, min_lift=3)
results = list(rules)

len(results)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")