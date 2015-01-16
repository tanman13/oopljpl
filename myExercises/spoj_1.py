#!/usr/bin/env python3

from sys import stdin

for x in stdin:
   if int(x) == 42 :
      break
   print(x, end = "")

