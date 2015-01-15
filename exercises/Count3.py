#!/usr/bin/env python3

# ---------
# Count3.py
# ---------

from unittest import main, TestCase

def count (b, s = 1) :
    ...

class MyUnitTests (TestCase) :
    def test_1 (self) :
        p = count(0)
        assert iter(p) is p
        assert next(p) == 0
        assert next(p) == 1
        assert next(p) == 2

    def test_2 (self) :
        p = count(2)
        assert iter(p) is p
        assert next(p) == 2
        assert next(p) == 3
        assert next(p) == 4

    def test_3 (self) :
        p = count(5, 2)
        assert iter(p) is p
        assert next(p) == 5
        assert next(p) == 7
        assert next(p) == 9

if __name__ == "__main__" :
    main()
