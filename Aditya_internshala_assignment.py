#Exporting the necessory Libraries
#Accessing Yahoo finance api using yfinance
#Importing plotly for ploting charts and pandas for dataframe
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Downloading Reliance(NSE) stock data(Each day open,high,volume,close,open) of one year
#From January 2021 to January 2022
RIL_stock = yf.download("RELIANCE.NS", start="2021-01-01" , end ="2022-01-01" )

#Fixing the indexing,merging the two columns 
df=RIL_stock
df=df.reset_index()
volumes=df[['Date','Volume']]

#Creating another column for cumulative average till date
average_volumes=[]
n=len(volumes)
#This loops averages out the volume till date
for i in range(0,n-1):
    average_volumes.append(volumes.iloc[0:i+1,1:].mean())
average_volumes
average_volume=pd.DataFrame(average_volumes)
average_volume
df['Average_till_date']=average_volume['Volume']

#Plotting the Candlestick chart
candle_fig =go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])
#Plotting the Cumulative average chart
avg_vol_fig=go.Bar(x=df['Date'],y=df['Average_till_date'])
#Plotting the Volume chart
vol_fig=go.Bar(x=df['Date'],y=df['Volume'])


##
fig=make_subplots(rows=4, cols=1,subplot_titles=("Candlestick","", "Volume", "Cumalative"))
fig.add_trace(candle_fig, row=1, col=1)
fig.add_trace(vol_fig, row=3, col=1)
fig.add_trace(avg_vol_fig, row=4, col=1)
fig.update_layout(height=1000, width=800)
fig.show()


