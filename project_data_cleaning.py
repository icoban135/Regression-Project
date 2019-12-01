import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv(r'C:\Users\Ibrahim\Desktop\Regression project csv\pek-sha.csv')

'''Departure Date and Time Seperation'''

departureDate = []
departureTime = []


for i in range(0, len(df.departureDate)):
    date_time = df.departureDate[i].split(' ')
    date_list = date_time[0].split('-')
    time_list = date_time[1].split(':')
    
    departureDate.append(''.join(date_list))
    departureTime.append(''.join(time_list))


df['departureDate'] = departureDate
df['departureTime'] = departureTime



'''arrival date and time seperation'''

arrivalDate = []
arrivalTime = []

for i in range(0, len(df.arrivalDate)):
    date_time = df.arrivalDate[i].split(' ')
    date_list = date_time[0].split('-')
    time_list = date_time[1].split(':')
    
    arrivalDate.append(''.join(date_list))
    arrivalTime.append(''.join(time_list))
    
df['arrivalDate'] = arrivalDate
df['arrivalTime'] = arrivalTime

'''purchase Date and Time Seperation'''

purchaseDate =[]
purchaseTime = []

for i in range(0,len(df.createDate)):
    date_time = df.createDate[i].split(' ')
    date_list = date_time[0].split('-')
    time_list = date_time[1].split(':')
    
    purchaseDate.append(''.join(date_list))
    purchaseTime.append(''.join(time_list))   

df['purchaseDate'] = purchaseDate
df['purchaseTime'] = purchaseTime

#print(df.columns)
#
#print(df.traAirport.value_counts())

#numeric_features = df.select_dtypes(include = [np.number])
#corr = numeric_features.corr()
#print(corr['price'].sort_values(ascendin[g=False))
'''checking for NaN values'''
print(df.isnull().sum())
#list(df.columns) 
#for column in list(df.columns):
#    print(column)
#    print(df[column].isnull().values.any())
#    if df[column].isnull().values.any():    
#        num_null = df[column].isnull().sum()
#        print('Number of Null Values: {}'.format(num_null))
#    else:
#        print('There are no Null Values')
'''I have conculed that only traAirport Column has null values 
therefore using Pandas get_dummies method will be enough to deal with single column'''    
    
df['traAirport'] = pd.get_dummies(df.traAirport, dummy_na = True)
'''rerun it for assurance'''
#
#for column in list(df.columns):
#    print(column)
#    print(df[column].isnull().values.any())
#    
print(df.columns)


print(df.isnull().sum())
#'''filling Na Values'''
#
#
#df['flightNumber'].fillna('missing')
#
#'''Label encoder'''
#
#lb = LabelEncoder()
#df['flightNumber'] = lb.fit_transform(df['flightNumber'])