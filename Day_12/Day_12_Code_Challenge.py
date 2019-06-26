"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
import pandas as pd


df=pd.read_csv("training_titanic.csv")

df.isnull().any(axis=0)

df[df.isnull().any(axis=1)]

df_nw=df.dropna()

df_fill=df.fillna(df.mean())

df_fill.isnull().any(axis=0)


a=df_fill['Survived'].value_counts()
print("No of person Survived is={} \n and NO of person Dead is= {}".format(a[0],a[1]))

b=df_fill['Survived'].value_counts(normalize=True)
print("No of % person Survived is={} and NO of % person Dead is= {}".format(b[0]*100,b[1]*100))


df_fill['Sex'].value_counts()

male_sur=df_fill[df_fill['Sex']=='male']['Survived'].value_counts(normalize=True)
print("No of % male Survived is={} and NO of % male Dead is= {}".format(male_sur[0]*100,male_sur[1]*100))
female_sur=df_fill[df_fill['Sex']=='female']['Survived'].value_counts(normalize=True)
print("No of % female Survived is={} and NO of % female Dead is= {}".format(female_sur[0]*100,female_sur[1]*100))

df_fill['Child']=df_fill['Age'].apply(lambda x:1 if x<18 else 0)

child_sur=df_fill[df_fill['Child']==1]['Survived'].value_counts(normalize=True)

print("No of % elder Survived is={} and NO of % child Survived is= {}".format(child_sur[0]*100,child_sur[1]*100))


"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import pandas as pd
import numpy as np

df=pd.read_csv("Automobile.csv")
df[df.isnull().any(axis=1)]

df_fill=df.fillna(df.mean())
df_fill[df_fill.isnull().any(axis=1)]

nparr=np.asarray(df_fill['price'])
print(type(nparr))

print("minimum price={}".format(nparr.min()))

print("max price={}".format(nparr.max()))

print("mean price={}".format(nparr.mean()))

print("standard Deviation ={}".format(nparr.std()))



"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""
import pandas as pd
import numpy as np
import re
import csv

with open("thanksgiving.csv",'rt') as file:
    print(file)  

df=pd.read_csv("thanksgiving.csv",encoding='cp1252')


columns=list(df.columns)

column_Name=[x for x in range(0,len(columns))]

df.columns=column_Name

columns_ref = dict(zip(column_Name, columns))



df = df[df[1] == "Yes"]


df[df.isnull().any(axis=1)]

df=df.replace(np.nan,"Missing")

result_state=df.groupby(64)[2].value_counts().unstack().fillna(0)

result_income=df.groupby(63)[2].value_counts().unstack().fillna(0)

result_area=df.groupby(60)[2].value_counts().unstack().fillna(0)

result_suaceincome=df.groupby(8)[63].value_counts().unstack().fillna(0)

df[62]=df[62].apply(lambda x: "M" if x=="Male" else "F")

df[63] = df[63].replace(['Prefer not to answer', 'mising'],['0','0'])

regex = re.compile("\d+\W*\d+")

def income_filter(value):
        value = regex.findall(value)
        value = [int(x.replace(",", "")) for x in value]
        if len(value)==0:
            return 0
        else:
            return sum(value)/(len(value))

df[63] = df[63].apply(income_filter)


result_sauceAvgIncome=df.groupby(8)[63].mean()


#ploting

sauceAvgIncome=result_sauceAvgIncome.plot.bar()

sauce_compare=result_sauceAvgIncome.iloc[[0,1]]

sauce_compare_plot=sauce_compare.plot.pie(autopct="%1.1f%%")

#Do people in Suburban areas eat more Tofurkey than people in Rural areas?
 
compare_area=result_area.iloc[[1,2],[6]]   

compare_areaplot=compare_area.plot.bar()

#Is there a correlation between praying on Thanksgiving and income?
    
prayer=df.groupby(51)[63].value_counts().unstack().fillna(0).iloc[[1,2]]

prayer_plot=prayer.plot.bar()



"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght?
   Predict and print it
6. Predict a relation between the customer and customer care service that 
whether churned customer have shown their concern to inform the customer care 
service about their problem or not
7. In which area code the international plan is most availed?
"""
import pandas as pd
import matplotlib.pylab as plt

df=pd.read_csv("Telecom_churn.csv")


#count of Churned customer availing both voice mail plan and international plan schema

churn_count=df[(df["international plan"]=="yes") & (df["voice mail plan"]=="yes")]

churn_count=len(churn_count[churn_count["churn"]==True])


#Total charges for international calls made by churned and non-churned customer and visualize it

international_charge=df.groupby('churn')['total intl charge'].sum()

international_charge.plot.bar()

#Predict the state having highest night call minutes for churned customer

max_night=df["state"][df["total night minutes"].max()]

#Visualize -  a. the most popular call type among churned user
#    b. the minimum charges among all call type among churned user

popular_call=df[["total day calls","total eve calls","total night calls","total intl calls"]][df['churn']==True]
popular_call.sum().plot.bar(color='red')

min_charge=df[["total day charge","total eve charge","total night charge","total intl charge"]][df['churn']==True]
min_charge.sum().plot.bar(color='red')


#Which category of customer having maximum account lenght? Predict and print it

max_length=df['churn'][df['account length'].max()]

if max_length:
    print("churn has max length account")
else:
    print("not churn has max lenght account")
    
#Predict a relation between the customer and customer care service that 
#whether churned customer have shown their concern to inform the customer care 
#service about their problem or not
    
    
customer_care=df.groupby('churn')['customer service calls'].sum()

customer_care.plot.pie(autopct="%1.1f")

#In which area code the international plan is most availed?

most_intl_plan=df.groupby("area code")["international plan"].value_counts().unstack()

most_intl_plan.plot.bar()