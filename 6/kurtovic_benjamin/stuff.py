#! /usr/bin/env python

# I'm not sure how to demonstrate my knowledge best, so here's an example of
# some really esoteric concepts in the form of metaclasses (because I can).

import sys
import time

class CacheMeta(type):
    """Caches the return values of every function in the child class."""
    def __new__(cls, name, bases, values):
        def use_cache(func):
            """Wraps a function to use the caching system."""
            def wrapper(self, *args):
                key = (func, args)
                if key in self._cache:
                    return self._cache[key]
                result = func(self, *args)
                self._cache[key] = result
                return result
            return wrapper
        for key, func in values.iteritems():
            if callable(func):
                values[key] = use_cache(func)
        values["_cache"] = {}
        return super(CacheMeta, cls).__new__(cls, name, bases, values)


class WithoutCache(object):
    """Some time-consuming methods that don't use a cache."""
    def fib(self, n):
        """Calculates the nth Fibonacci number inefficiently."""
        if n <= 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


class WithCache(object):
    """Some time-consuming methods that use a cache."""
    __metaclass__ = CacheMeta
    def fib(self, n):
        """Calculates the nth Fibonacci number efficiently."""
        if n <= 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


def test():
    n = 35
    classes = [(WithoutCache(), "without"), (WithCache(), "with")]
    for obj, desc in classes:
        print "First %i Fibonacci numbers %s cache:\n\t" % (n, desc),
        for i in xrange(1, n + 1):
            if i == n:
                t1 = time.time()
            sys.stdout.write(str(obj.fib(i)) + (" "))
            sys.stdout.flush()
            if i == n:
                t2 = time.time()
                print "\n\t%.8f seconds to find %ith number" % (t2 - t1, n)
        print

if __name__ == "__main__":
    test()
