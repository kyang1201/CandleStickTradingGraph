import plotly.plotly as py
import plotly.graph_objs as go

import pandas_datareader as web
from datetime import datetime

df = web.DataReader("aapl", 'yahoo')

trace = go.Candlestick(x=df.index,
                       open=df.Open,
                       high=df.High,
                       low=df.Low,
                       close=df.Close)
data = [trace]
py.plot(data, filename='simple_candlestick')
