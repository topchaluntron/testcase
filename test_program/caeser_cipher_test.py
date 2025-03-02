import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from my_tests_code.caeser_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 1), "")

    def test_no_shift(self):
        self.assertEqual(caesarCipher("abcxyzABCXYZ123", 0), "abcxyzABCXYZ123")

    def test_lowercase_shift(self):
        self.assertEqual(caesarCipher("abcxyz", 1), "bcdyza")
        self.assertEqual(caesarCipher("abcxyz", 2), "cdezab")
        self.assertEqual(caesarCipher("xyz", 1), "yza")
        self.assertEqual(caesarCipher("xyz", 26), "xyz")
        self.assertEqual(caesarCipher("xyz", 27), "yza")

    def test_uppercase_shift(self):
        self.assertEqual(caesarCipher("ABCXYZ", 1), "BCDYZA")
        self.assertEqual(caesarCipher("ABCXYZ", 2), "CDEZAB")
        self.assertEqual(caesarCipher("XYZ", 1), "YZA")
        self.assertEqual(caesarCipher("XYZ", 26), "XYZ")
        self.assertEqual(caesarCipher("XYZ", 27), "YZA")

    def test_mixed_case_shift(self):
        self.assertEqual(caesarCipher("AbCdEfGhIjKlMnOpQrStUvWxYz", 1), "BcDeFgHiJkLmNoPqRsTuVwXyZa")

    def test_with_numbers_and_symbols(self):
        self.assertEqual(caesarCipher("Hello, World! 123", 1), "Ifmmp, Xpsme! 123")

    def test_large_shift(self):
        self.assertEqual(caesarCipher("abcxyz", 53), "bcdyza")

if __name__ == '__main__':
    unittest.main()