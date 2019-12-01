# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:20:52 2019

@author: Ibrahim
"""

import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy.stats import norm 
df = pd.read_csv(r'C:\Users\Ibrahim\.spyder-py3\plane_tickets_edited.csv', index_col = 0)



#corr1 = np.corrcoef(df['departureTime'],df['price'])[1,0]
#
#print(corr1)

corr = df.corr(method='pearson')['price']

#print(corr)


#plt.scatter(df['purchaseTime'],df['price'], s=1)

best_of_columns = ['departureDate', 'arrivalDate','dateDifference', 'departureTime', 'arrivalTime', 'purchaseDate', 'purchaseTime']

#mean_list = []
#std_list = []
#    
#for feature in best_of_columns:
#    grouped = df.groupby([feature])
#    mean = grouped.mean()
#    std = grouped.std()
#    mean_list.append(mean)
#    std_list.append(std)
#    print(mean_list)
#    print(std_list)
#    
#
#stat_df = pd.DataFrame([mean_list, std_list])
#
#print(stat_df)

g = df.groupby(['dateDifference'])
mean = g.mean()
std = g.std()
mean_price = mean.price
std_price = std.price
mean.hist()
plt.figure(constrained_layout=False)

#print(mean_price)
#print(std_price)


#corrmat = df.corr() 
#  
#f, ax = plt.subplots(figsize =(9, 8)) 
#sns.heatmap(corrmat, ax = ax, cmap ="YlGnBu", linewidths = 0.1) 
#
#k = 15 
#  
#cols = corrmat.nlargest(k, 'price')['price'].index 
#  
#cm = np.corrcoef(df[cols].values.T) 
#f, ax = plt.subplots(figsize =(12, 10)) 
#  
#sns.heatmap(cm, ax = ax, cmap ="YlGnBu", 
#            linewidths = 0.1, yticklabels = cols.values,  
#                              xticklabels = cols.values)

            
    
