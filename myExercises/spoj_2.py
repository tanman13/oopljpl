#!/usr/bin/env python3

from sys import stdin

from math     import sqrt
from unittest import main, TestCase

d = {}

def is_prime (n) :
    assert n > 0
    if n in d :
      return d[n]
    
    if n == 1 :
        d[n] = False
        return False
    if n == 2 :
        d[n] = True
        return True
    if (n % 2) == 0 :
        d[n] = False
        return False
    for i in range(3, int(sqrt(n)) + 1, 2) :
        if (n % i) == 0 :
            d[n] = False
            return False
    d[n] = True
    return True


if __name__ == "__main__" :
    firstLine = True;
    for v in stdin :
        if(firstLine) :
           numLines = int(v)
           firstLine = False
        else:
           s = v.split(" ")
           i = int (s[0])
           j = int (s[1])

           if j < i :
             for r in range(j,i+1) :
               if(is_prime(r)) :
                  print(r);
             print("")
           else :
             for r in range(i,j+1) :
               if(is_prime(r)) :
                  print(r);
             print("")

           if(numLines == 1) :
              break
           else:
              numLines -= 1





