

```python
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float
import pandas as pd
```


```python
# creates an engine to a database file called `hawaii.sqlite`

engine = create_engine("sqlite:///hawaii.sqlite")
```


```python
# creates a connection to the engine called `conn`

conn = engine.connect()
```


```python
# use declarative_base and creates ORM classes for each table

Base = declarative_base()
```


```python
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
```


```python
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
```


```python
# creates all the tables in the database

Base.metadata.create_all(engine)
```


```python
# load clean csv file

c_measurements_df = pd.read_csv('clean_hawaii_measurements.csv')
c_stations_df = pd.read_csv('clean_hawaii_stations.csv')
```


```python
# orient records to create list of writable data

measure_data = c_measurements_df.to_dict(orient='records')
stations_data = c_stations_df.to_dict(orient='records')
```


```python
# reflect the tables

metadata = MetaData(bind=engine)
metadata.reflect()
```


```python
# save the table

measure_table = sqlalchemy.Table('measurements', metadata, autoload=True)
stations_table = sqlalchemy.Table('stations', metadata, autoload=True)
```


```python
# use `table.insert()` to insert the data into the table

conn.execute(measure_table.insert(), measure_data)
conn.execute(stations_table.insert(), stations_data)
```




    <sqlalchemy.engine.result.ResultProxy at 0x108768198>




```python
# grab the first 10 rows

conn.execute("select * from measurements limit 10").fetchall()
```




    [(1, 'USC00519397', '2010-01-01', 0.08, 65.0),
     (2, 'USC00519397', '2010-01-02', 0.0, 63.0),
     (3, 'USC00519397', '2010-01-03', 0.0, 74.0),
     (4, 'USC00519397', '2010-01-04', 0.0, 76.0),
     (5, 'USC00519397', '2010-01-07', 0.06, 70.0),
     (6, 'USC00519397', '2010-01-08', 0.0, 64.0),
     (7, 'USC00519397', '2010-01-09', 0.0, 68.0),
     (8, 'USC00519397', '2010-01-10', 0.0, 73.0),
     (9, 'USC00519397', '2010-01-11', 0.01, 64.0),
     (10, 'USC00519397', '2010-01-12', 0.0, 61.0)]




```python
# grab all of the data

conn.execute("select * from stations").fetchall()
```




    [(1, 'USC00519397', 'WAIKIKI 717.2, HI US', 21.2716, -157.8168, 3.0),
     (2, 'USC00513117', 'KANEOHE 838.1, HI US', 21.4234, -157.8015, 14.6),
     (3, 'USC00514830', 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 21.5213, -157.8374, 7.0),
     (4, 'USC00517948', 'PEARL CITY, HI US', 21.3934, -157.9751, 11.9),
     (5, 'USC00518838', 'UPPER WAHIAWA 874.3, HI US', 21.4992, -158.0111, 306.6),
     (6, 'USC00519523', 'WAIMANALO EXPERIMENTAL FARM, HI US', 21.33556, -157.71139, 19.5),
     (7, 'USC00519281', 'WAIHEE 837.5, HI US', 21.45167, -157.84888999999995, 32.9),
     (8, 'USC00511918', 'HONOLULU OBSERVATORY 702.2, HI US', 21.3152, -157.9992, 0.9),
     (9, 'USC00516128', 'MANOA LYON ARBO 785.2, HI US', 21.3331, -157.8025, 152.4)]


