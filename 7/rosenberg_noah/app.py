#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route("/home")
def home():
    return"<h1>Hi</h1>"
