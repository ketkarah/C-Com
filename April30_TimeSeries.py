### Load file
df=pd.read_csv("C:/Users/Akshay/Desktop/Project/Sorted_Pace_full.csv")

### Isolate Fall Week, Spring Week & Winter Week
df1=df[32972864:33221334]
df1.to_csv("C:/Users/Akshay/Desktop/Project/Fall_Week08-09to08-15.csv")
df2=df[39962126:40193921]
df2.to_csv("C:/Users/Akshay/Desktop/Project/SpringWeek2016-03-13to03-19.csv")
df3=df[9758912: 10012650]
df3.to_csv("C:/Users/Akshay/Desktop/Project/Winter_Week2015-01-18to01-24.csv")
