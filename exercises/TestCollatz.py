#!/usr/bin/env python3

from unittest import main, TestCase

from Collatz import cycle_length, max_cycle_length

class MyUnitTests (TestCase) :
    def test_cycle_length_1 (self) :
        self.assertRaises(AssertionError, cycle_length, 0)

    def test_cycle_length_2 (self) :
        self.assertEqual(cycle_length(1), 1)

    def test_cycle_length_3 (self) :
        self.assertEqual(cycle_length(5), 6)

    def test_cycle_length_4 (self) :
        self.assertEqual(cycle_length(10), 7)

    def test_max_cycle_length_1 (self) :
        self.assertEqual(max_cycle_length(1, 10), 20)

    def test_max_cycle_length_2 (self) :
        self.assertEqual(max_cycle_length(100, 200), 125)

    def test_max_cycle_length_3 (self) :
        self.assertEqual(max_cycle_length(201, 210), 89)

    def test_max_cycle_length_eval_4 (self) :
        self.assertEqual(max_cycle_length(900, 1000), 174)

if __name__ == "__main__" :
    main()
