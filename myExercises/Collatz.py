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

    s = 0
    for v in range (i, j+1) :
        t = cycle_length (v)
        if t > s :
            s = t
    return (s)
 
if __name__ == "__main__" :
    for v in stdin :
        s = v.split(" ")
        i = int (s[0])
        j = int (s[1])

        if j < i :
            t = max_cycle_length (j, i)
        else :
            t = max_cycle_length (i,j)
        s = v.replace("\n","") + " " + str(t) 
        print (s)
