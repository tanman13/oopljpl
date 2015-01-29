#!/usr/bin/env python3

# --------
# Range.py
# --------

from unittest import main, TestCase

class range :
    class iterator:
        def __init__(self,k,l):
            self.k = k
            self.l = l

        def __next__(self):
            if (self.k == self.l):
                raise StopIteration
            v = self.k
            self.k += 1
            return v        

    def __init__(self,i,j):
        self.i = i
        self.j = j

    def __iter__(self):
        return range.iterator(self.i, self.j)


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

