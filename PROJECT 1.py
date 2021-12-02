
# coding: utf-8

# In[22]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('happyscore_income.csv')

happy = data['happyScore']
income = data['avg_income']

data.sort_values('avg_income', inplace=True)

rich = data[data['avg_income']>12000]


plt.xlabel('Income')
plt.ylabel('Happy Score')
plt.scatter(rich['avg_income'],rich['happyScore'])

income_happy = np.column_stack((income, happy))
kmresult = KMeans(n_clusters = 2).fit(income_happy)

clusters = kmresult.cluster_centers_

plt.scatter(clusters[:,0],clusters[:,1],)

plt.text(rich.iloc[10]['avg_income'],
        rich.iloc[10]['happyScore'],
        rich.iloc[10]['country'])


    

