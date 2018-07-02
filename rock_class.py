#!/usr/bin/python
import pandas as pd 
data = pd.read_csv("training_data.csv")
#data =  pd.Series(['a', 'a', 'b', 'c'])

print data.describe()
#data.boxplot()
print data.cov()

#print data(1,3)
print data.PE.quantile(0.5)   ##column name is case sensitive 
print data.head()
#data=data.drop('Well Name',1) #1 is axis 
#print data.head()
test_data = data[data['Well Name'] == 'SHANKLE']  #select row 
data = data[data['Well Name'] != 'SHANKLE']  #drop row
features = ['GR', 'ILD_log10', 'DeltaPHI','PHIND','PE','NM_M', 'RELPOS']
feature_vectors = data[features]  ##type(facies_labels) ==class 'pandas.core.series.Series
facies_labels = data['Facies']
print type(feature_vectors)
print type(facies_labels)
data.Formation.unique()
data['Well Name'].unique()
#data[:3]  #keep top 3 row
#data[:-3] #drop last 3 row 


#plot it. 
print type(data)
data.plot.scatter(x='GR', y='ILD_log10') # in newer version of dataframe. 

