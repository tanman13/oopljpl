#!/usr/bin/env python3

# ---------
# StDev2.py
# ---------

# https://docs.python.org/3/library/statistics.html

from functools  import reduce
from math       import sqrt
from statistics import mean, stdev, StatisticsError
from unittest   import TestCase, TestLoader, TestSuite, TextTestRunner

def stdev_for_range (a) :
    s = len(a)
    if s < 2 :
        raise StatisticsError('variance requires at least two data points')
    m = mean(a)
    v = 0
    for i in range(s) :
        v += (a[i] - m) ** 2
    return sqrt(v / (s - 1))

def stdev_for (a) :
    s = len(a)
    if s < 2 :
        raise StatisticsError('variance requires at least two data points')
    m = mean(a)
    v = 0
    for u in a :
        v += (u - m) ** 2
    return sqrt(v / (s - 1))

def stdev_reduce (a) :
    s = len(a)
    if s < 2 :
        raise StatisticsError('variance requires at least two data points')
    m = mean(a)
    v = reduce(lambda w, u : w + (u - m) ** 2, a, 0)
    return sqrt(v / (s - 1))

def stdev_map (a) :
    s = len(a)
    if s < 2 :
        raise StatisticsError('variance requires at least two data points')
    m = mean(a)
    v = sum(map(lambda v : (v - m) ** 2, a))
    return sqrt(v / (s - 1))

def stdev_list (a) :
    s = len(a)
    if s < 2 :
        raise StatisticsError('variance requires at least two data points')
    m = mean(a)
    v = sum([(v - m) ** 2 for v in a])
    return sqrt(v / (s - 1))

def stdev_generator (a) :
    s = len(a)
    if s < 2 :
        raise StatisticsError('variance requires at least two data points')
    m = mean(a)
    v = sum((v - m) ** 2 for v in a)
    return sqrt(v / (s - 1))

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            self.assertEqual(f([2, 2]),    0)

        def test_2 (self) :
            self.assertEqual(f([2, 3]),    0.7071067811865476)

        def test_3 (self) :
            self.assertEqual(f([2, 2, 2]), 0)

        def test_4 (self) :
            self.assertEqual(f([2, 3, 4]), 1)

        def test_5 (self) :
            self.assertRaises(StatisticsError, f, [])

        def test_6 (self) :
            self.assertRaises(StatisticsError, f, [2])
    return MyUnitTests

if __name__ == "__main__" :
    s = TestSuite()
    s.addTest(TestLoader().loadTestsFromTestCase(bind(stdev_for_range)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(stdev_for)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(stdev_reduce)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(stdev_map)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(stdev_list)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(stdev_generator)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(stdev)))
    TextTestRunner().run(s)
