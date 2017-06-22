import csv
import pandas as pd
def one(csvfile):
    b=csv.reader(csvfile)
    next(b)
    Stst=[]
    Etst=[]
    miles=[]
    time=[]
    for row in b:
        if row[2]=='' or row[3]=='' or row[4]=='' or row[5]=='' or float(row[4])==0.0 or float(row[5])==0.0 or row[8]=='' or row[9]=='': 
            continue
        elif int(row[8])==32.0 and int(row[9])==32:
            Stst.append(row[2])
            Etst.append(row[3])
            time.append(int(row[4]))
            miles.append(float(row[5]))
    return Stst,Etst,time,miles

def two(csvfile):
    b=csv.reader(csvfile)
    next(b)
    plat=[]
    plon=[]
    dlat=[]
    dlon=[]    
    for row in b:
        if row[2]=='' or row[3]=='' or row[4]=='' or row[5]=='' or float(row[4])==0.0 or float(row[5])==0.0 or row[8]=='' or row[9]=='': 
            continue
        elif int(row[8])==32.0 and int(row[9])==32:
            plat.append(float(row[17]))
            plon.append(float(row[18]))
            dlat.append(float(row[20]))
            dlon.append(float(row[21]))
    return plat,plon,dlat,dlon

### Running line 40 and 41 alternately by first commenting out 41 to run 40 and then the other way round.

with open("C:/Users/Akshay/Desktop/Project/Taxi_Trips.csv",encoding='utf-8',newline='') as csvfile:
        """Stst,Etst,time,miles=one(csvfile)"""
        plat,plon,dlat,dlon=two(csvfile)
        
###Command Line to convert line 40 and 41 to dataframe and export to csv
d={"pickup_datetime":Stst,"dropoff_datetime":Etst,"trip_time_in_secs":time,"trip_distance":miles,"pickup_longitude":plon,"pickup_latitude":plat,"dropoff_longitude":dlon,"dropoff_latitude":dlat}
df=pd.DataFrame(d)
df.to_csv("C:/Users/Akshay/Desktop/Project/Loop_Trips.csv")
