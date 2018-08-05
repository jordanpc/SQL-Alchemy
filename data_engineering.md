

```python
import pandas as pd
import numpy as np
import csv
```


```python
#read csv files

hi_measure = pd.read_csv('hawaii_measurements.csv')
hi_stations = pd.read_csv('hawaii_stations.csv')

#convert files to data frames

measure_df = pd.DataFrame(hi_measure)
stations_df = pd.DataFrame(hi_stations)
```


```python
#missing data is in the precipitation column

measure_df.count()
```




    station    19550
    date       19550
    prcp       18103
    tobs       19550
    dtype: int64




```python
#viewing hawaii measurement data

measure_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>2010-01-01</td>
      <td>0.08</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>2010-01-02</td>
      <td>0.00</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>2010-01-03</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>2010-01-04</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>2010-01-06</td>
      <td>NaN</td>
      <td>73</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519397</td>
      <td>2010-01-07</td>
      <td>0.06</td>
      <td>70</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519397</td>
      <td>2010-01-08</td>
      <td>0.00</td>
      <td>64</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00519397</td>
      <td>2010-01-09</td>
      <td>0.00</td>
      <td>68</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00519397</td>
      <td>2010-01-10</td>
      <td>0.00</td>
      <td>73</td>
    </tr>
    <tr>
      <th>9</th>
      <td>USC00519397</td>
      <td>2010-01-11</td>
      <td>0.01</td>
      <td>64</td>
    </tr>
  </tbody>
</table>
</div>




```python
#row count of data

stations_df.count()
```




    station      9
    name         9
    latitude     9
    longitude    9
    elevation    9
    dtype: int64




```python
#confirmed no missing data

stations_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.49920</td>
      <td>-158.01110</td>
      <td>306.6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>19.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519281</td>
      <td>WAIHEE 837.5, HI US</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>32.9</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00511918</td>
      <td>HONOLULU OBSERVATORY 702.2, HI US</td>
      <td>21.31520</td>
      <td>-157.99920</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00516128</td>
      <td>MANOA LYON ARBO 785.2, HI US</td>
      <td>21.33310</td>
      <td>-157.80250</td>
      <td>152.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
#pivot by station, to view the averages of precipitation and temperature w/ the NaN's included in the data

nan_eval = measure_df
nan_eval = pd.pivot_table(nan_eval,index=['station'], values=['prcp','tobs'])
nan_eval
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
    <tr>
      <th>station</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>USC00511918</th>
      <td>0.047971</td>
      <td>71.615968</td>
    </tr>
    <tr>
      <th>USC00513117</th>
      <td>0.141921</td>
      <td>72.689184</td>
    </tr>
    <tr>
      <th>USC00514830</th>
      <td>0.121058</td>
      <td>74.873297</td>
    </tr>
    <tr>
      <th>USC00516128</th>
      <td>0.429988</td>
      <td>70.915008</td>
    </tr>
    <tr>
      <th>USC00517948</th>
      <td>0.063602</td>
      <td>74.684402</td>
    </tr>
    <tr>
      <th>USC00518838</th>
      <td>0.207222</td>
      <td>72.724070</td>
    </tr>
    <tr>
      <th>USC00519281</th>
      <td>0.212352</td>
      <td>71.663781</td>
    </tr>
    <tr>
      <th>USC00519397</th>
      <td>0.049020</td>
      <td>74.553231</td>
    </tr>
    <tr>
      <th>USC00519523</th>
      <td>0.114961</td>
      <td>74.543649</td>
    </tr>
  </tbody>
</table>
</div>




```python
#pivot by station, to view the averages of precipitation and temperature w/ the NaN's removed from the data

nan_eval_0 = measure_df.dropna(how='any')
nan_eval_0_pivot = pd.pivot_table(nan_eval_0,index=['station'], values=['prcp','tobs'])
nan_eval_0_pivot
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
    <tr>
      <th>station</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>USC00511918</th>
      <td>0.047971</td>
      <td>71.527433</td>
    </tr>
    <tr>
      <th>USC00513117</th>
      <td>0.141921</td>
      <td>72.678042</td>
    </tr>
    <tr>
      <th>USC00514830</th>
      <td>0.121058</td>
      <td>74.813113</td>
    </tr>
    <tr>
      <th>USC00516128</th>
      <td>0.429988</td>
      <td>70.865137</td>
    </tr>
    <tr>
      <th>USC00517948</th>
      <td>0.063602</td>
      <td>74.587116</td>
    </tr>
    <tr>
      <th>USC00518838</th>
      <td>0.207222</td>
      <td>72.675439</td>
    </tr>
    <tr>
      <th>USC00519281</th>
      <td>0.212352</td>
      <td>71.663781</td>
    </tr>
    <tr>
      <th>USC00519397</th>
      <td>0.049020</td>
      <td>74.564246</td>
    </tr>
    <tr>
      <th>USC00519523</th>
      <td>0.114961</td>
      <td>74.532659</td>
    </tr>
  </tbody>
</table>
</div>




```python
#delta of the precipitation and temperature averages between the data w/ the NaN's included and the data w/o the NaN's
#no station's temperature average changes by more than +/- 0.10, so the NaN's will be removed
#removing the rows containing NaN values does not skew the data by a significant margin
#additionally, there are still 18,103 rows of data after the NaN's are removed

nan_delta = nan_eval - nan_eval_0_pivot
nan_delta
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
    <tr>
      <th>station</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>USC00511918</th>
      <td>0.0</td>
      <td>0.088535</td>
    </tr>
    <tr>
      <th>USC00513117</th>
      <td>0.0</td>
      <td>0.011143</td>
    </tr>
    <tr>
      <th>USC00514830</th>
      <td>0.0</td>
      <td>0.060184</td>
    </tr>
    <tr>
      <th>USC00516128</th>
      <td>0.0</td>
      <td>0.049871</td>
    </tr>
    <tr>
      <th>USC00517948</th>
      <td>0.0</td>
      <td>0.097287</td>
    </tr>
    <tr>
      <th>USC00518838</th>
      <td>0.0</td>
      <td>0.048632</td>
    </tr>
    <tr>
      <th>USC00519281</th>
      <td>0.0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>USC00519397</th>
      <td>0.0</td>
      <td>-0.011015</td>
    </tr>
    <tr>
      <th>USC00519523</th>
      <td>0.0</td>
      <td>0.010990</td>
    </tr>
  </tbody>
</table>
</div>




```python
#re-naming the cleaned data frames

clean_hawaii_measurements_df = measure_df.dropna(how='any')
clean_hawaii_measurements_df = clean_hawaii_measurements_df.reset_index(drop=True)
clean_hawaii_stations_df = hi_stations
```


```python
#saving the cleaned data as csv files

clean_hawaii_measurements_df.to_csv("clean_hawaii_measurements.csv", index = False)
clean_hawaii_stations_df.to_csv("clean_hawaii_stations.csv", index = False)
```
