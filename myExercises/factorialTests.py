#!/c/Python34/python

#------------------
# factorialTests.py
#------------------

from unittest import main, TestCase

def myFactorial (n) :
   assert n >= 0

   if ( n > 1 ) :
      return n*myFactorial(n-1)

   return 1

     
class FactorialTest(TestCase):
   def test_0(self):
      self.assertEqual(myFactorial(0), 1)
   
   def test_1(self):
      self.assertEqual(myFactorial(1), 1)

   def test_2(self):
      self.assertEqual(myFactorial(2), 2)

   def test_3(self):
      self.assertEqual(myFactorial(3), 6)

   def test_4(self):
      self.assertEqual(myFactorial(4), 24)

   def test_5(self):
      self.assertEqual(myFactorial(5), 120)

main()
