import time
import math
from random import randint

def fact(n):
	if n==0:
		return "Error"
	elif n==1:
		return 1
	else:
		return n*fact(n-1)

def fib(n):
	if n==0:
		return "Error"
	elif n==1 or n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

def listFibs():
	n= int(raw_input("How many Fibonacci's do you want? "))
	for i in range (1,n+1):
		print fib(i)

def isPrime(n):
	a=3
	if n<=1:
		return False
	elif n==2 or n==3:
		return True
	elif n%2==0 or n%3==0:
		return False
	elif (n+1)%6!=0 and (n-1)%6!=0:
		return False
	else:
		while a<=(math.sqrt(n)):
			if n%a==0:
				return False
			a+=2
		return True
		
def listPrimes():
	a= int(raw_input("How many prime numbers do you want? "))
	start=time.time()
	n=0
	p=1
	if a>=1:
		print 2
	
	while n<a-1:
		if isPrime(p):
			print p
			n+=1
		p+=2
	end=time.time()
	print end-start
#inefficient method of listing primes; only exists for the sake of testing the speed of isPrime(n)

def GuessANumber(low,high):
	ans=randint(low,high)
	#print ans
	win=False
	while win==False:
		text="".join(["Please guess a number between ",str(low)," and ",str(high),". "])
		guess=int(raw_input(text))
		if guess==-1:
			break
		elif guess==ans:
			print "You Win"
			win=True
		elif guess>ans:
			high=guess
			print "Please Try Again"
		elif guess<ans:
			low=guess
			print "Please Try Again"

#print fact(5)
#listFibs()
#listPrimes()
#GuessANumber(1,10)
#print isPrime(124791);



