
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


import datetime as dt


# In[4]:


# Reflect tables into SQL Alchemy ORM


# In[5]:


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[6]:


engine = create_engine("sqlite:///../Resources/hawaii.sqlite")


# In[7]:


# reflect an existing datebase into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


# In[8]:


# view all classes from automap
Base.classes.keys()


# In[9]:


# save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[10]:


# create session link from python to db
session = Session(engine)


# In[11]:


# EXPLORATORY CLIMATE ANALYSIS
# query to retrieve last 12 months of data
# calculate the date 1 year ago today
prev_date = dt.date(2017,8,23) - dt.timedelta(days=365)

# perform a query to retrieve the data and precipitation scores
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > prev_date).all()

# save the query results as panda dataframe and set the index to the date
df = pd.DataFrame(results, columns=['date', 'precipitation'])

# sort the dataframe by date
df.sort_values('date')
df.set_index('date', inplace=True)

# use pandas plotting with matplotlib to plot the data
df.plot()

# rotate the ticks for the dates
plt.xticks(rotation=45)
plt.tight_layout()


# In[12]:


# use pandas to calculate the summary statistics for the precipitation data
df.describe()


# In[16]:


# how many positions are available in the dataset?
session.query(func.count(Station.station)).all()


# In[25]:


# what are the most active stations?
# list the stations and the counts in descending order
(session.query(Measurement.station, func.count(Measurement.station))
    .group_by(Measurement.station)
    .order_by(func.count(Measurement.station).desc())
    .all())


# In[33]:


# using the station id from the previous query, calculate the lowest temperature
# highest temperature recorded, and average temperature of most active station
session.query(func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.station == 'USC00519281').all()


# In[39]:


# choose the station with the highest number of temperature observations
# query the last 12 months of temperature observation data for this station
results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date>prev_date).all()

df = pd.DataFrame(results, columns=['temp'])
df.plot.hist()

