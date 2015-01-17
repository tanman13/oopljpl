#!/usr/bin/env python3

# ---------
# Range4.py
# ---------

from unittest import TestCase, TestLoader, TestSuite, TextTestRunner

class my_range :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        b = self.b
        e = self.e
        while b != e :
            yield b
            b += 1

def bind (c) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            x = c(2, 2)
            assert list(x) == []
            assert list(x) == []

        def test_2 (self) :
            x = c(2, 3)
            assert list(x) == [2]
            assert list(x) == [2]

        def test_3 (self) :
            x = c(2, 4)
            assert list(x) == [2, 3]
            assert list(x) == [2, 3]

        def test_4 (self) :
            x = c(2, 5)
            assert list(x) == [2, 3, 4]
            assert list(x) == [2, 3, 4]
    return MyUnitTests

if __name__ == "__main__" :
    s = TestSuite()
    s.addTest(TestLoader().loadTestsFromTestCase(bind(my_range)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(   range)))
    TextTestRunner().run(s)
