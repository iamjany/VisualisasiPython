#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


data=pd.read_csv("vgsales.csv")
data


# In[6]:


#DATA CLEANING
#Mengecek Missing Value
data.isnull().sum()


# In[10]:


# melakukan isian missing value,
from scipy.stats import mode

data['Year'] = data['Year'].fillna(data['Year'].mode()[0])
data['Publisher'] = data['Publisher'].fillna(data['Publisher'].mode()[0])


# In[12]:


#mengecek data missing value
data.isnull().sum()


# In[14]:


data.info()


# In[17]:


data['Year']=data['Year'].astype('int64')
data.info()


# In[18]:


data.to_csv("vgsales_clean.csv")


# In[42]:


#import package
import pandas as pd
import numpy as np
import matplotlib as plt
from pylab import *
import seaborn as sns
from matplotlib import *
import sys
from pylab import pl
f = figure.Figure(figsize=(17,10))


# In[43]:


#TOTAL PENJUALAN DAN JUMLAH GAME DI SELURUH DUNIA (BAR CHART)
plt.figure(figsize=(17,10))

plt.subplot(2,2,1)
sns.barplot(x='Year', y='Global_Sales', data=data.groupby(data['Year']).sum().Global_Sales.reset_index(), palette='Spectral')
plt.ylabel('Global_sales')
plt.xlabel('Tahun')
plt.xticks(rotation=90)
plt.title('Total Penjualan Game di Seluruh Dunia')

plt.subplot(2,2,2)
sns.barplot(x=data['Year'].value_counts().index, y=data['Year'].value_counts())
plt.ylabel('Jumlah Game')
plt.xlabel('Tahun')
plt.xticks(rotation=90)
plt.title('Total Jumlah Game yang Dirilis setiap Tahun')

# Karna data sebelumnya belum tampil, naka


# In[51]:


EU= data.pivot_table('EU_Sales', columns='Name',index='Year', aggfunc='sum').sum(axis=1)
NA= data.pivot_table('NA_Sales', columns='Name',index='Year', aggfunc='sum').sum(axis=1)
JP= data.pivot_table('JP_Sales', columns='Name',index='Year', aggfunc='sum').sum(axis=1)
Other= data.pivot_table('Other_Sales', columns='Name',index='Year', aggfunc='sum').sum(axis=1)
years= Other.index.astype(int)

plt.figure(figsize=(10,6))
ax = sns.pointplot(x=years, y=EU, color='mediumslateblue', scale=0.7)
ax = sns.pointplot(x=years, y=NA, color='cornflowerblue', scale=0.7)
ax = sns.pointplot(x=years, y=JP, color='orchid', scale=0.7)
ax = sns.pointplot(x=years, y=Other, color='thistle', scale=0.7)
ax.set_xticklabels(labels=years, rotation=90)
ax.set_xlabel(xlabel='Tahun', fontsize=14)
ax.set_ylabel(ylabel='Penjualan', fontsize=14)
ax.set_title(label='Penjualan Game di Berbagai Negara', fontsize=15)
ax.legend(handles=ax.lines[::len(years)+1], labels=['European Unio','Nort America', 'Japan','Other'])
plt.show()


# In[55]:


#Persentase Genre Game (Pie Chart)
plt.figure(figsize=(8,8))
color=['#0a5f38','#048243','#0cb577','#12e193','#05ffa6','#7bfdc7','#b8ffeb','#13eac9','#24bca8','#029386','#014d4e']
exp=[0.1,0,0,0,0,0,0,0,0,0,0,0]
plt.pie(data['Genre'].value_counts(), labels=data['Genre'].value_counts().index, autopct='%1.1f%%',explode=exp, colors=color);
plt.title('Genre');


# In[61]:


df= data.groupby(['Publisher']).sum()['Global_Sales']
df=pd.DataFrame(df.sort_values(ascending=False))[0:10]
publisher=df.index
df.columns=['Global Sales']

plt.figure(figsize=(10,6))
ax= sns.barplot(y=publisher, x='Global Sales', data=df, palette='Purples_r')
ax.set_xlabel(xlabel='Global Sales', fontsize=14)
ax.set_ylabel(ylabel='Publisher', fontsize=14)
ax.set_title(label='Top 10 Total Penjualan Publisher', fontsize=15)
ax.set_yticklabels(labels= publishers)
plt.show()


# In[ ]:




