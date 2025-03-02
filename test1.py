#!/bin/python3

import math
import os
import random
import re
import sys
import unittest
#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

def alternatingCharacters(s):
    delete = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            delete +=1
        else :
            pass
    return delete

class testAlternatingCharacters(unittest.TestCase):
    def test_all_A(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_all_B(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_alternating_AB(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_alternating_BA(self):
        self.assertEqual(alternatingCharacters("BABABA"), 0)

    def test_mixed_AAABBB(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_empty_string(self):
        self.assertEqual(alternatingCharacters(""), 0)

    def test_single_char(self):
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("B"), 0)

    def test_single_pair(self):
        self.assertEqual(alternatingCharacters("AA"), 1)

    def test_long_alternating(self):
        self.assertEqual(alternatingCharacters("A" * 1000), 999)
        self.assertEqual(alternatingCharacters("AB" * 500), 0)

    def test_edge_cases(self):
        self.assertEqual(alternatingCharacters("ABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        self.assertEqual(alternatingCharacters("A" * 1000), 999)
        self.assertEqual(alternatingCharacters("B" * 1000), 999)

    def test_large_cases(self):
        self.assertEqual(alternatingCharacters("A" * 1000), 999)
        self.assertEqual(alternatingCharacters("AB" * 500), 0)
        self.assertEqual(alternatingCharacters("BA" * 500), 0)


if __name__ == '__main__':
    unittest.main()