### Load the pace data
import csv
import pandas as pd
df=pd.read_csv("C:/Users/Akshay/Desktop/Project/Sorted_Pace_full.csv")

### Isolate the pace column
pace=df['Pace']

### Find the quantiles(0, 0.33, 0.66, 1)
pace.quantile([0.0,1/4,1/2,3/4,1.0])

### Chicago Snow Storm(Jan 31 to Feb 2,2015)
sn_strm=df[25496105:25598460]
sn_strm.to_csv("C:/Users/Akshay/Desktop/Project/Snow_Storm.csv")

### Day One 2013(1/1/2013- First day of the dataset)
day_one=df[0:20849]
day_one.to_csv("C:/Users/Akshay/Desktop/Project/Day_One2013.csv")
df.iloc[14122193]

### Random_week (5/5/2014-5/11/2014)
random_week=df.iloc[14122193:14421103]
random_week.to_csv("C:/Users/Akshay/Desktop/05May2014to11May2014.csv")
