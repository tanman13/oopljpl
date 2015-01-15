#!/usr/bin/env python3

# ---------
# Count4.py
# ---------

from itertools import count
from unittest  import TestCase, TestLoader, TestSuite, TextTestRunner

def my_count (b = 0, s = 1) :
    while True :
        yield b
        b += s

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            p = f(0)
            assert iter(p) is p
            assert next(p) == 0
            assert next(p) == 1
            assert next(p) == 2

        def test_2 (self) :
            p = f(2)
            assert iter(p) is p
            assert next(p) == 2
            assert next(p) == 3
            assert next(p) == 4

        def test_3 (self) :
            p = f(5, 2)
            assert iter(p) is p
            assert next(p) == 5
            assert next(p) == 7
            assert next(p) == 9
    return MyUnitTests

if __name__ == "__main__" :
    s = TestSuite()
    s.addTest(TestLoader().loadTestsFromTestCase(bind(my_count)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(   count)))
    TextTestRunner().run(s)
