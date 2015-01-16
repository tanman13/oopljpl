#!/usr/bin/env python3

# ---------
# Range2.py
# ---------

from unittest  import TestCase, TestLoader, TestSuite, TextTestRunner

class my_range :
    class iterator () :
        def __init__ (self, b, e) :
            self.b = b
            self.e = e

        def __iter__ (self) :
            return self

        def __next__ (self) :
            if self.b == self.e :
                raise StopIteration()
            v = self.b
            self.b += 1
            return v

    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return my_range.iterator(self.b, self.e)

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
