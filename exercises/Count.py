#!/usr/bin/env python3

# --------
# Count.py
# --------

from unittest import main, TestCase

class count () :
    ...

class MyUnitTests (TestCase) :
    def test_1 (self) :
        p = count(2)
        assert iter(p) is p
        assert next(p) == 2
        assert next(p) == 3
        assert next(p) == 4

    def test_2 (self) :
        p = count(2, 3)
        assert iter(p) is p
        assert next(p) == 2
        assert next(p) == 5
        assert next(p) == 8

if __name__ == "__main__" :
    main()
