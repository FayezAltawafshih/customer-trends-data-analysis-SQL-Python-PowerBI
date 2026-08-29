#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


df = pd.read_csv(r'C:\Users\Dell\Downloads\customer_shopping_behavior.csv')


# In[2]:


df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.describe(include='all')


# In[6]:


df.isnull().sum()


# In[7]:


df['Review Rating'] = df.groupby('Category') ['Review Rating'].transform(lambda x:x.fillna(x.median())) 


# In[8]:


df.isnull().sum()


# In[9]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')


# In[10]:


df.columns


# In[11]:


df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[12]:


df.columns


# In[13]:


# cretae a column age_group 
labels = ['Young Adult' , 'Adult' , 'Middle-aged' , 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)          


# In[14]:


df[['age','age_group']].head(10)


# In[15]:


# create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90

}


# In[16]:


# create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[17]:


df[['purchase_frequency_days', 'frequency_of_purchases']].head(10)


# In[18]:


df[['discount_applied', 'promo_code_used']].head(10)


# In[19]:


(df['discount_applied'] == df['promo_code_used'].all)


# In[20]:


df = df.drop('promo_code_used',axis=1)


# In[21]:


df.columns


# In[22]:


pip install psycopg2-binary sqlalchemy


# In[23]:


import pandas as pd
from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
username = "postgres"        # default user
password = 123456        # your password
host = "localhost"           # local server
port = "5432"                # default PostgreSQL port
database = "Customer_Behavior"  # your database name

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Step 2: Load DataFrame into PostgreSQL
table_name = "customer"    # table name in Postgres
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"✅ Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[ ]:




