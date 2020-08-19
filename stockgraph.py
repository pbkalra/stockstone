def getstockdata(StockSymb):

    csvurl = ('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + StockSymb + '&apikey=ECO7VXU7CT9JLWCT&datatype=csv')
    csvstockdata = requests.get(csvurl)
    with open('stockdata.csv', 'wb') as f:
           f.write(csvstockdata.content)
    return csvstockdf = pd.read_csv('stockdata.csv')


def plotstockgraph():    
    from bokeh.layouts import gridplot
    from bokeh.plotting import figure, output_file, show

  def datetime(x):
      return np.array(x, dtype=np.datetime64)
    #future feature: filter for one month--either set or ask user to choose month

    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'
    p1.line(datetime(csvstockdf['timestamp']), csvstockdf['close'], color='#A6CEE3', legend_label=StockSymb)
    #p1.line(datetime(csvstockdf['timestamp']), csvstockdf['open'], color='#B2DF8A', legend_label='open')

    outfilename = 'template/time_series.html' #+ StockSymb 

    output_file(outfilename, title="adapted from stocks.py example")

    return show(p1)
