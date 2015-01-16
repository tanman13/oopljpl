#!/usr/bin/env python3

# -------------
# Decorators.py
# -------------

from unittest import main, TestCase

def pre_gtz (f) :
    def g (n) :
        assert n > 0
        return f(n)
    return g

def post_gtz (f) :
    def g (n) :
        v = f(n)
        assert v > 0
        return v
    return g

@pre_gtz
@post_gtz
def cycle_length (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(cycle_length(1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length(5), 6)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

    def test_4 (self) :
        self.assertRaises(AssertionError, cycle_length, 0)

if __name__ == "__main__" :
    main()
