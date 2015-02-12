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
   lineIter = iter(stdin)

   numLines = int(next(lineIter))

   intervals = [];
   intCnt = 0;

   for v in lineIter :
      s = v.split(" ")
      i = int (s[0])
      j = int (s[1])

      if(intervals == []):
         primes = [r for r in range(i, j+1) if is_prime(r)]
         intervals[intCnt] = (i, j, primes)
         intCnt += 1

      else
         # Figure out of there is overlap
         for tempInt in intervals:

            # new interval subset of existing intervale
            if (i >= tempInt(1) and j <= tempInt(2)):
               # do stuff

            # new interval overlaps lower part of existing interval
            else if (i<tempInt(1) and j>=tempInt(1) and j<=tempInt(2)):
               # do stufff
            
            # new interval overlaps upper part of existing interval
            else if (i>=tempInt(1) and i<=tempInt(2) and j>tempInt(2)):
               # do stuff

            # new interval is a superset of existing interval
            else if (i <= tempInt(2) and j >= tempInt(1)):
               # do stuff
               primesLower = [r for r in range(i


         # new interval is disjoint from existing intervals
         primes = [r for r in range(i, j+1) if is_prime(r)]
         intervals[intCnt] = (i, j, primes)
         intCnt += 1
            

            
      







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

'''
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
'''




