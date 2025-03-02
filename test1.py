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
    return delete
