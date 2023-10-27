import numpy as np
import pandas as pd

from datetime import datetime

#Missing data in dataframe :
# data = {"col1":[2,3,1,5,4] , "year":[2001,2002,2003,2004,2005]}

def PandasBasics():
    data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
            "year": [2000, 2001, 2002, 2001, 2002, 2003],
            "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    #Dataframe index items
    frame = pd.DataFrame(data)

    #Adding a new column 
    #a) Without values
    frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])

    print(frame2.columns)

    dfState = frame2['state']

    print(frame2)
    # print(dfState)
    print(type(dfState))
    print(type(frame2.iloc[1]))

    #Selecti
    GetRow1 = frame2.iloc[1]
    print(GetRow1)

    #Column modification by assignment:
    frame2['debt'] = np.arange(6.0)
    print(frame2)
    print(frame2.debt)

    #Delete col by using del keyword
    print(frame2.index.names)

    populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
                "Nevada": {2001: 2.4, 2002: 2.9}}

    frame3 = pd.DataFrame(populations)

    print(frame3)
    print(frame3["Ohio"])
    print(frame3["Ohio"][:-2])

    #Specify columns name & index name
    frame3.index.name = "year"
    frame3.columns.name = "state"
    print(frame3)
    return


#Try Essential functionality
def TryEssentialFunctionality5_2():
    obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
    print(obj)
    obj2 = obj.reindex(["a","b","c","d","e"])
    print(obj2)
    obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
    print(obj3)
    obj3.reindex(np.arange(6), method='ffill')
    frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                        index=["a", "c", "d"],
                        columns=["Ohio", "Texas", "California"])
    print(frame)
    frame2 = frame.reindex(index=["a","b","c","d","e"])
    print(frame2)

    #Colmns reindexed with columns keyword
    states = ["Texas", "Utah", "California"]
    frame3 = frame.reindex(columns=states)
    print(frame3)
    frame4 = frame.reindex(states,axis="columns")
    print(frame4)

def Try5_2DroppingEntries():
    obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
    print(obj)
    new_obj = obj.drop("c")
    print(new_obj)
    new_obj2 = obj.drop(["a","d","c"])
    print(new_obj2)

    #With dataframe
    data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                index=["Ohio", "Colorado", "Utah", "New York"],
                columns=["one", "two", "three", "four"])
    print(data)
    data1 = pd.DataFrame(np.arange(16,dtype=float).reshape((4,4)),
                         index=np.arange(4),
                         columns=np.arange(4))
    data1.index.name = "index"
    data1.columns.name = "column"
    print(data1)

    #drop data using index and columns
    data2 = data.drop(index=["Colorado","Ohio"])
    print(data2)
    data3 = data.drop(columns=["two","one"])
    print(data3)

def Try5_2Indexing_Selection_Filter():
    obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
    print(obj)
    print(obj["b"])
    print(obj[2]) #depreceated
    print(obj.iloc[3])
    print(obj.iloc[2:4])
    obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])
    obj2 = pd.Series([1, 2, 3], index=["a", "b", "c"])
    print(obj1[[0,1,2]])
    print(obj2[[0,1,2]])
    print(obj2.iloc[[0,1,2]])
    obj2.loc["b"] = 20
    print(obj2)
    obj2.loc["b":"c"] = 11
    print(obj2)

    data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])
    print(data)
    print(data["two"])
    print(data["three"] < 5)
    ser1 = data["three"] < 5
    print(data[ser1])

    
    # print(data["Ohio"])
    print(data[["three" , "two"]])
    print(data < 5)
    print(data[data < 5])
    # return
    data[data < 5] = 0
    print(data)
    #Selection on dataframe using loc & iloc
    print(data.loc["Colorado"]) #result is a Series
    print(data.loc[["Colorado","Ohio"]])

    #Both row & column selection can be combined in loc
   
    print(data.loc["Colorado", ["two", "three"]])
    print(data)
    
    print(data.iloc[0])
    print(data.iloc[[2,1]])
    print(data.iloc[2, [3, 0, 1]])

    #Indexing functions work with slices
    print(data.loc["Utah","two"])
    print(data)
    print(data.iloc[:, :3])
    print(data.three > 5)
    print(data.iloc[:, :3][data.three > 5])

