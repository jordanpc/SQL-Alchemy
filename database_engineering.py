
# coding: utf-8

# In[1]:


import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float
import pandas as pd


# In[2]:


# creates an engine to a database file called `hawaii.sqlite`

engine = create_engine("sqlite:///hawaii.sqlite")


# In[3]:


# creates a connection to the engine called `conn`

conn = engine.connect()


# In[4]:


# use declarative_base and creates ORM classes for each table

Base = declarative_base()


# In[5]:


# creates measurement class

class Measurements(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key=True)
    station = Column(String(50))
    date = Column(String(50))
    prcp = Column(Float)
    tobs = Column(Float)

    def __repr__(self):
        return f"id={self.id}, name={self.name}"


# In[6]:


# creates station class

class Stations(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    station = Column(String(50))
    name = Column(String(50))
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    
    def __repr__(self):
        return f"id={self.id}, name={self.name}"


# In[7]:


# creates all the tables in the database

Base.metadata.create_all(engine)


# In[8]:


# load clean csv file

c_measurements_df = pd.read_csv('clean_hawaii_measurements.csv')
c_stations_df = pd.read_csv('clean_hawaii_stations.csv')


# In[9]:


# orient records to create list of writable data

measure_data = c_measurements_df.to_dict(orient='records')
stations_data = c_stations_df.to_dict(orient='records')


# In[10]:


# reflect the tables

metadata = MetaData(bind=engine)
metadata.reflect()


# In[11]:


# save the table

measure_table = sqlalchemy.Table('measurements', metadata, autoload=True)
stations_table = sqlalchemy.Table('stations', metadata, autoload=True)


# In[12]:


# use `table.insert()` to insert the data into the table

conn.execute(measure_table.insert(), measure_data)
conn.execute(stations_table.insert(), stations_data)


# In[13]:


# grab the first 10 rows

conn.execute("select * from measurements limit 10").fetchall()


# In[14]:


# grab all of the data

conn.execute("select * from stations").fetchall()

