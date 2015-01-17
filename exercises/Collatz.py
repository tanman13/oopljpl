#!/usr/bin/env python3

from sys import stdin

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

def max_cycle_length (i, j) :
    ...

if __name__ == "__main__" :
    ...
