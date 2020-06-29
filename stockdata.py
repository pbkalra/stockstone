import requests
import simplejson
import numpy as np
import pandas as pd

##This part-asking the user for the stock symbol--will eventually be part of an HTML page on flask on heroku
StockSymb = input("What stock do you want to see?")
print("You asked for %s" %StockSymb)

#You could make a dictionary here for all the variables such as symbol, api key, and if you were using intraday, even for the interval

csvurl = ('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + StockSymb + '&apikey=ECO7VXU7CT9JLWCT&datatype=csv')

csvstockdata = requests.get(csvurl)

with open('stockdata.csv', 'wb') as f:
       f.write(csvstockdata.content)

jsonurl = ('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + StockSymb + '&outputsize=full&apikey=ECO7VXU7CT9JLWCT') 

jsonstockdata = requests.get(jsonurl)

#with open('stockdata.csv', 'wb') as f:
 #      f.write(csvstockdata.content)
        
with open ('stockdata.json', 'wb') as f:
    f.write(jsonstockdata.content)

csvstockdf = pd.read_csv('stockdata.csv')

jsonstockdf = pd.read_json(jsonstockdata.content)

#print(csvstockdf.columns)

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

def datetime(x):
    return np.array(x, dtype=np.datetime64)

#filter for one month--either set or ask user to choose month

p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'
p1.line(datetime(csvstockdf['timestamp']), csvstockdf['close'], color='#A6CEE3', legend_label=StockSymb)
#p1.line(datetime(csvstockdf['timestamp']), csvstockdf['open'], color='#B2DF8A', legend_label='open')

outfilename = StockSymb + 'time_series.html'

output_file(outfilename, title="adapted from stocks.py example")

show(p1)
