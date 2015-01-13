#!/usr/bin/env python3

# ---------
# Reduce.py
# ---------

# https://docs.python.org/3.4/library/functools.html

from operator import add, mul, sub

def reduce (bf, a, v) :
    ...

print("Reduce.py")

assert reduce(add, [], 0) == 0

a = [2, 3, 4]
assert reduce(add, a, 0) ==  9
assert reduce(sub, a, 0) == -9
assert reduce(mul, a, 1) == 24

a = ([2, 3, 4], [5, 6])
assert reduce(add, a, []) == [2, 3, 4, 5, 6]

a = [(2, 3, 4), (5, 6)]
assert reduce(add, a, ()) == (2, 3, 4, 5, 6)

a = ("abc", "de")
assert reduce(add, a, "") == "abcde"

print("Done.")
