#!/usr/bin/python
from random import randrange

#ConvBinToDec

def main(): 
    a = randrange(10)
    b = a / 100
    c = (a % 100) / 10
    d = (a % 100) % 10
    print((b * 4) + (c * 2) + d)

if __name__ == "__main__":
    main()