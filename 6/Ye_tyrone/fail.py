from flask import Flask

app = Flask(__name__)
recurse = 0

@app.route("/")
def hello():
    return """
    <h1> Jabakaweez <h1>
<a href="/home">backhere</a> 
"""

@app.route("/home")
def inside():
    recurse = recurse + 1
    return """ <h1>You've been here<h1>
<a href="/home/out">go out</a>
"""

@app.route("/home/out")
def outside():
    return """ <h2>BYE?<h2>
<a href="/home">back inside</a>
"""


if __name__ == '__main__':
    app.run()


