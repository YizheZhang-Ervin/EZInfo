from sqlalchemy import create_engine
import tushare as ts
import pandas as pd
import pymysql
from sqlalchemy.types import VARCHAR
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect 
import json
from backend import settings

def initEngine(whichone):
    paras = settings.DATABASES["default"]
    host=paras["HOST"]
    port=paras["PORT"]
    user=paras["USER"]
    password=paras["PASSWORD"]
    database=paras["NAME"]
    # 获取引擎
    if whichone =="fromweb":
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
    else:
        engine = pymysql.connect(host=host,port=port,user=user,password=password,database=database)
    return engine

def getDataFromWeb(request):
    engine = initEngine("fromweb")
    dt = ts.get_hist_data(code='sh',start='2019-01-01',end='2021-02-04')
    dt.to_sql(name='shindex',con=engine,if_exists='append',dtype={'code':VARCHAR(dt.index.get_level_values('date').str.len().max())})
    return redirect('/home/')

def getDataFromDB(request):
    tableName='shindex'
    engine = initEngine("fromDB")
    cursor = engine.cursor()
    sql = f"SELECT date,open,close,low,high,volume FROM {tableName} order by date ASC"
    rows = cursor.execute(sql)  
    data = cursor.fetchall()
    rst = []
    [rst.append([i[0],i[1],i[2],i[3],i[4],i[5]]) for i in data]
    engine.commit()
    cursor.close()
    engine.close()
    return JsonResponse(rst,safe=False)