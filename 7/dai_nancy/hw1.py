#!/usr/bin/python

# Wasn't sure what to do to show python skills.

# Project Euler Problem # 5

import math

def prob5():
    ans = 1;
    i = 2;
    while i < 21:
        if ans % i != 0:
            ans = ans * i
        i = i + 1
    return ans
