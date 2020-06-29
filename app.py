from flask import Flask, render_template, request, redirect
import stockgraph

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('input1.html')

#stockgraph(StockSymb)

#@app.route('/time_series')
#def about():
#  return render_template('time_series.html')

if __name__ == '__main__':
  app.run(port=33507)
