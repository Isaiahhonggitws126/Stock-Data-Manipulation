import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()
# Setted up start and end datetime object.

df = web.DataReader("VOO", 'yahoo', start, end)
# Pulled data from Yahoo for its start and end dates.

df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

df.to_csv('VOO.csv')
# Saved dataframe into a csv

df = pd.read_csv('VOO.csv', parse_dates=True, index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
# calculates the moving average for 100 days
df['20ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
# calculates the moving average for 20 days


plot_1 = plt.subplot2grid((6,1), (0,0), rowspan= 5, colspan = 1)
plot_2 = plt.subplot2grid((6,1), (5,0), rowspan= 1, colspan= 1,sharex= plot_1)



plot_1.plot(df.index, df['Adj Close'])
plot_1.plot(df.index, df['100ma'])
# plots the moving average for 100 rolling days
plot_1.plot(df.index, df['20ma'])
# plots the moving average for 20 rolling days
plot_1.legend()


# plots the Adj close and 100ma

plot_2.plot(df.index, df['Volume'])
plot_2.legend()

# plots the volume of the fund


plt.show()
