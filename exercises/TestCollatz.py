#!/usr/bin/env python3

from unittest import main, TestCase

from Collatz import max_cycle_length

class MyUnitTests (TestCase) :
    def test_eval_1 (self) :
        self.assertEqual(max_cycle_length(1, 10), 20)

    def test_eval_2 (self) :
        self.assertEqual(max_cycle_length(100, 200), 125)

    def test_eval_3 (self) :
        self.assertEqual(max_cycle_length(201, 210), 89)

    def test_eval_4 (self) :
        self.assertEqual(max_cycle_length(900, 1000), 174)

if __name__ == "__main__" :
    main()
