#!/usr/bin/env python

# -------------------
# FunctionParallel.py
# -------------------

print "FunctionParallel.py"

def f ((x, y), z) :
    return [x, y, z]

#def g ([x, y], z) :  # SyntaxError: invalid syntax
#    return [x, y, z]

assert f((2, 3), 4)                 == [2, 3, 4]
assert f([2, 3], 4)                 == [2, 3, 4]
assert f({2, 3}, 4)                 == [2, 3, 4] # not a guaranteed order
assert f({2 : "abc", 3 : "def"}, 4) == [2, 3, 4] # not a guaranteed order
assert f(range(2, 4), 4)            == [2, 3, 4]

#f(2, 3, 4)                                      # TypeError: f() takes exactly 2 arguments (3 given)
#f((2,), 3)                                      # ValueError: need more than 2 values to unpack
#f((2, 3, 4), 5)                                 # ValueError: too many values to unpack
#f(range(2, 5), 4)                               # ValueError: too many values to unpack

print "Done."
