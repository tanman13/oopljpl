#!/c/Python34/python

#------------------
# reduce.py
#------------------

from unittest import main, TestCase
from types import FunctionType
from operator import *

def reduce(op, value, seed):

#   if(type(value) is not range):
#      iterRange = range(value)

   output = seed
#   for n in range(0, len(value)) :
#      output = op(output,value[n])

   for n in value:
      output = op(output,n)
   return output
 

class ReduceTest(TestCase):
   def test_0(self):
      self.assertEqual(reduce(add, (2,3,4), 5), 14)

   def test_1(self):
      self.assertEqual(reduce(add, range(2, 5), 0), 9)

   def test_2(self):
      self.assertEqual(reduce(sub, [2,3,4], 0), -9)

   def test_3(self):
      self.assertEqual(reduce(add, ["a", "b", "c"], ""), "abc")
   
   def test_4(self):
      self.assertEqual(reduce(add,[[2],[3],[4]] , []), [2,3,4])

   def test_5(self):
      self.assertEqual(reduce(add, [(2,),(3,),(4,)], ()), (2,3,4))

main()
