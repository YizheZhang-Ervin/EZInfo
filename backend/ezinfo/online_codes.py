class Run:
  def run():
    import tushare as ts
    import pandas as pd
    df = ts.get_realtime_quotes('000581')
    return list(df.values)