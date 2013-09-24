#!/usr/bin/python
from math import sqrt

def isPrime(n):
	for i in xrange(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def naiveNthPrime(n):
	assert n >= 1
	i = 2;
	while (n > 1):
		i += 1
		if isPrime(i):
			n -= 1
	return i

def getWord():
	a = [ 42, 95, 49, 88, 59, 84, 38, 72 ]
	s = ""
	for i in xrange(1, len(a)):
		s += chr(a[i] ^ a[i - 1])
	return s