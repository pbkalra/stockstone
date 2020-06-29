from flask import Flask, render_template, request, redirect
from stockgraph import getstockdata, plotstockgraph

app = Flask(__name__)

app.vars = {}

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('input1.html')
    else:
        app.vars['name'] = request.form['StockSymb']
        result = stockgraph(name)
        plotstockgraph()
        #currently having trouble with the definition of this function
#future: add input validation in case the user enters an invalid stock symbol

@app.route('/time_series', methods = ['POST'])
def time_series():
  return render_template('time_series.html')

if __name__ == '__main__':
  app.run(port=33507)
