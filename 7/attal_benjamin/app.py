#!/usr/local/bin/python

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pvwatts.html', methods=['GET', 'POST'])
def pvwatts():
  return render_template('pvwatts.html')

if __name__ == '__main__':
  app.run(debug=True)
