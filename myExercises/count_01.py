#!/usr/bin/env python3

# --------
# Count.py
# --------

from unittest import main, TestCase

class count () :
    def __init__(self, i, j=1):
        self.i = i
        self.j = j

    def __iter__(self):
        return self

    def __next__(self):
        v = self.i
        self.i = v + self.j
        return v


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

