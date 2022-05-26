#!/usr/bin/env python
# coding: utf-8

# # Data Visualization with Python Studio
# 
# At this point, you should already have connected with the rest of your group to divide up who is going to do what. Use this notebook to create your visualizations.
# 
# Below we set up the dataframe with the Goodreads dataset for you. If you run this cell, you may get an error that some lines were skipped. Do not worry about that! For this studio, we want to focus on creating an effective

# In[1]:


# Here is the setup of the dataframe. Feel free to use .info() or .head() to get a better understanding of what is inside the dataframe!

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv("books.csv", error_bad_lines=False)

years = []

for y in df['publication_date']:
    date = y.split("/")
    years.append(date[2])

df["year"] = years


# In[2]:


df.head()


# With your dataframe set up, time to start creating visualizations!

# In[3]:


df.info()


# In[26]:


df.isnull( ).sum( )


# In[58]:


style.use('ggplot')
df_publisher = pd.DataFrame(df['year'].value_counts().head(20).sort_values(ascending = True))


# In[61]:


df_publisher.plot.bar()
plt.title('Distribution of Publishers')
plt.xlabel('year')
plt.ylabel("publisher")
plt.show()


# In[32]:


len(df. index)


# In[35]:


# df.plot.scatter('publisher') 


# In[37]:


df['publisher'].value_counts()


# In[25]:


plt.bar('publisher', 111223)


# In[49]:


plt.rcParams['figure.figsize']=(10, 8)


# In[17]:


df.describe()


# In[40]:


# sns.barplot(x= 'index', y='publisher', data=df['publisher'].value.counts().reset_index().head(10)


# In[43]:


# sns.barplot(x= 'index', y='publisher')


# In[57]:


plt.bar(df['publisher'].head(10), df['year'].head(10)


# In[48]:


df_publisher= df['publisher'].value_counts().reset_index()
df_publisher.rename(columns={"index": "publisher", "publisher": "number_of_books"})


# In[47]:


plt.show(df_publisher)


# In[30]:



# Make a random dataset:
height = [3, 12, 5, 18, 45]
bars = (['publisher'])
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show(df['publisher'])


# In[12]:


# Use your Python skills to create a visualization here.


# In[13]:


# Use your Python skills to create a visualization here.

