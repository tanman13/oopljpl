#!/usr/bin/env python3

# --------
# StDev.py
# --------

# https://docs.python.org/3/library/statistics.html

from functools  import reduce
from math       import sqrt
from statistics import mean
from unittest   import main, TestCase
from operator  import add

def stdev (a) :
   # sqrt(E[(x-mu)^2])

   return sqrt(reduce(add,((x - mean(a))**2 for x in a),0)/(len(a)-1))
   


class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(stdev([2, 2]),    0)

    def test_2 (self) :
        self.assertEqual(stdev([2, 3]),    0.7071067811865476)

    def test_3 (self) :
        self.assertEqual(stdev([2, 2, 2]), 0)

    def test_4 (self) :
        self.assertEqual(stdev([2, 3, 4]), 1)

if __name__ == "__main__" :
    main()

