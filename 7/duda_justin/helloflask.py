
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


def fact(n):
    ans = 1
    while(n > 1):
        ans *= n
        n -= 1
	return ans

def fib(n):
    a = 1
    b = 1
    ans = a + b
    if (n < 3):
        return 1
    n -= 2
    while(n > 0):
        ans = a + b
        a = b
        b = ans
        n -= 1
	return ans

def isPrime(n):
    i = n-1
    if(n==1 or n==0):
        return False
    if(n==2):
        return True
    while(i>1):
        if(n%i==0):
            return False
        i -= 1
	return True
