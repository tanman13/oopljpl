#!/usr/bin/env python3

# -----------
# IsPrime2.py
# -----------

from math     import sqrt
from unittest import main, TestCase

def is_prime (n) :
    assert n > 0
    if n == 1 :
        return False
    if n == 2 :
        return True
    if (n % 2) == 0 :
        return False
    for i in range(3, int(sqrt(n)) + 1, 2) :
        if (n % i) == 0 :
            return False
    return True

print("IsPrime2.py")

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertFalse(is_prime( 1))

    def test_2 (self) :
        self.assertTrue(is_prime( 2))

    def test_3 (self) :
        self.assertTrue (is_prime( 3))

    def test_4 (self) :
        self.assertFalse(is_prime( 4))

    def test_5 (self) :
        self.assertTrue (is_prime( 5))

    def test_6 (self) :
        self.assertFalse(is_prime( 6))

    def test_7 (self) :
        self.assertTrue (is_prime( 7))

    def test_8 (self) :
        self.assertFalse(is_prime( 8))

    def test_9 (self) :
        self.assertFalse(is_prime( 9))

    def test_10 (self) :
        self.assertFalse(is_prime(10))

    def test_11 (self) :
        self.assertTrue (is_prime(11))

print("Done.")

"""
% coverage run --branch IsPrime.py
IsPrime.py
Done.

% coverage report
Name      Stmts   Miss Branch BrMiss  Cover
-------------------------------------------
IsPrime      23      0      6      0   100%
"""
