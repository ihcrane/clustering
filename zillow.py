#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from acquire import wrangle_zillow
from prepare import remove_outliers, train_val_test, x_y_split

import warnings
warnings.filterwarnings('ignore')

from scipy.stats import stats
from env import get_connection
import os


# In[151]:


def get_zillow_data():
    
    '''
    This function is used to get zillow data from sql database.
    '''
    
    if os.path.isfile('zillow.csv'):
        
        return pd.read_csv('zillow.csv')
    
    else:
        
        url = get_connection('zillow')
        query = '''
                SELECT * FROM properties_2017
                LEFT JOIN airconditioningtype USING(airconditioningtypeid)
                LEFT JOIN architecturalstyletype USING(architecturalstyletypeid)
                LEFT JOIN buildingclasstype USING(buildingclasstypeid)
                LEFT JOIN heatingorsystemtype USING(heatingorsystemtypeid)
                LEFT JOIN predictions_2017 USING(parcelid)
                LEFT JOIN propertylandusetype USING(propertylandusetypeid)
                LEFT JOIN storytype USING(storytypeid)
                LEFT JOIN typeconstructiontype USING(typeconstructiontypeid)
                WHERE transactiondate LIKE '2017%%'
                AND latitude IS NOT NULL
                AND longitude IS NOT NULL;
                '''
        df = pd.read_sql(query, url)
        df.to_csv('zillow.csv')
        return df



# In[153]:





# In[175]:


def drop_duplicates(df):
    
    df.drop(columns=['Unnamed: 0', 'id.1'], inplace=True)
    
    df = df.sort_values('transactiondate')
    df = df[df.duplicated(subset=['parcelid'], keep='last')==False]
    
    return df


# In[155]:





# In[156]:


def missing_values(df):
    
    missing_df = pd.DataFrame(df.isna().sum(), columns=['num_rows_missing'])
    
    missing_df['pct_rows_missing'] = missing_df['num_rows_missing'] / len(df)
    
    return missing_df


# In[157]:




# ## Prepare

# In[158]:


def sfh(df):
    
    sp = [261, 266, 263, 275, 264]
    df = df[df['propertylandusetypeid'].isin(sp)]
    return df


# In[173]:





# In[174]:





# In[168]:


def handle_missing_values(df, prop_required_col, prop_required_row):
    
    drop_cols = round(prop_required_col * len(df))
    df.dropna(thresh=drop_cols, axis=1, inplace=True)

    drop_rows = round(prop_required_row * len(df.columns))
    df.dropna(thresh=drop_rows, axis=0, inplace=True)
    


    return df


# In[169]:





# In[ ]:





# In[ ]:




