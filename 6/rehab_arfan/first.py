#random functions

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    if bigger(a,b) < c:
        return bigger(a,b)
    else:
        if bigger(a,c) < b:
            return bigger(a,c)
        else:
            return bigger(b,c)

def print_multiplication_table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print str(i) + " * " + str(j) + " = " +  str(i*j)
            j = j + 1
        i = i + 1