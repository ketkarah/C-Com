### Modified of code by Prof.Sowers

WayDict={}
WayLookup=set()
ctr=0

###Function to create link pair dictionary
def addLink(begin,end,temp_ctr):
    newWay=(begin,end)
    temp=str(newWay)
    if (not (temp in WayLookup)):
        WayLookup.add(temp)
        WayDict[ctr]=newWay
    return temp_ctr+1

def linkcsv(WayDict):
    StartLat=[]
    StartLon=[]
    EndLat=[]
    EndLon=[]
    link_id=[]
    Start_Node_id=[]
    End_Node_id=[]
    for i in WayDict.keys():
       temp1=MyApi.NodeGet(WayDict[i][0])
       temp2=MyApi.NodeGet(WayDict[i][1])
       StartLat.append(temp1["lat"])
       StartLon.append(temp1["lon"])
       EndLat.append(temp2["lat"])
       EndLon.append(temp2["lon"])
       link_id.append(i)
       Start_Node_id.append(WayDict[i][0])
       End_Node_id.append(WayDict[i][1])
    return StartLat,StartLon,EndLat,EndLon,link_id,Start_Node_id,End_Node_id
       
from osmapi import OsmApi
MyApi = OsmApi()

### latitude and longitude of approximate centre of the area.
lat=41.878299
lng=-87.632304

###Create a box for selecting map area and loading its data
data=MyApi.Map(lng-0.004445,lat-0.001477,lng+0.004479,lat+0.003758)

nodes=[doc for doc in data if doc["type"]=="node"]
ways=[doc for doc in data if doc["type"]=="way"]

###Create link dictionaries by considering and avoiding oneway links
for way in ways:
    nodeList=way["data"]["nd"]
    N_nodes=len(nodeList)
    for n in range(N_nodes-1):
        start=nodeList[n]
        end=nodeList[n+1]
        ctr=addLink(start,end,ctr)
        flag= ('data' in way) and ('tag' in way['data']) and ('oneway' in way['data']['tag']) and (way['data']['tag']['oneway']=='yes')
        if (not flag):
            ctr=ctr=addLink(end,start,ctr)
StartLat,StartLon,EndLat,EndLon,link_id,Start_Node_id,End_Node_id=linkcsv(WayDict)

###Also the above on line 60 were converted into a dataframe and exported to links.csv on Command Line
