#!usr/bin/python

def fact(n):
    # return n factorial
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def fib(n):
    # calculate and return the nth Fibonacci number
    if n <= 2:
        return n - 1
    else:
        return fib(n-1) + fib(n-2)

def isPrime(n):
     #returns True (which is a value in Python) if n is prime
     # returns False otherwise (which is also a value)
    a = 2
    b = False
    while n % a != 0 & a < n:
        a = a + 1
    if a >= n:
        b = True
	return b
    else:
        return b


print fact(1)
print fact(6)
print fib(1)
print fib(2)
print fib(6)
print isPrime(4)
print isPrime(7)

