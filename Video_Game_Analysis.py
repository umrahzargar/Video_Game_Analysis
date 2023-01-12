#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


data = pd.read_csv("C:/Users/umrahzargar/Downloads/vgsales.csv")


# In[4]:


data.head()


# In[5]:


unique_values = data.nunique()
print(unique_values)


# In[6]:


unique_values_genre = data['Genre'].unique()
print(unique_values_genre)


# In[7]:


data.dropna(how="any", inplace=True)


# In[8]:


data.sort_values(by="Global_Sales", ascending=False, inplace=True)
data.reset_index(drop=True, inplace=True)
data["Rank"] = np.arange(1, len(data) + 1)


# In[9]:


data["Year"] = data["Year"].astype(int)
data["Global_Sales"]= data["Global_Sales"].astype(float)


# In[10]:


data.info()


# # VISUALIZATION

# In[11]:


plt.pie(data.Genre.value_counts(), labels=data.Genre.value_counts().index, autopct='%1.0f%%')
plt.title('Genre')
plt.ylabel(' ')
plt.show()


# In[13]:


plt.barh(data.Genre,data.Global_Sales,color="maroon")
plt.xlabel('Global_Sales')
plt.ylabel('Genre')
plt.title('Global_Sales as per Genre')


# In[14]:


data.Genre.value_counts().head(5).plot(kind = 'bar', color = 'pink')
plt.xlabel('Genre')
plt.ylabel(' ')
plt.title('Top 5 game genre')
plt.show()


# In[15]:


print(data["Year"].unique())


# In[23]:


data_year= data.groupby(['Year'])
data_year = data_year['NA_Sales','EU_Sales','JP_Sales'].aggregate(np.mean)
data_year.plot( linestyle='dashed')
plt.title('Average Sales of the Game')


# In[25]:


data=data[data.Year==1990]
data=data.sort_values('Global_Sales',ascending=False).head(5)
data.Name.value_counts().head(5).plot(kind = 'bar', color = 'yellow')
plt.xlabel('Name')
plt.ylabel('Global_Sales')
plt.title('Top 5 game Names')
plt.show()


# In[27]:


data.Genre.value_counts().head(5).plot(kind = 'bar', color = 'purple')
plt.xlabel('Genre')
plt.ylabel(' ')
plt.title('Top 5 game genre')
plt.show()


# In[31]:


data=data.groupby('Publisher').agg({'JP_Sales':'sum','EU_Sales':'sum','NA_Sales':'sum','Other_Sales':'sum'})
data=data.sort_values('NA_Sales',ascending=False).head(3)
data.plot(kind='bar',figsize=(8,8))
plt.xlabel('Publisher')
plt.ylabel('Sales')
plt.title('Game Sales Per Region from Publishers')

