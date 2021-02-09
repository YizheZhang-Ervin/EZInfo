class Run:
  def run():
    from datetime import datetime
    from pandas_datareader import DataReader
    stock="TGT"
    t1=datetime(2020,1,1) 
    t2=datetime(2021,2,5)
    data=DataReader(stock,"yahoo",t1,t2)
    x = list(map(lambda x:str(x.date()),data.index))
    y = list(map(float,data["Adj Close"].values))
    y2 = list(map(float,data["Open"].values))
    return {"x":x,"y":y,"y2":y2}