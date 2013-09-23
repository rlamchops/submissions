#David Cahn, Homework 1
#!//Library/Frameworks/Python.framework/Versions/2.7/bin/python

def fact(n):
    ans = 1
    if n == 0:
        return ans
    else:
       return n * fact(n-1)

print (fact (5))

def fib (n):
    if n == 1:
        return n
    elif n <= 0:
        return 0
    else:
        return fib (n-1) + fib (n-2)

print (fib (5))

def isPrime(n):
    for i in range (2,n-1):
        if n % i == 0:
            return 'false'
    return 'true'

print (isPrime (7))
print (isPrime (150))
print (isPrime (11))

def minCoins (cents):
    q = cents / 25
    cents = cents % 25
    d = cents / 10
    cents = cents % 10
    n = cents / 5
    cents = cents % 5
    p = cents
    return ('Quarters: ' + str(q) + ' Dimes: ' +  str(d) +  ' Nickles: ' + str(n) + ' Pennies: ' + str (p))

print (minCoins (1005))
