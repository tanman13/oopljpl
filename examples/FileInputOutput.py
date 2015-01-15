#!/usr/bin/env python3

# ------------------
# FileInputOutput.py
# ------------------

import sys

f = open(sys.argv[0])

for v in f :
    print(v, end = "")
