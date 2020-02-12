import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use(['ggplot','dark_background'])
# set up the style of the plot

start = dt.datetime(2015, 10, 10)
end = dt.datetime.now()
source= 'yahoo'
ticker = 'TSLA'
# set up the pandas_datareader

df = web.DataReader(ticker, source, start, end)
# downloads the historical price


df['50ma'] = df['Close'].ewm(span=50, adjust=False).mean()
df['100ma'] = df['Close'].ewm(span=100, adjust=False).mean()
df['1000ma'] = df['Close'].ewm(span=1000, adjust=False).mean()
# computes the moving average

df = df[df.index > '2015-1-1']


df['Date'] = df.index.map(mdates.date2num)
ohlc = df[['Date','Open','High','Low','Close']]
# converted date format for ohlc to run

f1, ax = plt.subplots(figsize = (50,10))
# sets the size of the graph

candlestick_ohlc(ax, ohlc.values, width= .6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# plotting the candlesticks


ax.plot(df.index, df['50ma'], color = 'white', label = '50ma')
ax.plot(df.index, df['100ma'], color = 'orange', label = '100ma')
ax.plot(df.index, df['1000ma'], color = 'blue', label = '1000ma')
# plots the moving average lines


ax.grid(True)
ax.legend()

plt.show()

