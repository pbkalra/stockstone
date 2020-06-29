from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('input1.html')

@app.route('/about')
def about():
  return render_template('time_series.html')

if __name__ == '__main__':
  app.run(port=33507)
