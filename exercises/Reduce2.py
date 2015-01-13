#!/usr/bin/env python3

# ---------
# Reduce.py
# ---------

# https://docs.python.org/3.4/library/functools.html

from functools import reduce
from operator  import add, mul, sub

def reduce_for_range (bf, a, v) :
    for i in range(len(a)) :
        v = bf(v, a[i])
    return v

def reduce_while (bf, a, v) :
    p = iter(a)
    try :
        while True :
            w = next(p)
            v = bf(v, w)
    except StopIteration :
        pass
    return v

def reduce_for (bf, a, v) :
    for w in a :
        v = bf(v, w)
    return v

def test (f) :
    assert f(add, [], 0) == 0

    a = [2, 3, 4]
    assert f(add, a, 0) ==  9
    assert f(sub, a, 0) == -9
    assert f(mul, a, 1) == 24

    a = ([2, 3, 4], [5, 6])
    assert f(add, a, []) == [2, 3, 4, 5, 6]

    a = [(2, 3, 4), (5, 6)]
    assert f(add, a, ()) == (2, 3, 4, 5, 6)

    a = ("abc", "de")
    assert f(add, a, "") == "abcde"

print("Reduce.py")

test(reduce_for_range)
test(reduce_while)
test(reduce_for)
test(reduce)

print("Done.")
