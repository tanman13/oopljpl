#!/usr/bin/env python3

# ----------
# Complex.py
# ----------

# https://docs.python.org/3.4/library/stdtypes.html#typesnumeric

from unittest import main, TestCase

class complex :
    def __init__ (self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def __str__ (self):
        return ("(" + str(self.real) + ("+" if self.imag >= 0 else "") +  str(self.imag)+"j)")

    def __eq__ (self, y):
        return ((self.real == y.real) and (self.imag == y.imag))
   
    def __add__ (self, y):
        return complex((self.real + y.real), (self.imag + y.imag))

    def __sub__ (self, y):
        return complex((self.real - y.real), (self.imag - y.imag))

    def __isub__ (self, y):
        return complex((self.real - y.real), (self.imag - y.imag))

    def conjugate(self):
        return complex(self.real, self.imag * -1)



        

class MyUnitTests (TestCase) :
    def test_1 (self) :
        x = complex()
        self.assertEqual(x.real, 0)
        self.assertEqual(x.imag, 0)

    def test_2 (self) :
        x = complex(2)
        self.assertEqual(x.real, 2)
        self.assertEqual(x.imag, 0)

    def test_3 (self) :
        x = complex(2, 3)
        self.assertEqual(x.real, 2)
        self.assertEqual(x.imag, 3)

    def test_4 (self) :
        x = complex(2, -3)
        self.assertEqual(str(x), "(2-3j)") # x.__str__()

    def test_5 (self) :
        x = complex(2, 3)
        y = complex(2, 3)
        self.assertEqual(x, y)             # x.__eq__(y)

    def test_6 (self) :
        x = complex(2, 3)
        y = complex(4, 5)
        x = x + y                          # x = x.__add__(y)
        self.assertEqual(x, complex(6, 8))

    def test_7 (self) :
        x = complex(2, 3)
        y = complex(4, 5)
        x += y                             # x = x.__add__(y)
        self.assertEqual(x, complex(6, 8))

    def test_8 (self) :
        x = complex(4, 5)
        y = complex(2, 3)
        x = x - y                          # x = x.__sub__(y)
        self.assertEqual(x, complex(2, 2))

    def test_9 (self) :
        x = complex(4, 5)
        y = complex(2, 3)
        x -= y                             # x = x.__isub__(y)
        self.assertEqual(x, complex(2, 2))

    def test_10 (self) :
        x = complex(2, 3)
        y = x.conjugate()
        self.assertEqual(x,complex(2,3))
        self.assertEqual(y,complex(2,-3))


if __name__ == "__main__" :
    main()