def Try5_2ArithmeticOp():
    frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
            columns=list("bde"),
            index=["Utah", "Ohio", "Texas", "Oregon"])
    print(frame)
    ser1 = pd.Series(np.arange(3) , index=list("abd"))
    print(ser1)
    print(frame-ser1)
    ser2 = pd.Series(np.arange(4) , index=list("abde"))
    print(ser2.T)
    print(frame - ser2)


def Try11_1DateTimeDataTypeAndTools():
    from datetime import datetime
    now = datetime.now()
    print(now)
    print(now.year , now.month, now.day , now.hour , now.minute , now.second)
    print(type(now))
    value = "2011-01-03"
    print(datetime.strptime(value, "%Y-%m-%d"))

    datestrs = ["2011-07-06 12:00:00", "2011-08-06 00:00:00"]
    res = pd.to_datetime(datestrs)
    print(res)
    arr1 = pd.Series(["ab" , "abc" , "ad" , "bd"])
    print(arr1)
    # arr1 = arr1 + [["cd" , "dd"]]
    arr1.iloc[3] = "cd"
    print(arr1)
    
def Try11_2TimeSeriesBasics():
    
    dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
            datetime(2011, 1, 7), datetime(2011, 1, 8),
            datetime(2011, 1, 10), datetime(2011, 1, 12)]
    ts = pd.Series(np.random.standard_normal(6), index= dates)
    print(ts)
    
    #Longer Series
    longer_ts = pd.Series(np.random.standard_normal(1000), index=pd.date_range("2000-01-01",
                          periods=1000))
    print(longer_ts)
    timeseries = pd.Series(np.random.standard_normal(86400), 
                                  index=pd.date_range("2023-10-23 00:00:01",periods=86400, freq='1s'))
    print(timeseries)
    sliced_timeseries = timeseries[timeseries.index[0:10]]
    
    print(sliced_timeseries)
    sliced_timeseries2 = timeseries[timeseries.index[0] :timeseries.index[4]]
    print(sliced_timeseries2)

    dates = pd.date_range("2000-01-01", periods=100, freq="W-WED")
    long_df = pd.DataFrame(np.random.standard_normal((100, 4)),
                        index=dates,
                        columns=["Colorado", "Texas",
                        "New York", "Ohio"])
    print(long_df)
    sliced_df = long_df.loc["2001-05"]
    print(sliced_df)
    sliced_df2 = long_df.loc["xxxx-05"]
    print(sliced_df2)
    # print(long_df["2001-05"])


def Try11_6ResamplingAndFreq():
    dates = pd.date_range("2000-01-01", periods=100, freq='1D')
    print(dates)
    ts = pd.Series(np.random.standard_normal(len(dates)),index=dates)
    print(ts)
    ts1 = ts.resample("M").mean()
    print(ts1)
    ts2 = ts.resample("M")
    print(ts2)
    #Try with dataframe:
    frame = pd.DataFrame(np.random.standard_normal((2, 4)),
                index=pd.date_range("2000-01-01", periods=2,
                freq="W-WED"),
                columns=["Colorado", "Texas", "New York", "Ohio"])
    print(frame)
    df_daily = frame.resample("D").asfreq()
    print(df_daily)

    frame2 = pd.DataFrame(np.random.standard_normal((200,4)),
                          index=pd.date_range("2023-10-23 00:00:01",periods=200,freq='1s'),
                          columns=["Colorado","Texas","new York", "Ohio"])
    
    ts_day = pd.date_range("2023-10-23 00:00:01","2023-10-23 00:00:10",
                           freq='1s')
    print(ts_day)
    frame2_dropped = frame2.drop(ts_day[0])
    print("frame2_dropped")
    print(frame2_dropped.head(2))
    print(len(frame2_dropped))
    #Upsampling for more points
    frame3 = frame2_dropped.resample("1s").asfreq()
    print("frame3")
    print(frame3.head(2))
    print(len(frame3))
    frame4 = frame2_dropped.resample("1s").ffill(limit=1)
    print(frame4.head(2))
    return
    print(frame2)

    
    # frame2_Dropped = frame2.drop([0,1,2], axis=0)
    frame2_Dropped = frame2.drop(index=[0,1])
    print(frame2_Dropped.head())



# PandasBasics()
# TryEssentialFunctionality5_2()
# Try5_2DroppingEntries()
# Try5_2Indexing_Selection_Filter()
# Try5_2ArithmeticOp()
# Try11_1DateTimeDataTypeAndTools()
# Try11_2TimeSeriesBasics()
Try11_6ResamplingAndFreq()


if __name__ == 'main':
    # PandasBasics()
    TryEssentialFunctionality5_2()