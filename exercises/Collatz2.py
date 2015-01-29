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
    for s in stdin :
        a = s.split()
        i = int(a[0])
        j = int(a[1])
        v = max_cycle_length(i, j)
        print(i, j, v)
