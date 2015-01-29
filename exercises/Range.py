#!/usr/bin/env python3

# --------
# Range.py
# --------

from unittest import main, TestCase

class range :
    ...

class MyUnitTests (TestCase) :
    def test_1 (self) :
        x = range(2, 2)
        assert list(x) == []
        assert list(x) == []

    def test_2 (self) :
        x = range(2, 3)
        assert list(x) == [2]
        assert list(x) == [2]

    def test_3 (self) :
        x = range(2, 4)
        assert list(x) == [2, 3]
        assert list(x) == [2, 3]

    def test_4 (self) :
        x = range(2, 5)
        assert list(x) == [2, 3, 4]
        assert list(x) == [2, 3, 4]

if __name__ == "__main__" :
    main()
