from flask import Flask,redirect
import time
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World! </h1>"

@app.route("/<string>")
def troll(string):
    return "I'm sorry, I'm not sure what to do about " + string + ". Maybe you should look <a href=\"http://www.google.com\">here</a>?"
#look into render_template()
if __name__== '__main__':
    app.debug=True
    app.run()
#    app.run(host = "0,0,0", port=5000)

