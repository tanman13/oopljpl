#!/usr/bin/env python3

# ----------
# Reduce3.py
# ----------

# https://docs.python.org/3.4/library/functools.html

from operator import sub
from unittest import main, TestCase

def reduce (bf, a, v = None) :
    i1 = iter(a)
    if v == None :
        if len(a) == 0:
            raise TypeError
        else:
            v1 = next(i1)
    else:
        v1 = v
    for x in i1:
        v1 = bf(v1,x)
    return v1

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(reduce(sub, [2]),           2)

    def test_2 (self) :
        self.assertEqual(reduce(sub, [2, 3]),       -1)

    def test_3 (self) :
        self.assertEqual(reduce(sub, [2, 3, 4]),    -5)

    def test_4 (self) :
        self.assertEqual(reduce(sub, [],        0),  0)

    def test_5 (self) :
        self.assertEqual(reduce(sub, [2],       0), -2)

    def test_6 (self) :
        self.assertEqual(reduce(sub, [2, 3],    0), -5)

    def test_7 (self) :
        self.assertEqual(reduce(sub, [2, 3, 4], 0), -9)

    def test_8 (self) :
        self.assertRaises(TypeError, reduce, sub, [])

if __name__ == "__main__" :
    main()


