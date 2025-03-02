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
    def test_empty(self):
        self.assertEqual(alternatingCharacters(""), 0)
    def test_1char(self):
        self.assertEqual(alternatingCharacters("A"),0)
        self.assertEqual(alternatingCharacters("B"),0)



if __name__ == '__main__':
    unittest.main()