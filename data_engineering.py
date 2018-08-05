
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv


# In[2]:


#read csv files

hi_measure = pd.read_csv('hawaii_measurements.csv')
hi_stations = pd.read_csv('hawaii_stations.csv')

#convert files to data frames

measure_df = pd.DataFrame(hi_measure)
stations_df = pd.DataFrame(hi_stations)


# In[3]:


#missing data is in the precipitation column

measure_df.count()


# In[4]:


#viewing hawaii measurement data

measure_df.head(10)


# In[5]:


#row count of data

stations_df.count()


# In[6]:


#confirmed no missing data

stations_df.head(10)


# In[7]:


#pivot by station, to view the averages of precipitation and temperature w/ the NaN's included in the data

nan_eval = measure_df
nan_eval = pd.pivot_table(nan_eval,index=['station'], values=['prcp','tobs'])
nan_eval


# In[8]:


#pivot by station, to view the averages of precipitation and temperature w/ the NaN's removed from the data

nan_eval_0 = measure_df.dropna(how='any')
nan_eval_0_pivot = pd.pivot_table(nan_eval_0,index=['station'], values=['prcp','tobs'])
nan_eval_0_pivot


# In[9]:


#delta of the precipitation and temperature averages between the data w/ the NaN's included and the data w/o the NaN's
#no station's temperature average changes by more than +/- 0.10, so the NaN's will be removed
#removing the rows containing NaN values does not skew the data by a significant margin
#additionally, there are still 18,103 rows of data after the NaN's are removed

nan_delta = nan_eval - nan_eval_0_pivot
nan_delta


# In[10]:


#re-naming the cleaned data frames

clean_hawaii_measurements_df = measure_df.dropna(how='any')
clean_hawaii_measurements_df = clean_hawaii_measurements_df.reset_index(drop=True)
clean_hawaii_stations_df = hi_stations


# In[11]:


#saving the cleaned data as csv files

clean_hawaii_measurements_df.to_csv("clean_hawaii_measurements.csv", index = False)
clean_hawaii_stations_df.to_csv("clean_hawaii_stations.csv", index = False)

