# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:29:11 2019

@author: Ibrahim
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score
import seaborn as seabornInstance


df = pd.read_csv(r'C:\Users\Ibrahim\.spyder-py3\plane_tickets_edited.csv', index_col = 0)
X = df[['rate','craftTypeCode','departureTime','departureDate', 'arrivalTime', 
        'arrivalDate','purchaseDate','purchaseTime','flightNumber', 'ID', 'traAirport','dateDifference']].values
y = df[['price']].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state = 0)

regressor = LinearRegression()

regressor.fit(X_train, y_train)

#print(regressor.intercept_)
#
#print(regressor.coef_)
#
#plt.figure(figsize=(15,10))
#plt.tight_layout()
#seabornInstance.distplot(df['price'])

y_pred = regressor.predict(X_test)
#
#dfw = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
#df2 = pd.DataFrame.from_records([{'Actual': y_test, 'Predicted': y_pred}])
#print(df2.head())

r2 = r2_score(y_test, y_pred)

print(r2)

#X1 = df[['rate','craftTypeCode','departureTime','departureDate', 'arrivalTime', 
#        'arrivalDate','purchaseDate','flightNumber', 'ID', 'dateDifference']].values
#         
#X1_train, X1_test, y_train, y_test = train_test_split(X1, y, test_size=0.4, random_state = 0)
#
#regressor.fit(X1_train, y_train)
#
#y1_pred = regressor.predict(X1_test)
#
#r21 = r2_score(y_test, y1_pred)
#
#print(r21)