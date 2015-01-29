#!/usr/bin/env python3

from sys import stdin

for v in stdin :
    if v == "42\n":
        break
    print(v, end = "")
