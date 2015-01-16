#!/usr/bin/env python3

# ---------
# Count2.py
# ---------

from itertools import count
from unittest  import TestCase, TestLoader, TestSuite, TextTestRunner

class my_count () :
    def __init__ (self, b = 0, s = 1) :
        self.b = b
        self.s = s

    def __iter__ (self) :
        return self

    def __next__ (self) :
        v = self.b
        self.b += self.s
        return v

def bind (c) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            p = c()
            assert iter(p) is p
            assert next(p) == 0
            assert next(p) == 1
            assert next(p) == 2

        def test_2 (self) :
            p = c(2)
            assert iter(p) is p
            assert next(p) == 2
            assert next(p) == 3
            assert next(p) == 4

        def test_3 (self) :
            p = c(5, 2)
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
