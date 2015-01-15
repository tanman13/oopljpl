#!/usr/bin/env python3

# ------------------
# FileInputOutput.py
# ------------------

import sys
import types

assert type(sys)      is types.ModuleType
assert type(sys.argv) is list
assert len(sys.argv)  == 1
f = open(sys.argv[0])

for v in f :
    print(v, end = "")
