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
    if i > j :
        i, j = j, i
    v = 0
    for n in range(i, j + 1) :
        c = cycle_length(n)
        if c > v :
            v = c
    return v

if __name__ == "__main__" :
    a = ([int(v) for v in s.split()] for s in stdin)
    m = ([i, j, max_cycle_length(i, j)] for i, j in a)
    for i, j, v in m :
        print(i, j, v)
