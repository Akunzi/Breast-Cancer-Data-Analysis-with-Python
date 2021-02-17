import pandas as pd
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt


#IMPORTING DATA-SET
df = pd.read_csv('Breastcancer.csv') 

BreastCancerdata = df.head()

print('IMPORTING DATA-SET\n\n',BreastCancerdata, '\n') 


#CHECKING ACCURACY OF DATA TYPES
informationdatatype = df.dtypes

print ('CHECKING ACCURACY OF DATA TYPES\n\n',informationdatatype, '\n')


#CHECKING STATISTICAL SUMMARY 
statisticalsummary = df.describe()

print ('CHECKING STATISTICAL SUMMARY\n\n',statisticalsummary, '\n') 


#CHECKING DATA-SET INFORMATION 
informationdataset = df.info

print ('CHECKING DATA-SET INFORMATION\n\n',informationdataset, '\n') 


#CORRECT THE INCORRECT DATATYPES 
#df["radius_mean"] = df["radius_mean"].astype("int")


#NORMALIZING DATA-SET 
#df["radius_mean"] = df["radius_mean"] / df["radius_mean"].max() 
#print(df["radius_mean"]) 
df = df / df.max() 
print(df)


#SAVING DATAFRAME TO CSV FILE
#df.to_csv('Cancer.csv', encoding ='utf-8', index = False) 


#TURNING CATEGORICAL VARIABLES INTO QUANTITATIVE VARIABLES 
dums = pd.get_dummies(df['diagnosis'])
#print(dums)

#DESCRIPTIVE ANALYSIS USING VALUE_COUNTS METHOD 
des_texture_mean = df['texture_mean'].value_counts()
print(des_texture_mean)


#sns.boxplot(x= 'id', y= 'texture_mean', data= df)

#print(sns.get_texture_mean())
print(matplotlib.__version__)
sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()