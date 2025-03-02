import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from my_tests_code.funnystr import funnyString

class TestFunnyString(unittest.TestCase):
    
    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), 'Funny')
        self.assertEqual(funnyString("abccba"), 'Funny')
        self.assertEqual(funnyString("a"), 'Funny')
        self.assertEqual(funnyString("abc"), 'Funny')
        self.assertEqual(funnyString("abcd"), 'Funny')
        self.assertEqual(funnyString("abcdefg"), 'Funny')
        self.assertEqual(funnyString(""), 'Funny')
        self.assertEqual(funnyString("!@#@!"), 'Funny')
        self.assertEqual(funnyString("!a@b#c"), 'Not Funny')

if __name__ == '__main__':
    unittest.main()
