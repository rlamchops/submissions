#!/usr/bin/python

import math

print("Hello, I am a basic statistics calculator.")
stats = input("Please give me a list of numerical data: ")
stats.sort()

sum = 0
for num in stats:
    sum += num

mean = float(sum) / len(stats)
print("The mean is: " + str(mean))

median = stats[len(stats) / 2]
print("The median is: " + str(median))

var = 0
for num in stats:
    var += (num - mean)**2
var = var / len(stats)
stdev = math.sqrt(var)
print("The standard deviation is: " + str(stdev))
